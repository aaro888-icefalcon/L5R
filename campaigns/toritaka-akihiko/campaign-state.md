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
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 3 sprung a Scorpion trap, the secret leaked, the spymaster escaped → +1.)_

## Threads (open goals/vows; weighted)
1. **The First Ward (PRIMARY QUEST)** *(w3)* — recover the First Yotogi's lost sealing-relic ("the First Ward"); Hatsue's visions place it **north & west, in the old hills, near the founder's reputed tomb.** Wake it, use it to bar the Shinomen power. Charged by Hatsue **in secret.**
2. **The leak / the Scorpion close in** *(w3)* — a Scorpion cell on the road (the "peddler" **Gennai** + crew) got word out that the Falcon Warden rides the hills on a secret errand. **Gennai escaped**; his **porter is Akihiko's prisoner.** The Scorpion now suspect the marches are troubled — expect them to move.
3. **The power in the deep Shinomen** *(w2)* — waking, hungry, *learning*; reaches through consecrated wards unaided. (Hatsue has seen it for 2 years.)
4. **The taken souls of Hibari Mura** *(w2)* — ~39 souls dragged into the deep Shinomen; reclaimable?
5. **Ninjō — To truly belong** *(w2)* — Hatsue named the wound; this charge is a chance to matter (and now, a failure to swallow).
6. **Lord Hatsue's fraying mind** *(w1)* — she is *spending* her sight on the threat; how long can she hold?
7. **The secret Imperial blood** *(w1)* — Hatsue hinted "more to you than your modesty admits."

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **Gennai** *(w2)* — Scorpion spymaster posing as a medicine-peddler; charming, sharp, **escaped into the hills** with his swordsman — wants the Falcon's secret; **hostile, now exposed**
- **The Scorpion Clan** *(w2)* — seize Toritaka lands; their cell just got word the marches may be open — **hostile / closing in**
- **The power in the deep Shinomen** *(w2)* — harvest souls / spread — malign, looming
- **Lord Toritaka Hatsue** *(w1)* — hold the line via Akihiko — his lord & secret-sharer; fraying
- **The captured porter** *(w1)* — a low Scorpion operative, taken alive on the hill — sullen, knows *something* (handlers, the message, the network)

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

## Current scene — Scene 3: *A Meeting on the Road* → the sprung trap (night, hill saddle)
- **Where / when:** a cold saddle between two bald hills in the old highlands, dead of night; camp roused.
- **Last beat:** A smooth "peddler," **Gennai**, joined them on the road and probed for their destination; Akihiko's thin cover ("visiting a friend") didn't fool him. Akihiko rode on and watched — and at night caught Gennai's "porter" slipping off to a hooded contact. He roused the camp and **charged on horseback** to stop the courier, but his horse stumbled on shale at the crest: **the message got passed off and away (the leak succeeded).** He rode down and **captured the porter** alive; **Gennai and the swordsman escaped** into the dark.
- **Akihiko's state:** **strife 5/8** (pursuit + Fear of Failure), fatigue 0, Void 2/2; unharmed. Honor 55 / Glory 35 / Status 36.
- **On the table now:** a **captured Scorpion porter** to question; Gennai loose; the leak racing to Scorpion handlers; still days from the founder's tomb; dawn hours off. Scene 1 XP not yet awarded.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
