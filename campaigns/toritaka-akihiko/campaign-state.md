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
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 2 audience was controlled → −1 from 6.)_

## Threads (open goals/vows; weighted)
1. **The First Ward (PRIMARY QUEST)** *(w3)* — recover the First Yotogi's lost sealing-relic ("the First Ward"); Hatsue's visions place it **north & west, in the old hills, near the founder's reputed tomb.** Wake it, use it to bar the Shinomen power. Charged by Hatsue **in secret.**
2. **The power in the deep Shinomen** *(w2)* — waking, hungry, *learning*; reaches through consecrated wards unaided. (Hatsue has been seeing it in meditation for 2 years.)
3. **The taken souls of Hibari Mura** *(w2)* — ~39 souls dragged into the deep Shinomen; reclaimable?
4. **Ninjō — To truly belong** *(w2)* — Hatsue named the wound aloud ("never quite either"); this charge is a chance to matter.
5. **The Scorpion covet Toritaka Province** *(w2)* — and must NOT learn the marches are open (secrecy = the clan's survival).
6. **Lord Hatsue's fraying mind** *(w1)* — she is *spending* her sight staring at the threat; how long can she hold?
7. **The secret Imperial blood** *(w1)* — Hatsue hinted "there may be more to you than your modesty admits."

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **The power in the deep Shinomen** *(w2)* — harvest souls / spread — malign, looming
- **Scorpion Clan** *(w2)* — seize Toritaka lands; would pounce if the failure leaks — **hostile / scornful**
- **Lord Toritaka Hatsue** *(w2)* — hold the line; recover the First Ward via Akihiko — his lord & secret-sharer, trusts him; fraying from her visions
- **Toritaka Jōji** *(w1)* — wry veteran Warden, riding with Akihiko on the quest — loyal
- **Suzu** *(w1)* — sole survivor of Hibari Mura, recovering in Akiro's care at Kyūden Toritaka — bonded to Akihiko
- **Toritaka Akiro (brother)** *(w1)* — tending Suzu; devoted; left behind

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Clocks (offscreen factions / threats / progress)
- **Scorpion land-grab scheme:** advancing (early)
- **Hatsue's decline:** worsening (slow) — tied to her visions of the Shinomen power
- **The Shinomen harvest:** active — the forest's edge is being grazed for souls
- **Secrecy risk:** if word of the failing wards reaches the Scorpion → they move politically

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a

## Current scene — Scene 3: *The Road to the Founder's Tomb* (just setting out)
- **Where / when:** departing Kyūden Toritaka at sunrise, riding north & west into the old Falcon hills.
- **Last beat:** Hatsue, lucid and formidable, charged Akihiko **in secret** to recover **the First Ward** (the First Yotogi's lost sealing-relic) — revealing she has been *seeing* the deep-Shinomen power in her meditations for two years, and naming his lifelong sense of not-belonging as the very reason she trusts him. He accepted, left Suzu with Akiro, took **Jōji + a troop of ashigaru**, and rode out.
- **Akihiko's state:** strife 0, fatigue 0, Void 2/2; unharmed. Honor 55 / Glory 35 / Status 36. Carrying Hatsue's secret charge.
- **Stakes / next:** reach the old hills & the founder's tomb; find/wake the First Ward; keep the secret; the Shinomen power grows bolder by the day. Scene 1 XP not yet awarded.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
