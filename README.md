# SpamWall

![SpamWall: spam call and SMS block patterns for India](assets/banner.svg)

**For Indian phone numbers (+91), calls and SMS.** SpamWall is an open list of spam number patterns and numbers. Use the raw CSV or JSON lists in any blocker app, or import the ready-made files into SpamBlocker, the Android app we currently use.

It blocks whole number ranges used by telemarketers and call centres instead of single numbers. Every rule filters both calls and SMS. Calls and messages from shopping, delivery, ride and payment apps, from your contacts, and from official service lines are never blocked.

> SMS filtering works only when **SMS** is switched on under *Settings > Screening* in SpamBlocker; follow the setup prompt it shows.
## The app we currently use

We use **[SpamBlocker](https://github.com/aj3423/SpamBlocker)** (free, open source, Android), so the one-click import files are in its format. Any other blocker works with the raw lists.

- Get SpamBlocker from [F-Droid](https://f-droid.org/packages/spam.blocker/) or its [GitHub releases](https://github.com/aj3423/SpamBlocker/releases).
- App questions go to the [SpamBlocker repository](https://github.com/aj3423/SpamBlocker/issues); questions about these lists go [here](../../issues).

SpamWall is an independent project, not made by or affiliated with SpamBlocker.

## Quick start (if you use SpamBlocker)

1. Export a backup first (**Settings > Backup > Export**), because an import replaces your number rules.
2. Download [`spamblocker/spamwall-full-setup.gz`](spamblocker/spamwall-full-setup.gz), then **Settings > Backup > Import** and pick it.
3. Follow the full guide, including the manual steps the import cannot do: [docs/IMPORT.md](docs/IMPORT.md).

## Files

| Label | File | Description | Download |
|---|---|---|---|
| Full setup (recommended) | `spamblocker/spamwall-full-setup.gz` | App settings plus all spam rules in one import | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-full-setup.gz) |
| App settings only | `spamblocker/spamwall-settings.gz` | Only the Others category: contacts, STIR, repeated call, dialed, answered, Recent Apps | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-settings.gz) |
| All spam rules | `spamblocker/spamwall-all-rules.gz` | Allow rules plus the three default groups (not the bank group) | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-all-rules.gz) |
| Promo and telemarketing calls | `spamblocker/spamwall-telemarketing.gz` | Group `telemarketing`: the 140 promotional series, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-telemarketing.gz) |
| Call-centre ranges | `spamblocker/spamwall-call-centres.gz` | Group `call-centres`: call-centre landline and Bengaluru ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-call-centres.gz) |
| Spam mobile ranges | `spamblocker/spamwall-spam-mobiles.gz` | Group `spam-mobiles`: bulk telemarketing mobile ranges, plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-spam-mobiles.gz) |
| Bank and government calls (optional) | `spamblocker/spamwall-banks-govt.gz` | Group `banks-govt`: the official 1600 series (also blocks your real bank), plus the allow rules | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-banks-govt.gz) |
| Raw list (CSV) | `raw/spamwall-in.csv` | Every pattern and business number with its group, for any app or spreadsheet | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.csv) |
| Raw list (JSON) | `raw/spamwall-in.json` | Same data with a meta object, for scripts and AI | [Download](https://github.com/wasimness/spamwall/releases/latest/download/spamwall-in.json) |

Release downloads use the file name only; the folder shows where it lives in the repo.

Groups don't stack in SpamBlocker (each rules import replaces the number rules), so to block two groups, import `spamwall-all-rules.gz`, or import one group and add the other patterns by hand from `rules/in/`. For all rules plus banks, import `spamwall-all-rules.gz`, then add the IN-1600 pattern by hand.

Each `.gz` has a readable `.json` twin in `spamblocker/`. The raw list also exists as a Markdown table, [`raw/spamwall-in.md`](raw/spamwall-in.md), for reading in the repo (not a release download). Source rules: [`rules/in/`](rules/in/) (one file per pattern in `allow/`, `block/` and `optional/`, each block pattern with a `# Group:` line, plus [`allow-apps.txt`](rules/in/allow-apps.txt) and `numbers/`), table of every pattern: [`rules/in/patterns.md`](rules/in/patterns.md).

**What can be combined:** `spamwall-settings.gz` + any ONE rules file is fine. `spamwall-full-setup.gz` already has settings and all default rules.

**Short version of the caveats:** settings never touch number rules; rules never touch settings. Importing `spamwall-settings.gz` replaces your Recent Apps list and allow switches. Export a backup first, it is your undo. Not tested on every phone and SpamBlocker version, so report problems as issues. Details: [docs/IMPORT.md](docs/IMPORT.md).

**Releases:** download the files from the [latest release](../../releases/latest).

## Using SpamWall without SpamBlocker

The raw lists in `raw/` (CSV, JSON) are app-agnostic: the same rows as the SpamBlocker files, with columns `type,id,kind,value,description,source,priority,group`. `type` is allow, block or optional; `group` is the block group (`telemarketing`, `call-centres`, `spam-mobiles`, `banks-govt`; empty for allow rows and numbers); `kind` is `pattern` (a regular expression) or `number` (an exact number). Numbers and patterns match the national number, without +91 or a leading 0.

- **Any blocker or your phone's own block list:** open the CSV file and copy what you need. Add `number` rows one by one, or paste them in bulk where the app allows.
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

### Optional (group `banks-govt` only)

| ID | Pattern | What it blocks | Why it is off by default |
|---|---|---|---|
| IN-1600 | `^1600\d{6}$` | Service and transactional calls from banks, insurers, brokers, mutual funds and government | This is the **official** series that regulated entities must use ([TRAI, PIB](https://pib.gov.in/PressReleasePage.aspx?PRID=2191647)). Blocking it also blocks your real bank. |

**Credit card and loan spam:** promotions must come from the 140 series, which is blocked. Official bank calls must come from 1600, which is not blocked by `spamwall-full-setup.gz` or `spamwall-all-rules.gz`. A loan or credit-card pitch from an ordinary mobile or landline breaks TRAI rules; report it in the **Report Spam** app (TRAI DND) and open a *New spam pattern* issue here.

## Blocked by mistake?

Open an [**Unblock request**](../../issues/new?template=unblock-request.yml). Give the number (or its first digits), the company and why it is legitimate. If a rule blocks a real business, we narrow it or remove it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Edit the files in `rules/<country>/allow/`, `block/` and `optional/` (a new block pattern must name its group), then run `python -I tools/build_spamblocker.py` to rebuild the import files.

## License

MIT. This project is not affiliated with SpamBlocker, TRAI or any telecom operator.
