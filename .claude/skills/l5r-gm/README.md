# l5r-gm — Legend of the Five Rings 5E Game Master skill

A self-contained, mythic-gm-compatible GM engine for running a challenging, tactical, full-spectrum
**Legend of the Five Rings 5th Edition** campaign in Rokugan.

- **SKILL.md** — the router/spine: creed, the three-tier play loop, the oracle ladder, the discipline,
  the reference-loading guide, and script commands.
- **scripts/** — honest engines: `dice.py` (roll-and-keep, validated), `lookup.py` (query the data),
  `oracle.py` (generation primitives + oracle-ladder router), `npc.py` (compose antagonists from the
  shared toolbox), `state.py`, `build_data.py` / `build_refs.py` (rebuild content from the books).
- **data/** — tagged, queryable content extracted from all 8 books: 315 techniques, 206 adversaries,
  20 conditions, the exact dice faces, and a 3.9k-entry heading index.
- **references/** — rules prose sharded by subsystem (resolution, the four conflicts, character, GM)
  plus the full setting, file-gated by the campaign active-set so unused books cost no context.
- **assets/templates/** — character sheet, campaign state (with the active-set filter), conflict
  tracker, the mythic system-profile, and setting-canon.

Honest dice are rolled in the shell and shown — never invented. Defeat (death, dishonor, seppuku,
capture, ruin) is real. To rebuild data from the converted books:
`python3 scripts/build_data.py <md_dir> && python3 scripts/build_refs.py <md_dir>`.

*This is a working v1 vertical slice + full content extraction. See the master plan for the full
roadmap (structured schools/heritages/titles/artifacts, npc.py composition depth, finer setting
sharding, and the skill-creator eval harness).*
