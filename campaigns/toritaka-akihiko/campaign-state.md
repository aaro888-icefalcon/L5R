# Campaign State — Toritaka Akihiko, Warden of the Sun

> **The single source of truth.** Overwrite this at the END of every scene.
> If a change happened in the fiction but isn't written here, it didn't happen.
> Validate: `python3 .claude/skills/l5r-gm/scripts/state.py validate campaign-state.md`

## Active set (the context filter — only matching content loads)
```yaml
active_set:
  sources:    [core, shadowlands, celestial-realms]
  clans:      [falcon, centipede, scorpion, mantis, phoenix]
  subsystems: [core-check, skirmish, duel, intrigue, mass-battle, downtime, advancement]
  modes:      [court, war, wilderness, spiritual]
  flags_allowed: []        # maho | mature | gaijin — OFF unless player opts in aloud
```

## Frame
- **Premise / tone:** Samurai drama on the haunted marches of **Toritaka Province**. Akihiko — a scorned Minor-Clan warrior-priest, secretly Imperial-blooded — guards flesh and steel against rival schemes and the spirit-dark, aching to belong. Full-spectrum: duel · intrigue · skirmish · mass battle.
- **Adventure source:** **Pure Mythic** (mythic-gm owns oracle / scene pacing / Chaos / events / plot)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm)
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **System profile:** `system-profile.md`   ·   **Setting canon:** `setting-canon.md`

## Chaos Factor: 5
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic)_

## Threads (open goals/vows; weighted)
1. **Giri — Warden of the Physical** *(w2)* — serve Lord Hatsue; keep the Falcon's people, lands, and diplomats safe.
2. **Ninjō — To truly belong** *(w2)* — find true acceptance, or prove he needs no one.
3. **The Scorpion covet Toritaka Province** *(w2)* — uncover and thwart their land-grab.
4. **Lord Hatsue's fraying mind** *(w1)* — shield her and the clan from her decline, and from what she sees.
5. **The secret Imperial blood** *(w1)* — what it means, who knows, who would kill or use him for it.

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **Scorpion Clan** *(w2)* — seize Toritaka lands by scheme — **hostile / scornful**
- **Lord Toritaka Hatsue** *(w2)* — hold the line / hide her decline — trusts Akihiko
- **Toritaka Akiro (brother)** *(w1)* — become a healer, stay close — devoted
- **The Shinomen spirit-dark** *(w1)* — ?? — looming threat
- **Moshi Hizashi (father)** *(w1)* — prove his healing-heresies — loving, scattered

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Clocks (offscreen factions / threats / progress)
- **Scorpion land-grab scheme:** advancing (early)
- **Hatsue's decline:** worsening (slow)

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a

## Current scene
- **Where / when:** _Scene 1 — to be framed._
- **Last beat (2–3 sentences):** _The campaign opens here. Session Zero complete: Toritaka Akihiko created, world seeded._
- **Stakes on the table:** _set at scene frame (pre-commit before any roll)._
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
