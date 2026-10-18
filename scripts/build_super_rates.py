"""Aggregate verified SUPER LOSSES over all completed games, 2011–2025."""
import pathlib,json,csv
root=pathlib.Path(__file__).resolve().parents[1]
A=json.loads((root/'data/mwc-2011-2025.json').read_text());D=json.loads((root/'data/mwc-super-audit-2011-2025.json').read_text());R=[]
for r in A:
 rows=[d for d in D if d['team']==r['team']]
 assert len(rows)==r['losses']
 assert all(d['pf']<d['pa'] and d['superLoss']==(d['opponentTDs']>d['firstDowns']) for d in rows)
 n=sum(d['superLoss'] for d in rows)
 R.append(dict(team=r['team'],games=r['games'],losses=r['losses'],super_losses=n,super_rate=round(n/r['games']*100,1),audited_losses=len(rows)))
(root/'data/mwc-super-rates-2011-2025.json').write_text(json.dumps(R,indent=2))
with (root/'data/mwc-super-rates-2011-2025.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=R[0].keys());w.writeheader();w.writerows(R)
print('Verified',len(D),'losses;',sum(r['super_losses'] for r in R),'SUPER LOSSES')
