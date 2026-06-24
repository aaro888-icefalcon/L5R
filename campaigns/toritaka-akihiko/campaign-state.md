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

## Chaos Factor: 6
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 8: an Interrupt the deep power drove — a soul-harvest puppet ambushed the camp and the Falcon mask shattered (unmask); reactive & chaotic → +1, 5→6.)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Dawn Mirror & the binding-duty (PRIMARY QUEST)** *(w3)* — *Asahi no Kagami*, claimed (Sc.5), now borne by Akihiko. Not a weapon — it BINDS the deep power in captured sunlight; can cure his mark & free the taken souls. Wake it: Akihiko's Sacred sun-fire at an open dawn, by a willing soul who takes the binding as a lasting duty (Akihiko, the chain's new anchor). Immediate: deliver it safely to Lord Hatsue.
2. **The Mark — danger AND key (the leash)** *(w3)* — The power's hook in Akihiko (Marked by the Deep); CONTAINED but used as the conduit (Sc.8) to reach & sear the power — double-edged, proven both ways. The leash by which he may drag the power to the Mirror.
3. **The power in the deep Shinomen** *(w2)* — Nameless, older than the Empire & the Kami; cannot be killed, only BOUND; its one fear is the sun. STUNG (Sc.8): Akihiko ran sun-fire up a soul-thread and wounded it — first hurt in 1200 years; it now knows his fire all the way down, fixed on him.
4. **The taken souls of Hibari Mura** *(w2)* — Gathered & woven toward some purpose, NOT destroyed. PROVEN partly reclaimable (Sc.8): Akihiko's sun-fire severed one puppet-thread & freed a boy's body — the soul still in the deep (the Mirror is the full cure).
5. **The leak / the Scorpion closing in** *(w2)* — Gennai got limited word out (a Falcon Warden rides the hills secretly) and escaped. The handlers now hold the report and are acting on it; expect a probe while the marches seem open.
6. **Ninjō — to truly belong** *(w2)* — The binding-duty sets Akihiko apart even as he longs for a place. Jōji named it: not an errand with an end — the relic delivers him.
7. **Lord Hatsue's fraying mind** *(w1)* — Spending her sight on the threat; declining at home while Akihiko is away.
8. **The Imperial (Seppun) blood — known heritage** *(w1)* — No buried secret: runs through grandmother Seppun Yuki (minor Imperial scion) → Sumiko → Akihiko, and grants the house a notch of extra Falcon standing. The Dawn Mirror recognized it. Still a thing high-Status others could exploit or resent.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Gennai (Scorpion spymaster)** *(w2)* — Posed as a medicine-peddler; charming, sharp, escaped into the hills with his swordsman — wants the Falcon's secret; hostile, now exposed.
- **The Scorpion Clan** *(w2)* — Seize Toritaka lands; their cell holds the leak and is moving — hostile / closing in.
- **The power in the deep Shinomen** *(w2)* — Harvest souls / spread — malign, looming (quiet near the PC for now).
- **Toritaka Jōji** *(w2)* — Akihiko's closest comrade-Warden, sworn confidant; senior to him; riding home at his side, blunt and loyal.
- **Lord Toritaka Hatsue** *(w1)* — Hold the line via Akihiko — his lord & secret-sharer; fraying, declining.
- **The captured porter** *(w1)* — Left bound on the hill 'for the Kami to judge' (days ago): freed himself, died, or retrieved by Gennai — and remembers the Warden who left him.
- **Matsu Toshimoko (Emerald Magistrate)** *(w2)* — Emerald Magistrate (Lion/Matsu), gray-templed, by-the-book; came to the marches over the silenced villages & the Scorpion border. Witnessed Akihiko free the husk-boy with sun-fire. Wary, duty-bound, DEFERRED not won over — rides to Kyūden Toritaka for Lord Hatsue's answers; 'resumes on the Emperor's terms' if they don't hold.
- **The freed boy of Hibari Mura** *(w1)* — A Hibari Mura reed-cutter the deep power puppeted across the ford; Akihiko severed the thread with Sacred sun-fire. Body alive & reclaimed, soul still gathered in the deep — soul-empty like Suzu.

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Campaign roster (persists across adventures: recurring NPCs, long arcs — full detail in `setting-canon.md`)
- **Gennai** — Scorpion spymaster; recurring antagonist who knows Akihiko's face and that he hides something.
- **Lord Toritaka Hatsue, "the Yotogi"** — Akihiko's lord, hard mentor, and secret-sharer; spending her sight on the deep Shinomen.
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, heretic Centipede sun-priest), Sumiko (mother; carrier of the Seppun blood), **Seppun Yuki** (grandmother; minor Imperial scion, family matriarch, keeper of the line's truth).
- **Suzu** — sole survivor of Hibari Mura's soul-harvest; soul-shocked, bonded to her rescuer; the only living witness; recovering with Akiro at Kyūden Toritaka.
- **Toritaka Jōji** — Akihiko's closest comrade-Warden; senior; rode to the barrow and home.
- **The Scattered Corps** — healers & wardens of many clans bound to Akihiko by a past crisis; far apart on duty (Eniko, Genzō, Bara, Hiroyuki, Saburō, Kasumi).
- **Matsu Toshimoko** — Emerald Magistrate (Lion); witnessed the ford and rides to Kyūden Toritaka for the daimyō's answers. Imperial law, wary, deferred not won.
- **The freed boy of Hibari Mura** — reclaimed from the deep power's puppetry by Akihiko's sun-fire; body alive, soul still taken (a second soul-shocked survivor, like Suzu).
- **Long arcs:** the Seppun blood (who exploits or honors it); the Dawn Mirror's binding-duty (cure the mark · free the souls · bind the deep power).

## Clocks (offscreen factions / threats / progress — advanced by `tick.py`; a night passed at the ford)
- **The leak / Scorpion:** handlers acting on the report; the marches are being watched — though an Emerald Magistrate found Akihiko before the Scorpion did
- **Scorpion land-grab scheme:** advancing — probing Toritaka lands while Akihiko is away; border tension now drawing Imperial attention
- **Hatsue's decline:** worsening — and an Emerald Magistrate now rides to her gate demanding answers she may be too frayed to manage
- **The Shinomen harvest:** active — the deep power spent reach to strike Akihiko at the ford and was **WOUNDED** (sun-fire up a soul-thread); repelled here, but fixed on him and aware his fire can hurt it
- **NEW — Imperial scrutiny:** Matsu Toshimoko (Emerald Magistrate) rides with the company to Kyūden Toritaka; the secret errand & the Mirror are now under the Emperor's eye

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic)

