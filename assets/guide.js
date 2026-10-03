/* Shared behaviour for every guide page; each widget is wired by markup alone.
   - Scene tabs: .scene-tabs > .scene-tab[data-scene] shows the matching [data-scene-panel] in the same <section>.
   - Reference filters: .ref-filters > .ref-filter[data-ref-filter] ("all" or a location) shows the
     .album-card[data-locations] in the same <section>; "{n}" in .filter-status[data-template] becomes the count.
   - Lightbox: the #lb dialog opens from .shot / .reference-photo (caption in data-cap) and .concept img[data-cap]. */
(()=>{
function press(buttons,button){buttons.forEach(tab=>{const selected=tab===button;tab.classList.toggle('active',selected);tab.setAttribute('aria-pressed',String(selected));});}
document.querySelectorAll('.scene-tabs').forEach(group=>{
  const scope=group.closest('section')||document,tabs=group.querySelectorAll('.scene-tab');
  tabs.forEach(button=>button.addEventListener('click',()=>{
    press(tabs,button);
    scope.querySelectorAll('[data-scene-panel]').forEach(panel=>panel.hidden=panel.dataset.scenePanel!==button.dataset.scene);
  }));
});
document.querySelectorAll('.ref-filters').forEach(group=>{
  const scope=group.closest('section')||document,filters=group.querySelectorAll('.ref-filter'),status=scope.querySelector('.filter-status[data-template]');
  filters.forEach(button=>button.addEventListener('click',()=>{
    press(filters,button);
    let count=0;
    scope.querySelectorAll('.album-card').forEach(card=>{const show=button.dataset.refFilter==='all'||card.dataset.locations.split(' ').includes(button.dataset.refFilter);card.hidden=!show;if(show)count++;});
    if(status)status.textContent=status.dataset.template.replace('{n}',count);
  }));
});
const lb=document.getElementById('lb');
if(!lb)return;
const img=document.getElementById('lb-img'),cap=document.getElementById('lb-cap');
let returnFocus=null;
function openLb(src,c,alt){returnFocus=document.activeElement;img.src=src;img.alt=alt||c;cap.textContent=c;lb.classList.add('open');lb.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';lb.querySelector('.lb-x').focus();}
function closeLb(){lb.classList.remove('open');lb.setAttribute('aria-hidden','true');document.body.style.overflow='';if(returnFocus&&returnFocus.isConnected)returnFocus.focus();}
document.querySelectorAll('.shot,.reference-photo').forEach(s=>{
  const picture=s.querySelector('img');
  if(s.classList.contains('shot')){s.setAttribute('role','button');s.tabIndex=0;s.setAttribute('aria-label','放大：'+picture.alt);s.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openLb(picture.src,s.dataset.cap,picture.alt);}});}
  s.addEventListener('click',()=>openLb(picture.src,s.dataset.cap,picture.alt));
});
document.querySelectorAll('.concept img').forEach(el=>{el.setAttribute('role','button');el.tabIndex=0;el.setAttribute('aria-label','放大：'+el.alt);el.addEventListener('click',()=>openLb(el.src,el.dataset.cap||'',el.alt));el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openLb(el.src,el.dataset.cap||'',el.alt);}});});
lb.querySelector('.lb-x').addEventListener('click',closeLb);
lb.addEventListener('click',e=>{if(e.target===lb)closeLb();});
document.addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')closeLb();if(e.key==='Tab'){e.preventDefault();lb.querySelector('.lb-x').focus();}});
})();
