# Campaign State — <campaign name>

> **The single source of truth.** Overwrite this at the END of every scene.
> If a change happened in the fiction but isn't written here, it didn't happen.
> Validate: `python3 .claude/skills/l5r-gm/scripts/state.py validate campaign-state.md`

## Active set (the context filter — only matching content loads)
```yaml
active_set:
  sources:    [core]                 # + emerald-empire, courts-of-stone, shadowlands, fields-of-victory, celestial-realms, path-of-waves, writ-of-wilds
  clans:      []                     # PCs + likely antagonists; "universal" always in scope
  subsystems: [core-check, skirmish, duel, intrigue, downtime, advancement]
  modes:      []                     # court | war | wilderness | shadowlands-incursion | spiritual
  flags_allowed: []                  # mature | maho | gaijin  (confirm at session zero)
```

## Frame
- **Premise / tone:**
- **Adventure source:** Pure Mythic | Adventure Crafter | Prepared (`references/adventures/…`)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm) | Fate Check
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **System profile:** `system-profile.md`   ·   **Setting canon:** `setting-canon.md`

## Chaos Factor: 5
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic)_

## Threads (open goals/vows; weighted, max 3 entries each)
1.

## Characters & Factions (NPCs/forces — want — disposition; weighted, max 3 each; PC NOT listed)
-

## Adventure Features (prepared-adventure mode only)
-

## Clocks (offscreen factions / threats / progress)
-

## Overlays
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(or: N remaining, player-invoked only)_

## Adventure Crafter state (crafter mode only)
- Active Turning Point: —   ·   Theme priority: Action, Tension, Mystery, Social, Personal

## Current scene
- **Where / when:**
- **Last beat (2–3 sentences):** _<the campaign opens here>_
- **Stakes on the table:**
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
