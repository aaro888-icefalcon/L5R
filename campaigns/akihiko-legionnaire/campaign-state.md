# Campaign State — Toritaka Akihiko, Chūi of the Imperial Legions

> **The single source of truth.** Overwrite this at the END of every scene.
> If a change happened in the fiction but isn't written here, it didn't happen.
> Validate: `python3 .claude/skills/l5r-gm/scripts/state.py validate campaign-state.md`

## Active set (the context filter — only matching content loads)
```yaml
active_set:
  sources:    [core, emerald-empire, fields-of-victory]   # war + Imperial; add others as the campaign reaches them
  clans:      [falcon, lion, crane, scorpion, imperial]   # PC Falcon (Seppun blood); the warring sides; Scorpion scorn
  subsystems: [core-check, skirmish, duel, intrigue, mass-battle, downtime, advancement]
  modes:      [war, court, wilderness, spiritual]
  flags_allowed: []                  # mature | maho | gaijin — OFF unless the player opts in aloud
```

## Frame
- **Premise / tone:** Samurai **war-drama** on the Lion–Crane front at **Toshi Ranbo**. Akihiko — a Falcon sun-priest of **known (scandalous) Seppun blood** — is a **chūi** in the **Imperial Legions**, sent to police a war between two great clans that hate each other and the Emperor's interference equally. His **ninjō** (bring his soldiers — a **Falcon contingent** of his own clansmen — home alive to the Valley of the Spirits) wars with his **giri** (win the Emperor's wars to bring **honor to the Falcon**, spending what must be spent). The trap: both pull toward the Falcon, in opposite directions — *to honor the clan he must spend the clan.* Full-spectrum: mass battle · skirmish · duel · court intrigue.
- **TONE CALIBRATION:** **realism · challenging · gritty.** Status 36 is a low ceiling; Akihiko is a junior officer and a black-sheep nephew, not a chosen one. **Elevation is a Status-priced Fate Question, never narrated; a Yes arrives with strings.** Consult `facts.py` before inventing politics; move Honor/Glory/Status via `social.py`. A Fate-Yes leans toward complication.
- **Adventure source:** **Pure Mythic** (mythic-gm owns oracle / scene pacing / Chaos / events / plot)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm) | Fate Check
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md`
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: Arc 1 — *The Edict at Toshi Ranbo*
_Each adventure has its **own** Threads & Characters Lists and its own Theme priority. A **new
adventure** begins when the current one's main Thread(s) Conclude (the Threads List empties) or the
player declares one._
- **Adventure status:** **active** — Scenes 1–2 played. Akihiko took up his command (Sc.1), lit a forward post on the contested road to deter the Lion (Sc.2); the display drew **Matsu Kasumi** + 7 riders demanding passage west. His deterrence failed, he refused to fold, she challenged, and a **death-duel** followed. He lost — but met death with such grace she **spared his life**. The Lion crossed west; the edict broke on his post his first night; he owes his life to a Lion. The reckoning with his taisa comes at dawn.
- **Theme priority (this adventure):** **Personal › Action › Social › Tension › Mystery** — in `adventure.json` (`state.py adventure show campaigns/akihiko-legionnaire`); _player-set._

> **The Lists are JSON — the single source of truth.** Threads/Characters Lists + Theme priority live
> in `threads.json` · `characters.json` · `adventure.json` (entries carry `{name, weight, note}`; the
> dice roll over them, any length). `state.py init` scaffolds them; set weight/themes with `state.py
> thread|char|adventure …` and prose with `render_lists.py set-note …`. The `## Threads` /
> `## Characters & Factions` sections below are a **GENERATED** view — **never hand-edit them**;
> regenerate with `l5r-gm/scripts/render_lists.py render <dir> --in-place` (drift-check: `… --check`).

