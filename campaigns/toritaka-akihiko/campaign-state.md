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

## Chaos Factor: 7
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 4: the deep-Shinomen power reached through a portal and MARKED Akihiko — apex-negative, out of his control → +1.)_

## Threads (open goals/vows; weighted)
1. **The First Ward (PRIMARY QUEST)** *(w3)* — recover the First Yotogi's lost sealing-relic; **north & west, the old hills, the founder's tomb** (~2 days on, vision-compass confirmed). **VISION-CONFIRMED (Sc.4): the First Ward once BOUND this very power — it works, and is why the thing fears the sun.** **COMMUNE (Sc.4): the tomb is *kept* — something ancient holds vigil over the founder's rest (guardian; for or against, unknown).**
2. **The Mark — bound to the Deep** *(w3)* — the power set a hook in Akihiko's soul (**Marked by the Deep**); spirits of the deep are drawn to him; *double-edged* (he can faintly sense the power in return). **CONTAINED (Sc.4 Cleansing Rite):** can't deepen/spread, beacon blunted (the power struggles to reach him for a while) — but only the First Ward (or the power's undoing) truly cures it.
3. **The power in the deep Shinomen** *(w2)* — vast, ancient (older than the Empire), beneath the forest's heart (north); reaches through wards unaided; bound once before. Now fixed on Akihiko personally.
4. **The taken souls of Hibari Mura** *(w2)* — **VISION-CONFIRMED: gathered & woven toward some purpose, NOT destroyed** — the village's people still 'singing' among a galaxy of stolen souls. Reclaimable?
5. **The leak / the Scorpion close in** *(w2)* — Gennai (Scorpion spymaster) got limited word out (*a Falcon Warden rides the hills secretly*) and **escaped**; his porter was left bound on the hill. Expect them to probe.
6. **Ninjō — To truly belong** *(w2)* — Hatsue named the wound; this charge is his chance to matter.
7. **Lord Hatsue's fraying mind** *(w1)* — spending her sight on the threat.
8. **The secret Imperial blood** *(w1)* — Hatsue hinted "more to you than your modesty admits."

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **Gennai** *(w2)* — Scorpion spymaster posing as a medicine-peddler; charming, sharp, **escaped into the hills** with his swordsman — wants the Falcon's secret; **hostile, now exposed**
- **The Scorpion Clan** *(w2)* — seize Toritaka lands; their cell just got word the marches may be open — **hostile / closing in**
- **The power in the deep Shinomen** *(w2)* — harvest souls / spread — malign, looming
- **Lord Toritaka Hatsue** *(w1)* — hold the line via Akihiko — his lord & secret-sharer; fraying
- **The captured porter** *(w1)* — **left bound on the hill "for the Kami to judge"** (alive, abandoned, just out of reach of his knife). Latent: may free himself, die, or be retrieved by Gennai — and remember the Warden who left him.

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Clocks (offscreen factions / threats / progress)
- **The leak in motion:** the Scorpion message is loose — word of the Falcon's secret errand racing to handlers (**advancing fast**)
- **Scorpion land-grab scheme:** advancing
- **Hatsue's decline:** worsening (tied to her visions)
- **The Shinomen harvest:** active

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a

## Current scene — Scene 4 *The Reaching Cold* → resolved; camped & rallied, ~2 days from the tomb
- **Where / when:** a defensible shoulder of rock beyond the cursed defile; the company camped, watches set, rested.
- **Last beat:** the deep-Shinomen power Marked Akihiko through a portal (his Void-bolstered sun-ward fell one short). He steadied the men with dry calm; **confided the full truth to Jōji** (who's all-in — and that keeps Hatsue's "three mouths"); then rested, communed, and worked a Cleansing Rite that **contained the mark** (beacon blunted). The kami affirmed the road and warned the **founder's tomb is *kept* by something ancient.**
- **Akihiko's state:** **strife 1/8**, fatigue 0, **Void 1/2**; **Marked by the Deep — contained.** Honor 55 / Glory 35 / Status 36.
- **On the table now:** ride the last ~2 days to the founder's tomb; a guardian waits there; the leak/Gennai loose behind; the mark's reprieve is temporary. Scene 1 XP still un-awarded.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
