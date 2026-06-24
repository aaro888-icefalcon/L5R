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
- **Adventure source:** Pure Mythic | Adventure Crafter | Prepared (`l5r-gm/bridge/adventures/…`)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm) | Fate Check
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md`
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: <title>
_Each adventure has its **own** Threads & Characters Lists and its own Theme priority. A **new
adventure** begins when the current one's main Thread(s) Conclude (the Threads List empties) or the
player declares one — then: roll new Themes (`adventure_crafter.py themes --style drama --campaign <dir>`,
weighted by the bridge's `theme-weights.md`), clear the Threads List, carry over only still-relevant
Characters/Threads, archive the rest._
- **Adventure status:** active | concluding | concluded
- **Theme priority (this adventure):** in `adventure.json` (`state.py adventure show <dir>`) — _rolled from `theme-weights.md`_

> **The Lists are JSON — the single source of truth.** Threads/Characters Lists + Theme priority live
> in `threads.json` · `characters.json` · `adventure.json` (entries carry `{name, weight, note}`; the
> dice roll over them, any length). `state.py init` scaffolds them; set weight/themes with `state.py
> thread|char|adventure …` and prose with `render_lists.py set-note …`. The `## Threads` /
> `## Characters & Factions` sections below are a **GENERATED** view — **never hand-edit them**;
> regenerate with `l5r-gm/scripts/render_lists.py render <dir> --in-place` (drift-check: `… --check`).

## Chaos Factor: 5
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic — see `bridge/chaos-tendency.md`)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
-

## Adventure Features (prepared-adventure mode only)
-

## Campaign roster (persists across adventures: recurring NPCs, long arcs)
-

## Clocks (offscreen factions / threats / progress — advanced by `tick.py` at bookkeeping)
-

## Overlays
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(or: N remaining, player-invoked only)_

## Adventure Crafter state (crafter mode only)
- Active Turning Point: —   ·   Theme priority: Personal, Social, Tension, Mystery, Action

## Current scene
- **Where / when:**
- **Last beat (2–3 sentences):** _<the campaign opens here>_
- **Stakes on the table:**
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
