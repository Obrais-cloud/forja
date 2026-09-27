# speccheck

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/speccheck` |
| github | https://github.com/Obrais-cloud/speccheck |
| version | 0.2.0 |
| created | 2026-09-24 |
| tags | video ffmpeg qc delivery filmmaking cli python deterministic fillos-do-vento |

**What it is.** QC de entregables audiovisuales con ffprobe/ffmpeg: valida un vídeo (o una carpeta entera con --all) contra un spec de entrega — códec, resolución, fps, escaneo, pix_fmt, faststart mp4, audio, sample rate, loudness EBU R128/true peak. PASS/WARN/FAIL, exit≠0. 11 presets, incluidos los 4 de Fillos do Vento (feature DCP-source, TV 52min, instalación front-wall, VR) derivados de los másters reales.

**When to reach for it.** Antes de mandar un máster a festival/broadcaster/plataforma o de cerrar un paquete de entrega: 'speccheck master.mov --spec X' te confirma que cumple, y 'speccheck carpeta/ --all' clasifica cada entregable a su preset (o marca el que no cuadra). Presets YAML propios o --from-brief con Ollama local.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
