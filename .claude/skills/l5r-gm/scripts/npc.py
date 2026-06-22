#!/usr/bin/env python3
"""Adversary COMPOSITION over the shared toolbox (master plan §9).

Antagonists draw techniques & school abilities from the SAME library PCs use; clan is a soft sort,
never an actor-gate; prerequisites are waived on grant; adversaries may exceed PC caps by intent.

  npc.py get <name>                         # retrieve a stat block (verbatim)
  npc.py list [--source S] [--clan C]
  npc.py build-rival --name N --clan C --rank R [--ring fire] [--techniques "a,b"]
        # compose a PC-footing Adversary: scaled profile + rank-appropriate techniques from the library
"""
import argparse, json, os
from random import SystemRandom
RNG = SystemRandom()
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
def load(n):
    p = os.path.join(DATA, n); return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []
def norm(s): return "".join(c for c in s.lower() if c.isalnum())

def cmd_get(a):
    rows = load("adversaries.json")
    hits = [r for r in rows if norm(a.name) in norm(r["name"])]
    if not hits: print(f"No adversary '{a.name}'. Try: lookup.py find {a.name}"); return
    print(hits[0]["text"])

def cmd_list(a):
    rows = load("adversaries.json")
    if a.source: rows = [r for r in rows if r["source"] in set(a.source.split(","))]
    if a.clan: rows = sorted(rows, key=lambda r: 0 if a.clan in r.get("clan", []) else 1)
    print(f"{len(rows)} adversaries:")
    for r in rows[:60]:
        print(f"  {r['tier']:9} {r['name']:<34} [{r['source']}]")

def cmd_rival(a):
    R = a.rank
    rings = {"air": 2, "earth": 2, "fire": 2, "water": 2, "void": 2}
    if a.ring: rings[a.ring] = 2 + (R + 1) // 2          # emphasis ring scales (may exceed PC caps)
    end = 6 + 2 * R + rings["earth"] * 2                  # illustrative derived attrs
    comp = 6 + 2 * R + rings["water"] * 2
    # pull rank-appropriate techniques from the shared library (clan = soft sort, prereqs waived on grant)
    techs = [t for t in load("techniques.json") if (t.get("rank") or 1) <= R]
    techs.sort(key=lambda t: (0 if a.clan in t.get("clan", []) or "universal" in t.get("clan", []) else 1,
                              RNG.random()))
    granted = [x.strip() for x in a.techniques.split(",")] if a.techniques else \
              [t["name"] for t in techs[:max(2, R)]]
    print(f"#### {a.name}  —  ADVERSARY (rank {R}, {a.clan})")
    print(f"CONFLICT RANK: [combat] {R + 1}   [intrigue] {max(1, R)}")
    print("RINGS: " + "  ".join(f"{k.title()} {v}" for k, v in rings.items()))
    print(f"DERIVED: Endurance {end}  Composure {comp}  Focus {R + 1}  Vigilance {1 + R // 2}")
    print(f"SCHOOL: {a.school or '(rival school — clan optional; an out-of-clan master is a story hook)'}")
    print("TECHNIQUES (from the shared toolbox; prerequisites waived on grant):")
    for g in granted:
        print(f"  • {g}")
    print("NOTES: plays to WIN — uses these techniques intelligently; defeat is real "
          "(death / dishonor / capture). Look up any technique with: lookup.py technique \"<name>\".")

def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("get"); g.add_argument("name"); g.set_defaults(func=cmd_get)
    l = sub.add_parser("list"); l.add_argument("--source"); l.add_argument("--clan"); l.set_defaults(func=cmd_list)
    r = sub.add_parser("build-rival"); r.add_argument("--name", required=True); r.add_argument("--clan", default="ronin")
    r.add_argument("--rank", type=int, default=2); r.add_argument("--ring", default="fire")
    r.add_argument("--school", default=""); r.add_argument("--techniques", default="")
    r.set_defaults(func=cmd_rival)
    a = p.parse_args(); a.func(a)

if __name__ == "__main__":
    main()
