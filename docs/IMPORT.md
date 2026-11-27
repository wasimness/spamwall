# Import guide (SpamBlocker)

> **Read this first**
>
> - Settings and rules import separately. `settings.gz` only touches app settings (allow switches, Recent Apps) and never your number rules. `rules-*.gz` and `types/*.gz` only touch number rules. `complete.gz` does both.
> - Number-rule imports do not stack. Each import replaces ALL number rules, including your own and any earlier SpamWall import. Pick ONE: a single type file (blocks only that kind of call) OR `rules-default.gz` / `rules-strict.gz` (all types). For two or three types, import the all-types file, or import one type file and add the other patterns by hand with "New" in Number Rules, copying the regex from `rules/in/block/<ID>.txt`.
> - Importing `settings.gz` replaces your Recent Apps list and the allow switches.
> - Always export a backup first; importing it again is the undo.
> - The maintainer has not tested this on every phone and SpamBlocker version. Report problems as [issues](../../issues).

## What you need

SpamBlocker for Android, from [F-Droid](https://f-droid.org/packages/spam.blocker/) or the [GitHub releases](https://github.com/aj3423/SpamBlocker/releases). Download the SpamWall files from the [latest release](../../releases/latest).

## Which file to pick

| Label | File | Description | Download |
|---|---|---|---|
| Everything | `complete.gz` | Settings plus default rules, one-tap full setup (SpamBlocker) | [Download](https://github.com/wasimness/spamwall/releases/latest/download/complete.gz) |
| App settings | `settings.gz` | Only the Others category: contacts, STIR, repeated call, dialed, answered, Recent Apps | [Download](https://github.com/wasimness/spamwall/releases/latest/download/settings.gz) |
| All rules | `rules-default.gz` | Only the Regex Settings category: allow rules and default block rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/rules-default.gz) |
| Strict rules | `rules-strict.gz` | `rules-default` plus IN-1600 (bank and government service calls) | [Download](https://github.com/wasimness/spamwall/releases/latest/download/rules-strict.gz) |
| Promo calls (140) | `IN-140.gz` | Block the 140 promotional series, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/IN-140.gz) |
| Call-centre landlines | `IN-CC-LANDLINE.gz` | Block call-centre landline ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/IN-CC-LANDLINE.gz) |
| Bengaluru call centres | `IN-CC-BLR.gz` | Block narrow Bengaluru call-centre blocks, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/IN-CC-BLR.gz) |
| Bulk telemarketing mobiles | `IN-BULK-MOBILE.gz` | Block bulk telemarketing mobile ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/IN-BULK-MOBILE.gz) |
| Bank and govt series (1600) | `IN-1600.gz` | Block the official 1600 service series (also blocks your real bank), plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/IN-1600.gz) |
| Raw list (CSV) | `spamwall-in.csv` | Every pattern and business number, for any app or spreadsheet | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.csv) |
| Raw list (JSON) | `spamwall-in.json` | Same data with a meta object, for scripts and AI | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.json) |
| Raw list (Markdown) | `spamwall-in.md` | Table for manual copying | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.md) |

Each file also has a readable `.json` twin in `spamblocker/`. Release assets are flat, so every file name is unique.

## Using SpamWall without SpamBlocker

The raw lists in `raw/` (CSV, JSON, Markdown) are app-agnostic: the same rows as the SpamBlocker files, with columns `type,id,kind,value,description,source,priority`. `type` is allow, block or optional; `kind` is `pattern` (a regular expression) or `number` (an exact number). Numbers and patterns match the national number, without +91 or a leading 0.

- **Any blocker or your phone's own block list:** open the CSV or Markdown file and copy what you need. Add `number` rows one by one, or paste them in bulk where the app allows.
- **Patterns need regex or prefix blocking.** If your app only blocks exact numbers, use the `number` rows. If it supports prefixes, turn simple patterns such as `^140\d{7}$` into the prefix `140`.
- **Build rules for another app with AI or a script:** feed `spamwall-in.json` (rules plus a `meta` object) to an AI assistant or a script and ask it to produce the format your app imports.
- **Mobile numbers are left out on purpose.** Individual 10-digit mobile numbers (starting 6 to 9) are never listed, for privacy. Only landline, toll-free and series numbers appear as `number` rows.


## Step-by-step import

1. In SpamBlocker, open **Settings > Backup > Export** and save a backup of your current setup first.
2. Download the file you picked to your phone.
3. Open **Settings > Backup > Import** and pick the file.
4. In the **Include Settings** dialog, tap a category to move it between Include and Exclude. Keep only the category the file has (Others for `settings.gz`, Regex Settings for `rules-*.gz` and `types/*.gz`, both for `complete.gz`).
5. Confirm the import.

## Nuances

- Import REPLACES the whole section. Number rules are cleared and re-added, so importing a `rules-*.gz` file (or `complete.gz`) deletes your own number rules. Export first, or add your own rules again afterwards.
- A file that lacks a category shows "This setting is missing from the backup file and cannot be restored" for that category. Exclude it, as in step 4.
- Allow and block rules must never share a priority. Here allow is 15, the built-in allow checks are 10 and block is 5.
- Numbers are matched without +91 or a leading 0.
- Recent Apps ignores apps that are not installed.
- If you install a new shopping app, add it in Recent Apps by hand.

## Manual steps the import cannot do

- Grant SpamBlocker's permissions when it asks: the call screening role, contacts, and usage access for Recent Apps.
- Turn on SMS screening under **Settings > Screening** if you want it, and follow the app's prompts.
- Add your own bank and broker numbers to contacts (with the strict file).
- Optionally turn off Tellows, which sends unknown numbers to tellows.com.
- On Xiaomi/MIUI, allow autostart and set no battery restriction for SpamBlocker so screening keeps running.

## Using single patterns in another app

Each pattern is one file: `rules/in/<type>/<ID>.txt`, where type is `allow`, `block` or `optional`. Copy the regex from the line (the part before `#`) into any blocker that accepts regular expressions. [`rules/in/patterns.md`](../rules/in/patterns.md) lists every pattern.

## Undo

Import the backup you exported in step 1.
