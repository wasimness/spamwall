# Import guide (SpamBlocker)

> **Read this first**
>
> - Settings and rules import separately. `spamblocker-settings.gz` only touches app settings (allow switches, Recent Apps) and never your number rules. `spamblocker-all-rules.gz` and the four group files (`spamblocker-telemarketing.gz`, `spamblocker-call-centres.gz`, `spamblocker-spam-mobiles.gz`, `spamblocker-banks-govt.gz`) only touch number rules. `spamblocker-full-setup.gz` does both.
> - Number-rule imports do not stack. Each import replaces ALL number rules, including your own and any earlier SpamWall import. To block two or three groups, import `spamblocker-all-rules.gz`, or import one group and add the other patterns by hand with "New" in Number Rules, copying the regex from `rules/in/block/<ID>.txt`. For all rules plus banks, import `spamblocker-all-rules.gz` and add IN-1600 (from `rules/in/optional/IN-1600.txt`) by hand.
> - Importing `spamblocker-settings.gz` replaces your Recent Apps list and the allow switches.
> - Always export a backup first; importing it again is the undo.
> - The maintainer has not tested this on every phone and SpamBlocker version. Report problems as [issues](../../issues).

## What you need

SpamBlocker for Android, from [F-Droid](https://f-droid.org/packages/spam.blocker/) or the [GitHub releases](https://github.com/aj3423/SpamBlocker/releases). Download the SpamWall files from the [latest release](../../releases/latest).

## Which file to pick

| Label | File | Description | Download |
|---|---|---|---|
| Full setup (recommended) | `spamblocker-full-setup.gz` | App settings plus all spam rules in one import | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-full-setup.gz) |
| App settings only | `spamblocker-settings.gz` | Only the Others category: contacts, STIR, repeated call, dialed, answered, Recent Apps | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-settings.gz) |
| All spam rules | `spamblocker-all-rules.gz` | Allow rules plus the three default groups (not the bank group) | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-all-rules.gz) |
| Promo and telemarketing calls | `spamblocker-telemarketing.gz` | Group `telemarketing`: the 140 promotional series, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-telemarketing.gz) |
| Call-centre ranges | `spamblocker-call-centres.gz` | Group `call-centres`: call-centre landline and Bengaluru ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-call-centres.gz) |
| Spam mobile ranges | `spamblocker-spam-mobiles.gz` | Group `spam-mobiles`: bulk telemarketing mobile ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-spam-mobiles.gz) |
| Bank and government calls (optional) | `spamblocker-banks-govt.gz` | Group `banks-govt`: the official 1600 series (also blocks your real bank), plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamblocker-banks-govt.gz) |
| Raw list (CSV) | `spamwall-in.csv` | Every pattern and business number with its group, for any app or spreadsheet | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.csv) |
| Raw list (JSON) | `spamwall-in.json` | Same data with a meta object, for scripts and AI | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.json) |

Groups don't stack in SpamBlocker (each rules import replaces the number rules), so to block two groups, import `spamblocker-all-rules.gz`, or import one group and add the other patterns by hand from `rules/in/`. For all rules plus banks, import `spamblocker-all-rules.gz`, then add the IN-1600 pattern by hand.

Each `.gz` also has a readable `.json` twin in `spamblocker/`. The Markdown table `raw/spamwall-in.md` is for reading in the repo, not a release download. Release assets are flat, so every file name is unique.

## Using SpamWall without SpamBlocker

The raw lists in `raw/` (CSV, JSON) are app-agnostic: the same rows as the SpamBlocker files, with columns `type,id,kind,value,description,source,priority,group`. `type` is allow, block or optional; `group` is the block group (`telemarketing`, `call-centres`, `spam-mobiles`, `banks-govt`; empty for allow rows and numbers); `kind` is `pattern` (a regular expression) or `number` (an exact number). Numbers and patterns match the national number, without +91 or a leading 0.

- **Any blocker or your phone's own block list:** open the CSV file and copy what you need. Add `number` rows one by one, or paste them in bulk where the app allows.
- **Patterns need regex or prefix blocking.** If your app only blocks exact numbers, use the `number` rows. If it supports prefixes, turn simple patterns such as `^140\d{7}$` into the prefix `140`.
- **Build rules for another app with AI or a script:** feed `spamwall-in.json` (rules plus a `meta` object) to an AI assistant or a script and ask it to produce the format your app imports.
- **Mobile numbers are left out on purpose.** Individual 10-digit mobile numbers (starting 6 to 9) are never listed, for privacy. Only landline, toll-free and series numbers appear as `number` rows.


## Step-by-step import

1. In SpamBlocker, open **Settings > Backup > Export** and save a backup of your current setup first.
2. Download the file you picked to your phone.
3. Open **Settings > Backup > Import** and pick the file.
4. In the **Include Settings** dialog, tap a category to move it between Include and Exclude. Keep only the category the file has (Others for `spamblocker-settings.gz`, Regex Settings for `spamblocker-all-rules.gz` and the four group files (`spamblocker-telemarketing.gz`, `spamblocker-call-centres.gz`, `spamblocker-spam-mobiles.gz`, `spamblocker-banks-govt.gz`), both for `spamblocker-full-setup.gz`).
5. Confirm the import.

## Nuances

- Import REPLACES the whole section. Number rules are cleared and re-added, so importing a `spamblocker-all-rules.gz` or the four group files (`spamblocker-telemarketing.gz`, `spamblocker-call-centres.gz`, `spamblocker-spam-mobiles.gz`, `spamblocker-banks-govt.gz`) file (or `spamblocker-full-setup.gz`) deletes your own number rules. Export first, or add your own rules again afterwards.
- A file that lacks a category shows "This setting is missing from the backup file and cannot be restored" for that category. Exclude it, as in step 4.
- Allow and block rules must never share a priority. Here allow is 15, the built-in allow checks are 10 and block is 5.
- Numbers are matched without +91 or a leading 0.
- Recent Apps ignores apps that are not installed.
- If you install a new shopping app, add it in Recent Apps by hand.

## Manual steps the import cannot do

- Grant SpamBlocker's permissions when it asks: the call screening role, contacts, and usage access for Recent Apps.
- Turn on SMS screening under **Settings > Screening** if you want it, and follow the app's prompts.
- Add your own bank and broker numbers to contacts (if you add the bank group).
- Optionally turn off Tellows, which sends unknown numbers to tellows.com.
- On Xiaomi/MIUI, allow autostart and set no battery restriction for SpamBlocker so screening keeps running.

## Using single patterns in another app

Each pattern is one file: `rules/in/<type>/<ID>.txt`, where type is `allow`, `block` or `optional`. Copy the regex from the line (the part before `#`) into any blocker that accepts regular expressions. [`rules/in/patterns.md`](../rules/in/patterns.md) lists every pattern.

## Undo

Import the backup you exported in step 1.
