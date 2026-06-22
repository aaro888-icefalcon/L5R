#!/usr/bin/env python3
"""Query the L5R data stores. Returns exact rules text — pull one record, not a chapter.

  lookup.py technique <name> [--rank N] [--ring R] [--category C] [--clan C] [--source S]
  lookup.py condition <name>
  lookup.py adversary <name>
  lookup.py find <query>                 # search names across all stores + heading index
  lookup.py list techniques [--clan crane] [--rank 1] [--category kata] [--source core,..]

Filtering: `--source` and `--clan minor/ronin` are HARD gates; a plain `--clan X` is a SOFT
default — matching records sort first but others still appear (a school need not be from the clan).
"""
import argparse, json, os, sys

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
def load(name):
    p = os.path.join(DATA, name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []

STORES = {"technique": "techniques.json", "condition": "conditions.json",
          "adversary": "adversaries.json", "npc": "adversaries.json"}

def norm(s): return "".join(c for c in s.lower() if c.isalnum())

def score(rec, q):
    n, qq = norm(rec["name"]), norm(q)
    if n == qq: return 3
    if n.startswith(qq) or qq in n: return 2
    if all(w in n for w in qq.split()): return 1
    return 0

def soft_sort(rows, clan):
    if not clan: return rows
    return sorted(rows, key=lambda r: 0 if clan in r.get("clan", []) or "universal" in r.get("clan", []) else 1)

def cmd_get(kind, a):
    rows = load(STORES[kind])
    # hard source gate
    if a.source:
        srcs = set(a.source.split(","))
        rows = [r for r in rows if r["source"] in srcs]
    for attr, key in [("rank", "rank"), ("ring", "ring"), ("category", "category")]:
        v = getattr(a, attr, None)
        if v is not None:
            rows = [r for r in rows if str(r.get(key)) == str(v)]
    scored = sorted([(score(r, a.name), r) for r in rows], key=lambda x: -x[0])
    hits = [r for s, r in scored if s > 0]
    if not hits:
        print(f"No {kind} matching '{a.name}'. Try: lookup.py find {a.name}"); return
    r = hits[0]
    tags = f"[{r['source']}" + (f" · {r.get('category')}" if r.get('category') else "") \
           + (f" · rank {r['rank']}" if r.get('rank') else "") \
           + (f" · {r['ring']}" if r.get('ring') else "") + "]"
    print(f"=== {r['name']} {tags} ===\n{r['text']}")
    if len(hits) > 1:
        print(f"\n(+{len(hits)-1} more: " + ", ".join(h['name'] for h in hits[1:6]) + ")")

def cmd_find(a):
    out = []
    for kind, fn in [("technique", "techniques.json"), ("condition", "conditions.json"),
                     ("adversary", "adversaries.json")]:
        for r in load(fn):
            if score(r, a.query) > 0: out.append((kind, r["name"], r["source"]))
    for h in load("index.json"):
        if norm(a.query) in norm(h["name"]): out.append(("heading", h["name"], h["source"]))
    seen = set(); uniq = []
    for o in out:
        if o[:2] not in seen: seen.add(o[:2]); uniq.append(o)
    print(f"{len(uniq)} matches for '{a.query}':")
    for kind, name, src in uniq[:40]:
        print(f"  {kind:9} {name}  [{src}]")

def resolve_store(kind):
    k = kind.lower()
    if k.startswith("techni"): return "techniques.json"
    if k.startswith("condi"): return "conditions.json"
    if k.startswith("advers") or k.startswith("npc"): return "adversaries.json"
    return k.rstrip("s") + "s.json"

def cmd_list(a):
    rows = load(resolve_store(a.kind))
    if a.source:
        srcs = set(a.source.split(",")); rows = [r for r in rows if r["source"] in srcs]
    if a.rank is not None: rows = [r for r in rows if str(r.get("rank")) == str(a.rank)]
    if a.category: rows = [r for r in rows if r.get("category") == a.category]
    rows = soft_sort(rows, a.clan)
    lead = [r for r in rows if a.clan and (a.clan in r.get("clan", []))]
    print(f"{len(rows)} {a.kind} (clan '{a.clan}' leads; others follow — soft default)" if a.clan
          else f"{len(rows)} {a.kind}:")
    for r in rows[:60]:
        c = "*" if a.clan and a.clan in r.get("clan", []) else " "
        extra = f"r{r.get('rank')}" if r.get("rank") else ""
        print(f" {c} {r['name']:<34} {extra:<3} [{r['source']}]")

def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    for kind in ("technique", "condition", "adversary", "npc"):
        s = sub.add_parser(kind); s.add_argument("name")
        s.add_argument("--rank"); s.add_argument("--ring"); s.add_argument("--category")
        s.add_argument("--clan"); s.add_argument("--source")
        s.set_defaults(func=lambda a, k=kind: cmd_get(k, a))
    f = sub.add_parser("find"); f.add_argument("query"); f.set_defaults(func=cmd_find)
    l = sub.add_parser("list"); l.add_argument("kind")
    l.add_argument("--clan"); l.add_argument("--rank"); l.add_argument("--category"); l.add_argument("--source")
    l.set_defaults(func=cmd_list)
    a = p.parse_args(); a.func(a)

if __name__ == "__main__":
    main()
