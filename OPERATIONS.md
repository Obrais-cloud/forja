# Operational observations

`forja status [NAME]` reads evidence for existing catalog items. `--json` returns
the same observations for agents. It does not contact deployments, execute
checks, update memory, or modify the catalog. An absent observation means
unverified, not unavailable. An expired observation has `needs_review: true`.

Keep the file at `~/.local/state/forja/operations.json` (or set
`FORJA_OPERATIONS_FILE`). It is separate from `registry.json`, generated entry
pages, Claude's catalog summary and Ollaverse exports. Do not place private
operational records in the public repository. Use file permissions appropriate
for their content, for example a private directory and an owner-readable file.

Schema example for an item already registered as `my-tool`:

```json
{
  "schema_version": 1,
  "observations": [
    {
      "item": "my-tool",
      "observed_at": "2026-09-05T12:00:00Z",
      "expires_at": "2026-09-06T12:00:00Z",
      "state": "partial",
      "summary": "Read-only retrieval worked; write workflow not tested.",
      "evidence": ["/private/check-receipt.json"],
      "next_action": "Verify the next authorized write.",
      "runtime": "Where the application actually runs",
      "source": "Repository and exact revision checked",
      "consumer": "Application or agent using the result"
    }
  ]
}
```

`runtime`, `source`, and `consumer` are optional. Other fields are required.
States are `verified`, `partial`, `blocked`, or `unverified`; the summary should
say exactly what the evidence supports. Dates require timezones. Unknown or
duplicate catalog items, invalid dates, missing references, and unexpected
fields make the whole file invalid rather than silently hiding records.
The command validates the record shape, not the truth of its referenced evidence.
After expiry it preserves the original record and asks for review; it does not
refresh or promote results automatically.

Run the offline test suite with `python3 -m unittest discover -s tests -v`.
