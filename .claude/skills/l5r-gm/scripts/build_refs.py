#!/usr/bin/env python3
"""Slice the converted books into reference shards (prose, loaded on demand).

Core chapters -> rules/setting shards (Chapter 6 split per conflict subsystem). Each supplement is
copied in as one source-tagged setting shard, file-gated by the campaign active-set.

Run: python3 scripts/build_refs.py <converted_md_dir>
"""
import os, re, sys, glob

REF = os.path.join(os.path.dirname(__file__), "..", "references")
SRC = {"L5R-Emerald-Empire": "emerald-empire", "L5R-Celestial-Realms": "celestial-realms",
       "L5R-Courts-of-Stone": "courts-of-stone", "L5R-Shadowlands": "shadowlands",
       "L5R-Path-of-Waves": "path-of-waves", "L5R-Writ-of-the-Wilds": "writ-of-wilds",
       "L5R-Fields-of-Victory": "fields-of-victory"}

# core chapter title -> target shard
CORE_MAP = {
    "Introduction": "setting/intro-rokugan.md",
    "Chapter 1: Playing the Game": "resolution/checks-strife-and-the-character.md",
    "Chapter 2: Creating a Character": "character/creation.md",
    "Chapter 3: Skills": "character/skills.md",
    "Chapter 4: Techniques": "techniques/overview.md",
    "Chapter 5: Equipment": "equipment/equipment.md",
    "Chapter 6: Scenes and Conflicts": "__SPLIT__",
    "Chapter 7: The Game Master": "gm/running-the-game.md",
    "Chapter 8: Non-Player Characters": "gm/npc-design.md",
}

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

def front(source, title, scope):
    return f"---\nsource: {source}\ntitle: {title}\nscope: {scope}\n---\n\n"

def write(rel, text):
    path = os.path.join(REF, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    return rel, len(text.split())

def split_core(md_dir):
    core = open(os.path.join(md_dir, "L5R-5th-Edition.md"), encoding="utf-8").read()
    # chapter boundaries on top-level '# ' headings
    parts = re.split(r"(?m)^# (.+)$", core)
    # parts: [pre, title1, body1, title2, body2, ...]
    out = []
    for i in range(1, len(parts), 2):
        title, body = parts[i].strip(), parts[i + 1]
        tgt = CORE_MAP.get(title)
        if not tgt:
            continue
        if tgt == "__SPLIT__":
            # split Chapter 6 by its H2 sections into conflict shards
            subs = re.split(r"(?m)^## (.+)$", body)
            header = subs[0]
            for j in range(1, len(subs), 2):
                stitle, sbody = subs[j].strip(), subs[j + 1]
                rel = f"conflict/{slug(stitle)}.md"
                out.append(write(rel, front("core", stitle, "conflict")
                                 + f"# {stitle}\n{sbody}"))
        else:
            scope = tgt.split("/")[0]
            out.append(write(tgt, front("core", title, scope) + f"# {title}\n{body}"))
    return out

def copy_supplements(md_dir):
    out = []
    for p in sorted(glob.glob(os.path.join(md_dir, "L5R-*.md"))):
        base = os.path.basename(p)[:-3]
        src = SRC.get(base)
        if not src:
            continue
        text = open(p, encoding="utf-8").read()
        rel = f"setting/{src}.md"
        out.append(write(rel, front(src, base, "supplement (file-gated by active_set)") + text))
    return out

def main():
    md_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    res = split_core(md_dir) + copy_supplements(md_dir)
    for rel, words in res:
        print(f"  {rel:<52} {words:>7} words")
    print(f"wrote {len(res)} reference shards")

if __name__ == "__main__":
    main()
