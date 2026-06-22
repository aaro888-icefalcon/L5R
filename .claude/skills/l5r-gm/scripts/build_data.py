#!/usr/bin/env python3
"""Decompose the converted L5R books into tagged, queryable data.

Lossless approach: structured where the source is clean (conditions; technique rank/ring),
verbatim-text-by-name everywhere else, plus a master index so lookup.py can return the exact
rules text for any named entry across all 8 books.

Run:  python3 scripts/build_data.py /path/to/converted_md_dir
Outputs into ../data/:  techniques.json conditions.json adversaries.json index.json manifest.json
"""
import json, os, re, sys, glob

SRC = {
    "L5R-5th-Edition": "core", "L5R-Emerald-Empire": "emerald-empire",
    "L5R-Celestial-Realms": "celestial-realms", "L5R-Courts-of-Stone": "courts-of-stone",
    "L5R-Shadowlands": "shadowlands", "L5R-Path-of-Waves": "path-of-waves",
    "L5R-Writ-of-the-Wilds": "writ-of-wilds", "L5R-Fields-of-Victory": "fields-of-victory",
}
CLAN_HINT = {"core": "universal", "emerald-empire": "universal", "celestial-realms": "phoenix",
             "courts-of-stone": "crane", "shadowlands": "crab", "path-of-waves": "ronin",
             "writ-of-wilds": "minor", "fields-of-victory": "lion"}
CLANS = ["crab", "crane", "dragon", "lion", "phoenix", "scorpion", "unicorn"]
RINGS = ["air", "earth", "fire", "water", "void"]
CATS = {"kata": "kata", "kihō": "kiho", "kiho": "kiho", "invocation": "invocation",
        "ritual": "ritual", "shūji": "shuji", "shuji": "shuji", "mahō": "maho",
        "maho": "maho", "ninjutsu": "ninjutsu"}

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")

def detect(text, options):
    t = text.lower()
    return [o for o in options if re.search(r"\b" + re.escape(o) + r"\b", t)]

