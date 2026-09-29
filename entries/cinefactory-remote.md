# cinefactory-remote

| field | value |
|---|---|
| kind | `service` |
| path | `/Users/braisrevalderia/cinefactory-remote` |
| github | https://github.com/Obrais-cloud/cinefactory-remote |
| version | 0.4.0 |
| created | 2026-09-27 |
| tags | cinefactory, fillos-do-vento, mcp, scheduler, coeditor, codex, claude, fleet, macstudio, resolve, subtitles |

**What it is.** Control y herramientas del coeditor de Cinefactory en el Mac Studio. Horario único por proveedor (codex|claude|local), puerta 'cfr gate', turno exclusivo, encargos, decisiones, cuota de cortes narrativos, límite de revisiones. App web de feedback (/app: revisiones, comentarios con TC, decisiones A/B con vídeo, encargos, actividad, horario). Sincronización horaria de comentarios de Shade. Herramientas: premontaje (escenas en Resolve con tarjeta de razonamiento), eleccion (renders de decisión A/B), indice (búsqueda en transcripciones de Resolve), subtitula (Whisper + glosario de Fillos + traducción local). MCP en Tailscale 100.68.94.14:11460 con token; 38 tests.

**When to reach for it.** Para decidir cuándo y con qué IA se edita Fillos, dirigir al coeditor y revisar su trabajo desde cualquier sitio: app /app o MCP 'cinefactory' desde Claude Code; en el Mac Studio, bin/cfr, bin/premontaje, bin/eleccion, bin/indice, bin/subtitula.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*

**0.3.0 (2026-09-28).** Avisos: `cfr/avisos.py` en el mini (parte de la noche 08:50 y vigía cada 15 min por Telegram, lee `/api/salud`). MCP también en Hermes principal y OpenClaw (`chief-of-staff`, `main`) con lista blanca de 8 herramientas; Codex del MacBook con lecturas auto-aprobadas. App con pestañas enlazables (`#ab`, `#rev`…). Revisión de derechos en cada premontaje (`bin/derechos`: cuesheet + reglas del largo; marca sin licencia, efectos de librería y audio sin clasificar).

**0.4.0 (2026-09-28).** Dictado por voz en la app: «🎙 Dictar» en revisiones y 🎙 en la nota A/B (con el minuto del vídeo); `POST /api/voz` transcribe en el Studio con mlx-whisper y el glosario de Fillos, borra el audio y solo rellena el cuadro. La app también por HTTPS dentro de la tailnet (`https://admins-mac-studio.tail79cef6.ts.net/app`, `tailscale serve` → 127.0.0.1; `also_localhost` en el servidor).
