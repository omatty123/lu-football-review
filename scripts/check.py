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
html=(r/'full-report.html').read_text()
assert html.index('id="victories"')<html.index('id="trend"')
print('PASS: 19-game current losing streak and prominent victory graph placement.')

sl=json.loads((r/'data/super-losses.json').read_text())
assert len(sl)==15 and len({x['source'] for x in sl})==15
assert all(x['opponent_touchdowns']>x['lu_first_downs'] and x['opponent_points']>x['lu_points'] for x in sl)
assert sum(x['year']==2025 for x in sl)==5
chicago=next(x for x in sl if x['year']==2025 and x['opponent']=='Chicago')
assert (chicago['opponent_touchdowns'],chicago['lu_first_downs'])==(9,1)
assert html.index('id="victories"')<html.index('id="super-losses"')<html.index('id="trend"')
print('PASS: 15 super losses, 2025 count, Chicago 9-to-1, and prominent placement.')

peers=json.loads((r/'data/mwc-2025.json').read_text());audit=json.loads((r/'data/mwc-2025-loss-audit.json').read_text());inventory=json.loads((r/'data/mwc-2025-games.json').read_text())
assert len(peers)==10 and len({x['team'] for x in peers})==10 and len(audit)==55
assert sum(x['superLoss'] for x in audit)==12
for peer in peers:
 games=next(x['games'] for x in inventory if x['team']==peer['team']);los=[x for x in audit if x['team']==peer['team']]
 assert len(games)==peer['games'] and len(los)==peer['losses']
 assert sum(x['pf'] for x in games)==peer['points_for'] and sum(x['pa'] for x in games)==peer['points_against']
 assert sum(x['outcome']=='W' for x in games)==peer['wins']
 assert sum(x['superLoss'] for x in los)==peer['super_losses']
 assert all(x['superLoss']==(x['opponentTDs']>x['firstDowns']) for x in los)
 assert abs(peer['margin_per_game']-(peer['points_for']-peer['points_against'])/peer['games'])<1e-9
lu=next(x for x in peers if x['team']=='Lawrence')
assert lu['super_losses']==5 and lu['wins']==0 and lu['margin_per_game']==min(x['margin_per_game'] for x in peers)
assert 'id="share-button"' in html and 'id="conference"' in html
print('PASS: all 10 MWC teams, 55 audited defeats, 12 SUPER LOSSES, and sharing control.')

assert max(x['losses'] for x in peers)==9
assert {x['team'] for x in peers if x['losses']==9}=={'Lawrence','Beloit'}
assert html.index('id="conference"')<html.index('id="super-losses"')
assert 'KEY METRICS OF LAWRENCE FOOTBALL FAILURE' in html
assert round(119/137*100,1)==86.9
print('PASS: straight-loss comparison, nine-loss tie, 100% LU loss rate, historical loss rate.')

# Full-period conference comparison: every season and game reconciles.
historical = json.loads((r / 'data/mwc-2011-2025.json').read_text())
historical_seasons = json.loads((r / 'data/mwc-2011-2025-seasons.json').read_text())
historical_games = json.loads((r / 'data/mwc-2011-2025-game-audit.json').read_text())
membership = json.loads((r / 'data/mwc-membership-2011-2025.json').read_text())
assert len(historical) == 10 and len(membership) == 13
assert len(historical_seasons) == len(historical_games) == 160
assert len({(r['team'], r['year']) for r in historical_seasons}) == 160
for row in historical_seasons:
    game_row = next(g for g in historical_games if (g['team'],g['year']) == (row['team'],row['year']))
    games_ = game_row['games']
    assert row['games'] == len(games_) == row['wins'] + row['losses']
    for key in ['pf','pa']:
        assert row[key] == sum(g[key] for g in games_)
    assert row['wins'] == sum(g['outcome'] == 'W' for g in games_)
    assert all((g['pf'] > g['pa']) == (g['outcome'] == 'W') for g in games_)
for table_, member_only in [(historical,False),(membership,True)]:
    for row in table_:
        years_ = [s for s in historical_seasons if s['team']==row['team'] and (not member_only or s['membership'])]
        for key in ['wins','losses','games','pf','pa']:
            assert row[key] == sum(s[key] for s in years_)
        assert row['loss_rate'] == round(100*row['losses']/row['games'],1)
        assert row['margin'] == round((row['pf']-row['pa'])/row['games'],1)
        if not member_only:
            assert sorted(s['year'] for s in years_) == [y for y in range(2011,2026) if y != 2020]
    assert max(table_,key=lambda r:r['losses'])['team'] == 'Beloit'
    assert max(table_,key=lambda r:r['loss_rate'])['team'] == 'Lawrence'
    assert min(table_,key=lambda r:r['margin'])['team'] == 'Lawrence'
lu_history = next(r for r in historical if r['team']=='Lawrence')
assert (lu_history['losses'],lu_history['games'],lu_history['pf'],lu_history['pa']) == (119,137,2151,5386)
assert html.index('id="conference-history"') < html.index('id="conference"')
assert 'Beloit has more total losses: 120 to Lawrence’s 119' in html
print('PASS: 160 team-seasons reconciled to game scores; all current and former members; historical rankings and placement.')

from collections import Counter
super_audit=json.loads((r/'data/mwc-super-audit-2011-2025.json').read_text())
super_rates=json.loads((r/'data/mwc-super-rates-2011-2025.json').read_text())
assert len(super_audit)==761 and sum(x['superLoss'] for x in super_audit)==54
assert len(super_rates)==10
for row in super_rates:
    observed=[x for x in super_audit if x['team']==row['team']]
    reference=[g for s in historical_games if s['team']==row['team'] for g in s['games'] if g['outcome']=='L']
    assert len(observed)==row['audited_losses']==row['losses']==len(reference)
    assert Counter((x['pf'],x['pa']) for x in observed)==Counter((x['pf'],x['pa']) for x in reference)
    assert row['super_losses']==sum(x['superLoss'] for x in observed)
    assert row['super_rate']==round(row['super_losses']/row['games']*100,1)
    assert row['games']==next(x['games'] for x in historical if x['team']==row['team'])
    for x in observed:
        assert x['superLoss']==(x['opponentTDs']>x['firstDowns'])
        assert x['pf']<x['pa'] and x['opponentTDs']*6<=x['pa'] and x['firstDowns']>=0
        assert x['source'].startswith('https://')
assert next(x for x in super_rates if x['team']=='Lawrence')['super_losses']==15
assert next(x for x in super_rates if x['team']=='Lawrence')['super_rate']==10.9
assert max(super_rates,key=lambda x:x['super_rate'])['team']=='Beloit'
home=(r/'index.html').read_text()
assert home.count('class="chart-row lawrence"')==3
assert all(f'id="{x}"' in home for x in ['loss-rate','super-loss-rate','scoring-margin','victories','share-button'])
assert home.index('id="loss-rate"')<home.index('id="victories"')
assert 'Second-highest · 15 of 137 games' in home
assert 'Audit pending' not in home and 'full-report.html' in home
print('PASS: 761 defeats, 54 SUPER LOSSES; all rates use completed games; three homepage graphs highlight Lawrence.')