def parse_book(path):
    src = SRC.get(os.path.basename(path)[:-3], slug(os.path.basename(path)))
    lines = open(path, encoding="utf-8").read().split("\n")
    techniques, conditions, adversaries, index = [], [], [], []
    cur_h2 = cur_h3 = ""
    i = 0
    while i < len(lines):
        ln = lines[i]
        mh = re.match(r"^(#{2,6}) (.+)$", ln)
        if mh:
            lvl, title = len(mh.group(1)), mh.group(2).strip()
            if lvl == 2: cur_h2, cur_h3 = title, ""
            elif lvl == 3: cur_h3 = title
            index.append({"name": title, "level": lvl, "source": src, "line": i + 1})
            # condition: ### Name then **Description:**
            if lvl == 3 and i + 2 < len(lines):
                blk = "\n".join(lines[i + 1:i + 8])
                if "**Description:**" in blk and "**Effects:**" in blk:
                    body = []
                    j = i + 1
                    while j < len(lines) and not re.match(r"^#{1,6} ", lines[j]):
                        body.append(lines[j]); j += 1
                    btext = "\n".join(body).strip()
                    conditions.append({"id": f"cond.{slug(title)}", "name": title,
                        "type": "condition", "source": src,
                        "description": _field(btext, "Description"), "effects": _field(btext, "Effects"),
                        "text": btext})
            i += 1; continue
        # technique: a name line, then (blank lines), then "Rank N"
        m = re.match(r"^Rank ([0-9])\s*$", ln)
        if m:
            k = i - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            name = lines[k].strip().strip("*_ ") if k >= 0 else ""
            ok = (name and 2 <= len(name) <= 55 and name[0].isupper()
                  and not name.startswith(("#", "-", "**", "_"))
                  and not re.search(r"[.:,]$", name) and "Rank" not in name
                  and name not in ("Effects", "Activation", "Description", "New Techniques"))
            if ok:
                j = i + 1
                while j < len(lines) and not re.match(r"^#{1,6} ", lines[j]) \
                        and not re.match(r"^Rank [0-9]\s*$", lines[j]):
                    j += 1
                end = j
                if j < len(lines) and re.match(r"^Rank [0-9]\s*$", lines[j]):
                    e = j - 1
                    while e > i and not lines[e].strip():
                        e -= 1
                    end = e  # exclude the NEXT technique's name line
                btext = "\n".join(lines[k:end]).strip()
                if ("**Activation:**" in btext or "**Effects:**" in btext or "[opportunity]" in btext):
                    rings = detect(btext, RINGS)
                    cat = next((CATS[c] for c in CATS if c in (cur_h2 + " " + cur_h3).lower()), None)
                    techniques.append({"id": f"tech.{slug(name)}", "name": name, "type": "technique",
                        "category": cat, "rank": int(m.group(1)),
                        "ring": rings[0] if rings else None, "source": src,
                        "clan": _clan_ctx(cur_h2, cur_h3, src), "text": btext})
                    i = end; continue
        # adversary / minion stat block: marker line; name = nearest preceding heading
        if re.match(r"^(ADVERSARY|MINION)\b", ln.strip()):
            name = ""
            for k in range(i - 1, max(0, i - 6), -1):
                hm = re.match(r"^#{3,6} (.+)$", lines[k])
                if hm: name = hm.group(1).strip(); break
            if name:
                body = []
                j = i
                while j < len(lines) and not re.match(r"^#{1,5} ", lines[j]) and j < i + 60:
                    body.append(lines[j]); j += 1
                adversaries.append({"id": f"npc.{slug(name)}", "name": name, "type": "adversary",
                    "tier": "minion" if ln.strip().startswith("MINION") else "adversary",
                    "source": src, "clan": _clan_ctx(cur_h2, cur_h3, src),
                    "text": (("#### " + name + "\n") + "\n".join(body)).strip()})
        i += 1
    return techniques, conditions, adversaries, index

def _field(text, label):
    m = re.search(r"\*\*" + label + r":\*\*\s*(.+?)(?=\n\*\*[A-Z]|\Z)", text, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

def _clan_ctx(h2, h3, src):
    ctx = (h2 + " " + h3).lower()
    found = [c for c in CLANS if c in ctx]
    return found if found else [CLAN_HINT.get(src, "universal")]

def main():
    md_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    out = os.path.join(os.path.dirname(__file__), "..", "data")
    T, C, A, I = [], [], [], []
    for p in sorted(glob.glob(os.path.join(md_dir, "L5R-*.md"))):
        if any(x in p for x in ("Build-Plan", "Master-Plan", "Addendum", "Tagging", ".body.")):
            continue
        t, c, a, idx = parse_book(p)
        T += t; C += c; A += a; I += idx
        print(f"  {os.path.basename(p):<28} techniques={len(t):4} conditions={len(c):3} adversaries={len(a):3}")
    # de-dup techniques by id (keep first / core priority already by sort order)
    def dedup(rows):
        seen = {};
        for r in rows:
            seen.setdefault(r["id"], r)
        return list(seen.values())
    T, C, A = dedup(T), dedup(C), dedup(A)
    json.dump(T, open(f"{out}/techniques.json", "w"), ensure_ascii=False, indent=0)
    json.dump(C, open(f"{out}/conditions.json", "w"), ensure_ascii=False, indent=0)
    json.dump(A, open(f"{out}/adversaries.json", "w"), ensure_ascii=False, indent=0)
    json.dump(I, open(f"{out}/index.json", "w"), ensure_ascii=False, indent=0)
    manifest = {"techniques": len(T), "conditions": len(C), "adversaries": len(A),
                "index_headings": len(I), "sources": sorted(set(SRC.values()))}
    json.dump(manifest, open(f"{out}/manifest.json", "w"), ensure_ascii=False, indent=2)
    print("TOTAL:", manifest)

if __name__ == "__main__":
    main()