## Chaos Factor: 6
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic — see `bridge/chaos-tendency.md`. Sc.2: Akihiko was overwhelmed — lost the duel, lost the road, ended at an enemy's mercy → **+1 → 6**.)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Toshi Ranbo front — the Lion–Crane war** *(w3)* — PRIMARY. The Lion and Crane — ancestral enemies — are at open war over the contested town of Toshi Ranbo (Akodo Arasou slain by Doji Hotaru's arrow, 1123). Akihiko's Legion is deployed to enforce an Imperial edict between two armies that hate each other. (facts.py relation lion crane)
2. **Keep my soldiers alive — ninjō vs the orders that spend them** *(w3)* — The engine of the drama. His cohort carries a FALCON (Toritaka) contingent — clansmen serving the Legion under their famous-blooded son; his ninjō is to march them home to the Valley of the Spirits ALIVE. Every order that spends lives to win the Emperor's war pokes it. The cruelty: his giri (honor the Falcon) is paid in the same Falcon lives his ninjō would save. Watch the kill-or-spare & harm-to-dependents triggers (Softheartedness, Fear of Failure).
3. **The black-sheep blood & uncle Seppun Tadanobu's leash** *(w2)* — His known Imperial blood comes from the scandalous branch — grandfather left the Seppun to marry a Toritaka; uncle Tadanobu redeemed it and sponsors Akihiko. The favor is a leash: what does the uncle expect in return, and who resents the upjumped black-sheep nephew?
4. **Officers who know whose nephew he is — expectation & resentment** *(w2)* — Akihiko serves under officers aware of his Seppun patron and his minor-clan origins. ELEVATION here is rolled, not narrated (Status-priced Fate Questions); trust and favor arrive with strings.
5. **The spirit-dark of the battlefield — what the Falcon sees that the war hides** *(w1)* — Quiet thread. A battlefield is a feast for the dead; Akihiko's Falcon spirit-sight (Sixth Sense) may find yūrei, gaki, or worse moving under cover of the mundane war. Latent — let the dice surface it.
6. **A Lion's debt — the life I owe Matsu Kasumi** *(w1)* — Akihiko lives because Matsu Kasumi chose not to kill him in a death-duel he lost. A life-debt to a Lion enemy, witnessed by both armies. She will remember; so must he. The string will pull — in court, in war, or the next time their paths cross.
7. **Answering for the broken post — the lost road and taisa Saburō** *(w1)* — Akihiko's two riders carry word up the ridge: the post fell, the Lion crossed west, the edict broke — and the Throne's officer lives by a Matsu's mercy. His first duty, failed publicly his first night. The reckoning with taisa Seppun Saburō (who already despises his patron-bought commission) is coming with the dawn.
8. **The poisoned camp — find the hand killing the Legion (Saburō's charge)** *(w1)* — Turning Point (Sc.3): on a feast-night a fifth of the company was poisoned — men maddened (quarrelsome, giddy) then dying; the festivity turned deadly. Reeks of BETRAYAL (a human hand, not spirit — Sixth Sense quiet). Saburō's charge & Akihiko's road back from disgrace: find the cause AND the hand, fast, or be 'just another Michio.' Akihiko's medic/priest skills + ninjō (his men dying) all point here. New NPCs to surface: an 'attractive' ashigaru tied to the night's entertainment (Art); the poisoner.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Seppun Tadanobu (uncle / Imperial patron)** *(w2)* — Akihiko's illustrious maternal uncle, reclaimed into the Seppun; his sponsor into the Legions. Powerful, watchful; his patronage is a leash. Wants — UNKNOWN (roll it); disposition: proprietary, demanding.
- **Akihiko's cohort — the soldiers under his command** *(w2)* — The squads he leads — including a FALCON (Toritaka) contingent of clansmen-levies he means to bring home alive (his ninjō), plus Legion ashigaru & bushi of mixed clans. Names & faces drawn in play (npc.py / generators). Their lives are the stakes; their home is the Valley of the Spirits.
- **The Lion army at Toshi Ranbo** *(w1)* — The largest, most formidable army in Rokugan; martial, honor-bound, hungry for vengeance after Arasou's death. Right Hand of the Emperor — being policed by the Emperor's own Legion is a humiliation they feel keenly. (facts.py clan lion)
- **The Crane army at Toshi Ranbo** *(w1)* — Smaller but exquisitely trained; the Left Hand of the Emperor, masters of court and the duel. Defending what they hold; will fight with law and word as much as steel. (facts.py clan crane)
- **Seppun Saburō (taisa / commanding officer)** *(w1)* — Akihiko's direct superior — taisa of the Legion company. A TRUE-BLOODED Seppun who rose from OBSCURITY by merit (seed: Succeed·Obscurity), not by name — and so has no patience for a commission bought with Tadanobu's favor. Knows exactly whose nephew Akihiko is and rides him HARDER for it, to be seen showing the patron's pup no slack. Demanding, watchful, competent; gives orders that spend lives to win the Throne's war. Want: deepen in play — make this posting prove his command was earned. Disposition: cold, testing, proprietary-but-skeptical.
- **Matsu Kasumi (Lion duelist — spared his life)** *(w1)* — Young Matsu officer (Akihiko's age), scarred, proud, the superior blade. Led 7 riders to test the post; challenged Akihiko to a death-duel after his deterrence failed. He taunted her (Lady Matsu's bravery), then apologized and met certain death with grace — and she STAYED HER HAND, sparing Imperial blood that knelt well. Took the road west; left him his life and a debt: 'Remember who gave it to you.' A complicated bond now — enemy, benefactor, equal. Disposition: respect, ownership, watchful.
- **The Legion healer corps (overwhelmed field-surgeons)** *(w1)* — The Legion's field-surgeons — the 'physician organization' (TP: Organization, Assistant, Harmful). Drowning under the poisoning, unable to name the cause; possibly implicated, possibly just overwhelmed. Akihiko, the sun-priest-physician, is set over/among them to solve it. Disposition: exhausted, defensive, out of their depth.

## Adventure Features (prepared-adventure mode only)
-

## Overlays
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(or: N remaining, player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic) · Theme priority lives in `adventure.json`: Personal, Action, Social, Tension, Mystery

## Campaign roster (persists across adventures: recurring NPCs, long arcs)
- **Seppun Tadanobu** — illustrious maternal uncle; Akihiko's Imperial patron & the hand that placed him in the Legions.
- **Toritaka Michio (b. Seppun Michio)** — maternal grandfather, the talented black sheep who left the Seppun to marry a Toritaka. (deceased)
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, Centipede sun-priest), Sumiko (mother, half-Seppun, carries the known line).
- **The Scattered Corps** — cross-clan healers/wardens bound to Akihiko by a past crisis; scattered on duty.

