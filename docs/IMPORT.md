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

| File | What it has | Pick it when |
|---|---|---|
| `complete.gz` | Settings plus default rules (both categories) | You want a full setup in one tap |
| `settings.gz` | Only the "Others" category: contacts, STIR, repeated call, dialed, answered, Recent Apps (120 min) | You want the settings without touching your number rules |
| `rules-default.gz` | Only the "Regex Settings" category: all allow rules and the default block rules | You want the rules without touching your settings |
| `types/<ID>.gz` | One block pattern (IN-140, IN-CC-LANDLINE, IN-CC-BLR, IN-BULK-MOBILE or IN-1600) plus the allow rules (IN-1601, IN-AMAZON). Regex Settings only | You want to block only that kind of call |
| `rules-strict.gz` | Same as `rules-default.gz` plus IN-1600 | You also want bank, insurer and government service calls blocked (add your own bank and broker numbers to contacts first) |

Each file also has a readable `.json` twin in `spamblocker/`.

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
