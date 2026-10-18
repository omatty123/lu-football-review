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
