import contextlib
import datetime
import importlib.machinery
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("forja", str(ROOT / "forja"))
spec = importlib.util.spec_from_loader(loader.name, loader)
forja = importlib.util.module_from_spec(spec)
loader.exec_module(forja)
NOW = datetime.datetime(2026, 9, 5, 18, tzinfo=datetime.timezone.utc)


class FixedDatetime(datetime.datetime):
    @classmethod
    def now(cls, tz=None):
        return NOW if tz else NOW.replace(tzinfo=None)


def record(**changes):
    row = dict(item="demo", observed_at="2026-09-05T17:00:00Z", expires_at="2026-09-06T17:00:00Z", state="partial", summary="PRIVATE_OPERATIONAL_MARKER", evidence=["/private/report.md"], next_action="Check the next real delivery", runtime="Private runtime", source="Source revision", consumer="Local agent")
    row.update(changes)
    return row


class OperationsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.file = self.root / "private" / "operations.json"
        self.file.parent.mkdir()
        self.reg = {"items":[dict(name="demo",kind="tool",path="/demo",github=None,description="A demo",utility="A demo",tags=[])]}
        for key, value in [("REGISTRY",self.root/"registry.json"),("README",self.root/"README.md"),("ENTRIES",self.root/"entries")]:
            p=patch.object(forja,key,value); p.start(); self.addCleanup(p.stop)
        forja.REGISTRY.write_text(json.dumps(self.reg))
        self.env=patch.dict(os.environ,{"FORJA_OPERATIONS_FILE":str(self.file)})
        self.env.start(); self.addCleanup(self.env.stop)
        self.write([record()])

    def write(self, rows, **changes):
        data=dict(schema_version=1,observations=rows);data.update(changes)
        self.file.write_text(json.dumps(data))

    def command(self, *args):
        with patch.object(forja.datetime,"datetime",FixedDatetime), contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()) as err:
            code=forja.main(list(args))
        return code,out.getvalue(),err.getvalue()

    def test_private_default_path_and_explicit_override(self):
        self.assertEqual(forja.operations_path(),self.file)
        with patch.dict(os.environ,{},clear=True),patch.object(Path,"home",return_value=self.root):
            self.assertEqual(forja.operations_path(),self.root/".local/state/forja/operations.json")

    def test_fresh_expired_and_exact_expiry_boundary(self):
        fresh=forja.load_operations(self.reg,self.file,NOW)[0]
        self.assertFalse(fresh["needs_review"])
        self.assertEqual(fresh["state"],"partial")
        self.write([record(expires_at="2026-09-05T18:00:00Z")])
        self.assertTrue(forja.load_operations(self.reg,self.file,NOW)[0]["needs_review"])

    def test_invalid_dates_cannot_appear_verified(self):
        for values in [dict(observed_at="2026-09-05T19:00:00Z"),dict(observed_at="2026-09-05T17:00:00"),dict(observed_at="bad"),dict(expires_at="2026-09-05T16:00:00Z"),dict(expires_at="2026-09-05T17:00:00Z")]:
            with self.subTest(values=values),self.assertRaises(ValueError):
                self.write([record(**values)]);forja.load_operations(self.reg,self.file,NOW)
        with self.assertRaises(ValueError):forja.observation_date(None)

    def test_unknown_duplicate_or_unattributed_records_fail_closed(self):
        cases=[[record(item="unknown")],[record(),record()],[record(state="ready")],[record(evidence=[])],[record(evidence="not a list")],[record(evidence=[None])],[record(summary="")],[record(api_key="private-secret")],[None]]
        for key in record():
            if key not in {"runtime","source","consumer"}:
                r=record();del r[key];cases.append([r])
        for rows in cases:
            with self.subTest(rows=rows),self.assertRaises(ValueError):
                self.write(rows);forja.load_operations(self.reg,self.file,NOW)

    def test_invalid_document_shapes(self):
        for data in [None,[],{},dict(schema_version=True,observations=[]),dict(schema_version=2,observations=[]),dict(schema_version=1,observations={}),dict(schema_version=1,observations=[],secret="private-secret")]:
            self.file.write_text(json.dumps(data))
            with self.subTest(data=data),self.assertRaises(ValueError):forja.load_operations(self.reg,self.file,NOW)

    def test_missing_observation_is_not_a_claim_of_service_failure(self):
        self.file.unlink()
        self.assertEqual(forja.load_operations(self.reg,self.file,NOW),[])
        code,text,_=self.command("status","demo")
        self.assertEqual(code,0);self.assertIn("Sin evidencia",text)
        code,text,_=self.command("status","--json")
        self.assertEqual(json.loads(text)["observations"],[])

    def test_bad_file_errors_do_not_echo_secret_contents(self):
        for content in ['{"private-secret":',json.dumps({"private-secret":"token"})]:
            self.file.write_text(content)
            code,text,error=self.command("status")
            self.assertEqual(code,2);self.assertEqual(text,"");self.assertNotIn("private-secret",error)
        with patch.object(forja,"load_operations",side_effect=PermissionError("secret")):
            code,_,error=self.command("status")
            self.assertEqual(code,2);self.assertNotIn("secret",error)

    def test_selection_and_json_keep_provenance(self):
        code,text,error=self.command("status","demo","--json")
        self.assertEqual((code,error),(0,""))
        data=json.loads(text);self.assertEqual(data["observations"][0]["evidence"],["/private/report.md"])
        self.assertEqual(data["observations"][0]["item"],"demo")
        code,_,_=self.command("status","absent");self.assertEqual(code,1)

    def test_human_output_labels_stale_data(self):
        self.write([record(observed_at="2020-01-01T00:00:00Z",expires_at="2020-01-02T00:00:00Z")])
        code,text,_=self.command("status")
        self.assertEqual(code,0);self.assertIn("requiere revisión",text);self.assertIn("/private/report.md",text);self.assertIn("Siguiente:",text)
        self.write([record(expires_at="2099-01-01T00:00:00Z")])
        code,text,_=self.command("status");self.assertIn("partial",text)

    def test_no_catalog_write_network_or_subprocess_from_status(self):
        before=forja.REGISTRY.read_bytes();private_before=self.file.read_bytes()
        with patch.object(forja,"store",side_effect=AssertionError("write")),patch.object(forja,"sync_readme",side_effect=AssertionError("write")),patch.object(forja.subprocess,"run",side_effect=AssertionError("subprocess")):
            self.assertEqual(self.command("status","--json")[0],0)
        self.assertEqual(forja.REGISTRY.read_bytes(),before);self.assertEqual(self.file.read_bytes(),private_before)

    def test_public_exports_and_memory_do_not_contain_private_observations(self):
        self.command("status")
        forja.sync_readme(self.reg);forja.write_entry(self.reg["items"][0])
        for public in [forja.REGISTRY,forja.README,forja.entry_path("demo")]:
            self.assertNotIn("PRIVATE_OPERATIONAL_MARKER",public.read_text())
        self.assertNotIn("PRIVATE_OPERATIONAL_MARKER",forja._memory_block(self.reg))
        self.assertIn("forja status NAME",forja._memory_block(self.reg))
        self.assertIn("con enlace GitHub",forja._memory_block(self.reg))
        self.assertIn("forja status",forja.README.read_text())


if __name__ == "__main__":
    unittest.main()
