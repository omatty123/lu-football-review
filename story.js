'use strict';
const $=s=>document.querySelector(s);
// Share only on the visitor's explicit click; never share cache-busting query strings.
$('#share-button').addEventListener('click',async()=>{
 const url='https://lu-football-review.vercel.app/';
 const status=$('#share-status');status.textContent='';$('#share-fallback').hidden=true;
 if(typeof navigator.share==='function'){
  try{await navigator.share({title:'Lawrence football: ten seasons, twelve wins',url});status.textContent='Share completed.';return}catch(error){if(error.name==='AbortError')return;}
 }
 try{if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(url);status.textContent='Link copied.';}
 catch(error){$('#share-fallback').hidden=false;const input=$('#share-url');input.focus();input.select();status.textContent='Select and copy the link below.';}
});

// Preserve existing section links after shortening the homepage.
if (['#conference','#key-metrics'].includes(location.hash)) document.querySelector('#conference-history').scrollIntoView();
if (['#seasons','#trend','#history'].includes(location.hash)) location.replace('full-report.html'+location.hash);

