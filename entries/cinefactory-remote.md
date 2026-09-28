# cinefactory-remote

| field | value |
|---|---|
| kind | `service` |
| path | `/Users/braisrevalderia/cinefactory-remote` |
| github | — |
| version | 0.2.0 |
| created | 2026-09-27 |
| tags | cinefactory, fillos-do-vento, mcp, scheduler, coeditor, codex, claude, fleet, macstudio, resolve, subtitles |

**What it is.** Control y herramientas del coeditor de Cinefactory en el Mac Studio. Horario único por proveedor (codex|claude|local), puerta 'cfr gate', turno exclusivo, encargos, decisiones, cuota de cortes narrativos, límite de revisiones. App web de feedback (/app: revisiones, comentarios con TC, decisiones A/B con vídeo, encargos, actividad, horario). Sincronización horaria de comentarios de Shade. Herramientas: premontaje (escenas en Resolve con tarjeta de razonamiento), eleccion (renders de decisión A/B), indice (búsqueda en transcripciones de Resolve), subtitula (Whisper + glosario de Fillos + traducción local). MCP en Tailscale 100.68.94.14:11460 con token; 38 tests.

**When to reach for it.** Para decidir cuándo y con qué IA se edita Fillos, dirigir al coeditor y revisar su trabajo desde cualquier sitio: app /app o MCP 'cinefactory' desde Claude Code; en el Mac Studio, bin/cfr, bin/premontaje, bin/eleccion, bin/indice, bin/subtitula.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
