# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-11-27

### Changed
- Downloads reduced to 7 SpamBlocker files (`spamblocker-full-setup`, `-settings`, `-all-rules` and one per group, `spamblocker-<group>`) in 4 essential groups plus raw CSV/JSON; per-pattern import files removed. Block patterns now carry a `group` (header line and raw `group` column).

### Added
- Raw, app-agnostic lists in `raw/`: `spamwall-in.csv`, `spamwall-in.json` (with a `meta` object) and `spamwall-in.md`.
- `rules/in/numbers/IN-REPORTED-BUSINESS.txt`: business landline, toll-free and series numbers reported as spam (mobiles excluded for privacy). Used in the raw lists only, not in the SpamBlocker files.
- Checks that `raw/` is current, that no 10-digit 6-9 mobile appears in numbers or raw files, and that each number parses.
- README and `docs/IMPORT.md` file tables with labels and download links, and a "Using SpamWall without SpamBlocker" section.

## [0.2.0] - 2026-11-27

### Added
- Separate import files: `settings.gz` (Others), `rules-default.gz` and `rules-strict.gz` (Regex Settings), and `complete.gz` (both), each with a readable `.json` twin.
- Per-type import files `spamblocker/types/<ID>.gz` (one block rule plus the allow rules).
- `docs/IMPORT.md`: which file to pick, step-by-step import, nuances and manual steps.
- `rules/in/patterns.md`, a generated table of every pattern.
- Checks for file header comments, IDs matching file names and shared priorities.

### Changed
- Display name is now SpamWall in prose, banner and rule descriptions.
- Rule sources split into one file per pattern under `rules/in/allow/`, `block/` and `optional/`.
- README Quick start shortened; added a Files table and a Releases line.
- Removed `spamwall-in*.{gz,json}` (replaced by the files above).

## [0.1.0] - 2026-11-27

### Added
- First India ruleset: block 140 promotional series, call-centre landline ranges, Bengaluru call-centre blocks and bulk telemarketing mobile ranges; allow 1601 delivery/utility series; optional strict file blocks 1600.
- One-click SpamBlocker import files and plain regex lists.
- Unblock-request and new-pattern issue templates.

[Unreleased]: https://github.com/wasimness/spamwall/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/wasimness/spamwall/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/wasimness/spamwall/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/wasimness/spamwall/releases/tag/v0.1.0
