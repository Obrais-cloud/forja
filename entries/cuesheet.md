# cuesheet

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/cuesheet` |
| github | https://github.com/Obrais-cloud/cuesheet |
| version | 0.3.0 |
| created | 2026-09-27 |
| tags | filmmaking, delivery, rights, music, cue-sheet, edl, fcpxml, cli, python, deterministic, fillos-do-vento |

**What it is.** Lee un export de timeline (EDL CMX3600, FCP 7 XML de Resolve/Premiere o FCPXML/.fcpxmld) y genera cue sheet de música (título, compositor, editorial, SGAE/PRO, uso BI/VI…, TC in/out, duración) + informe de efectos/archivo/stock con titular/licencia y tiempo en pantalla. Música sólo con evidencia (carpetas/nombres music/score/BSO/OST), categoría sfx, sonido directo nunca es cue, resto → audio-review. --init genera el TOML de derechos; --strict sale 2 si faltan datos o queda audio sin revisar; formato no reconocido → exit 1. Validado contra un largo real de Fillos do Vento (Resolve 21.1): 31/31 cues idénticos a la API de Resolve.

**When to reach for it.** Antes de entregar a festival/TV/agente de ventas: 'cuesheet timeline.edl -r rights.toml --strict' te da el music cue sheet y el informe de archivo que pide el checklist, y falla si alguna fuente no tiene derechos documentados. Pareja natural de speccheck (QC técnico → QC de derechos).

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
