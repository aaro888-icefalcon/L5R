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

## Chaos Factor: 6
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 1 was harrowing & largely out of his control → +1.)_

## Threads (open goals/vows; weighted)
1. **The taken souls of Hibari Mura** *(w2)* — ~40 souls dragged down/north into the deep Shinomen toward the power that *sent* Kuchinashi. Not destroyed — **taken.** Can they be reclaimed?
2. **Giri — Warden of the Physical** *(w2)* — serve Lord Hatsue; keep the Falcon's people, lands, and diplomats safe.
3. **Ninjō — To truly belong** *(w2)* — find true acceptance, or prove he needs no one.
4. **The Scorpion covet Toritaka Province** *(w2)* — uncover and thwart their land-grab.
5. **Lord Hatsue's fraying mind** *(w1)* — shield her and the clan from her decline, and from what she sees.
6. **The secret Imperial blood** *(w1)* — what it means, who knows, who would kill or use him for it.

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **The power in the deep Shinomen** *(w2)* — sent the gaki as a hook; harvesting souls — unknown, looming, malign
- **Scorpion Clan** *(w2)* — seize Toritaka lands by scheme — **hostile / scornful**
- **Lord Toritaka Hatsue** *(w2)* — hold the line / hide her decline — trusts Akihiko
- **Suzu** *(w1)* — reed-cutter's daughter; sole survivor of Hibari Mura, saved by Akihiko — traumatized, bonded to him
- **Toritaka Akiro (brother)** *(w1)* — become a healer, stay close — devoted
- **Moshi Hizashi (father)** *(w1)* — prove his healing-heresies — loving, scattered

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Clocks (offscreen factions / threats / progress)
- **Scorpion land-grab scheme:** advancing (early)
- **Hatsue's decline:** worsening (slow)
- **The Shinomen harvest:** active — souls being taken at the forest's edge (Hibari Mura was one bite)

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a

## Current scene — Scene 1 *The Silent Hamlet* → **RESOLVED** (aftermath)
- **Where / when:** Hibari Mura, just after full dark; the village silent and empty but for one living girl.
- **Last beat:** Akihiko sealed the soul-gate with Sacred sun-fire — **banishing Kuchinashi for good** and saving **Suzu**, the lone survivor — but the gate closed before he could reclaim the other ~40 villagers, whose souls were dragged down/north into the deep Shinomen toward the power that *sent* the gaki. The act broke his control: he **unmasked**, singing the dawn-hymn aloud in grief, Jōji silent at his side.
- **Akihiko's state:** strife **0** (post-unmask), fatigue 0, physically unharmed; **Void 2/2**; fire-nōdachi can be dismissed at will. Honor 55 / Glory 35 / Status 36 (unchanged).
- **Stakes / next:** care for Suzu; report the harvest to Lord Hatsue; the taken souls (rescue thread); the unknown Shinomen power. XP for Scene 1 not yet awarded.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
