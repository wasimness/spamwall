# SpamWall

![SpamWall: spam call and SMS block patterns for India](assets/banner.svg)

**For Indian phone numbers (+91), calls and SMS.** SpamWall is an open list of spam number patterns and numbers. Use the raw CSV, JSON or Markdown lists in any blocker app, or import the ready-made files into SpamBlocker, the Android app we currently use.

It blocks whole number ranges used by telemarketers and call centres instead of single numbers. Every rule filters both calls and SMS. Calls and messages from shopping, delivery, ride and payment apps, from your contacts, and from official service lines are never blocked.

> SMS filtering works only when **SMS** is switched on under *Settings > Screening* in SpamBlocker; follow the setup prompt it shows.
## The app we currently use

We use **[SpamBlocker](https://github.com/aj3423/SpamBlocker)** (free, open source, Android), so the one-click import files are in its format. Any other blocker works with the raw lists.

- Get SpamBlocker from [F-Droid](https://f-droid.org/packages/spam.blocker/) or its [GitHub releases](https://github.com/aj3423/SpamBlocker/releases).
- App questions go to the [SpamBlocker repository](https://github.com/aj3423/SpamBlocker/issues); questions about these lists go [here](../../issues).

SpamWall is an independent project, not made by or affiliated with SpamBlocker.

## Quick start (if you use SpamBlocker)

1. Export a backup first (**Settings > Backup > Export**), because an import replaces your number rules.
2. Download [`spamblocker/complete.gz`](spamblocker/complete.gz), then **Settings > Backup > Import** and pick it.
3. Follow the full guide, including the manual steps the import cannot do: [docs/IMPORT.md](docs/IMPORT.md).

## Files

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

Each `.gz` has a readable `.json` twin in `spamblocker/`. Source rules: [`rules/in/`](rules/in/) (one file per pattern in `allow/`, `block/` and `optional/`, plus [`allow-apps.txt`](rules/in/allow-apps.txt) and `numbers/`), table of every pattern: [`rules/in/patterns.md`](rules/in/patterns.md).

**What can be combined:** `settings` + any ONE rules file (`rules-default`, `rules-strict` or one `types/` file) is fine. Two rules files do not stack: the second replaces the first, and also deletes your own number rules. `complete` already has settings and default rules.

**Short version of the caveats:** settings never touch number rules; rules never touch settings. Importing `settings.gz` replaces your Recent Apps list and allow switches. Export a backup first, it is your undo. Not tested on every phone and SpamBlocker version, so report problems as issues. Details: [docs/IMPORT.md](docs/IMPORT.md).

**Releases:** download the files from the [latest release](../../releases/latest).

## Using SpamWall without SpamBlocker

The raw lists in `raw/` (CSV, JSON, Markdown) are app-agnostic: the same rows as the SpamBlocker files, with columns `type,id,kind,value,description,source,priority`. `type` is allow, block or optional; `kind` is `pattern` (a regular expression) or `number` (an exact number). Numbers and patterns match the national number, without +91 or a leading 0.

- **Any blocker or your phone's own block list:** open the CSV or Markdown file and copy what you need. Add `number` rows one by one, or paste them in bulk where the app allows.
- **Patterns need regex or prefix blocking.** If your app only blocks exact numbers, use the `number` rows. If it supports prefixes, turn simple patterns such as `^140\d{7}$` into the prefix `140`.
- **Build rules for another app with AI or a script:** feed `spamwall-in.json` (rules plus a `meta` object) to an AI assistant or a script and ask it to produce the format your app imports.
- **Mobile numbers are left out on purpose.** Individual 10-digit mobile numbers (starting 6 to 9) are never listed, for privacy. Only landline, toll-free and series numbers appear as `number` rows.

## How the rules are checked

SpamBlocker checks higher priorities first. Allow and block rules never share a priority.

| Priority | Type | Rules |
|---|---|---|
| 15 | Allow | `rules/in/allow/` (official delivery series, known support numbers) |
| 10 | Allow | Contacts, repeated calls, numbers you dialled or answered, Recent Apps (built into SpamBlocker) |
| 5 | Block | `rules/in/block/` |

## India rules

Numbers are matched without `+91` or a leading `0`.

### Allowed

| ID | Pattern | What it is | Source |
|---|---|---|---|
| IN-1601 | `^1601\d{6}$` | Official series for service and transactional calls from utilities, courier and logistics companies (your deliveries) | [TRAI Direction, 10 Aug 2026](https://trai.gov.in/sites/default/files/2026-08/Direction_10082026.pdf) |
| IN-AMAZON | `^2263257863$` | Amazon India customer service | Public number |

### Blocked by default

| ID | Pattern | What it blocks | Source |
|---|---|---|---|
| IN-140 | `^140\d{7}$` | Promotional and telemarketing calls. This series is for promotions only, so no real service call uses it | [TRAI TCCCPR 2018](https://trai.gov.in/release-publication/directions), [RBI circular, Jan 2025](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12770) |
| IN-CC-LANDLINE | `^(1725\|2250\|2269\|3366\|3368\|3371\|4071\|7935\|7969\|7971)\d{6}$` | Call-centre landline ranges in Chandigarh (0172-5), Mumbai (022-50, 022-69), Kolkata (033-66, 033-68, 033-71), Hyderabad (040-71) and Ahmedabad (079-35, 079-69, 079-71) | Clustered from community spam reports |
| IN-CC-BLR | `^(803710\|...)\d{4}$` | Narrow Bengaluru call-centre blocks. Bengaluru `080` numbers are not blocked as a whole, because delivery apps call from them | Clustered from community spam reports |
| IN-BULK-MOBILE | `^(657350\|...)\d{4}$` | Mobile number blocks used for bulk telemarketing | Clustered from community spam reports |

### Optional (`rules-strict` only)

| ID | Pattern | What it blocks | Why it is off by default |
|---|---|---|---|
| IN-1600 | `^1600\d{6}$` | Service and transactional calls from banks, insurers, brokers, mutual funds and government | This is the **official** series that regulated entities must use ([TRAI, PIB](https://pib.gov.in/PressReleasePage.aspx?PRID=2191647)). Blocking it also blocks your real bank. |

**Credit card and loan spam:** promotions must come from the 140 series, which is blocked. Official bank calls must come from 1600, which stays allowed in the default file. A loan or credit-card pitch from an ordinary mobile or landline breaks TRAI rules; report it in the **Report Spam** app (TRAI DND) and open a *New spam pattern* issue here.

## Blocked by mistake?

Open an [**Unblock request**](../../issues/new?template=unblock-request.yml). Give the number (or its first digits), the company and why it is legitimate. If a rule blocks a real business, we narrow it or remove it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Edit the files in `rules/<country>/allow/`, `block/` and `optional/`, then run `python -I tools/build_spamblocker.py` to rebuild the import files.

## License

MIT. This project is not affiliated with SpamBlocker, TRAI or any telecom operator.
