# spamwall

![spamwall: spam call and SMS block patterns for India](assets/banner.svg)

**For Indian phone numbers (+91), calls and SMS.** spamwall is a set of pattern-based block rules you can import in one click. It is built for [SpamBlocker](https://github.com/aj3423/SpamBlocker) on Android; the plain regex lists work in any blocker that accepts regular expressions.

It blocks whole number ranges used by telemarketers and call centres instead of single numbers. Every rule filters both calls and SMS. Calls and messages from shopping, delivery, ride and payment apps, from your contacts, and from official service lines are never blocked.

> SMS filtering works only when **SMS** is switched on under *Settings > Screening* in SpamBlocker; follow the setup prompt it shows.
## Quick start (SpamBlocker)

1. In SpamBlocker, export a backup first: **Settings > Backup > Export**. An import replaces your number rules.
2. Download [`spamblocker/spamwall-in.gz`](spamblocker/spamwall-in.gz) to your phone.
3. **Settings > Backup > Import**, pick the file, keep only **Others** and **Regex Settings** under *Include Settings*, then tap **Import**.
4. **Settings > Recent Apps**: switch on the apps you use from [`rules/in/allow-apps.txt`](rules/in/allow-apps.txt) and set the time to 120 minutes, so delivery riders and drivers on masked numbers get through.
5. Check that **Contacts**, **Repeated Call**, **Dialed Number** and **Answered Number** are on.

Want bank and insurance service calls blocked too? Use `spamwall-in-strict.gz` instead, and add your own banks' 1600 numbers to your contacts first.

## How the rules are checked

SpamBlocker checks higher priorities first. Allow and block rules never share a priority.

| Priority | Type | Rules |
|---|---|---|
| 15 | Allow | `allow.txt` (official delivery series, known support numbers) |
| 10 | Allow | Contacts, repeated calls, numbers you dialled or answered, Recent Apps (built into SpamBlocker) |
| 5 | Block | `block.txt` |

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

### Optional (strict file only)

| ID | Pattern | What it blocks | Why it is off by default |
|---|---|---|---|
| IN-1600 | `^1600\d{6}$` | Service and transactional calls from banks, insurers, brokers, mutual funds and government | This is the **official** series that regulated entities must use ([TRAI, PIB](https://pib.gov.in/PressReleasePage.aspx?PRID=2191647)). Blocking it also blocks your real bank. |

**Credit card and loan spam:** promotions must come from the 140 series, which is blocked. Official bank calls must come from 1600, which stays allowed in the default file. A loan or credit-card pitch from an ordinary mobile or landline breaks TRAI rules; report it in the **Report Spam** app (TRAI DND) and open a *New spam pattern* issue here.

## Blocked by mistake?

Open an [**Unblock request**](../../issues/new?template=unblock-request.yml). Give the number (or its first digits), the company and why it is legitimate. If a rule blocks a real business, we narrow it or remove it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Edit the `.txt` files in `rules/<country>/`, then run `python -I tools/build_spamblocker.py` to rebuild the import files.

## License

MIT. This project is not affiliated with SpamBlocker, TRAI or any telecom operator.
