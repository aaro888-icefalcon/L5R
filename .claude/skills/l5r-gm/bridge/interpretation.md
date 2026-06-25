# Interpretation & GM Lens — Rokugan / L5R 5E   (hook: meaning)

> **Operative digest:** Read every oracle result (Fate answer, Meaning pair, Random Event, NPC behavior) as
> **samurai drama in Rokugan** — honor the raw result first, *then* re-skin to clan / giri-ninjō / honor / face.
> A No is a real No; a bad event is not rescued. NPCs read setting-true, competent, and act to win.
> **Three load-bearing rules (anti-softening):**
> 1. **Fate-YES → COMPLICATION.** When a Fate Question comes back Yes, read it toward the answer that
>    *opens* trouble / a new thread, never toward comfort. "Yes, **and** it costs / draws notice / pulls a
>    string." (Exceptional Yes = a Yes whose complication is large.) A Yes that makes the PC's life easier
>    is almost always the wrong reading.
> 2. **ELEVATION IS A FATE QUESTION.** Any beat that would *trust, reward, promote, befriend, or center*
>    the PC — an NPC's favor, a lord's notice, a title, an inheritance — is NOT narrated; it is a Fate
>    Question at odds priced by the PC's real **Status** (low Status ⇒ Unlikely/Very Unlikely). This is the
>    fix for the "chosen-one drift": the softening used to live in the big questions never asked.
> 3. **CONSULT THE FACTS, don't remember them.** Before inventing any clan/court/military/political detail,
>    run `facts.py clan|relation|imperial|map` — grounded canon, not convenient memory. Record campaign-new
>    facts to the campaign's `setting-canon.md`. Track Honor/Glory/Status/titles via `social.py` (never freehand).

Broad GM-craft for **Rokugan**. NOT a reskin table — read this on every interpretation/NPC moment
so oracle results and NPC behavior come out setting-true, competent, and dramatically L5R.

## Reading the oracle here
- Re-skin every raw oracle result (Fate Question, Meaning pair, Random Event, Turning Point) into
  **Rokugan terms**: clan politics, the Celestial Order, honor/face, giri (duty) vs ninjō (desire),
  the kami and the spirit realms, the ever-present pressure of *what is proper*.
- Lean **dramatic, not literal**: a "betray / sacred" Meaning pair is a broken on (obligation), a
  defiled shrine, a vassal forced to choose lord over love — not a generic backstab.
- Rokugan is a world of **indirection**: the truth is usually said sideways, through poetry, gifts,
  silence, and the third party. A blunt result still arrives wrapped in courtesy.
- The supernatural is **real and close** — kami answer invocations, ancestors watch, the Shadowlands
  Taint corrupts, ghosts and yūrei linger. Treat omen/spirit results as literally true unless canon says otherwise.
- **Honor the result, then record the new fact** to the campaign's `setting-canon.md`.

### The three anti-softening rules (read these every oracle/elevation moment)
1. **A Fate YES leans toward complication, not comfort.** The oracle saying "yes" is the engine handing
   you a *new problem*, not a reprieve. Read every Yes as the door that opens trouble or a thread:
   *Yes — and the favor has a price · and someone now owes/is owed · and it draws a rival's eye · and it
   binds the PC to a duty.* Save the frictionless reading for when the fiction genuinely has no edge (rare).
   A **No** still stands as a hard No (it is not softened either) — but a Yes is never a gift.
2. **Never narrate the PC's elevation — roll it.** Rokugan is an indifferent machine of rank; it does not
   rearrange itself around a low-Status samurai to be kind. So any beat that *trusts / rewards / promotes /
   befriends / centers* the PC is a **Fate Question**, asked and shown, at odds set by realism: a great
   lord confiding in a Status-30 vassal is *Unlikely*; being named heir over trueborn kin is *Very Unlikely*.
   If the dice say Yes, it arrives **with the strings a real Rokugani would attach** — a leash, a debt, a
   target on the back, the resentment of those passed over. (This is the documented fix for the prior
   campaign's "chosen-one drift," where the big elevations were authored, never rolled, and all broke the
   PC's way.)
3. **Ground politics in the facts layer.** The clan map, rivalries, court, military, and Imperial structure
   are canon — `facts.py clan <key>` · `facts.py relation <a> <b>` · `facts.py imperial` · `facts.py map`.
   Consult before inventing; the Lion and Crane are *ancestral enemies at war over Toshi Ranbo* whether or
   not that's convenient. Honor/Glory/Status & titles are mechanical — move them only through `social.py`
   (Table 7-1 scale, threshold alarms, title Status-awards), so standing can't drift upward for free.

## NPCs in this world (so NPC-behavior interpretations are competent)
- Everyone serves **someone**: a lord, a clan, an ancestor, the Emperor, a Fortune. An NPC's first
  question is rarely "what do I want" but "**what does my station/duty require, and who is watching?**"
  Their *ninjō* (private desire) pushes against that — that tension is where they become human.
- **Clan stereotypes are competent defaults, not jokes:** Crab blunt and dutiful; Crane proud,
  artful, lethal duelists; Dragon cryptic; Lion martial and honor-bound; Phoenix scholarly and
  self-righteous; Scorpion subtle, deniable, patient ("we can stop you"); Unicorn forthright and
  foreign-tinged; Minor Clans scrappy and slighted. Play each to **win by its own methods**.
- Face is currency. NPCs avoid open insult, maneuver for **advantage without losing composure**,
  and answer a loss of face with patience and a long memory — not a tantrum. A Scorpion who is
  thwarted does not rage; they smile and adjust the ledger.
- Status governs who may speak, sit, or strike first. A higher-status NPC can ruin a lower one with
  a word; a lower one fights with deference, implication, and allies. Never play a superior as dumb
  or a schemer as careless.

## Good-GM advice for L5R
- **The strife economy is the soul of the loop.** Most checks offer success *at the price of strife*;
  strife → exceeding Composure → **Unmasking** is where giri-vs-ninjō bites. Foreground the cost on
  every roll; the real drama is what the samurai must spend (face, honor, composure) to succeed.
- Stakes sit in **honor, duty, and belonging**, not just survival. "Maximal honest consequence" here
  is genre-mapped: a fight → death/maiming; a court → ruin/dishonor; a duty → seppuku or a broken
  bond; a secret → exposure that unmakes a life. The harshness scales to the scene; honesty never relaxes.
- Keep the four conflicts at **equal weight** — a winter court intrigue is as deadly as a skirmish.
- Hold the tone: restrained, formal, melancholy-beautiful; cruelty is quiet, mercy is costly.

## Term equivalences (only where helpful)
- Mythic "Magic Item" ≈ a **nemuranai** (named/awakened artifact) or a blessed object.
- Mythic "Faction / Organization" ≈ a **clan, family, or lord's house**.
- AC "Theme: Personal" ≈ the **ninjō / giri** axis; "Social" ≈ **court & intrigue**.
