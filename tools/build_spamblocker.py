"""Build the SpamBlocker one-click import files from rules/<country>/*.txt.

Usage: python -I tools/build_spamblocker.py
Writes spamblocker/spamwall-<cc>.json, spamwall-<cc>.gz (default) and
spamwall-<cc>-strict.gz (also blocks the optional list).
"""
import gzip
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "spamblocker"
ALLOW_PRIORITY = 15  # whitelist rules run first
BLOCK_PRIORITY = 5   # never equal to an allow priority (SpamBlocker issue #166)
FLAGS_CALL_AND_SMS = 3
REGEX_FLAGS = 8192


def read_rules(path):
    rules = []
    if not path.exists():
        return rules
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        pattern, _, note = line.partition("#")
        parts = [p.strip() for p in note.split("|")]
        rules.append({"pattern": pattern.strip(), "id": parts[0], "what": parts[1] if len(parts) > 1 else ""})
    return rules


def rule(idx, r, blacklist):
    re.compile(r["pattern"])
    return {
        "id": idx, "pattern": r["pattern"], "patternFlags": REGEX_FLAGS, "patternModeType": 0,
        "patternExtra": "", "patternExtraFlags": 0, "patternExtraModeType": 0,
        "description": f"spamwall {r['id']}: {r['what']}"[:120],
        "priority": BLOCK_PRIORITY if blacklist else ALLOW_PRIORITY,
        "isBlacklist": blacklist, "flags": FLAGS_CALL_AND_SMS, "channel": "Low",
        "schedule": "", "blockType": 0, "blockTypeConfig": "",
    }


def build(cc, strict):
    d = ROOT / "rules" / cc
    allow, block = read_rules(d / "allow.txt"), read_rules(d / "block.txt")
    if strict:
        block += read_rules(d / "optional-block.txt")
    rules = [rule(i + 100, r, False) for i, r in enumerate(allow)]
    rules += [rule(i + 200, r, True) for i, r in enumerate(block)]
    return {
        "categories": {"all": ["OTHERS", "REGEX_RULES"]},
        "contacts": {"enabled": True, "isExcusive": False, "permissivePriority": 10, "strictPriority": 0},
        "stir": {"enabled": True, "includeUnverified": False, "strictPriority": 0},
        "repeatedCall": {"enabled": True, "times": 1, "inXMin": 5},
        "dialed": {"enabled": True, "smsEnabled": True, "always": False, "inXDay": 7},
        "answered": {"warningAcknowledged": True, "enabled": True, "minDuration": 15, "inXDay": 7},
        "numberRules": {"rules": rules},
    }


def main():
    OUT.mkdir(exist_ok=True)
    for cc_dir in sorted((ROOT / "rules").iterdir()):
        cc = cc_dir.name
        for strict in (False, True):
            name = f"spamwall-{cc}{'-strict' if strict else ''}"
            data = json.dumps(build(cc, strict), indent=1, ensure_ascii=False)
            (OUT / f"{name}.json").write_text(data, encoding="utf-8")
            with gzip.GzipFile(OUT / f"{name}.gz", "wb", mtime=0) as f:
                f.write(data.encode("utf-8"))
            print("built", name)


if __name__ == "__main__":
    main()
