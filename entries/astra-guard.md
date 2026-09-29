# astra-guard

| field | value |
|---|---|
| kind | `script` |
| path | `/Users/braisrevalderia/.local/bin/astra-guard.py` |
| github | — |
| version | 0.2.0 |
| created | 2026-09-28 |
| tags | models, fleet, guard, launchd, codex, hermes, openclaw, gpt-6-astra, corsair |

**What it is.** Guardián de modelos: mantiene gpt-6-astra como principal y Corsair qwen3.8:27b como respaldo en Codex, Hermes y el canónico de OpenClaw; restaura con copia de seguridad y avisa por Telegram

**When to reach for it.** Cuando algo (una actualización, un agente, un cambio manual) pueda cambiar el modelo principal o la cadena de respaldo de la flota y quieras que vuelva solo a lo decidido

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*

**Despliegue (2026-09-28).** Mismo script en MacBook, mac mini y Mac Studio: `~/.local/bin/astra-guard.py` + launchd `com.fleet.astra-guard` (cada 30 min y al arrancar). Log: `~/Library/Logs/astra-guard.log`.

**Qué vigila.**
- Codex (`~/.codex/config.toml`): `model = "gpt-6-astra"`.
- Hermes (`~/.hermes/config.yaml`): la cadena `fallback_providers` = Corsair qwen3.8:27b → gpt-5.6-terra. Solo toca un Hermes cuyo modelo principal ya sea astra (el principal lo impone `hermes-config-watchdog`).
- OpenClaw: solo comprueba el canónico (`models-canonical.json`); lo impone `auto-repair.sh`.

**Cambiar la decisión.** Editar `PRIMARY` / `HERMES_FB` del script en las tres máquinas ANTES que las configuraciones, o el guardián las revertirá.

**Incidente v0.1 (2026-09-28).** Una regex con `re.S` (DOTALL) borró ~900 líneas del `config.yaml` de Hermes en el mini y tocó un Hermes local ajeno en el MacBook. Restaurado en ~2 min desde sus copias `.bak-*-astra-guard`. v0.2: sin DOTALL y probado contra copias antes de instalar. Lección: nunca `re.S` para bloques YAML; probar guardianes que reescriben config contra copias.

