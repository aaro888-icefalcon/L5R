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
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md` (+ this folder's `system-profile.md` overrides)
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: Arc 1 — *The First Ward*
_Each adventure has its own Threads & Characters Lists and its own Theme priority. A new adventure
begins when the current one's main Thread(s) Conclude or the player declares one — roll new Themes
from `bridge/theme-weights.md`, start fresh Lists, carry over still-relevant Characters/Threads,
archive the rest._
- **Adventure status:** **concluded** — capstone reached at Scene 5 (the Dawn Mirror claimed; the Imperial blood confirmed). **Session break.** The next session frames a new adventure (the long road back / wielding the Mirror) from the Threads carried below; archived arc summary in `archive.md`.
- **Theme priority (this adventure):** — _Arc 1 ran Pure Mythic without tracked AC Themes; roll the next adventure's priority from `bridge/theme-weights.md` (`adventure_crafter.py themes --style drama`) when it is framed._

## Chaos Factor: 6
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 5: Akihiko drove a hard scene with control — parley, the chosen mercy, the claiming → −1.)_

## Threads (open goals/vows; weighted; carry into the next adventure)
1. **The First Ward = the Dawn Mirror (PRIMARY QUEST)** *(w3)* — *Asahi no Kagami,* in the First Yotogi's barrow (reached, Sc.5). **Not a weapon — it BINDS** the deep power in captured sunlight. **Wake it:** Akihiko's Sacred sun-fire, at an **open dawn**, by a willing soul who takes up the binding **as a lasting duty** (the chain's new anchor). Claim it from the barrow once the Keeper is at rest. *(Claimed Sc.5; the duty now = wield it: cure the mark, free the souls, bind the power.)*
2. **The Mark — danger AND key** *(w3)* — the power's hook in Akihiko (**Marked by the Deep**); *double-edged* (he senses it back); **CONTAINED** (Sc.4 — can't deepen/spread, beacon blunted). **NOW ALSO THE KEY (Sc.5):** to bind a thing you must hold it — the mark is the *leash* by which he may drag the power to the Mirror. The First Yotogi bore such a mark willingly.
3. **The power in the deep Shinomen** *(w2)* — nameless, older than the Empire & the Kami; beneath the forest's heart (north). **CANNOT be killed — only BOUND (trying to kill it feeds it); its one fear is the sun.** Has gnawed the First Yotogi's binding thin for 1200 years; harvests souls to loose its chains. Now fixed on Akihiko personally.
4. **The taken souls of Hibari Mura** *(w2)* — **VISION-CONFIRMED: gathered & woven toward some purpose, NOT destroyed** — the village's people still 'singing' among a galaxy of stolen souls. Reclaimable?
5. **The leak / the Scorpion close in** *(w2)* — Gennai (Scorpion spymaster) got limited word out (*a Falcon Warden rides the hills secretly*) and **escaped**; his porter was left bound on the hill. Expect them to probe.
6. **Ninjō — To truly belong** *(w2)* — Hatsue named the wound; this charge is his chance to matter.
7. **Lord Hatsue's fraying mind** *(w1)* — spending her sight on the threat.
8. **The Imperial blood — CONFIRMED** *(w2)* — the Dawn Mirror (Amaterasu-blessed) recognized Akihiko as **kin to the line of Lady Sun** — bone-truth, no longer rumor. *How* a Falcon Minor-Clan warden carries the Emperor's blood is now the live mystery (and a thing others would kill or use him for).

## Characters & Factions (NPC/force — want — disposition; weighted; PC NOT listed)
- **Gennai** *(w2)* — Scorpion spymaster posing as a medicine-peddler; charming, sharp, **escaped into the hills** with his swordsman — wants the Falcon's secret; **hostile, now exposed**
- **The Scorpion Clan** *(w2)* — seize Toritaka lands; their cell just got word the marches may be open — **hostile / closing in**
- **The power in the deep Shinomen** *(w2)* — harvest souls / spread — malign, looming
- **Lord Toritaka Hatsue** *(w1)* — hold the line via Akihiko — his lord & secret-sharer; fraying
- **The captured porter** *(w1)* — **left bound on the hill "for the Kami to judge"** (alive, abandoned, just out of reach of his knife). Latent: may free himself, die, or be retrieved by Gennai — and remember the Warden who left him.

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Campaign roster (persists across adventures: recurring NPCs, long arcs — full detail in `setting-canon.md`)
- **Gennai** — Scorpion spymaster; recurring antagonist who knows Akihiko's face and that he hides something.
- **Lord Toritaka Hatsue, "the Yotogi"** — Akihiko's lord, hard mentor, and secret-sharer; spending her sight on the deep Shinomen.
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, heretic Centipede sun-priest), Sumiko (mother; carrier of the quiet Imperial claim), Yuki (grandmother; keeper of the line's truth).
- **Suzu** — sole survivor of Hibari Mura's soul-harvest; soul-shocked, bonded to her rescuer; the only living witness.
- **Toritaka Jōji** — Akihiko's closest comrade-Warden; present at the barrow.
- **The Scattered Corps** — healers & wardens of many clans bound to Akihiko by a past crisis; far apart on duty (Eniko, Genzō, Bara, Hiroyuki, Saburō, Kasumi).
- **Long arcs:** the Imperial blood (how & who learns it); the Dawn Mirror's binding-duty (cure the mark · free the souls · bind the deep power).

## Clocks (offscreen factions / threats / progress — ~a week passed at the barrow; advanced by `tick.py`)
- **The leak:** **delivered** — the Scorpion handlers now hold the report; they will act on it
- **Scorpion land-grab scheme:** advancing (a week on; likely probing while Akihiko is away)
- **Hatsue's decline:** worsening
- **The Shinomen harvest:** active — and the power has drawn its eye to this hill

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic)

## Current scene — Scene 5: *The Broken Wards* → **CLOSED**; the Dawn Mirror claimed
- **Where / when:** the firelit vale outside the First Yotogi's barrow, night.
- **Last beat (2–3 sentences):** Akihiko kept the bargain (the mercy-kill of the Keeper, **Toritaka Genkō**, against his Softheartedness; Genkō passed whole), then entered the tomb and lifted **Asahi no Kagami.** It woke to his blood — **confirming his Imperial (Amaterasu) lineage beyond doubt** — and the binding-duty settled onto him, willingly taken. He emerged with the Mirror; Jōji is asking what happened.
- **Akihiko's state:** strife **0** (session-end rest), fatigue 0, Void 2/2; Marked (contained); **bears the Dawn Mirror & its duty.** Honor 55 / Glory 35 / Status 36. **Advanced (Sc.1, 9 XP): Air 1→2 → Focus 5; learned Striking as Fire.** XP 0.
- **Stakes on the table now:** what to tell Jōji; the long road back to wield the Mirror (cure the mark, free Hibari Mura's souls, bind the deep power) — and a week+ of Scorpion/harvest movement waiting. **Strong arc-capstone / session-break point.**
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md` (Keeper *Toritaka Genkō*; the gaki *Kuchinashi*; Arc 1 summary).
