# Lawrence football review

Independent analysis of publicly available Lawrence University Athletics results. Detailed coverage: all 2011–2026 season schedule pages, 143 completed games through October 17, 2026. Published October 18, 2026.

## Run locally

`python3 -m http.server 8873`

## Verify

`python3 scripts/check.py`

`node --check app.js`

GitHub Actions validates the dataset and JavaScript, then deploys the static assets to GitHub Pages on each push to main. No build dependencies or external runtime services are required. Fonts are self-hosted under their included open licenses.

## Data method

Season points and records are calculated from official schedule game results. The JSON and CSV files include source URLs. Cumulative statistics were independently checked for all 15 played seasons. 2011 and 2014 cumulative pages do not include all the points shown in their complete schedules; the report discloses the exact differences. A canceled game is not a defeat. 2026 is incomplete. This is a dated snapshot, not a live feed.

The page includes primary-source links for historical milestones, coaching succession and investment. It makes no unsupported claim about causality or comparative funding adequacy. No private institutional records or student-level information are included.

## Full-period Midwest Conference comparison
`data/mwc-2011-2025.json` contains full-period totals for the ten 2025 members. Chicago's pre-2017 and Cornell's 2011 seasons are included to keep the calendar window consistent. `data/mwc-membership-2011-2025.json` includes all 13 historical members but only their member seasons. The season-level CSV/JSON links every source; the game-audit JSON supports all 160 team-season totals. No 2020 games or canceled games are counted. Nonconference and postseason games are included. Loss rates and scoring margins use total games as the denominator. Checks reconcile every season with its scores, then recompute both sets of aggregates and rankings.

2011–2018 data come from official MWC standings/schedule archives. Later results and pre-membership seasons come from official school schedules. Grinnell's recent conference results were checked against opponent schedules and nonconference results against Grinnell's schedule archive. Its 2019 season had three played games; 2022 had eight. St. Norbert's 2019 schedule lists winning-team scores first even on losses; scores are normalized to team points for/against.
