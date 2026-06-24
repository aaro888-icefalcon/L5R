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
- **Premise / tone:** Samurai drama on the haunted marches of **Toritaka Province**. Akihiko — a scorned Minor-Clan warrior-priest of known Seppun (Imperial) blood — guards flesh and steel against rival schemes and the spirit-dark, aching to belong. Full-spectrum: duel · intrigue · skirmish · mass battle.
- **Adventure source:** **Pure Mythic** (mythic-gm owns oracle / scene pacing / Chaos / events / plot)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm)
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md` (+ this folder's `system-profile.md` overrides)
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: Arc 2 — *The Long Road Back*
_Each adventure has its own Threads & Characters Lists and its own Theme priority. A new adventure
begins when the current one's main Thread(s) Conclude or the player declares one — roll new Themes
from `bridge/theme-weights.md`, start fresh Lists, carry over still-relevant Characters/Threads,
archive the rest._
- **Adventure status:** **active** — Arc 1 (*The First Ward*) concluded as a capstone (the Dawn Mirror claimed, Imperial blood confirmed). Arc 2 opens with the journey home to deliver the Mirror to Lord Hatsue, through a week-stale, Scorpion-watched march — then the long work of wielding it (cure the mark · free the souls · bind the deep power).
- **Theme priority (this adventure):** **Tension › Action › Social › Mystery › Personal** — stored in `adventure.json` (`state.py adventure show campaigns/toritaka-akihiko`); _rolled `adventure_crafter.py themes --style drama`, Arc 2 open._

## Chaos Factor: 5
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 6: the barrow morning / route-planning ran calm and controlled → −1, 6→5.)_

## Threads — snapshot of `threads.json` (open goals/vows; weight = re-add, max 3; the dice roll the JSON)
1. **The Dawn Mirror & the binding-duty (PRIMARY QUEST)** *(w3)* — *Asahi no Kagami*, claimed (Sc.5), now borne by Akihiko. **Not a weapon — it BINDS** the deep power in captured sunlight; can cure his mark & free the taken souls. **Wake it:** Akihiko's Sacred sun-fire, at an **open dawn**, by a willing soul who takes the binding **as a lasting duty** (Akihiko, now the chain's new anchor). **Immediate:** deliver it safely to Lord Hatsue.
2. **The Mark — danger AND key** *(w3)* — the power's hook in Akihiko (**Marked by the Deep**); *double-edged*; **CONTAINED** (Sc.4, beacon blunted — quiet on the road so far). **The leash** by which he may drag the power to the Mirror to bind it.
3. **The power in the deep Shinomen** *(w2)* — nameless, older than the Empire & the Kami; beneath the forest's heart (north). **CANNOT be killed — only BOUND; its one fear is the sun.** Harvests souls to loose its 1200-year binding; fixed on Akihiko personally.
4. **The taken souls of Hibari Mura** *(w2)* — **gathered & woven toward some purpose, NOT destroyed.** Reclaimable, perhaps via the Mirror.
5. **The leak / the Scorpion close in** *(w2)* — Gennai (Scorpion spymaster) got limited word out (*a Falcon Warden rides the hills secretly*) and **escaped**. The handlers now hold the report and are acting on it; expect a probe while the marches seem open.
6. **Ninjō — To truly belong** *(w2)* — the binding-duty sets Akihiko apart even as he longs for a place. Jōji named it: this is not an errand with an end; the relic delivers *him*.
7. **Lord Hatsue's fraying mind** *(w1)* — spending her sight on the threat; declining at home while Akihiko is away.
8. **The Imperial (Seppun) blood — KNOWN heritage** *(w1)* — no buried secret: it runs through grandmother **Seppun Yuki** (minor scion of the Imperial guardian-family) → mother Sumiko → Akihiko, and grants the house a notch of extra Falcon standing. The Dawn Mirror recognized it. Still a thing high-Status others could exploit or resent.

## Characters & Factions — snapshot of `characters.json` (NPC/force — want — disposition; weight = re-add, max 3; PC NOT listed)
- **Gennai** *(w2)* — Scorpion spymaster posing as a medicine-peddler; charming, sharp, **escaped into the hills** with his swordsman — wants the Falcon's secret; **hostile, now exposed**
- **The Scorpion Clan** *(w2)* — seize Toritaka lands; their cell holds the leak and is moving — **hostile / closing in**
- **The power in the deep Shinomen** *(w2)* — harvest souls / spread — malign, looming (quiet near the PC for now)
- **Toritaka Jōji** *(w2)* — Akihiko's closest comrade-Warden, sworn confidant; senior to him; riding home at his side, blunt and loyal
- **Lord Toritaka Hatsue** *(w1)* — hold the line via Akihiko — his lord & secret-sharer; fraying, declining
- **The captured porter** *(w1)* — **left bound on the hill "for the Kami to judge"** (days ago now): freed himself, died, or retrieved by Gennai — and remembers the Warden who left him

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Campaign roster (persists across adventures: recurring NPCs, long arcs — full detail in `setting-canon.md`)
- **Gennai** — Scorpion spymaster; recurring antagonist who knows Akihiko's face and that he hides something.
- **Lord Toritaka Hatsue, "the Yotogi"** — Akihiko's lord, hard mentor, and secret-sharer; spending her sight on the deep Shinomen.
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, heretic Centipede sun-priest), Sumiko (mother; carrier of the Seppun blood), **Seppun Yuki** (grandmother; minor Imperial scion, family matriarch, keeper of the line's truth).
- **Suzu** — sole survivor of Hibari Mura's soul-harvest; soul-shocked, bonded to her rescuer; the only living witness; recovering with Akiro at Kyūden Toritaka.
- **Toritaka Jōji** — Akihiko's closest comrade-Warden; senior; rode to the barrow and home.
- **The Scattered Corps** — healers & wardens of many clans bound to Akihiko by a past crisis; far apart on duty (Eniko, Genzō, Bara, Hiroyuki, Saburō, Kasumi).
- **Long arcs:** the Seppun blood (who exploits or honors it); the Dawn Mirror's binding-duty (cure the mark · free the souls · bind the deep power).

## Clocks (offscreen factions / threats / progress — advanced by `tick.py`; ~2 days passed on the road)
- **The leak:** delivered → the Scorpion handlers are now **acting** on the report (a notch toward an active move)
- **Scorpion land-grab scheme:** advancing — likely probing Toritaka lands while Akihiko is away
- **Hatsue's decline:** worsening — her court notices her withdrawal in his absence
- **The Shinomen harvest:** active in the deep; the power's eye drifts (beacon-blunting holds near the PC for now)

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic)

## Current scene — Scene 7: *Down to the Marches* (Expected) — **at the herders' ford, dusk**
- **Where / when:** a broad herders' ford on the marches' main river, two days down from the old hills; sun setting behind the far bank; the bridge-town (and its likely Scorpion watcher) a half-day downstream.
- **Last beat (2–3 sentences):** Akihiko told Jōji plainly what the Dawn Mirror is and that his Seppun blood is no secret, then deferred the route to his senior. Jōji chose the slow, ugly, safe way — off the high-road, cross-country on herder-tracks, a quiet ford instead of the bridge-town. **Scene Test = 8 vs CF 6 → Expected:** two days of cautious travel passed without incident (earned safety); the Mark stayed quiet under the borne Mirror.
- **Akihiko's state:** strife **0**, fatigue 0, Void 2/2; Marked (contained, quiet); **bears the Dawn Mirror & its duty.** Honor 55 / Glory 35 / Status 36. XP 0.
- **Stakes on the table now:** the crossing decision — wade 100 paces of moving water onto an unseen far bank in failing light, or camp this side and give a night to the clock (Hatsue failing; Scorpion moving) and cross fresh at dawn (when he'd take his dawn-rite). Jōji defers the read to Akihiko.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md` (Keeper *Toritaka Genkō*; the gaki *Kuchinashi*; Arc 1 summary).
