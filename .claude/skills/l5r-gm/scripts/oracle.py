#!/usr/bin/env python3
"""Self-contained generation primitives + the oracle-ladder router (master plan §4).

Generation order: CANON first -> an L5R-native generator if one exists -> a Mythic oracle, then
RE-SKIN the raw result into Rokugan and RECORD it to canon. These primitives cover the Mythic rung
when mythic-gm isn't loaded; with --defer-mythic they print the equivalent mythic command instead.

  oracle.py fate <odds> [--cf 5] [--defer-mythic]      # yes/no Fate Question
  oracle.py meaning [--n 1]                             # action + descriptor inspiration pair
  oracle.py event                                       # random event: focus + meaning
  oracle.py name [--kind person|place|family]           # L5R-flavored name (rung-2 native table)
  oracle.py route "<what to generate>"                  # print the ladder routing for a need
"""
import argparse, json, os
from random import SystemRandom
RNG = SystemRandom()

ODDS = {"certain": 95, "nearly-certain": 90, "very-likely": 85, "likely": 75, "50-50": 50,
        "unlikely": 25, "very-unlikely": 15, "nearly-impossible": 10, "impossible": 5}
ACTIONS = ["Oppose", "Pursue", "Honor", "Betray", "Conceal", "Reveal", "Demand", "Offer", "Protect",
           "Abandon", "Threaten", "Bargain", "Mourn", "Celebrate", "Judge", "Forgive", "Provoke",
           "Submit", "Investigate", "Sabotage", "Bless", "Curse", "Ally", "Exile", "Summon", "Refuse"]
DESCRIPTORS = ["honorable", "treacherous", "desperate", "serene", "ambitious", "ruinous", "sacred",
               "corrupt", "fragile", "ancient", "hidden", "lavish", "austere", "vengeful", "loyal",
               "shameful", "fated", "tainted", "dutiful", "proud", "secret", "doomed", "auspicious"]
FOCUS = ["a rival clan acts", "an ancestor's legacy", "duty vs. desire (giri/ninjō)", "a courtly intrigue",
         "an omen or kami", "a debt comes due", "violence erupts", "a secret surfaces", "the Taint stirs",
         "a superior's command", "a peasant's plight", "the weather/season turns", "an outsider arrives"]
NAMES_PERSON = ["Hotaru", "Kachiko", "Toshimoko", "Sukune", "Yoshi", "Akodo", "Tetsuko", "Shinjo",
                "Doji", "Bayushi", "Mirumoto", "Isawa", "Kuni", "Utaku", "Hida", "Asako", "Kitsuki"]
NAMES_PLACE = ["Kyūden", "Shiro", "Mura", "Toshi Ranbo", "Otosan Uchi", "Beiden Pass", "Crane's Wing",
               "the Wall", "Pale Oak", "Last Stand", "Five Dragons", "Wintry Falls"]
FAMILIES = ["Akodo", "Doji", "Hida", "Isawa", "Bayushi", "Shinjo", "Mirumoto", "Kakita", "Kuni",
            "Asako", "Ide", "Yogo", "Agasha", "Matsu", "Daidoji", "Soshi", "Utaku"]

def cmd_fate(a):
    if a.defer_mythic:
        print(f"[defer-mythic] run: python3 <mythic>/scripts/dice.py fate {a.odds} {a.cf}"); return
    tgt = ODDS.get(a.odds.lower())
    if tgt is None:
        print("odds: " + ", ".join(ODDS)); return
    roll = RNG.randint(1, 100)
    yes = roll <= tgt
    exc = roll <= max(1, tgt // 5) or roll >= 100 - (100 - tgt) // 5
    d1, d2 = roll // 10, roll % 10
    event = (d1 == d2) and (d1 <= a.cf)
    print(f"[Adjudication: Fate Question — {a.odds} (yes≤{tgt}), Chaos {a.cf}]")
    print(f"  d100 = {roll}  ->  {'EXCEPTIONAL ' if exc else ''}{'YES' if yes else 'NO'}")
    if event:
        print("  doubles ≤ Chaos -> RANDOM EVENT fires (run: oracle.py event)")
    print("  -> honor this result; re-skin into Rokugan; record the new fact to canon.")

def cmd_meaning(a):
    for _ in range(a.n):
        print(f"  {RNG.choice(ACTIONS)} / {RNG.choice(DESCRIPTORS)}")
    print("  -> interpret as L5R: clan politics, honor, giri/ninjō, the Celestial Order.")

def cmd_event(a):
    print(f"[Random Event]  Focus: {RNG.choice(FOCUS)}")
    print(f"  Meaning: {RNG.choice(ACTIONS)} / {RNG.choice(DESCRIPTORS)}")
    print("  -> weave into the scene now; honor it; record to canon/state.")

def cmd_name(a):
    if a.kind == "place":
        print("  " + RNG.choice(NAMES_PLACE) + " " + RNG.choice(["Province", "Castle", "Village", "Pass", "Shrine"]))
    elif a.kind == "family":
        print("  " + RNG.choice(FAMILIES))
    else:
        print("  " + RNG.choice(FAMILIES) + " " + RNG.choice(NAMES_PERSON))
    print("  (rung-2 native table; for richer names see Path of Waves name tables)")

LADDER = {
  "name": ("Name tables (Path of Waves)", "oracle.py name / mythic Meaning Tables"),
  "npc-motive": ("Demeanors; 'NPC Motivations through Needs' (Courts of Stone)", "oracle.py meaning / mythic NPC behavior"),
  "npc-stats": ("NPC Templates + npc.py", "mythic NPC Statistics -> express in L5R units"),
  "court": ("'Assembling a Court in Seven Steps' (Courts of Stone)", "oracle.py meaning + fate"),
  "oni": ("Oni Generation (Shadowlands)", "oracle.py meaning -> re-skin"),
  "scene-shift": ("scene types (Ch.6); prepared adventures/", "mythic Scene Test"),
  "complication": ("—", "oracle.py event (Random Event)"),
  "plot-beat": ("sample adventures; three-act tools (Path of Waves)", "mythic Adventure Crafter turning-point"),
  "yes-no": ("— (L5R has no general oracle)", "oracle.py fate <odds> <cf>"),
}
def cmd_route(a):
    print("Oracle ladder: 1) CANON first  2) L5R-native generator  3) Mythic oracle -> re-skin to Rokugan.")
    key = a.what.lower().replace(" ", "-")
    hit = LADDER.get(key)
    if hit:
        print(f"  '{a.what}':  rung-2 L5R: {hit[0]}\n            rung-3 Mythic: {hit[1]}")
    else:
        print("  topics: " + ", ".join(LADDER))
        print(f"  no specific L5R generator known for '{a.what}' -> use a Mythic oracle, then re-skin.")

def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fate"); f.add_argument("odds"); f.add_argument("--cf", type=int, default=5)
    f.add_argument("--defer-mythic", action="store_true"); f.set_defaults(func=cmd_fate)
    m = sub.add_parser("meaning"); m.add_argument("--n", type=int, default=1); m.set_defaults(func=cmd_meaning)
    e = sub.add_parser("event"); e.set_defaults(func=cmd_event)
    n = sub.add_parser("name"); n.add_argument("--kind", default="person"); n.set_defaults(func=cmd_name)
    r = sub.add_parser("route"); r.add_argument("what"); r.set_defaults(func=cmd_route)
    a = p.parse_args(); a.func(a)

if __name__ == "__main__":
    main()
