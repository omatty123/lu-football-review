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

## Concise homepage and full research report
`index.html` is the shorter chart-led presentation. `full-report.html` preserves the entire prior report and interactive season explorer. Rebuild the homepage with `python scripts/build_story.py`. Its CSS/JS are `story.css` and `story.js`; the full report retains `style.css`, `app.js`, and `data.js`.

The full-period SUPER LOSS audit covers all 761 defeats: 451 in 2011–2018 and 310 in 2019/2021–2025. All counts and scores reconcile to the game inventory. TDs include offense, defense, and returns. Defensive PAT returns are two points, not touchdowns. Scoring-summary checks agree in 759 games. Two malformed recent summaries have explanatory row notes; both classifications are unambiguously non-SUPER losses. A missing 2017 LU–Knox legacy box was resolved using Lawrence's official boxscore. Every defeat has verified first downs and touchdowns; no unknowns are treated as zero.

`data/mwc-super-audit-2011-2025.json` is the full audit. `scripts/build_super_rates.py` generates CSV/JSON with ALL completed games as the denominator, not only losses. There are 54 SUPER LOSSES: Beloit 17, Lawrence 15, Grinnell 11, Knox 3, Ripon 3, Cornell 2, Monmouth 2, Lake Forest 1, Chicago 0, Illinois College 0. Lawrence's rate is 10.9%, second to Beloit's 12.1%.

The homepage comparison now uses the last ten COMPLETED played seasons: 2015–2019 and 2021–2025. The canceled 2020 and incomplete 2026 seasons are excluded. `scripts/build_story.py` derives `data/mwc-last-10.json` and CSV from the unchanged audited season and SUPER LOSS datasets. The full report retains its 2011–2025 scope. The current losing streak is explicitly dated separately.
