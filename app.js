'use strict';
const $=s=>document.querySelector(s);
const fmt=n=>n==null?'—':n.toFixed(1);
const signed=n=>n==null?'—':(n>0?'+':'')+n.toFixed(1).replace('-', '−');
const sel=$('#season-select');
for(const s of SEASONS){
 const opt=new Option(s.year+(s.year===2026?' *':''),s.year);sel.add(opt);
 const row=document.createElement('tr');row.className=s.year===2026?'partial':s.year>=2022?'recent':'';
 row.innerHTML=s.games?`<th scope="row"><button data-year="${s.year}" aria-label="View ${s.year} games">${s.year}${s.year===2026?'*':''}</button></th><td>${s.wins}–${s.losses}</td><td>${(s.wins/s.games*100).toFixed(1)}%</td><td>${s.pf}</td><td>${s.pa}</td><td>${fmt(s.ppg)}</td><td>${fmt(s.papg)}</td><td class="bad">${signed(s.margin)}</td><td>${s.shutouts}</td>`:`<th scope="row">2020</th><td colspan="8" style="text-align:left;color:var(--muted)">Season canceled — COVID-19</td>`;
 $('#season-rows').append(row);
}
function showSeason(year){
 const s=SEASONS.find(s=>s.year===Number(year));sel.value=year;
 $('#game-title').textContent=`${year} game results`;
 $('#season-summary').textContent=s.games?`${s.wins}–${s.losses} · ${s.pf} points for, ${s.pa} against · ${s.coach}${s.year===2026?' · Six-game snapshot; season in progress':''}`:'No games played. The 2020 season was canceled.';
 $('#selected-source').href=s.source;
 $('#game-rows').innerHTML=GAMES.filter(g=>g.year===s.year).map(g=>`<tr><td>${g.date.replace(/ \(.*/, '')}</td><th scope="row">${g.opponent}</th><td>${g.venue}</td><td>${g.outcome} ${g.pf}–${g.pa}</td><td>${g.pf-g.pa>0?'+':''}${g.pf-g.pa}</td><td><a href="${g.links['Box Score']||g.source}">${g.links['Box Score']?'Box score':'Schedule'} ↗</a></td></tr>`).join('')||'<tr><td colspan="6">No completed games.</td></tr>';
}
sel.addEventListener('change',()=>showSeason(sel.value));
$('#season-rows').addEventListener('click',e=>{const b=e.target.closest('button[data-year]');if(b){showSeason(b.dataset.year);$('.gameexplorer').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});sel.focus({preventScroll:true})}});
showSeason(2026);
const abbr=['MLC','MON','COR','ILL','CHI','BEL','LFC','GRI','RIP'];
$('#games-2025').innerHTML=GAMES.filter(g=>g.year===2025).map((g,i)=>`<div class="scorebox ${g.pf===0?'zero':''}" title="${g.opponent}: Lawrence ${g.pf}, opponent ${g.pa}"><span class="team">${abbr[i]}</span><b>${g.pf}</b><span>to ${g.pa}</span></div>`).join('');
$('#source-inventory').innerHTML=SEASONS.map(s=>`<div><strong>${s.year}</strong><br><a href="${s.source}">Schedule</a>${s.games?` · <a href="${s.stats}">Statistics</a>`:''}</div>`).join('');
// Scoring chart: all values are generated from the same audited season dataset.
const width=1100,height=340,left=42,right=26,chartTop=28,bottom=42;
const x=i=>left+i*(width-left-right)/15,y=v=>height-bottom-v*(height-chartTop-bottom)/60;
let svg=`<svg viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg"><title>Points scored and allowed per game, 2011–2026</title><desc>Lawrence scored between 3.8 and 27.5 points per game. Opponents scored between 27.1 and 52.6. The season table gives precise values.</desc>`;
for(let v=0;v<=60;v+=10)svg+=`<line x1="${left}" x2="${width-right}" y1="${y(v)}" y2="${y(v)}" stroke="#dfe2df"/><text x="${left-12}" y="${y(v)+4}" text-anchor="end">${v}</text>`;
svg+=`<rect x="${x(10)+25}" y="${chartTop}" width="${x(14)-x(10)}" height="${height-chartTop-bottom}" fill="#aa372c" opacity=".035"/>`;
for(const [key,color] of [['papg','#aa372c'],['ppg','#08658e']]){
 let path='';let gap=true;
 SEASONS.forEach((s,i)=>{if(!s.games){gap=true;return}path+=`${gap?'M':'L'}${x(i)},${y(s[key])} `;gap=false});
 svg+=`<path d="${path}" fill="none" stroke="${color}" stroke-width="3"/>`;
 SEASONS.forEach((s,i)=>{if(!s.games)return;svg+=`<circle cx="${x(i)}" cy="${y(s[key])}" r="4" fill="${color}"><title>${s.year}: ${s[key].toFixed(1)} ${key==='ppg'?'scored':'allowed'} per game</title></circle>`;if(i>=10||i===5)svg+=`<text class="value" x="${x(i)}" y="${y(s[key])+(key==='papg'?-12:22)}" text-anchor="middle">${s[key].toFixed(1)}</text>`;});
}
SEASONS.forEach((s,i)=>{svg+=`<text x="${x(i)}" y="${height-15}" text-anchor="middle">${String(s.year).slice(2)}${s.year===2026?'*':''}</text>`});
svg+=`<text x="${x(9)}" y="${y(25)}" text-anchor="middle" transform="rotate(-90 ${x(9)} ${y(25)})">2020 canceled</text></svg>`;
$('#trend-chart').innerHTML=svg;

let bars='<svg viewBox="0 0 1100 260" xmlns="http://www.w3.org/2000/svg"><title>Wins and losses by season</title>';
const baseY=225, unit=17;
SEASONS.forEach((s,i)=>{const cx=x(i),bw=38;if(s.games){bars+=`<rect x="${cx-bw/2}" y="${baseY-s.games*unit}" width="${bw}" height="${s.losses*unit}" fill="#dbada6"/><rect x="${cx-bw/2}" y="${baseY-s.wins*unit}" width="${bw}" height="${s.wins*unit}" fill="#08658e"/><text class="value" x="${cx}" y="${baseY-s.games*unit-12}" text-anchor="middle">${s.wins}–${s.losses}</text>`}else bars+=`<text x="${cx}" y="155" text-anchor="middle" transform="rotate(-90 ${cx} 155)">Canceled</text>`;bars+=`<text x="${cx}" y="250" text-anchor="middle">${String(s.year).slice(2)}${s.year===2026?'*':''}</text>`});
$('#record-chart').innerHTML=bars+'</svg>';

$('#victory-graph').innerHTML=SEASONS.map(s=>`<div class="victoryyear"><div class="victorycolumn">${s.games?`<strong>${s.wins}</strong><div class="victorybar" style="height:${s.wins*30}px" aria-hidden="true"></div>`:'<span class="no-season">No<br>season</span>'}</div><span class="victorylabel">${s.year}${s.year===2026?'*':''}</span></div>`).join('');
