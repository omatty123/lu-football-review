import json,pathlib,csv
r=pathlib.Path(__file__).resolve().parents[1]
s=json.loads((r/'data/seasons.json').read_text());g=json.loads((r/'data/games.json').read_text())
expected={2011:(1,9),2012:(2,8),2013:(1,9),2014:(2,8),2015:(1,9),2016:(3,7),2017:(2,8),2018:(2,8),2019:(1,8),2020:(0,0),2021:(2,7),2022:(0,10),2023:(0,10),2024:(1,9),2025:(0,9),2026:(0,6)}
assert len(g)==143
for a in s:
 gs=[x for x in g if x['year']==a['year']]
 assert (a['wins'],a['losses'])==expected[a['year']]
 assert len(gs)==a['games']
 if not gs:assert a['pf'] is None;continue
 assert a['pf']==sum(x['pf'] for x in gs)
 assert a['pa']==sum(x['pa'] for x in gs)
 assert a['ppg']==round(a['pf']/a['games'],2)
 assert a['papg']==round(a['pa']/a['games'],2)
 assert a['margin']==round((a['pf']-a['pa'])/a['games'],2)
 assert a['shutouts']==sum(x['pf']==0 for x in gs)
 for x in gs:assert (x['outcome']=='W')==(x['pf']>x['pa'])
recent=[x for x in g if 2022<=x['year']<=2025]
assert len(recent)==39 and sum(x['pf'] for x in recent)==346 and sum(x['pa'] for x in recent)==1920
assert sum(0<x['pa']-x['pf']<=8 for x in recent)==2
assert sum(x['pa']-x['pf']>=30 for x in recent)==24
assert sum(x['pf']==0 for x in recent)==15
assert sum(x['pa']-x['pf']>50 for x in g if x['year']==2025)==5
assert sum(x['wins'] for x in s if x['year']<2026)==18
assert sum(x['losses'] for x in s if x['year']<2026)==119
print('PASS: 143 game results, 16 season rows, records, scoring totals, averages, and major report claims.')

streak=0
for game in reversed(g):
 if game['outcome']!='L':break
 streak+=1
assert streak==19
assert g[-streak-1]['year']==2024 and g[-streak-1]['opponent']=='Beloit College'
html=(r/'index.html').read_text()
assert html.index('id="victories"')<html.index('id="trend"')
print('PASS: 19-game current losing streak and prominent victory graph placement.')
