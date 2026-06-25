#!/usr/bin/env python3
"""
facts.py — query the canon-grounded Rokugan FACTS layer (bridge/facts/*.json).

The setting canon is rich prose but was not queryable as data, so under load the GM
"remembered" politics instead of looking them up — and remembered politics bend toward
convenience. This tool makes the load-bearing facts (clan relations, Imperial structure,
the map, the title catalog) retrievable in one shot, so political/military/social play is
GROUNDED, not invented. The discipline: CONSULT facts before inventing any such detail;
record campaign-discovered facts to campaigns/<slug>/setting-canon.md (which overrides this).

Commands:
  clans                       list every clan (name · agenda one-liner)
  clan <key>                  full record for one clan (relations, court, military, tensions)
  relation <keyA> <keyB>      how two clans stand to each other (ally / rival / enemy / at war)
  imperial                    the Throne, Hands of the Emperor, Imperial families, courts & law
  map [clan]                  territorial regions & (derived) borders
  titles [name]               the title catalog (military/Imperial) + Status bands; or one title
  search <query>              grep across all facts files
"""
import os, sys, json, glob

FACTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "bridge", "facts")


def _load(name):
    p = os.path.join(FACTS, name)
    if not os.path.exists(p):
        sys.exit(f"missing {p} — (re)build the facts layer")
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def cmd_clans():
    d = _load("clans.json")
    for key, c in d["clans"].items():
        print(f"  {key:18} {c['name']}")
        print(f"  {'':18} {(c.get('agenda') or '')[:110]}")
    print("\nRelations summary:")
    for r in d.get("relations_summary", []):
        print("  • " + r)


def cmd_clan(key):
    d = _load("clans.json")
    c = d["clans"].get(key)
    if not c:
        sys.exit(f"no clan '{key}'. keys: {', '.join(d['clans'])}")
    print(f"=== {c['name']}  [{c.get('type')}]  key={key} ===")
    print(f"Leader:  {c.get('leader','')}")
    print(f"Agenda:  {c.get('agenda','')}")
    if c.get("personality"): print(f"Register: {c['personality']}")
    if c.get("families"):    print(f"Families: {', '.join(c['families'])}")
    print(f"Court:   {c.get('court_power','')}")
    print(f"Military:{c.get('military','')}")
    for rel in ("allies", "rivals", "enemies"):
        if c.get(rel): print(f"{rel.capitalize():8}: {', '.join(c[rel])}")
    if c.get("ancestral_enemy"): print(f"Ancestral enemy: {c['ancestral_enemy']}")
    if c.get("at_war"): print(f"AT WAR:  {', '.join(c['at_war'])}")
    print(f"Tensions: {c.get('tensions','')}")


def cmd_relation(a, b):
    d = _load("clans.json")
    clans = d["clans"]
    if a not in clans or b not in clans:
        sys.exit(f"unknown clan key(s). keys: {', '.join(clans)}")
    ca, cb = clans[a], clans[b]
    def standing(src, dst_key):
        tags = []
        for rel in ("allies", "rivals", "enemies", "at_war"):
            if dst_key in (src.get(rel) or []): tags.append(rel)
        if src.get("ancestral_enemy") == dst_key: tags.append("ANCESTRAL ENEMY")
        return tags or ["(no direct relation recorded — neutral/contextual)"]
    print(f"{ca['name']}  →  {cb['name']}:  {', '.join(standing(ca, b))}")
    print(f"{cb['name']}  →  {ca['name']}:  {', '.join(standing(cb, a))}")
    for r in d.get("relations_summary", []):
        if a in r and b in r: print("  • " + r)


def cmd_imperial():
    d = _load("imperial.json")
    t = d["throne"]
    print("=== THE THRONE ===")
    for k in ("title", "seat", "mandate"): print(f"  {t.get(k,'')}")
    h = d["hands_of_the_emperor"]
    print("\n=== HANDS OF THE EMPEROR ===")
    print(f"  LEFT  (laws/edicts):  {h['left_hand']}")
    print(f"  RIGHT (the army):     {h['right_hand']}")
    print("\n=== IMPERIAL FAMILIES ===")
    for f in d["imperial_families"]: print(f"  {f['name']}: {f['role']}")
    print("\n=== COURTS & LAW ===")
    for k, v in d["courts_and_law"].items(): print(f"  [{k}] {v}")


def cmd_map(clan=None):
    d = _load("map.json")
    print(d["note"]); print()
    for r in d["regions"]:
        if clan and r["clan"] != clan: continue
        print(f"  {r['clan']:10} {(r.get('region') or '')}")
        print(f"  {'':10} borders: {', '.join(r.get('borders', []))}")
    if not clan:
        print("\nLandmarks:")
        for k, v in d.get("landmarks", {}).items(): print(f"  {k}: {v}")


def cmd_titles(name=None):
    d = _load("titles.json")
    if name:
        t = next((t for t in d["titles"] if name.lower() in t["name"].lower()), None)
        if not t: sys.exit(f"no title matching '{name}'. have: {', '.join(x['name'] for x in d['titles'])}")
        print(json.dumps(t, ensure_ascii=False, indent=1)); return
    print("Status bands (Table 7-4, corrected):")
    for b in d.get("status_bands_table_7_4_corrected", []):
        print(f"  {b['band']:6} {b['exemplars']}")
    print("\nTitle catalog (military / Imperial):")
    for t in d["titles"]:
        print(f"  ★ {t['name']:34} status {t.get('status_award','?')}  ({t.get('xp_to_completion','?')} xp)")
    print("\n(facts.py titles \"Gunsō\" for a full title + ability)")


def cmd_search(q):
    ql = q.lower(); hits = 0
    for p in sorted(glob.glob(os.path.join(FACTS, "*.json"))):
        txt = open(p, encoding="utf-8").read()
        for ln in txt.splitlines():
            if ql in ln.lower():
                print(f"  [{os.path.basename(p)}] {ln.strip()[:160]}"); hits += 1
    if not hits: print(f"  (no facts match '{q}')")


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    cmd = a[0]
    if   cmd == "clans":    cmd_clans()
    elif cmd == "clan":     cmd_clan(a[1])
    elif cmd == "relation": cmd_relation(a[1], a[2])
    elif cmd == "imperial": cmd_imperial()
    elif cmd == "map":      cmd_map(a[1] if len(a) > 1 else None)
    elif cmd == "titles":   cmd_titles(a[1] if len(a) > 1 else None)
    elif cmd == "search":   cmd_search(" ".join(a[1:]))
    else: sys.exit(f"unknown command '{cmd}'\n{__doc__}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try: sys.stdout.close()
        except Exception: pass
