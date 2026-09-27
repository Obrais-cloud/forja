# cuesheet

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/cuesheet` |
| github | https://github.com/Obrais-cloud/cuesheet |
| version | 0.2.0 |
| created | 2026-09-27 |
| tags | filmmaking, delivery, rights, music, cue-sheet, edl, fcpxml, cli, python, deterministic, fillos-do-vento |

**What it is.** Lee un export de timeline (EDL CMX3600, FCP 7 XML de Resolve/Premiere o FCPXML/.fcpxmld) y genera cue sheet de música (título, compositor, editorial, SGAE/PRO, uso BI/VI…, TC in/out, duración) + informe de uso de archivo/stock con titular/licencia y tiempo en pantalla. Fusiona pares estéreo y usos contiguos, clips conectados y compounds; --init genera el TOML de derechos; --strict sale 2 si faltan datos. Formato no reconocido o timeline sin clips → exit 1 (nunca informe vacío). Validado con exports reales de Resolve de Fillos do Vento (sin música).

**When to reach for it.** Antes de entregar a festival/TV/agente de ventas: 'cuesheet timeline.edl -r rights.toml --strict' te da el music cue sheet y el informe de archivo que pide el checklist, y falla si alguna fuente no tiene derechos documentados. Pareja natural de speccheck (QC técnico → QC de derechos).

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