## Current scene — Scene 8: *The Cold Crossing* (Interrupt · Turning Point) → **CLOSED**
- **Where / when:** the herders' ford, the dead of night → toward grey dawn; a cold camp on the near bank.
- **Last beat (2–3 sentences):** The deep power thinned the Mark's containment and sent a *puppeted Hibari Mura boy* up out of the ford to kill Akihiko (its terror is the sun, so it used a victim he couldn't burn). An Emerald Magistrate's patrol on the far bank rallied to him. He cast Katana of Fire + Biting Steel, *missed* a kill-stroke (his school ability won't let his fire harm the innocent), then chose to **sear the soul-thread** with Sacred fire — freeing the boy's body and WOUNDING the power, at the cost of the Falcon mask (UNMASK; strife → 0). He then won the magistrate to a deferral.
- **Akihiko's state:** strife **0** (post-unmask), fatigue **1/10**, Void 2/2; Marked (contained, used as a conduit). **Bears the Dawn Mirror.** Honor 55 / Glory **38** (witnessed holy deed) / Status 36. XP 0.
- **Stakes on the table now:** the road home resumes — now with **Matsu Toshimoko, Emerald Magistrate, at his side**, the wrapped Mirror under her eye, and a daimyō who must satisfy the Emperor's law without spilling a secret meant for "three mouths." A soul-empty freed boy and a half-throttled (alive) watchman to tend; Hatsue failing; the Scorpion still out there; the deep power now wounded and fixated.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md` (Keeper *Toritaka Genkō*; the gaki *Kuchinashi*; Arc 1 summary).
