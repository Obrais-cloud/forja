# forja

*Catálogo personal — todo lo que voy construyendo, con descripción y utilidad.*

_72 items registrados. Fuente de verdad: `registry.json`. Páginas por item en `entries/`._

## CLI
```
forja add                  # registrar (interactivo si faltan campos)
forja list [--kind X]      # ver el catálogo
forja show NAME            # ficha completa
forja edit NAME            # editar la ficha (Notas libres se conservan)
forja rm   NAME            # quitar
forja path NAME            # ruta registrada (útil: cd $(forja path X))
forja sync                 # regenerar este README desde registry.json
forja scan                 # candidatos en ~/ aún sin registrar
forja missing-gh           # cola de publicación (items sin github)
```

## launcher

| nombre | utilidad | ruta | github |
|---|---|---|---|
| **[relogin-hermes.command](entries/relogin-hermes.command.md)** | Cuando hermes vuelve a caer y prefieres no abrir terminal — doble clic en el Escritorio. | `/Users/braisrevalderia/Desktop/Relogin Hermes gpt-5.5.command` | — |

## script

| nombre | utilidad | ruta | github |
|---|---|---|---|
| **[hermes-codex-relogin](entries/hermes-codex-relogin.md)** | Cuando hermes falla con refresh_token_reused / context overflow. Se invoca a secas. Cubre el patrón hermes_codex_token_consumed_pattern. | `/Users/braisrevalderia/bin/hermes-codex-relogin.sh` | — |

## service

