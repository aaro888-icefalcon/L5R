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
- **TONE CALIBRATION (set by player, Sc.13):** **realism · challenging · gritty.** Rokugan is a vast indifferent machine of rank & obligation; Status 40 is a LOW ceiling. **Counter the "chosen-one drift":** the big social facts (does an NPC trust/sponsor/elevate/betray him?) are ROLLED as Fate Questions at honest, often-unfavorable odds — NOT narrated to flatter. Every elevation Akihiko already holds (yoriki, Imperial blood, the Mirror-anchor) must grow STRINGS and COST: resentment from outranked peers, a leash from Chiyo (she *uses* him), Imperial blood as a liability others reach for, lapsed Warden duties leaving real people exposed. Allies act to win their own ends. Defeat is real and frequent.
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
- **Adventure status:** **active** — Arc 1 (*The First Ward*) closed as a capstone. Arc 2 (*The Long Road Back*) carried the Mirror home (Sc.7–10) through the deep power's ford-ambush and the Scorpion's lane-trap to a dying Lord Hatsue. **Sc.11–12 pivoted the arc:** Hatsue died, Chiyo succeeded, the Mirror passed to the Yotogi priests, and Akihiko became the new Champion's *yoriki*. Arc 2 now runs as the **court-and-investigation phase at Kyūden Toritaka** — the Mirror's price (a way that doesn't consume the anchor), the engineered Lion-lie, the killer inside the walls, Chiyo's hidden fear — under the long work (cure the mark · free the souls · bind the deep power).
- **Theme priority (this adventure):** **Action › Social › Tension › Personal › Mystery** — stored in `adventure.json` (`state.py adventure show campaigns/toritaka-akihiko`); _player-set Sc.13 (was Tension›Action›Social›Mystery›Personal); biases Turning Points toward kinetic, consequence-forward beats._

## Chaos Factor: 3
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 12: a calm political denouement Akihiko wholly steered (report, questions, accepting the charge) → −1 toward 2; BUT the world moved against him offscreen the same night — the Scorpion reached inside the walls and silenced his only lead → +1. Net wash → **HOLD at 3.** Expect the morning's discovery to push it up.)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Dawn Mirror & the binding-duty (PRIMARY QUEST)** *(w3)* — *Asahi no Kagami*, claimed (Sc.5), borne home and DELIVERED (Sc.12): no longer on Akihiko's chest — entrusted to **Toritaka Yoshi** and the Yotogi priests for safekeeping & study while Akihiko seeks another way. Not a weapon — it BINDS the deep power in captured sunlight; can cure his mark & free the taken souls. Wakes to his Sacred sun-fire at an open dawn, by a willing soul who takes the binding as a lasting duty — and CONSUMES that anchor (see 'The Mirror's price').
2. **The Mark — danger AND key (the leash)** *(w3)* — The power's hook in Akihiko (Marked by the Deep); CONTAINED but used as the conduit (Sc.8) to reach & sear the power — double-edged, proven both ways. The leash by which he may drag the power to the Mirror.
3. **The Mirror's price — find a way that doesn't consume the anchor** *(w3)* — Hatsue's deathbed secret (Sc.11): the Mirror needs a living ANCHOR who spends self/soul/sight keeping the chain taut (the First Yotogi, the Keeper 1200y, Hatsue's 2 years of sight) — to wake & wield it is to be slowly devoured. Hatsue meant Akihiko. **Chiyo's charge #1 (Sc.12):** find a way to fight the deep dark that does NOT end with his soul poured into a bowl — a second anchor, a loophole in the First Yotogi's lore, or another road. The priest Yoshi & the Mirror are his resources. A primary quest now.
4. **The power in the deep Shinomen** *(w2)* — Nameless, older than the Empire & the Kami; cannot be killed, only BOUND; its one fear is the sun. STUNG (Sc.8): Akihiko ran sun-fire up a soul-thread and wounded it — first hurt in 1200 years; it now knows his fire all the way down, fixed on him. Regrouping quietly offscreen (no new sign the night of Sc.12).
5. **The taken souls of Hibari Mura** *(w2)* — Gathered & woven toward some purpose, NOT destroyed. PROVEN partly reclaimable (Sc.8): Akihiko's sun-fire severed one puppet-thread & freed a boy's body — the soul still in the deep (the Mirror is the full cure).
6. **The hand inside the walls — who silenced Gennai?** *(w3)* — OVERNIGHT after Sc.12 (Fate YES + PC-Negative random event): the Scorpion reached their captured spymaster Gennai inside Kyūden Toritaka's warded cellar and SILENCED him — the one live thread of Chiyo's investigation, cut before Akihiko could pull it. Proves a Scorpion hand already walks the Falcon's halls, and moved fast & well-informed. A murder & a method to inspect; the morning's cold open. Mere ruthless prudence, or a reaction to the charge Chiyo gave in a cleared room? Unknown.
7. **The Lion-lie — who engineered the Falcon's surrender?** *(w3)* — Chiyo's charge #2 (Sc.12). The Lion 'protectorate' rests on a MANUFACTURED fear — Scorpion raids that didn't quite happen, moved border-stones, a magistrate's patrol read as a noose — stacked into one lie: 'the Falcon can't hold its border; the Lion is the only roof.' The knot: the CRAFT is Scorpion (fog, patience, a frightened old man played like a flute) but the GAIN is the Lion's — they don't sum. The Lion face is **Ikoma Naoki**, the velvet broker (genuine grasp, or a mouth with another hand up the back of it?). Ujiyasu is the unwitting dupe Chiyo won't break. Open Imperial question: would the Throne even sanction swallowing a Minor Clan? Akihiko's private dread: a Falcon swallowed = wards broken = it serves the deep power. Was to start at the cellar — but the cellar lead is now dead (see 'the hand inside the walls').
8. **What's wrong with Chiyo — the hidden fear** *(w2)* — Iron Chiyo — 'scariest of his peers' — came undone at the deathbed in a way that is NOT mere grief, and (Sc.12, private interview) walled off a specific FEAR hard & clean the instant Akihiko's 'why me' brushed it (oracle: Exceptional No). It is NOT the Lion-lie (oracle: she shields no personal suspect there). She charged him (charge #3) to keep his eyes on her and tell her the things she's 'too proud or too frightened to see' — licensing him to hunt the very thing she's hiding.
9. **The Imperial (Seppun) blood — known heritage** *(w1)* — No buried secret: runs through grandmother Seppun Yuki (minor Imperial scion) -> Sumiko -> Akihiko, and grants the house a notch of extra Falcon standing. The Dawn Mirror recognized it. Still a thing high-Status others could exploit or resent.
10. **The leak / the wider Scorpion campaign** *(w2)* — The sunken-lane ambush was DEFEATED & Gennai taken (Sc.9) — but the cell silenced him in the cellar overnight (Sc.12) rather than lose what he knew. The land-grab continues under Emerald-Magistrate scrutiny; the broader word that 'a Falcon Warden rides the hills secretly' is still out. Now braided into the Lion-lie and the hand-inside-the-walls.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Toritaka Chiyo (Lady of the Falcon / Clan Champion)** *(w3)* — Hatsue's eldest; iron-willed, the scariest of Akihiko's peers; NEW Lady of the Falcon (Sc.11). Made Akihiko her **yoriki** (Sc.12) with a three-part charge — the Mirror's price, the Lion-lie's forger, and watching her own blind side. Calls him hers, not the clan's; named the 'cousin'/vassal distinction deliberate elevated trust. Hides a specific FEAR she walled off hard (see thread). Akihiko's LORD now.
- **Gennai (Scorpion spymaster) — silenced** *(w2)* — Captured Sc.9 (sword-hand maimed), held in Kyūden Toritaka's cellar — then SILENCED overnight after Sc.12 by an inside Scorpion hand before Akihiko could interrogate him. The lead cut; now a corpse and a method to inspect, and proof the enemy walks the halls. -> toward archive once the morning scene resolves him.
- **Ikoma Naoki (Lion diplomat)** *(w2)* — NEW (Sc.12, named by Chiyo). The velvet courtier who carried the Lion protectorate to Ujiyasu three times, brushwork too polished for a thing dreamt up in a panic. The Lion FACE of the lie — genuine Lion grasping a real opening, or a mouth with another hand up the back of it? The first thread of the Lion-lie investigation now that the cellar lead is dead. Not yet met.
- **Toritaka Yoshi (leader of the Yotogi priests)** *(w2)* — NEW (Sc.12). Head of the Falcon's spirit-warding priesthood; Akihiko handed him the Dawn Mirror for safekeeping & study. Keeper of the binding-lore now — the natural ally in hunting a way to wield the Mirror that doesn't consume its anchor (Chiyo's charge #1).
- **Matsu Toshimoko (Emerald Magistrate)** *(w2)* — ALLY (Sc.9) — Akihiko handed her a live Scorpion, cracking her marches-investigation. A LION magistrate, now an awkward asset for a probe into a Lion-benefiting plot; owed the new Lady's account (Hatsue, whom she rode to answer, is dead). Vowed the Scorpion answer to the Throne for the ambush.
- **Toritaka Ujiyasu (karō)** *(w1)* — The clan's aged seneschal; a frightened pragmatist, NOT wicked — the unwitting door the Lion-lie walked through. Chiyo won't break the old man (lose the door, never learn who used it). A dupe to be read, not punished.
- **Toritaka Jōji** *(w2)* — Akihiko's closest comrade-Warden, sworn confidant; senior to him; rode to the barrow and home. Blunt, loyal — the man who names the hard truth Akihiko is avoiding.
- **The Scorpion Clan** *(w2)* — Bloodied but ruthless: smashed at the lane (Sc.9), yet reached into a Champion's cellar to murder their own exposed agent rather than let him talk (Sc.12). The land-grab continues under Imperial scrutiny; a hand of theirs is inside Kyūden Toritaka. Hostile, exposed, patient.
- **The power in the deep Shinomen** *(w2)* — Harvest souls / spread — malign, looming; wounded by Akihiko's fire and fixed on him; regrouping quietly offscreen (no new sign the night of Sc.12).
- **The freed boy of Hibari Mura** *(w1)* — A reed-cutter the deep power puppeted across the ford; Akihiko severed the thread with Sacred sun-fire. Body alive & reclaimed, soul still gathered in the deep — soul-empty like Suzu; recovering at Kyūden Toritaka.
- **The captured porter** *(w1)* — Gennai's courier, left bound on the hill 'for the Kami to judge' (days ago): freed himself, died, or retrieved — and remembers the Warden who left him. A dangling loose end on the marches.

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Campaign roster (persists across adventures: recurring NPCs, long arcs — full detail in `setting-canon.md`)
- **Gennai** — Scorpion spymaster; captured (Sc.9), then **SILENCED in Kyūden Toritaka's cellar overnight after Sc.12** by an inside hand before he could talk. → toward `archive.md`; his murder is now the live thread ("the hand inside the walls").
- **Lord Toritaka Hatsue, "the Yotogi"** — Akihiko's lord, hard mentor, secret-sharer. **DIED (Sc.11)** — held on for the Mirror; named Akihiko "the other inheritance" (the ward, not the seat); revealed the Mirror's price, then passed. → `archive.md`.
- **Toritaka Chiyo** — Hatsue's eldest; **Lady of the Falcon / Clan Champion** (Sc.11). **Made Akihiko her *yoriki*** (Sc.12) with a three-part charge; refused to be rushed on the Lion deal and set him to find who engineered it; hides a specific fear. Akihiko's lord now.
- **Toritaka Ujiyasu** — the clan's aged *karō*; a frightened pragmatist (not wicked) who brokered the Lion protectorate to save a drowning clan.
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, heretic Centipede sun-priest), Sumiko (mother; carrier of the Seppun blood), **Seppun Yuki** (grandmother; minor Imperial scion, family matriarch, keeper of the line's truth).
- **Suzu** — sole survivor of Hibari Mura's soul-harvest; soul-shocked, bonded to her rescuer; the only living witness; recovering with Akiro at Kyūden Toritaka.
- **Toritaka Jōji** — Akihiko's closest comrade-Warden; senior; rode to the barrow and home.
- **The Scattered Corps** — healers & wardens of many clans bound to Akihiko by a past crisis; far apart on duty (Eniko, Genzō, Bara, Hiroyuki, Saburō, Kasumi).
- **Matsu Toshimoko** — Emerald Magistrate (Lion); ally (Sc.9). Owed the **new Lady's** account now (Hatsue dead); her live Scorpion prisoner just murdered on Falcon ground — Imperial jurisdiction & her wrath in play, plus her awkward Lion blood as Akihiko probes a Lion-benefiting plot.
- **The freed boy of Hibari Mura** — reclaimed from the deep power's puppetry by Akihiko's sun-fire; body alive, soul still taken (a second soul-shocked survivor, like Suzu).
- **Toritaka Yoshi** — head of the Yotogi priests; now keeps the Dawn Mirror (Sc.12) and the binding-lore; ally in the search for a non-consuming way to wield it.
- **Ikoma Naoki** — Lion (Ikoma) diplomat; the velvet broker of the protectorate; the Lion face of the engineered lie (suspect or mouthpiece). Not yet met.
- **Long arcs:** the Seppun blood (who exploits or honors it); the Dawn Mirror's binding-duty (cure the mark · free the souls · bind the deep power).

## Clocks (offscreen factions / threats / progress — advanced by `tick.py`; dawn after Hatsue's death, Kyūden Toritaka)
- **The succession → RESOLVED (Sc.12):** Lady **Chiyo** confirmed Clan Champion at the oath-renewal; Akihiko her yoriki. The Lion deal is *not* signed — Chiyo suspended it and turned it into an investigation.
- **The Lion-lie (active):** a manufactured threat engineered to walk the Falcon under the Lion; Scorpion craft / Lion gain; **Ikoma Naoki** the broker, **Ujiyasu** the dupe. Akihiko charged to find the hand.
- **The hand inside the walls (NEW, urgent):** the Scorpion **silenced Gennai** in the cellar overnight (Fate YES + PC-Negative event, Sc.12) — an inside agent, fast and informed. The morning's body is the cold open; the killer is still in the keep.
- **Scorpion campaign (active):** bloodied but reaching inside a Champion's walls; the land-grab continues under Imperial scrutiny; the cell that killed Gennai is here.
- **The Shinomen harvest (looming, quiet):** the WOUNDED deep power regroups offscreen, fixed on Akihiko; no new sign the night of Sc.12 (Fate No). His beacon-blunting still holds, for now.
- **Imperial (Matsu):** an ally owed the new Lady's account; her murdered prisoner raises the stakes & her jurisdiction.

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic)

## Current scene — Scene 12: *The Confirmation* (denouement / transition) → **CLOSED**
- **Where / when:** Kyūden Toritaka, the day after Hatsue's death into deep night — dawn-rites, the clan's oath-renewal, then a private interview with the new Lady; ends with Akihiko asleep.
- **Last beat (2–3 sentences):** At dawn Akihiko sang the sun-hymn (strife → 0). The Falcon confirmed **Chiyo** as Champion and renewed oaths; he handed the Dawn Mirror to the Yotogi priest **Yoshi** and gave the Champion his full report. He asked leave to return to his border post; Chiyo **refused** and bound him as her **yoriki** with a three-part charge (the Mirror's price · the forger of the Lion-lie · watching her blind side), acknowledging their houses' vassal-bond as deliberate trust. In a private interview she gave her read on the lie — **Scorpion craft, Lion gain, the broker Ikoma Naoki, start at the cellar** — but walled off a personal **fear** (oracle: Exc. No) that is *not* the Lion-lie (oracle: No protected suspect). He took his leave and slept.
- **OVERNIGHT (world-tick, Sc.12 → 13 hook):** Fate YES (50/50→22) + **Random Event (PC Negative · Inspect/Idea)** — the Scorpion **silenced Gennai** in the warded cellar before he could be questioned; an inside hand, fast and informed. Fate No (Unlikely→17) — no new spirit-dark sign overnight.
- **Akihiko's state:** strife **0/8**, fatigue 0/10, Void 2/2. Honor 55 / **Glory 43** / **Status 40** (Sc.12 succession + yoriki). **No longer carries the Mirror** (with Yoshi). New giri: **yoriki to Lady Chiyo**. Ninjō: resolved (Sc.11); a new one to emerge in play. XP 0 (tally at session-end).
- **Stakes / next scene (Scene 13 cold open):** morning at Kyūden Toritaka — the murdered prisoner in the cellar (who, how, and what it means that the enemy is inside the walls); then the Lion-lie investigation (Ikoma Naoki, the manufactured threat, Ujiyasu), the Mirror's-price search (Yoshi), and watching Chiyo. **Natural session pause taken here.**
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md` (Keeper *Toritaka Genkō*; gaki *Kuchinashi*; ashigaru *Haru*; **Lord Hatsue**; concluded threads: *Ninjō—to belong*, *Hatsue's fraying mind*, the Lion-deal binary; Arc 1 summary).
