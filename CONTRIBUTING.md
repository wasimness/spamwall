# Contributing

- Rules live in `rules/<country code>/`: one file per pattern in `allow/`, `block/` and `optional/` (named by ID), and `allow-apps.txt`. Every new `block/` or `optional/` pattern must name its group in a `# Group: <group>` header line: `telemarketing`, `call-centres`, `spam-mobiles` or `banks-govt` (groups are defined in `tools/build_spamblocker.py`; a new group needs a maintainer decision and README/IMPORT table rows).
- One regex per line, matched against the national number (no country code, no leading 0), followed by `# ID | what | source`.
- Prefer a range (pattern) over single numbers, but keep it narrow: a block must not catch shopping, delivery, ride, payment, bank or government service calls.
- Never add official service series (India: 1600, 1601) to `block/`.
- Never commit personal phone numbers or call logs.
- After editing, run `python -I tools/build_spamblocker.py` and commit the rebuilt files in `spamblocker/`.
- Fix false positives first. An unblock request outranks a new block.