## Clocks (offscreen factions / threats / progress — advanced by `tick.py` at bookkeeping)
- **The Toshi Ranbo war:** Lion (vengeful, vast) vs Crane (defending, smaller) — the Imperial edict Akihiko's Legion enforces sits between them. **Sc.2: a Lion patrol (Kasumi's 7) crossed WEST past Akihiko's broken post — a small Lion gain and a breach of the edict on the contested road.**
- **The reckoning with taisa Saburō (NEW, urgent):** Akihiko's 2 riders carry word up the ridge — the post fell, the Lion crossed, he was spared. Clock ticks toward Saburō's response at dawn (the Seppun who already despised the patron-bought commission, now handed proof the pup failed his first night).
- **A Lion's debt (NEW):** Akihiko's life belongs to Matsu Kasumi. A string that will pull — court, war, or their next meeting.
- **Uncle's expectations:** Tadanobu's patronage will call in its price; clock ticks toward what he wants (and now: how will the uncle take news his nephew lost a duel and the edict broke on his watch?).

## Current scene — Scene 2: *The Toll-House* (forward post → standoff → DUEL) → **CLOSED**
- **Where / when:** the firelit toll-house on the contested road below Toshi Ranbo, full dark into the small hours.
- **Last beat (2–3 sentences):** Akihiko held the post and lit it to deter the Lion; the display drew **Matsu Kasumi** and 7 riders demanding passage west (Fate: the display deterred a *probe* but invited a *confrontation*). His Fire·Courtesy deterrence failed (TN 3); he refused to fold; she challenged him to a duel. He pushed for any-weapon (Fate Exc No — she demanded steel), then a Fire·Courtesy **taunt** (success) reclaimed his face and rattled her, but locked steel-only. In the **iaijutsu death-duel** he opened Fire and his strike **missed**; her counter glanced off his armor; the staredown **Compromised** him (strife 8/8) and opened her finishing blow — but his graceful death-acceptance (apology + honoring her) moved her (Fate: **YES**) and she **spared him**, took the road, and rode west. He unmasked into serene acceptance (strife → 0).
- **Akihiko's state:** **ALIVE, defeated, spared.** strife **0/8** (unmasked), fatigue **1/10**, Void 2/2, no wounds. **Honor 57** (+2, grace) · **Glory 32** (−3, public duel loss) · **Status 36**. New: a life-debt to Matsu Kasumi; the lost road; a reckoning with Saburō pending.
- **Stakes / next scene (Scene 3 hook):** dawn at the toll-house and the ride back up the ridge — facing **taisa Seppun Saburō** with the news (the post fell, the Lion crossed, he lives by a Lion's mercy). How does the cold, merit-proud Seppun take it? And what does it do to Akihiko, his Falcons, and the giri/ninjō that just bought its first hard lesson? **Natural session pause available here.**
- **Self-audit drift counter (consecutive soft scenes):** 0 _(Sc.2 had real stakes & loss — not soft.)_

## Archive pointer
- Resolved threads / dead characters → `archive.md`
