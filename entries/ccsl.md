# ccsl

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/ccsl` |
| github | https://github.com/Obrais-cloud/ccsl |
| version | 0.1.1 |
| created | 2026-09-30 |
| tags | filmmaking, delivery, ccsl, subtitles, spotting, edl, fcpxml, cli, python, deterministic, fillos-do-vento |

**What it is.** Genera la Combined Continuity & Spotting List a partir de un timeline (EDL, FCP7 XML, FCPXML) y un SRT/VTT: plano a plano con TC in/out, duración, pies 35mm, fuente, descripción (CSV de notas) y diálogos/rótulos. Aplana multipista (manda la pista superior; huecos = BLACK). --qc aplica reglas de cambio de plano a los subtítulos y --strict sale con 2. Salida md/csv/json/html/docx. 27 tests. Validado 2026-09-30 con 8 premontajes reales de Fillos (Resolve FCP7 XML, 23,976 fps): planos y duración idénticos a Resolve. Falta validar subtítulos con un SRT real.

**When to reach for it.** Cuando un agente de ventas o una TV pida el CCSL o dialogue list: 'ccsl locked.edl --srt en.srt --notes planos.csv -f docx -o CCSL.docx'. También sirve para comprobar el timing de los subtítulos frente a los cortes antes de entregar (--qc --strict). Va después de speccheck y cuesheet.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
