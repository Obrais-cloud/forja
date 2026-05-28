# forja

*Catálogo personal — todo lo que voy construyendo, con descripción y utilidad.*

_6 items registrados. Fuente de verdad: `registry.json`. Páginas por item en `entries/`._

## CLI
```
forja add                  # registrar (interactivo si faltan campos)
forja list [--kind X]      # ver el catálogo
forja show NAME            # ficha completa
forja edit NAME            # editar la ficha (Notas libres se conservan)
forja rm   NAME            # quitar
forja path NAME            # ruta registrada (útil: cd $(forja path X))
forja sync                 # regenerar este README desde registry.json
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
| **[codex-appserver-reaper](entries/codex-appserver-reaper.md)** | Activo en cron de macmini — no se invoca manual. Ver ~/.hermes/logs/codex-reaper.log para auditar reaps. | `macmini:/Users/remotework/.openclaw/scripts/codex-appserver-reaper.py` | — |

## tool

| nombre | utilidad | ruta | github |
|---|---|---|---|
| **[forja](entries/forja.md)** | Tras crear algo: forja add. Para encontrar: forja list / forja show NAME. Para saltar: cd $(forja path NAME). | `/Users/braisrevalderia/forja` | — |
| **[ollathink](entries/ollathink.md)** | Cuando un cliente recibe respuestas vacías o ensuciadas con <think>...</think> de modelos híbridos. Apuntas el cliente a http://localhost:11533 y olvidas el problema. Encaja en la cadena → ollathink → ollafifo → ollasecret → ollama. | `/Users/braisrevalderia/ollathink` | — |
| **[panoforge](entries/panoforge.md)** | Cuando tienes una imagen 360 (generada por IA o sacada de cámara) y quieres meterla de verdad en un Quest o en la instalación de Fillos do Vento. También para pósters, anaglifo screen-only o vídeo de avance MP4 para festivales sin headset. | `/Users/braisrevalderia/panoforge` | [link](https://github.com/Obrais-cloud/panoforge) |