| nombre | utilidad | ruta | github |
|---|---|---|---|
| **[agentcrew](entries/agentcrew.md)** | Cuando arranques la orquestación de agentes para coordinar varios workers vía NATS — está en estado germinal. | `/Volumes/X10 Pro_A/AIPR/agentcrew` | — |
| **[codex-appserver-reaper](entries/codex-appserver-reaper.md)** | Activo en cron de macmini — no se invoca manual. Ver ~/.hermes/logs/codex-reaper.log para auditar reaps. | `macmini:/Users/remotework/.openclaw/scripts/codex-appserver-reaper.py` | — |
| **[fillos-mission-control](entries/fillos-mission-control.md)** | Para gestionar todas las submissions de Fillos do Vento (festivales, grants, prensa, distribución) sin Notion/Airtable. | `/Volumes/X10 Pro_A/AIPR/fillos-mission-control` | [link](https://github.com/Obrais-cloud/fillos-mission-control) |

## tool

| nombre | utilidad | ruta | github |
|---|---|---|---|
| **[chromacut](entries/chromacut.md)** | Cuando necesitas analizar la paleta cromática de un metraje (timeline de color, color script post-rodaje). | `/Users/braisrevalderia/chromacut` | — |
| **[clipdex](entries/clipdex.md)** | Cuando tienes horas de metraje y necesitas encontrar 'el plano del caballo blanco al amanecer' sin etiquetarlo a mano. | `/Users/braisrevalderia/clipdex` | — |
| **[cliplog](entries/cliplog.md)** | Cuando vuelves de rodaje con cientos de clips sin loggear y necesitas un shot log básico en minutos. | `/Users/braisrevalderia/cliplog` | — |
| **[clipvault](entries/clipvault.md)** | Cuando quieres una biblioteca buscable por significado en lugar de por nombre de archivo, todo local. | `/Users/braisrevalderia/clipvault` | — |
| **[dailies](entries/dailies.md)** | Cuando terminas el día de rodaje y necesitas mandar dailies sin pasarte la noche montándolas. | `/Users/braisrevalderia/dailies` | — |
| **[filmkit](entries/filmkit.md)** | Para festivales/distribución: convertir notas en YAML en un press kit publicable. Útil para DOCUFLOW (Fillos do Vento). | `/Users/braisrevalderia/filmkit` | — |
| **[fleetcheck](entries/fleetcheck.md)** | Por la mañana, ANTES de empezar: 'quién está vivo, qué responde, qué falla'. | `/Users/braisrevalderia/fleetcheck` | — |
| **[forja](entries/forja.md)** | Tras crear algo: forja add. Para encontrar: forja list / forja show NAME. Para saltar: cd $(forja path NAME). | `/Users/braisrevalderia/forja` | — |
| **[gitollama](entries/gitollama.md)** | Cuando quieres ayuda IA en git pero sin meter el repo en cloud (privado, on-prem). | `/Users/braisrevalderia/gitollama` | — |
| **[gollama](entries/gollama.md)** | Cuando necesitas operaciones de gestión de modelos con una TUI cómoda en lugar de comandos `ollama` sueltos. | `/Users/braisrevalderia/gollama` | [link](https://github.com/sammcj/gollama) |
| **[hubtrend](entries/hubtrend.md)** | Para tu rutina matinal: ver qué subió ayer a HF sin abrir navegador. | `/Users/braisrevalderia/hubtrend` | — |
| **[impulse-buy-freeze](entries/impulse-buy-freeze.md)** | Cuando quieres cortar las compras impulsivas con fricción (24h) sin bloquear sitios. | `/Users/braisrevalderia/impulse-buy-freeze` | [link](https://github.com/Obrais-cloud/impulse-buy-freeze) |
| **[localeval](entries/localeval.md)** | Para evaluar rápido un modelo nuevo en tu suite estándar de 34 preguntas y meterlo en la leaderboard. | `/Volumes/X10 Pro_A/AIPR/localeval` | — |
| **[localrag](entries/localrag.md)** | Cuando quieres preguntar a un corpus propio (notas, papers, código) y obtener respuestas citables, local. | `/Users/braisrevalderia/localrag` | — |
| **[modelbench](entries/modelbench.md)** | Para elegir qué modelo poner en cada slot del fleet por rendimiento real, no especs. | `/Users/braisrevalderia/modelbench` | [link](https://github.com/Obrais-cloud/modelbench) |
| **[olcaps](entries/olcaps.md)** | Cuando descargas un modelo nuevo y necesitas saber rápido qué capacidades tiene antes de meterlo en un agente o pipeline. | `/Volumes/X10 Pro_A/AIPR/olcaps` | [link](https://github.com/Obrais-cloud/olcaps) |
| **[olla](entries/olla.md)** | El punto de entrada cuando ya tienes muchas herramientas ollaX y necesitas un único comando que las descubra y arranque. | `/Volumes/X10 Pro_A/AIPR/olla` | — |
| **[ollabench](entries/ollabench.md)** | Cuando duplicas un modelo en varios nodos y necesitas saber a cuál enrutar para esa pareja. | `/Users/braisrevalderia/ollabench` | — |
| **[ollachat](entries/ollachat.md)** | Cuando quieres dar acceso a alguien a tus modelos por web sin instalar Docker / Open WebUI. | `/Users/braisrevalderia/ollachat` | — |
| **[ollaclean](entries/ollaclean.md)** | Cuando el disco está lleno y necesitas saber qué modelos puedes borrar sin romper otros que comparten blobs. | `/Volumes/X10 Pro_A/AIPR/ollaclean` | — |
| **[ollacode](entries/ollacode.md)** | Cuando configuras Claude Code con un backend local y necesitas saber qué modelo encaja mejor en la API de Anthropic. | `/Volumes/X10 Pro_A/AIPR/ollacode` | — |
| **[ollacost](entries/ollacost.md)** | Para justificar (en charla, en propuesta) cuánto vale el fleet local frente a OpenAI/Anthropic API. | `/Users/braisrevalderia/ollacost` | — |
| **[ollactl](entries/ollactl.md)** | Cuando ya tienes 30 herramientas ollaX y necesitas un único launcher / discovery. | `/Users/braisrevalderia/ollactl` | — |
| **[olladash](entries/olladash.md)** | Cuando quieres una pestaña en el navegador con el estado del fleet en vez de TUI. | `/Users/braisrevalderia/olladash` | — |
| **[olladiff](entries/olladiff.md)** | Cuando un modelo recibe update y necesitas saber si la calidad para TUS tests bajó o subió. | `/Volumes/X10 Pro_A/AIPR/olladiff` | — |
| **[olladiff-local](entries/olladiff-local.md)** | Cuando dudas entre dos modelos para una tarea concreta — el side-by-side te lo decide. | `/Users/braisrevalderia/olladiff-local` | — |
| **[ollaeval](entries/ollaeval.md)** | Antes de promover un modelo a producción/agente: pasarle suite de eval propia y comparar con baseline. | `/Users/braisrevalderia/ollaeval` | — |
| **[ollafifo](entries/ollafifo.md)** | Cuando varios clientes pegan a la vez al mismo Ollama y revientan VRAM con 500-OOM. | `/Users/braisrevalderia/ollafifo` | [link](https://github.com/Obrais-cloud/ollafifo) |
| **[ollafim](entries/ollafim.md)** | Cuando quieres autocompletado IDE local sin Copilot/Codex en la nube. | `/Users/braisrevalderia/ollafim` | [link](https://github.com/Obrais-cloud/ollafim) |
| **[ollafit](entries/ollafit.md)** | ANTES de cargar un modelo grande en M-series: calcula el num_ctx máximo seguro para tu RAM unificada. | `/Volumes/X10 Pro_A/AIPR/ollafit` | — |
| **[ollafleet](entries/ollafleet.md)** | Cuando quieres una única URL para tus clientes que reparta entre nodos del fleet sin que ellos sepan que hay varios. | `/Volumes/X10 Pro_A/AIPR/ollafleet` | — |
| **[ollaflow](entries/ollaflow.md)** | Para multi-paso (extract → reason → reformat) usando distintos modelos por paso, declarado en YAML. | `/Users/braisrevalderia/ollaflow` | — |
| **[ollahealth](entries/ollahealth.md)** | Cuando sospechas que un nodo está degradado o que un modelo se borró sin querer. | `/Users/braisrevalderia/ollahealth` | — |
| **[ollalog](entries/ollalog.md)** | Cuando quieres saber cuánto te ahorra correr local vs API cloud (números para justificar el fleet). | `/Users/braisrevalderia/ollalog` | — |
| **[ollama-fleet-mcp](entries/ollama-fleet-mcp.md)** | Cuando usas Claude Code y quieres exponer el fleet local como tools MCP (routing + bench desde dentro del agente). | `/Volumes/X10 Pro_A/AIPR/ollama-fleet-mcp` | — |
| **[ollama-structify](entries/ollama-structify.md)** | Cuando necesitas convertir texto libre en JSON con un esquema definido, vía LLM local. | `/Users/braisrevalderia/ollama-structify` | — |
| **[ollamatop](entries/ollamatop.md)** | En una pestaña fija: ver qué modelos hay vivos, carga y memoria por nodo, mientras trabajas. | `/Users/braisrevalderia/ollamatop` | — |
| **[ollamcp](entries/ollamcp.md)** | Cuando quieres montar un agente local con tools MCP sin pagar Claude API o Codex. | `/Users/braisrevalderia/ollamcp` | — |
| **[ollameter](entries/ollameter.md)** | Cuando necesitas métricas multi-tenant del fleet (quién consume qué) más allá de un solo proxy. | `/Users/braisrevalderia/ollameter` | — |
| **[ollametrics](entries/ollametrics.md)** | Cuando ya tienes Grafana/Prometheus y quieres ver Ollama en los mismos paneles que el resto del stack. | `/Users/braisrevalderia/ollametrics` | — |
| **[ollapark](entries/ollapark.md)** | Antes de una sesión intensiva: calientas el set de modelos que vas a usar para tener TTFT bajo. | `/Users/braisrevalderia/ollapark` | — |
| **[ollapipe](entries/ollapipe.md)** | Cuando una tarea necesita varias pasadas con modelos distintos (extraer → razonar → reformatear) en un solo comando. | `/Volumes/X10 Pro_A/AIPR/ollapipe` | — |
| **[ollaprompt](entries/ollaprompt.md)** | Cuando tus prompts útiles están dispersos por chats y notas — esto los versiona como código. | `/Users/braisrevalderia/ollaprompt` | — |
| **[ollarag](entries/ollarag.md)** | Cuando quieres hacer Q&A sobre un repo o un corpus de notas sin levantar Qdrant/Chroma/etc. | `/Volumes/X10 Pro_A/AIPR/ollarag` | — |
| **[ollarena](entries/ollarena.md)** | Para shootouts más largos: muchos prompts, muchos modelos, ELO que evoluciona. | `/Users/braisrevalderia/ollarena` | — |
| **[ollaroute](entries/ollaroute.md)** | Cuando quieres una sola URL que reparta solo entre tus modelos locales según el prompt, sin elegir a mano. | `/Users/braisrevalderia/ollaroute` | [link](https://github.com/Obrais-cloud/ollaroute) |
| **[ollasecret](entries/ollasecret.md)** | Cuando un agente IA podría meter sin querer claves/secretos en un prompt — esto los redacta antes de salir. | `/Users/braisrevalderia/ollasecret` | [link](https://github.com/Obrais-cloud/ollasecret) |
| **[ollasync](entries/ollasync.md)** | Para mantener consistencia de inventario de modelos entre nodos sin pulls manuales en cada uno. | `/Users/braisrevalderia/ollasync` | — |
| **[ollatag](entries/ollatag.md)** | Cuando tienes 30 modelos descargados y quieres elegir rápido por tarea ('para razonar', 'para resumir', 'para código'). | `/Volumes/X10 Pro_A/AIPR/ollatag` | — |
| **[ollatest](entries/ollatest.md)** | Cuando empiezas un módulo Python sin tests y quieres una primera batería razonable generada localmente. | `/Volumes/X10 Pro_A/AIPR/ollatest` | — |
| **[ollathink](entries/ollathink.md)** | Cuando un cliente recibe respuestas vacías o ensuciadas con <think>...</think> de modelos híbridos. Apuntas el cliente a http://localhost:11533 y olvidas el problema. Encaja en la cadena → ollathink → ollafifo → ollasecret → ollama. | `/Users/braisrevalderia/ollathink` | — |
| **[ollausage](entries/ollausage.md)** | Cuando necesitas un número 'cuántos tokens consumí, cuánto me habría costado en cloud' para justificar el fleet. | `/Volumes/X10 Pro_A/AIPR/ollausage` | — |
| **[ollaverse](entries/ollaverse.md)** | Para enseñar el ecosistema (charlas, perfil, links). El catálogo público frente a `forja` (catálogo interno). | `/Users/braisrevalderia/ollaverse` | [link](https://github.com/Obrais-cloud/ollaverse) |
| **[ollawake](entries/ollawake.md)** | Justo antes de rutear una petición a un nodo dormido: lo despiertas con confirmación. | `/Users/braisrevalderia/ollawake` | [link](https://github.com/Obrais-cloud/ollawake) |
| **[ollawatch](entries/ollawatch.md)** | Cuando trabajas con varios nodos del fleet y quieres ver carga/modelos en vivo en una pestaña. | `/Volumes/X10 Pro_A/AIPR/ollawatch` | — |
| **[panoforge](entries/panoforge.md)** | Cuando tienes una imagen 360 (generada por IA o sacada de cámara) y quieres meterla de verdad en un Quest o en la instalación de Fillos do Vento. También para pósters, anaglifo screen-only o vídeo de avance MP4 para festivales sin headset. | `/Users/braisrevalderia/panoforge` | [link](https://github.com/Obrais-cloud/panoforge) |
| **[promptcmp](entries/promptcmp.md)** | Cuando dudas entre 3-4 modelos para una tarea concreta: mismo prompt, comparación visual + markdown para luego decidir. | `/Volumes/X10 Pro_A/AIPR/promptcmp` | — |
| **[remote-terminal-pwa](entries/remote-terminal-pwa.md)** | Acceso rápido a tu shell desde el móvil cuando estás fuera y sin SSH client nativo. | `/Users/braisrevalderia/remote-terminal-pwa` | — |
| **[scenesnap](entries/scenesnap.md)** | Cuando necesitas notas de análisis cinematográfico sobre planos concretos (referencias, mood board). | `/Users/braisrevalderia/scenesnap` | — |
| **[scriptbreak](entries/scriptbreak.md)** | Para pre-producción: convertir un Fountain en un desglose por escena en minutos, sin Excel a mano. | `/Users/braisrevalderia/scriptbreak` | — |
| **[shellsense](entries/shellsense.md)** | Cuando recuerdas QUÉ hiciste (limpiar docker, comprimir vídeo…) pero no el comando exacto. | `/Users/braisrevalderia/shellsense` | — |
| **[shotcall](entries/shotcall.md)** | Pre-producción: del Fountain a una shot list inicial que luego refinas en preparación de rodaje. | `/Users/braisrevalderia/shotcall` | — |
| **[shotgen](entries/shotgen.md)** | Cuando quieres un animatic rápido para pitch/financiación o para previs sin storyboard artist. | `/Users/braisrevalderia/shotgen` | [link](https://github.com/Obrais-cloud/shotgen) |
| **[Siliv](entries/siliv.md)** | Cuando trabajas con modelos grandes en M-series y necesitas vigilar/ajustar la asignación VRAM unificada desde la barra de menús. | `/Volumes/X10 Pro_A/AIPR/Siliv` | — |
| **[takelog](entries/takelog.md)** | En el set, durante el rodaje: registrar takes contra la shot list sin papel y exportar limpio para edición. | `/Users/braisrevalderia/takelog` | — |
| **[toolprobe](entries/toolprobe.md)** | Antes de meter un modelo en un agente con tools: validar que dispara JSON tool calls correctamente. | `/Users/braisrevalderia/toolprobe` | — |
| **[visionlint](entries/visionlint.md)** | Pre-publicación: pasar capturas de una UI/diseño y obtener crítica de UX automatizada. | `/Users/braisrevalderia/visionlint` | — |
