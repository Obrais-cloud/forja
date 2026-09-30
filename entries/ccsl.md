# ccsl

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/ccsl` |
| github | — |
| version | 0.1.0 |
| created | 2026-09-30 |
| tags | filmmaking, delivery, ccsl, subtitles, spotting, edl, fcpxml, cli, python, deterministic, fillos-do-vento |

**What it is.** Genera la Combined Continuity & Spotting List a partir de un timeline (EDL, FCP7 XML, FCPXML) y un SRT/VTT: plano a plano con TC in/out, duración, pies 35mm, fuente, descripción (CSV de notas) y diálogos/rótulos. Aplana multipista (manda la pista superior; huecos = BLACK). --qc aplica reglas de cambio de plano a los subtítulos y --strict sale con 2. Salida md/csv/json/html/docx. Sólo probado con samples sintéticos; 24 tests.

**When to reach for it.** Cuando un agente de ventas o una TV pida el CCSL o dialogue list: 'ccsl locked.edl --srt en.srt --notes planos.csv -f docx -o CCSL.docx'. También sirve para comprobar el timing de los subtítulos frente a los cortes antes de entregar (--qc --strict). Va después de speccheck y cuesheet.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
