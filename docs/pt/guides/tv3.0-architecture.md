---
title: "Arquitetura da TV 3.0"
---

<style>
:root {
  --bg: #fcfcfd; --panel: #ffffff; --ink: #0b0c0f; --muted: #5f6672; --line: #e3e5ea; --grid: #eef0f4;
  --on: #ffffff; --pmp: #7b8495; --hub1: #ffffff; --hub2: #f1f3f7; --hatch: #c6cad4; --focus: #5b53f0;
  --screen: #1b2030; --screen2: #2a3146; --off: #0a0c11;
  --phy: #9a6400; --phy-bg: #fdf1d6; --tr: #0a6d85; --tr-bg: #dcf2f7; --sig: #8f2a86; --sig-bg: #f8e3f5;
  --app: #12714f; --app-bg: #dcf2e7; --alr: #b02f24; --alr-bg: #fbe3df;
  --radius: 10px; --radius-sm: 6px;
}
[data-md-color-scheme="slate"] {
  --bg: #08090c; --panel: #111318; --ink: #f3f4f7; --muted: #9aa2b1; --line: #22252d; --grid: #13161c;
  --on: #08090c; --pmp: #aeb6c4; --hub1: #171a21; --hub2: #0d0f14; --hatch: #353a46; --focus: #8b85ff;
  --screen: #161b27; --screen2: #242c3f; --off: #040509;
  --phy: #f5c84b; --phy-bg: #2b2208; --tr: #3fd0e8; --tr-bg: #07292f; --sig: #f07ad0; --sig-bg: #2b1026;
  --app: #4fd99a; --app-bg: #0a2a1b; --alr: #ff7e68; --alr-bg: #2f110c;
}
.md-typeset :is(.tv3-layers, .tv3-cite, .figlabel, .svgtxt, .figblock .controls button, .figblock .seg button, .figblock .sim .lbl, .figblock .sim button, #fig1 .blk .n, #fig1 .blk .k, #fig1 .panel .n, #fig5 .legend, #fig5 .bald, .tv3-keygrid span, .sigcol .sighdr, .sigchips button, #sigDetail .nm, #sigDetail .w, .mwband > .bl, .mwrow button small) {
  font-family: var(--md-code-font-family);
}
.md-typeset .c-phy { color: var(--phy); }
.md-typeset .c-tr { color: var(--tr); }
.md-typeset .c-sig { color: var(--sig); }
.md-typeset .c-app { color: var(--app); }
.md-typeset .c-alr { color: var(--alr); }
.md-typeset .tv3-hero { padding: 4px 0 24px; border-bottom: 1px solid var(--line); margin-bottom: 24px; }
.md-typeset .tv3-byline { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 14px; font-size: .72rem; line-height: 1.4; color: var(--muted); margin: 0 0 18px; padding-bottom: 12px; border-bottom: 1px solid var(--line); }
.md-typeset .tv3-byline b { color: var(--ink); font-weight: 600; }
.md-typeset .tv3-byline .sep { opacity: .45; }
.md-typeset .tv3-hero-sub { margin: 0 0 10px; font-weight: 700; font-size: clamp(22px, 3vw, 32px); line-height: 1.15; letter-spacing: -.02em; color: var(--ink); }
.md-typeset .tv3-hero .tv3-lead { font-size: 16px; line-height: 1.55; color: var(--muted); margin: 0; }
.md-typeset .tv3-layers { display: flex; flex-wrap: wrap; gap: 8px 16px; font-size: 12px; margin-top: 16px; }
.md-typeset .tv3-layers span { display: inline-flex; align-items: center; gap: 8px; }
.md-typeset .tv3-layers i { display: inline-block; width: 24px; height: 10px; border-radius: 2px; }
.md-typeset .tv3-cite { display: block; font-size: 12px; line-height: 1.5; color: var(--muted); margin-top: 10px; }
.md-typeset .grid.tv3-keygrid { grid-template-columns: repeat(auto-fit, minmax(9.5rem, 1fr)); }
.md-typeset .tv3-keygrid i { display: block; width: 26px; height: 4px; border-radius: 2px; margin-bottom: 8px; }
.md-typeset .tv3-keygrid b { display: block; font-size: 14px; }
.md-typeset .tv3-keygrid span { display: block; font-size: 11.5px; line-height: 16px; color: var(--muted); margin-top: 3px; }
.md-typeset .figblock { container-type: inline-size; padding: 8px 0 4px; margin: 18px 0 14px; color: var(--ink); }
.md-typeset .figblock .fig-head { margin-bottom: 14px; }
.md-typeset .figlabel { display: flex; align-items: center; gap: 10px; margin: 0 0 8px; font-weight: 500; font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); }
.md-typeset .figlabel span { background: var(--focus); color: #fff; padding: 3px 8px; border-radius: 5px; letter-spacing: .09em; }
.md-typeset .figblock p.figtitle { margin: 0 0 6px; font-weight: 600; font-size: 18px; line-height: 1.25; letter-spacing: -.012em; color: var(--ink); }
.md-typeset .figblock .fig-head > p.figdesc { margin: 0; color: var(--muted); font-size: 14px; line-height: 21px; }
.md-typeset .figblock figure { display: block; width: 100%; margin: 0; text-align: left; border: 1px solid var(--line); border-radius: var(--radius); padding: 16px; background: var(--panel); }
.md-typeset .figblock .scroll { overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; }
.md-typeset .figblock .scroll > svg { display: block; width: 100%; max-width: none; min-width: var(--minw, 0px); }
.md-typeset .figblock p.hint { font-size: 12px; color: var(--muted); margin: 0 0 6px; display: none; }
.md-typeset .figblock .controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.md-typeset .figblock .controls button { height: 40px; min-width: 40px; background: var(--panel); border: 1px solid var(--line); border-radius: 999px; color: var(--ink); display: inline-flex; align-items: center; justify-content: center; cursor: pointer; font-size: 12px; padding: 0 12px; transition: border-color .15s, background .15s; }
.md-typeset .figblock .controls button:hover { border-color: var(--focus); }
.md-typeset .figblock .controls button.icon { padding: 0; width: 40px; }
.md-typeset .figblock .controls button svg { width: 16px; height: 16px; max-width: none; flex: none; }
.md-typeset .figblock .controls button.primary,
.md-typeset .figblock .controls .pill[aria-current="step"] { background: var(--focus); border-color: var(--focus); color: #fff; font-weight: 500; }
.md-typeset .figblock .controls .pill { color: var(--muted); background: transparent; }
.md-typeset .figblock .controls .pill.done { color: var(--ink); }
.md-typeset .figblock .controls .sep { width: 6px; }
.md-typeset .figblock figcaption.caption { display: flex; justify-content: space-between; gap: 16px; align-items: baseline; border-top: 1px solid var(--line); padding-top: 10px; margin: 12px 0 0; max-width: none; font-style: normal; flex-wrap: wrap; }
.md-typeset .figblock figcaption.caption p { margin: 0; font-size: 14px; line-height: 20px; min-height: 40px; flex: 1 1 480px; max-width: none; color: var(--ink); }
.md-typeset .figblock .seg { display: inline-flex; border: 1px solid var(--line); border-radius: var(--radius-sm); overflow: hidden; }
.md-typeset .figblock .seg button { height: 38px; padding: 0 12px; background: transparent; border: 0; color: var(--muted); font-size: 12px; cursor: pointer; }
.md-typeset .figblock .seg button[aria-pressed="true"] { background: var(--phy-bg); color: var(--phy); font-weight: 500; }
.md-typeset .figblock .sim { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center; }
.md-typeset .figblock .sim .lbl { font-size: 12px; color: var(--muted); margin-right: 4px; }
.md-typeset .figblock .sim button { height: 36px; padding: 0 10px; background: var(--sig-bg); border: 1px solid var(--sig); border-radius: var(--radius-sm); color: var(--sig); font-size: 12px; cursor: pointer; }
#fig1 .wrap { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 24px; align-items: start; }
#fig1 .stackrow { display: grid; grid-template-columns: minmax(0, 1fr) 56px; gap: 10px; }
#fig1 .stack { display: flex; flex-direction: column; gap: 10px; }
#fig1 button.blk { all: unset; box-sizing: border-box; cursor: pointer; display: flex; flex-direction: column; gap: 4px; padding: 12px 14px; border: 1.5px solid var(--c); border-radius: var(--radius-sm); background: var(--cb); color: var(--ink); min-height: 44px; transition: transform .5s cubic-bezier(.2,.7,.2,1), opacity .5s, box-shadow .2s; }
#fig1 button.blk:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
#fig1 button.blk[aria-pressed="true"] { box-shadow: 0 0 0 2px var(--c), 0 0 18px -2px var(--c); }
#fig1 .blk .n { font-size: 12px; color: var(--c); }
#fig1 .blk .t { font-weight: 600; font-size: 14.5px; line-height: 1.2; }
#fig1 .blk .k { font-size: 11.5px; color: var(--muted); }
#fig1 .app { border: 2px solid var(--app); border-radius: var(--radius-sm); background: var(--app-bg); padding: 0 10px 10px; display: flex; flex-direction: column; }
#fig1 .app > .blk { border: 0; background: transparent; padding: 12px 4px 14px; }
#fig1 .five { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px; }
#fig1 .five .blk { background: var(--panel); min-height: 110px; }
#fig1 .bottom { display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr); gap: 10px; }
#fig1 button.blk.rx { writing-mode: vertical-rl; transform: rotate(180deg); align-items: center; justify-content: center; border-style: dashed; text-align: center; }
#fig1 button.blk.rx .t { font-size: 14px; }
#fig1 .panel { background: var(--bg); border: 1px solid var(--line); border-radius: var(--radius-sm); padding: 16px 18px; }
#fig1 .panel .n { display: block; font-size: 12px; color: var(--pc, var(--muted)); }
#fig1 .panel strong.pnt { display: block; margin: 4px 0 8px; font-weight: 600; font-size: 20px; line-height: 1.18; color: var(--ink); }
#fig1 .panel p { margin: 0; font-size: 14px; line-height: 21px; color: var(--ink); }
#fig1 .stack.pre .blk { transform: translateY(24px); opacity: 0; }
#fig5 .f5grid { display: grid; grid-template-columns: 360px minmax(0, 1fr); gap: 24px; align-items: start; }
#fig5 .left { display: flex; flex-direction: column; gap: 12px; min-width: 0; }
#fig5 .plate { width: 100%; max-width: none; display: block; }
#fig5 .legend { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 4px 12px; font-size: 12px; color: var(--muted); }
#fig5 .legend > span { display: flex; align-items: center; gap: 8px; }
#fig5 .bald { background: var(--sig-bg); border: 1.5px solid var(--sig); padding: 12px 14px 12px 28px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; line-height: 18px; clip-path: polygon(16px 0, 100% 0, 100% 100%, 16px 100%, 0 calc(100% - 16px), 0 16px); transition: opacity .4s; }
#fig5 .bald .head { display: flex; justify-content: space-between; color: var(--sig); }
.md-typeset #fig5 .bald dl { display: grid; grid-template-columns: auto minmax(0, 1fr); column-gap: 14px; margin: 0; }
.md-typeset #fig5 .bald dt { color: var(--sig); margin: 0; }
.md-typeset #fig5 .bald dd { margin: 0; color: var(--muted); overflow-wrap: anywhere; }
.md-typeset #fig5 .bald dd.v { color: var(--ink); }
#fig5 .bald .hl { background: var(--sig); color: var(--sig-bg); padding: 0 4px; }
.md-typeset .sigwrap { container-type: inline-size; display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 24px; align-items: start; margin: 14px 0; }
.md-typeset .sigcol p.sighdr { margin: 0 0 10px; font-weight: 500; font-size: 12px; letter-spacing: .1em; text-transform: uppercase; }
.md-typeset .sigchips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.md-typeset .sigchips button { height: 36px; padding: 0 11px; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius-sm); color: var(--ink); font-weight: 500; font-size: 12.5px; cursor: pointer; transition: box-shadow .15s, border-color .15s, transform .15s; }
.md-typeset .sigchips button:hover { border-color: currentColor; transform: translateY(-1px); }
.md-typeset .sigchips button[aria-pressed="true"] { box-shadow: inset 0 0 0 2px currentColor; }
.md-typeset .sigchips.lls button { color: var(--sig); }
.md-typeset .sigchips.sls button { color: var(--tr); }
.md-typeset .sigchips .id { opacity: .6; margin-left: 6px; font-weight: 400; }
.md-typeset #sigDetail { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 18px 20px; min-height: 190px; }
.md-typeset #sigDetail h4 { margin: 0 0 2px; font-weight: 600; font-size: 20px; color: var(--ink); }
.md-typeset #sigDetail .nm { font-size: 12.5px; color: var(--muted); margin: 0 0 12px; }
.md-typeset #sigDetail p.d { margin: 0; font-size: 14px; line-height: 20px; color: var(--ink); }
.md-typeset #sigDetail .w { display: block; margin-top: 12px; font-size: 12px; color: var(--muted); }
.md-typeset .mw { border: 1px solid var(--line); border-radius: var(--radius) var(--radius) 0 0; overflow: hidden; margin-top: 14px; }
.md-typeset .mwband { padding: 14px 16px; border-bottom: 1px solid var(--line); }
.md-typeset .mwband:last-child { border-bottom: 0; }
.md-typeset .mwband > span.bl { display: block; font-weight: 500; font-size: 12px; letter-spacing: .1em; margin-bottom: 10px; }
.md-typeset .mwband.aop { background: var(--app-bg); }
.md-typeset .mwband.aop > span.bl { color: var(--app); }
.md-typeset .mwband.prp { background: var(--panel); }
.md-typeset .mwband.prp > span.bl { color: var(--muted); }
.md-typeset .mwband.rf { background: var(--phy-bg); }
.md-typeset .mwband.rf > span.bl { color: var(--phy); }
.md-typeset .mwrow { display: flex; flex-wrap: wrap; gap: 8px; }
.md-typeset .mwrow button { flex: 1 1 150px; text-align: left; background: var(--bg); border: 1px solid var(--line); border-radius: var(--radius-sm); color: var(--ink); padding: 10px 12px; cursor: pointer; font-weight: 500; font-size: 13.5px; font-family: inherit; transition: box-shadow .15s, border-color .15s, transform .15s; }
.md-typeset .mwrow button small { display: block; font-size: 11.5px; color: var(--muted); margin-top: 3px; }
.md-typeset .mwrow button:hover,
.md-typeset .mwrow button[aria-pressed="true"] { box-shadow: inset 0 0 0 2px var(--app); transform: translateY(-1px); }
.md-typeset #mwDetail { background: var(--panel); border: 1px solid var(--line); border-top: 0; border-radius: 0 0 var(--radius) var(--radius); padding: 16px 18px; font-size: 14px; line-height: 20px; min-height: 74px; margin-bottom: 16px; color: var(--ink); }
@container (max-width: 900px) { #fig1 .wrap { grid-template-columns: minmax(0, 1fr); } }
@container (max-width: 860px) { #fig5 .f5grid { grid-template-columns: minmax(0, 1fr); } #fig5 .left { max-width: 440px; width: 100%; margin: 0 auto; } }
@container (max-width: 680px) { .md-typeset .figblock p.hint { display: block; } .md-typeset .sigwrap { grid-template-columns: minmax(0, 1fr); } }
@container (max-width: 580px) { #fig1 .five { grid-template-columns: repeat(2, minmax(0, 1fr)); } #fig1 .bottom { grid-template-columns: minmax(0, 1fr); } #fig1 .stackrow { grid-template-columns: minmax(0, 1fr) 48px; } }
@container (max-width: 480px) { #fig5 .legend { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) { #fig1 button.blk { transition: none; } #fig1 .stack.pre .blk { transform: none; opacity: 1; } }
</style>

<script>
var TV3 = (function(){
  var mq = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  function reduced(){ return !!(mq && mq.matches); }
  function clamp(x){ return x < 0 ? 0 : x > 1 ? 1 : x; }
  function lerp(a, b, t){ return a + (b - a) * t; }
  function ease(t){ t = clamp(t); return t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3) / 2; }
  function easeOut(t){ t = clamp(t); return 1 - Math.pow(1 - t, 3); }
  function seg(f, a, b){ return clamp((f - a) / (b - a)); }
  function pt(cx, cy, r, a){ var t = a * Math.PI / 180; return [cx + r * Math.sin(t), cy - r * Math.cos(t)]; }
  function sec(cx, cy, r1, r2, a1, a2){
    var lg = (a2 - a1) > 180 ? 1 : 0, p1 = pt(cx,cy,r2,a1), p2 = pt(cx,cy,r2,a2), p3 = pt(cx,cy,r1,a2), p4 = pt(cx,cy,r1,a1), f = function(n){ return n.toFixed(1); };
    return 'M'+f(p1[0])+' '+f(p1[1])+'A'+r2+' '+r2+' 0 '+lg+' 1 '+f(p2[0])+' '+f(p2[1])+'L'+f(p3[0])+' '+f(p3[1])+'A'+r1+' '+r1+' 0 '+lg+' 0 '+f(p4[0])+' '+f(p4[1])+'Z';
  }
  function op(el, v){ if (el) el.style.opacity = v; }
  function opAll(root, sel, v){ var n = root.querySelectorAll(sel); for (var i = 0; i < n.length; i++) n[i].style.opacity = v; }
  function attr(el, k, v){ if (el) el.setAttribute(k, v); }
  var ICON = {
    prev:'<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 3v10M13 3L6 8l7 5Z" style="fill:none;stroke:currentColor;stroke-width:1.5;stroke-linejoin:round"/></svg>',
    next:'<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12 3v10M3 3l7 5-7 5Z" style="fill:none;stroke:currentColor;stroke-width:1.5;stroke-linejoin:round"/></svg>',
    play:'M4 2.5L13 8l-9 5.5Z', pause:'M4 3h3v10H4ZM9 3h3v10H9Z'
  };
  function Fig(o){
    var root = o.root, PH = o.phases, START = [], TOTAL = 0;
    PH.forEach(function(p){ START.push(TOTAL); TOTAL += p.d; });
    var ctl = root.querySelector('[data-controls]');
    var capT = root.querySelector('[data-cap-title]'), capX = root.querySelector('[data-cap-text]');
    ctl.setAttribute('role', 'group'); ctl.setAttribute('aria-label', 'Controles da animação');
    ctl.innerHTML = '<button type="button" class="icon" data-k="prev" aria-label="Voltar uma fase">'+ICON.prev+'</button>' +
      '<button type="button" class="icon primary" data-k="play" aria-label="Reproduzir"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="'+ICON.play+'" style="fill:currentColor"/></svg></button>' +
      '<button type="button" class="icon" data-k="next" aria-label="Avançar uma fase">'+ICON.next+'</button><span class="sep"></span>' +
      PH.map(function(p, i){ return '<button type="button" class="pill" data-ph="'+i+'">'+(i+1)+' '+p.pill+'</button>'; }).join('');
    var playBtn = ctl.querySelector('[data-k=play]'), playIcon = playBtn.querySelector('path'), pills = ctl.querySelectorAll('.pill');
    var u = TOTAL, playing = false, stopAt = TOTAL, raf = 0, last = null, lastCap = -1;
    function idx(x){ for (var i = 0; i < PH.length; i++) if (x < START[i] + PH[i].d) return i; return PH.length - 1; }
    function draw(){
      var i = idx(u), f = clamp((u - START[i]) / PH[i].d);
      o.render(i, f, u);
      if (i !== lastCap){ capT.textContent = PH[i].title; capX.textContent = PH[i].text; lastCap = i; }
      for (var p = 0; p < pills.length; p++){
        if (p === i) pills[p].setAttribute('aria-current', 'step'); else pills[p].removeAttribute('aria-current');
        pills[p].classList.toggle('done', p < i);
      }
    }
    function setPlaying(v){ playing = v; playBtn.setAttribute('aria-label', v ? 'Pausar' : 'Reproduzir'); playIcon.setAttribute('d', v ? ICON.pause : ICON.play); }
    function tick(ts){
      if (!playing) return;
      var dt = last == null ? 0 : Math.min(.1, (ts - last) / 1000); last = ts; u += dt;
      if (u >= stopAt){ u = stopAt; draw(); setPlaying(false); return; }
      draw(); raf = requestAnimationFrame(tick);
    }
    function play(from, to){
      cancelAnimationFrame(raf);
      if (reduced()){ u = to; draw(); setPlaying(false); return; }
      u = from; stopAt = to; last = null; setPlaying(true); draw(); raf = requestAnimationFrame(tick);
    }
    function pause(){ cancelAnimationFrame(raf); setPlaying(false); }
    ctl.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      if (o.onUser) o.onUser();
      if (b.dataset.ph != null){ var j = +b.dataset.ph; play(START[j], START[j] + PH[j].d); return; }
      var k = b.dataset.k;
      if (k === 'play'){ if (playing) pause(); else play(u >= TOTAL - 1e-6 ? 0 : u, TOTAL); }
      else if (k === 'next'){ if (u < TOTAL - 1e-6){ var j2 = idx(u); play(u, START[j2] + PH[j2].d); } }
      else if (k === 'prev'){ var j3 = idx(u), t = (u - START[j3] > .3 || j3 === 0) ? START[j3] : START[j3 - 1]; if (u >= TOTAL - 1e-6) t = START[PH.length - 1]; pause(); u = t; draw(); }
    });
    draw();
    if (!reduced()){
      var started = false, go = function(){ if (!started){ started = true; play(0, TOTAL); } };
      if ('IntersectionObserver' in window){
        var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ go(); io.disconnect(); } }); }, {threshold: .15});
        io.observe(root);
      } else go();
    }
    if (mq && mq.addEventListener) mq.addEventListener('change', function(e){ if (e.matches){ pause(); u = TOTAL; draw(); } });
    return { redraw: draw, pause: pause };
  }
  function Loop(root, fn){
    var raf = 0, t0 = null, vis = false, paused = false, tNow = 0;
    function frame(ts){ if (t0 == null) t0 = ts - tNow * 1000; tNow = (ts - t0) / 1000; fn(tNow); raf = requestAnimationFrame(frame); }
    function start(){ if (raf || reduced() || paused || !vis) return; t0 = null; raf = requestAnimationFrame(frame); }
    function stop(){ cancelAnimationFrame(raf); raf = 0; }
    fn(0);
    if ('IntersectionObserver' in window){
      new IntersectionObserver(function(es){ es.forEach(function(e){ vis = e.isIntersecting; if (vis) start(); else stop(); }); }).observe(root);
    } else { vis = true; start(); }
    if (mq && mq.addEventListener) mq.addEventListener('change', function(e){ if (e.matches){ stop(); fn(0); } else start(); });
    return { toggle: function(){ paused = !paused; if (paused) stop(); else start(); return paused; }, redraw: function(){ fn(tNow); } };
  }
  return { Fig: Fig, Loop: Loop, clamp: clamp, lerp: lerp, ease: ease, easeOut: easeOut, seg: seg, pt: pt, sec: sec, op: op, opAll: opAll, attr: attr, reduced: reduced };
})();
</script>

# Arquitetura da TV 3.0

<section class="tv3-hero">
<p class="tv3-byline"><span>Por <b>Carlos Eduardo Coelho Batista</b> (LAViD / UFPB)</span><span class="sep">·</span><span>Baseado nas ABNT NBR 25601–25609:2025 (DTV+)</span></p>
<p class="tv3-hero-sub">A TV brasileira virou uma pilha de rede.</p>
<p class="tv3-lead">Cheat sheet da TV 3.0 para quem constrói aplicações e opera a retaguarda de transmissão. Os conceitos em ordem de leitura, com oito infográficos animados onde a sequência importa, e a referência normativa que sustenta cada afirmação.</p>
<p class="tv3-layers" aria-label="Legenda de camadas"><span><i style="background:var(--phy)"></i>Física</span><span><i style="background:var(--tr)"></i>Transporte</span><span><i style="background:var(--sig)"></i>Sinalização</span><span><i style="background:var(--app)"></i>Aplicação</span><span><i style="background:var(--alr)"></i>Alerta</span></p>
</section>

Cinco partes, em ordem de leitura:

1. **[O sistema](#sistema)** — O que mudou da TV 2.X e como as camadas se encaixam
2. **[Transmissão](#transmissao)** — Camada física, a cadeia até a antena, transporte IP e massas de teste
3. **[Sinalização](#sinalizacao)** — LLS e SLS tabela por tabela, descoberta de serviços e guia
4. **[Aplicações](#aplicacoes)** — O modelo, as duas linguagens, entrega, ciclo de vida, APIs e middleware
5. **[Serviços transversais](#servicos)** — Alerta de emergência, acessibilidade e privacidade

## Parte 1 · O sistema {#sistema}

A TV 3.0 não é uma atualização do SBTVD: é outro sistema, definido por [nove normas publicadas em 2025](../standards.md#tv-30) e conhecido comercialmente como DTV+. O que mudou de fundo é que o transporte deixou de ser um multiplex de TV e passou a ser uma rede IP, e que o componente principal de um serviço deixou de ser um fluxo de vídeo e passou a ser uma aplicação.

### 1.1 O que mudou da TV 2.X para a TV 3.0 {#mudou}

Se você conhece o SBTVD, a tabela abaixo é o atalho mais curto. Cada linha é uma substituição, não um acréscimo.

| Camada | TV 2.X · SBTVD, ISDB-Tb | TV 3.0 · DTV+ |
| :--- | :--- | :--- |
| `Camada física` | ISDB-T, segmentação em 13 segmentos | <span class="c-phy">ATSC A/322 com MIMO, LDM e TxID</span> |
| `Transporte` | MPEG-2 Transport Stream | <span class="c-tr">IP multicast, ROUTE/DASH — **MMT/MMTP excluído**</span> |
| `Sinalização` | SI, PSI, AIT | <span class="c-sig">LLS e SLS em XML, com BAMT, TBSAT, BALD e PRRD</span> |
| `Vídeo` | H.264 | VVC, com HEVC, AVC e LCEVC; HDR e até 8K |
| `Áudio` | AAC | MPEG-H Audio, com AAC, AC-4 e E-AC-3 JOC |
| `Legendas` | ARIB closed caption | IMSC1 e WebVTT |
| `Língua de sinais` | janela aberta, queimada no vídeo | **Closed signing**: vídeo de Libras, gloss e movimento, ligáveis pelo telespectador |
| `Aplicações` | Ginga-NCL e Ginga-J, opcionais ao serviço | <span class="c-app">TV 3.0 Ginga-NCL e Ginga-HTML5. **A aplicação é o serviço** — o Service Type 30 se chama *Service Based on Bootstrap Application*</span> |
| `Alerta` | EWBS, aviso simples | <span class="c-alr">AEA: mensagem rica, segmentada por área, capaz de ligar o receptor em standby</span> |
| `Dados do telespectador` | sem modelo | <span class="c-sig">PRRD: consentimento declarado por finalidade, antes de qualquer coleta</span> |
| `Banda larga` | acessório | parte do serviço: componentes podem vir pelo ar e pela internet no mesmo programa |

### 1.2 Como as camadas se encaixam {#camadas}

A figura abaixo é a mesma em todas as normas do conjunto. Note a assimetria: a codificação de aplicações não é uma camada no topo da pilha, é uma faixa que abraça vídeo, áudio, legendas, língua de sinais e alerta. Tudo o que o telespectador vê passa por ela.

<section class="figblock" id="fig1" aria-labelledby="fig1-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 1</span> idêntica nas cinco normas</p>
<p class="figtitle" id="fig1-h">Arquitetura em camadas</p>
<p class="figdesc">A pilha como a norma desenha: a codificação de aplicações abraça por cima as cinco codificações de mídia e alerta; abaixo, o transporte; na base, o ar e a banda larga. A 25609, de receptores, não está no desenho da norma — atravessa tudo. Selecione um bloco.</p>
</header>
<figure>
<section class="wrap">
<section class="stackrow">
<section class="stack pre" role="group" aria-label="Pilha de camadas da TV 3.0">
<section class="app" style="--c:var(--app);--cb:var(--app-bg)">
<button type="button" class="blk" data-k="apps" style="--c:var(--app);--cb:transparent"><span class="n">NBR 25608</span><span class="t">Codificação de aplicações</span><span class="k">AoP · Ginga-NCL · Ginga-HTML5 · BALD · PRRD</span></button>
<section class="five">
<button type="button" class="blk" data-k="video" style="--c:var(--app);--cb:var(--panel)"><span class="n">NBR 25603</span><span class="t">Vídeo</span><span class="k">VVC · HEVC · LCEVC</span></button>
<button type="button" class="blk" data-k="audio" style="--c:var(--app);--cb:var(--panel)"><span class="n">NBR 25604</span><span class="t">Áudio</span><span class="k">MPEG-H</span></button>
<button type="button" class="blk" data-k="cc" style="--c:var(--app);--cb:var(--panel)"><span class="n">NBR 25605</span><span class="t">Legendas</span><span class="k">closed captioning</span></button>
<button type="button" class="blk" data-k="cs" style="--c:var(--app);--cb:var(--panel)"><span class="n">NBR 25606</span><span class="t">Língua de sinais</span><span class="k">closed signing</span></button>
<button type="button" class="blk" data-k="aea" style="--c:var(--alr);--cb:var(--panel)"><span class="n">NBR 25607</span><span class="t">Alerta de emergência</span><span class="k">AEA · AEAT</span></button>
</section>
</section>
<button type="button" class="blk" data-k="tr" style="--c:var(--tr);--cb:var(--tr-bg)"><span class="n">NBR 25602</span><span class="t">Camada de transporte</span><span class="k">ROUTE/DASH · LLS · SLS — MMT/MMTP excluído</span></button>
<section class="bottom">
<button type="button" class="blk" data-k="phy" style="--c:var(--phy);--cb:var(--phy-bg)"><span class="n">NBR 25601</span><span class="t">Camada física over-the-air</span><span class="k">MIMO · LDM · TxID · 44–960 MHz</span></button>
<button type="button" class="blk" data-k="bb" style="--c:var(--muted);--cb:var(--panel)"><span class="n">—</span><span class="t">Interface de banda larga</span><span class="k">IP bidirecional</span></button>
</section>
</section>
<button type="button" class="blk rx" data-k="rx" style="--c:var(--ink);--cb:transparent"><span class="n">NBR 25609</span> <span class="t">Receptores</span></button>
</section>
<aside class="panel" aria-live="polite" id="pn1"><span class="n" id="pn1n"></span><strong class="pnt" id="pn1t"></strong><p id="pn1p"></p></aside>
</section>
<figcaption class="caption"><p>Figura 1 das ABNT NBR 25601 a 25608, reproduzida em estrutura; a coluna de receptores é acréscimo desta página.</p><span class="tv3-cite">NBR 25601–25609:2025, Figura 1</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig1');
  if (!S) return;
  var D = {
    phy:['NBR 25601','Camada física OTA','Cumpre a ATSC A/322. Combina MIMO e LDM para eficiência espectral e energética, e TxID para segmentação geográfica. VHF ou UHF de 44 MHz a 960 MHz, canais de 6, 7 ou 8 MHz.','var(--phy)'],
    bb:['—','Interface de banda larga','Qualquer interface bidirecional baseada em IP usada para acesso à internet.','var(--muted)'],
    tr:['NBR 25602','Camada de transporte','ROUTE/DASH da ATSC A/331. MMT/MMTP excluído. Acrescenta BAMT e TBSAT à LLS, substitui HELD por BALD na SLS.','var(--tr)'],
    video:['NBR 25603','Vídeo','VVC, HEVC, AVC, LCEVC; HDR10, SL-HDR1, SL-HDR2, HLG, SMPTE ST 2094-10 e 2094-40; V3C para volumétrico.','var(--app)'],
    audio:['NBR 25604','Áudio','MPEG-H Audio como referência; AAC, AC-4 e E-AC-3 JOC também decodificados.','var(--app)'],
    cc:['NBR 25605','Legendas','IMSC1 e WebVTT.','var(--app)'],
    cs:['NBR 25606','Língua de sinais','Stream de vídeo de Libras, stream de gloss e stream de movimento.','var(--app)'],
    aea:['NBR 25607','Alerta de emergência','Sistema AEA: mensagens AEA-MF transportadas na AEAT dentro da LLS.','var(--alr)'],
    apps:['NBR 25608','Codificação de aplicações','AoP, Ginga-NCL e Ginga-HTML5, WebServices, Application Catalog, Persistent Media Player, Access Panel, BALD, PRRD.','var(--app)'],
    rx:['NBR 25609','Receptores','BDR, STB e GTW; nove perfis de 4K@60fps a 8K@60fps.','var(--ink)']
  };
  var btns = S.querySelectorAll('button.blk');
  function sel(k){
    btns.forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.k === k); });
    var d = D[k]; S.querySelector('#pn1n').textContent = d[0]; S.querySelector('#pn1t').textContent = d[1]; S.querySelector('#pn1p').textContent = d[2];
    S.querySelector('#pn1').style.setProperty('--pc', d[3]);
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ sel(b.dataset.k); }); });
  sel('apps');
  var stack = S.querySelector('.stack'), order = ['phy','bb','tr','video','audio','cc','cs','aea','apps'];
  order.forEach(function(k, i){ var b = S.querySelector('[data-k="' + k + '"]'); b.style.transitionDelay = (i * 90) + 'ms'; });
  function reveal(){ stack.classList.remove('pre'); }
  if (TV3.reduced() || !('IntersectionObserver' in window)) reveal();
  else { var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ reveal(); io.disconnect(); } }); }, {threshold:.15}); io.observe(S); }
})();
</script>

<div class="grid cards tv3-keygrid" markdown>

- <i style="background:var(--phy)"></i><b>Física</b><span>MIMO, LDM, TxID, PLP, RF</span>
- <i style="background:var(--tr)"></i><b>Transporte</b><span>ROUTE, IP, UDP, DASH, HLS</span>
- <i style="background:var(--sig)"></i><b>Sinalização</b><span>LLS, SLS, BALD, BAMT, PRRD</span>
- <i style="background:var(--app)"></i><b>Aplicação</b><span>apps, catálogo, AoP, mídia</span>
- <i style="background:var(--alr)"></i><b>Alerta</b><span>AEA, AEAT, wake-up</span>

</div>

<span class="tv3-cite">A cor de cada termo neste site segue essa chave — vale nas figuras e nas tabelas.</span>

## Parte 2 · Transmissão {#transmissao}

Do arquivo que sai do encoder até a onda irradiada, e o caminho inverso dentro do receptor. É a parte que menos muda para quem escreve aplicação e a que mais muda para quem opera emissora: o multiplex de TV virou uma rede.

### 2.1 Camada física: três ferramentas {#fisica}

A NBR 25601 tem sete páginas e uma única referência normativa, a ATSC A/322. Ela adota o ATSC 3.0 e nomeia as três ferramentas que o Brasil fez questão de combinar: **MIMO** e **LDM** para maximizar eficiência espectral e energética, e **TxID** para habilitar segmentação geográfica de conteúdo e de alertas. Tudo o mais — OFDM, intervalo de guarda, padrão de pilotos — está na A/322, não na norma brasileira.

<section class="figblock" id="fig3" aria-labelledby="fig3-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 3</span> NBR 25601</p>
<p class="figtitle" id="fig3-h">As três ferramentas da camada física</p>
<p class="figdesc">Três mini-figuras com movimento contínuo — aqui o laço é o conteúdo: a portadora não para. O campo elétrico é desenhado como vetores ao longo da propagação; a polarização horizontal aparece em perspectiva, a vertical de pé.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 3, role na horizontal">
<svg viewBox="0 0 1200 400" style="--minw:680px" role="img" aria-label="Três painéis. MIMO: um PLP cria dois caminhos de sinal que alimentam um par de antenas de polarização cruzada, horizontal e vertical. Layered MIMO: as camadas Core e Enhanced do LDM; no tipo A as duas passam por MIMO, no tipo B só a Enhanced, com a Core em SISO. TxID: três transmissores de uma SFN, cada um com o seu txid_address de 13 bits e o polígono de melhor servidor da TBSAT.">
<defs>
<filter id="g3" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1000"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<g style="fill:var(--panel);stroke:var(--line)"><rect x="0" y="0" width="380" height="400"/><rect x="410" y="0" width="380" height="400"/><rect x="820" y="0" width="380" height="400"/></g>
<g style="font-size:20px;font-weight:600;fill:var(--ink)"><text x="20" y="34">MIMO</text><text x="430" y="34">layered MIMO</text><text x="840" y="34">TxID</text></g>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)"><text x="20" y="54">NBR 25601, 3.1</text><text x="430" y="54">NBR 25601, 3.2.1 e 3.2.2</text><text x="840" y="54">NBR 25601, 3.5 · 25602, 8.3</text></g>
<rect x="20" y="172" width="70" height="50" style="fill:var(--phy);stroke:var(--phy)"/>
<text x="38" y="202" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)">PLP</text>
<path id="m3p" d="M90 197H130L190 122M130 197L190 282" style="fill:none;stroke:var(--phy);stroke-width:2.5;stroke-dasharray:8 5"/>
<g style="stroke:var(--phy);stroke-width:5;stroke-linecap:round"><path d="M196 122H244"/><path d="M220 258V306"/></g>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)"><text x="196" y="108">H</text><text x="230" y="262">V</text></g>
<path d="M252 122H368M232 282H368" style="stroke:var(--line);stroke-width:1"/>
<g id="eh3" style="stroke:var(--phy);stroke-width:2"></g>
<g id="ev3" style="stroke:var(--phy);stroke-width:2"></g>
<text x="20" y="352" style="font-size:13px;fill:var(--muted)">O oposto é SISO: um caminho, uma antena.</text>
<text x="20" y="372" style="font-size:13px;fill:var(--muted)">Aqui, um PLP alimenta dois.</text>
<path d="M440 82V262" style="stroke:var(--muted);stroke-width:1.5"/>
<text x="436" y="78" class="svgtxt" style="font-size:12px;fill:var(--muted)">potência</text>
<rect x="450" y="110" width="120" height="52" style="fill:var(--phy);stroke:var(--phy)"/>
<rect x="450" y="176" width="120" height="30" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>
<g class="svgtxt" style="font-size:12px"><text x="462" y="141" style="fill:var(--on);font-weight:500">Core</text><text x="462" y="196" style="fill:var(--phy)">Enhanced</text></g>
<path d="M578 110h6v96h-6" style="fill:none;stroke:var(--muted);stroke-width:1.5"/><text x="590" y="162" class="svgtxt" style="font-size:12px;fill:var(--muted)">LDM</text>
<g style="stroke:var(--phy);stroke-width:5;stroke-linecap:round"><path d="M716 126H764"/><path d="M740 232V280"/></g>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)"><text x="768" y="130">H</text><text x="750" y="236">V</text></g>
<g id="lm3" style="fill:none;stroke-width:2.5;stroke-dasharray:8 5">
<path data-k="cH" d="M570 128C630 128 660 126 712 126" style="stroke:var(--phy)"/>
<path data-k="cV" d="M570 136C640 136 660 256 734 256" style="stroke:var(--phy)"/>
<path data-k="eH" d="M570 186C640 186 650 130 712 128" style="stroke:var(--phy);opacity:.6"/>
<path data-k="eV" d="M570 194C630 194 660 260 734 260" style="stroke:var(--phy);opacity:.6"/>
<path data-k="cS" d="M570 136C630 136 650 196 712 196" style="stroke:var(--phy)"/>
</g>
<g id="siso3"><rect x="712" y="184" width="50" height="24" style="fill:var(--panel);stroke:var(--phy);stroke-width:1.5"/><text x="720" y="200" class="svgtxt" style="font-size:12px;fill:var(--phy)">SISO</text></g>
<text id="lmt3" x="430" y="340" style="font-size:13px;fill:var(--ink)"></text>
<text id="lmt3b" x="430" y="360" style="font-size:13px;fill:var(--muted)"></text>
<g id="pl3" style="stroke:var(--phy);stroke-width:1.5;stroke-linejoin:round">
<path d="M836 70H990L970 190L836 214Z" style="fill:var(--phy-bg)"/>
<path d="M990 70H1184V176L970 190Z" style="fill:var(--phy-bg)"/>
<path d="M836 214L970 190L1184 176V262H836Z" style="fill:var(--phy-bg)"/>
</g>
<path id="plh3" d="" style="fill:none;stroke:var(--ink);stroke-width:2.5" filter="url(#g3)"/>
<g id="vx3" style="fill:var(--ink)"></g>
<g id="tx3" style="fill:var(--phy)"><path d="M900 128l-7 18h14Z"/><path d="M1090 112l-7 18h14Z"/><path d="M1010 222l-7 18h14Z"/></g>
<text x="840" y="282" class="svgtxt" style="font-size:12px;fill:var(--muted)">polígono WGS 84 · ≥ 4 pares de coordenadas</text>
<g class="svgtxt" style="font-size:12px"><text x="840" y="312" style="fill:var(--phy)">1º txId · H</text><text x="840" y="342" style="fill:var(--phy)">2º txId · V</text></g>
<g id="bits3"></g>
<text x="840" y="378" class="svgtxt" style="font-size:12px;fill:var(--muted)">13 bits · 0 a 8191 · valores de exemplo</text>
</svg>
</section>
<nav class="controls">
<button type="button" class="icon" id="pz3" aria-label="Pausar"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path id="pz3i" d="M4 3h3v10H4ZM9 3h3v10H9Z" style="fill:currentColor"/></svg></button>
<span class="seg" role="group" aria-label="Tipo de layered MIMO"><button type="button" id="tA3" aria-pressed="true">tipo A</button><button type="button" id="tB3" aria-pressed="false">tipo B</button></span>
</nav>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig3'), $ = function(id){ return document.getElementById(id); }, T = TV3, NS = 'http://www.w3.org/2000/svg';
  if (!S) return;
  var eh = $('eh3'), ev = $('ev3'), N = 19, LH = [], LV = [];
  for (var i = 0; i < N; i++){ var a = document.createElementNS(NS, 'line'), b = document.createElementNS(NS, 'line'); eh.appendChild(a); ev.appendChild(b); LH.push(a); LV.push(b); }
  var lm = {}; Array.prototype.forEach.call($('lm3').children, function(p){ lm[p.dataset.k] = p; });
  var type = 'A';
  var POLY = [[[836,70],[990,70],[970,190],[836,214]], [[990,70],[1184,70],[1184,176],[970,190]], [[836,214],[970,190],[1184,176],[1184,262],[836,262]]];
  var IDS = [[17,18],[33,34],[49,50]];
  var bitsG = $('bits3'), cells = [[],[]];
  for (var r = 0; r < 2; r++){
    for (var c = 0; c < 13; c++){
      var g = document.createElementNS(NS, 'g'), x = 940 + c * 17, y = 298 + r * 30;
      g.innerHTML = '<rect x="' + x + '" y="' + y + '" width="15" height="20" style="stroke:var(--phy);stroke-width:1"/><text x="' + (x + 7.5) + '" y="' + (y + 15) + '" text-anchor="middle" class="svgtxt" style="font-size:12px"></text>';
      bitsG.appendChild(g); cells[r].push(g);
    }
    var v = document.createElementNS(NS, 'text'); v.setAttribute('x', 1166); v.setAttribute('y', 313 + r * 30); v.setAttribute('class', 'svgtxt'); v.setAttribute('style', 'font-size:12px;fill:var(--ink)'); bitsG.appendChild(v); cells[r].val = v;
  }
  function setType(t){
    type = t; $('tA3').setAttribute('aria-pressed', t === 'A'); $('tB3').setAttribute('aria-pressed', t === 'B');
    lm.cH.style.display = lm.cV.style.display = t === 'A' ? '' : 'none';
    lm.cS.style.display = $('siso3').style.display = t === 'B' ? '' : 'none';
    $('lmt3').textContent = t === 'A' ? 'Tipo A: MIMO na Core e na Enhanced.' : 'Tipo B: MIMO só na Enhanced.';
    $('lmt3b').textContent = t === 'A' ? 'As duas camadas vão às duas polarizações.' : 'A Core segue em SISO.';
    loop.redraw();
  }
  function frame(t){
    var red = T.reduced();
    for (var i = 0; i < N; i++){
      var x = 256 + i * 6, ph = x * 0.11 - (red ? 0 : t * 6), a = Math.sin(ph) * 22;
      LH[i].setAttribute('x1', x); LH[i].setAttribute('y1', 122); LH[i].setAttribute('x2', (x + a * .55).toFixed(1)); LH[i].setAttribute('y2', (122 - a * .4).toFixed(1));
      LV[i].setAttribute('x1', x); LV[i].setAttribute('y1', 282); LV[i].setAttribute('x2', x); LV[i].setAttribute('y2', (282 - a).toFixed(1));
    }
    var off = red ? 0 : (-t * 30).toFixed(1);
    $('m3p').style.strokeDashoffset = off;
    for (var k in lm) lm[k].style.strokeDashoffset = off;
    var cyc = red ? 0 : Math.floor(t / 3.2) % 3, local = red ? 1 : (t % 3.2) / 3.2;
    var P = POLY[cyc]; $('plh3').setAttribute('d', 'M' + P.map(function(p){ return p.join(' '); }).join('L') + 'Z');
    $('vx3').innerHTML = P.map(function(p){ return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="4"/>'; }).join('');
    var txs = $('tx3').children; for (var q = 0; q < txs.length; q++){ txs[q].setAttribute('filter', q === cyc ? 'url(#g3)' : ''); txs[q].style.opacity = q === cyc ? 1 : .45; }
    for (var r = 0; r < 2; r++){
      var val = IDS[cyc][r], bits = val.toString(2).padStart(13, '0'), lit = Math.floor(T.clamp(local * 1.6) * 13 + .001);
      for (var c = 0; c < 13; c++){
        var on = bits[c] === '1', g = cells[r][c], shown = c < lit || red;
        g.children[0].style.fill = shown && on ? 'var(--phy)' : 'var(--panel)';
        g.children[1].textContent = shown ? bits[c] : '';
        g.children[1].style.fill = on ? 'var(--on)' : 'var(--phy)';
      }
      cells[r].val.textContent = (lit >= 13 || red) ? '= ' + val : '';
    }
  }
  var loop = T.Loop(S, frame);
  $('pz3').addEventListener('click', function(){ var p = loop.toggle(); $('pz3').setAttribute('aria-label', p ? 'Reproduzir' : 'Pausar'); $('pz3i').setAttribute('d', p ? 'M4 2.5L13 8l-9 5.5Z' : 'M4 3h3v10H4ZM9 3h3v10H9Z'); });
  $('tA3').addEventListener('click', function(){ setType('A'); });
  $('tB3').addEventListener('click', function(){ setType('B'); });
  setType('A');
})();
</script>

<div class="grid cards" markdown>

- **MIMO**

    Um PLP configurado para criar dois caminhos de sinal que alimentam um par de antenas de polarização cruzada — uma horizontal, uma vertical. O oposto é SISO.

- **layered MIMO**

    MIMO e LDM ativos ao mesmo tempo. **Tipo A**: MIMO aplicado às camadas Core e Enhanced. **Tipo B**: MIMO só na Enhanced, com a Core em SISO.

- **TxID**

    `txid_address` é um identificador de 13 bits, único por transmissor num dado canal de RF, de 0 a 8191. Em MIMO pode haver um por polarização: o primeiro `txId` é a horizontal, o segundo a vertical. A TBSAT associa cada um a um polígono WGS 84 de ao menos quatro pares de coordenadas, onde aquele transmissor é o melhor servidor.

- **O que fica com a regulação local**

    Faixa de operação de 44 MHz a 960 MHz em canais de 6, 7 ou 8 MHz; offset de frequência, estabilidade dos portadores e máscara de espectro são definidos por cada país. No Brasil, pela Anatel.

- **O que a aplicação enxerga**

    Uma Broadcaster Application consulta parâmetros da camada física pelos TV 3.0 WebServices. A robustez do PLP escolhido define se o pacote da aplicação chega inteiro, e em quanto tempo.

- **PLP, a unidade de serviço**

    Um sinal pode carregar até 64 PLPs, mas um serviço usa no máximo quatro. Com LDM, PLPs da camada Core consomem processadores do receptor para descobrir a Enhanced, mesmo sem pertencer ao serviço sintonizado.

</div>

### 2.2 Do arquivo ao ar {#cadeia}

Cinco estágios, e em cada um a carga muda de forma. O detalhe que mais importa para laboratório: o **PCAP da suíte de testes sai do scheduler**, no formato STLTP da ATSC A/324 — não do modulador. É por isso que o artefato de teste da TV 3.0 é um PCAP, e não um Transport Stream.

<section class="figblock" id="fig2" aria-labelledby="fig2-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 2</span> NBR 25601, Anexo A</p>
<p class="figtitle" id="fig2-h">Cadeia de transmissão</p>
<p class="figdesc">Em cima, a sala de equipamentos com o sinal correndo entre eles; embaixo, o microscópio: a estrutura interna do que passa pelo estágio ativo. O PCAP da suíte de testes sai do scheduler — não do modulador.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 2, role na horizontal">
<svg viewBox="0 0 1200 640" style="--minw:680px" role="img" aria-label="Cinco estágios desenhados como equipamentos: fontes codificadas em DASH, multiplexador que forma a sessão ROUTE e o ALP com a LMT, scheduler que gera o STLTP e de onde se deriva o PCAP, modulador que insere o Bootstrap e o TxID, e amplificador com antena de polarização cruzada. Encoder, multiplexador, scheduler e modulador sincronizados por NTP; o modulador também por GPS. Abaixo, um painel ampliado mostra a estrutura do sinal em cada estágio.">
<defs>
<filter id="g2" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="c2seg"><rect x="200" y="360" width="850" height="150"/></clipPath><clipPath id="c2pol"><rect x="236" y="420" width="190" height="100"/></clipPath><clipPath id="c2air"><rect x="1080" y="0" width="120" height="290"/></clipPath>
</defs>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)"><text x="40" y="24">SALA DE EQUIPAMENTOS</text></g>
<path d="M180 120C220 120 220 150 260 150M180 150H260M180 180C220 180 220 150 260 150" style="fill:none;stroke:var(--app);stroke-width:2"/>
<path d="M400 150H480" style="stroke:var(--tr);stroke-width:6"/>
<path d="M620 146H720M620 154H720" style="stroke:var(--tr);stroke-width:2.5"/>
<path d="M860 150H940" style="stroke:var(--phy);stroke-width:8"/>
<path d="M1020 150H1060V60H1088" style="fill:none;stroke:var(--phy);stroke-width:5"/>
<text x="406" y="140" class="svgtxt" style="font-size:12px;fill:var(--tr)">ROUTE</text>
<text x="640" y="138" class="svgtxt" style="font-size:12px;fill:var(--tr)">STLTP</text>
<text x="872" y="138" class="svgtxt" style="font-size:12px;fill:var(--phy)">RF</text>
<g id="tap2">
<path d="M670 154V244" style="stroke:var(--ink);stroke-width:2;stroke-dasharray:5 3"/>
<path d="M660 154h20l-4 10h-12Z" style="fill:var(--ink)"/>
<rect x="628" y="244" width="84" height="26" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>
<text x="648" y="262" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--ink)">PCAP</text>
</g>
<rect id="tapglow2" x="628" y="244" width="84" height="26" style="fill:none;stroke:var(--ink);stroke-width:3" filter="url(#g2)"/>
<path d="M110 236H790" style="stroke:var(--muted);stroke-width:1.5;stroke-dasharray:2 4"/>
<g style="stroke:var(--muted);stroke-width:1.5;stroke-dasharray:2 4"><path d="M166 190V236M386 180V236M606 180V236M846 180V236"/></g>
<path d="M790 236H846" style="stroke:var(--muted);stroke-width:1.5;stroke-dasharray:2 4"/>
<text x="40" y="240" class="svgtxt" style="font-size:12px;fill:var(--muted)">NTP</text>
<g style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5">
<rect x="40" y="106" width="140" height="26"/><rect x="40" y="137" width="140" height="26"/><rect x="40" y="168" width="140" height="26"/>
<rect x="260" y="120" width="140" height="60"/><rect x="480" y="120" width="140" height="60"/><rect x="720" y="120" width="140" height="60"/><rect x="940" y="120" width="80" height="60"/>
</g>
<g style="stroke:var(--ink);stroke-width:5"><path d="M40 106v88M180 106v88M260 120v60M400 120v60M480 120v60M620 120v60M720 120v60M860 120v60M940 120v60M1020 120v60"/></g>
<g style="stroke:var(--line);stroke-width:1"><path d="M272 166h50M272 171h50M492 166h50M492 171h50M732 166h50M732 171h50M952 166h40M952 171h40"/></g>
<g class="svgtxt" style="font-size:12px">
<text x="52" y="124" style="fill:var(--app)">vídeo</text><text x="52" y="155" style="fill:var(--app)">áudio</text><text x="52" y="186" style="fill:var(--app)">apps · <tspan style="fill:var(--alr)">AEA</tspan></text>
<text x="272" y="144" style="fill:var(--tr)">ROUTE · ALP</text>
<text x="492" y="144" style="fill:var(--tr)">PLP · ModCod</text>
<text x="732" y="144" style="fill:var(--phy)">Bootstrap · TxID</text>
<text x="952" y="144" style="fill:var(--phy)">PA</text>
</g>
<g id="leds2" style="fill:var(--app)"><circle cx="168" cy="119" r="3.5"/><circle cx="388" cy="168" r="3.5"/><circle cx="608" cy="168" r="3.5"/><circle cx="848" cy="168" r="3.5"/><circle cx="1008" cy="168" r="3.5"/></g>
<path d="M846 120V104M836 104a10 10 0 0 1 20 0Z" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"/>
<text x="862" y="102" class="svgtxt" style="font-size:12px;fill:var(--muted)">GPS</text>
<g style="font-size:15px;font-weight:600;fill:var(--ink)" text-anchor="middle">
<text x="110" y="216">Fontes</text><text x="330" y="208">Multiplexador</text><text x="550" y="208">Scheduler</text><text x="790" y="208">Modulador</text><text x="1030" y="208">Amplificador e antena</text>
</g>
<g style="fill:none;stroke:var(--ink);stroke-width:1.5">
<path d="M1110 40L1090 190M1110 40L1130 190M1094 160H1126M1098 128H1122M1102 96H1118M1106 66H1114M1094 160L1122 128M1098 128L1118 96M1102 96L1114 66"/>
</g>
<g style="stroke:var(--phy);stroke-width:3"><path d="M1092 50H1128M1110 32V68"/></g>
<text x="1136" y="44" class="svgtxt" style="font-size:12px;fill:var(--phy)">H</text><text x="1114" y="28" class="svgtxt" style="font-size:12px;fill:var(--phy)">V</text>
<g id="w2" clip-path="url(#c2air)" style="fill:none;stroke:var(--phy);stroke-width:2"><circle cx="1110" cy="50" r="20"/><circle cx="1110" cy="50" r="20"/><circle cx="1110" cy="50" r="20"/><circle cx="1110" cy="50" r="20"/></g>
<g id="tok2">
<g data-t="0"><rect x="-26" y="-14" width="52" height="7" style="fill:var(--app)"/><rect x="-26" y="-3" width="52" height="7" style="fill:var(--app);opacity:.75"/><rect x="-26" y="8" width="40" height="7" style="fill:var(--app);opacity:.55"/><circle cx="22" cy="11" r="4" style="fill:var(--alr)"/></g>
<g data-t="1"><rect x="-30" y="-18" width="60" height="36" style="fill:var(--tr-bg);stroke:var(--tr);stroke-width:2"/><path d="M-6 -12h18v24h-18l3-4-3-4 3-4-3-4 3-4-3-4Z" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5"/><rect x="-6" y="-12" width="18" height="6" style="fill:var(--tr)"/></g>
<g data-t="2"><path d="M-34 -20h-6v40h6M34 -20h6v40h-6" style="fill:none;stroke:var(--tr);stroke-width:2.5"/><rect x="-30" y="-12" width="18" height="24" style="fill:var(--tr-bg);stroke:var(--tr)"/><rect x="-9" y="-12" width="18" height="24" style="fill:var(--tr-bg);stroke:var(--tr)"/><rect x="12" y="-12" width="18" height="24" style="fill:var(--tr-bg);stroke:var(--tr)"/></g>
<g data-t="3"><rect x="-34" y="-18" width="12" height="36" style="fill:var(--phy)"/><path d="M-20 0c5-18 9-18 13 0s9 18 13 0 9-18 13 0 9 18 13 0" style="fill:none;stroke:var(--phy);stroke-width:2.5"/></g>
<g data-t="4"><path d="M-20 -14a20 20 0 0 1 0 28M-8 -22a32 32 0 0 1 0 44M4 -30a44 44 0 0 1 0 60" style="fill:none;stroke:var(--phy);stroke-width:2.5"/><circle cx="-26" cy="0" r="4" style="fill:var(--phy)"/></g>
</g>
<rect x="30" y="290" width="1140" height="340" style="fill:var(--panel);stroke:var(--line)"/>
<path id="lens2" d="M102 290L110 278L118 290Z" style="fill:var(--ink)"/>
<text x="50" y="318" class="svgtxt" style="font-size:12px;fill:var(--muted)">DENTRO DO ESTÁGIO</text>
<text id="mname2" x="50" y="344" style="font-size:20px;font-weight:600;fill:var(--ink)">Fontes</text>
<g id="m2a">
<g class="svgtxt" style="font-size:12px;fill:var(--app)" text-anchor="end"><text x="190" y="384">vídeo</text><text x="190" y="422">áudio</text><text x="190" y="460">legendas</text><text x="190" y="498">Libras</text><text x="190" y="536">apps</text><text x="190" y="574" style="fill:var(--alr)">AEA</text></g>
<g clip-path="url(#c2seg)"><g id="m2scroll">
<g style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5">
<rect x="210" y="368" width="112" height="24"/><rect x="330" y="368" width="112" height="24"/><rect x="450" y="368" width="112" height="24"/><rect x="570" y="368" width="112" height="24"/><rect x="690" y="368" width="112" height="24"/><rect x="810" y="368" width="112" height="24"/><rect x="930" y="368" width="112" height="24"/>
<rect x="210" y="406" width="112" height="24"/><rect x="330" y="406" width="112" height="24"/><rect x="450" y="406" width="112" height="24"/><rect x="570" y="406" width="112" height="24"/><rect x="690" y="406" width="112" height="24"/><rect x="810" y="406" width="112" height="24"/><rect x="930" y="406" width="112" height="24"/>
<rect x="210" y="444" width="112" height="24"/><rect x="330" y="444" width="112" height="24"/><rect x="450" y="444" width="112" height="24"/><rect x="570" y="444" width="112" height="24"/><rect x="690" y="444" width="112" height="24"/><rect x="810" y="444" width="112" height="24"/><rect x="930" y="444" width="112" height="24"/>
<rect x="210" y="482" width="112" height="24"/><rect x="330" y="482" width="112" height="24"/><rect x="450" y="482" width="112" height="24"/><rect x="570" y="482" width="112" height="24"/><rect x="690" y="482" width="112" height="24"/><rect x="810" y="482" width="112" height="24"/><rect x="930" y="482" width="112" height="24"/>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--app)"><text x="218" y="384">segmento DASH</text><text x="218" y="422">segmento DASH</text><text x="218" y="460">IMSC1 · WebVTT</text><text x="218" y="498">vídeo · gloss · movimento</text></g>
</g></g>
<g style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5"><path d="M210 522h20l8 8v18h-28Z"/><path d="M246 522h20l8 8v18h-28Z"/><path d="M282 522h20l8 8v18h-28Z"/></g>
<text x="322" y="540" class="svgtxt" style="font-size:12px;fill:var(--app)">pacotes da 25608</text>
<rect x="210" y="560" width="70" height="22" style="fill:var(--alr);stroke:var(--alr)"/><text x="217" y="575" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)">AEA-MF</text>
<text x="292" y="575" class="svgtxt" style="font-size:12px;fill:var(--alr)">mensagens da 25607</text>
<path d="M1060 380V580" style="stroke:var(--ink);stroke-width:1.5"/><text x="1072" y="476" class="svgtxt" style="font-size:12px;fill:var(--ink)">mesmo</text><text x="1072" y="492" class="svgtxt" style="font-size:12px;fill:var(--ink)">ponto de</text><text x="1072" y="508" class="svgtxt" style="font-size:12px;fill:var(--ink)">entrada</text>
</g>
<g id="m2b">
<rect x="50" y="364" width="500" height="160" style="fill:none;stroke:var(--tr);stroke-width:1.5"/>
<text x="62" y="382" class="svgtxt" style="font-size:12px;fill:var(--tr)">sessão ROUTE</text>
<g style="stroke:var(--tr);stroke-width:1"><path d="M60 410H540M60 446H540M60 482H540M60 434H540M60 470H540M60 506H540"/></g>
<g class="svgtxt" style="font-size:12px;fill:var(--tr)"><text x="62" y="426">LCT · vídeo</text><text x="62" y="462">LCT · áudio</text><text x="62" y="498">LCT · app</text></g>
<g id="m2objs" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.2">
<path d="M170 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M220 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M270 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M320 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M370 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M420 412h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M470 412h28v20h-28l3-5-3-5 3-5-3-5Z"/>
<path d="M190 448h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M260 448h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M330 448h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M400 448h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M470 448h28v20h-28l3-5-3-5 3-5-3-5Z"/>
<path d="M180 484h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M300 484h28v20h-28l3-5-3-5 3-5-3-5Z"/><path d="M420 484h28v20h-28l3-5-3-5 3-5-3-5Z"/>
</g>
<text x="62" y="548" style="font-size:13px;fill:var(--muted)">Dados e sinalização viram objetos, cada canal LCT por componente.</text>
<path d="M556 444H596" style="stroke:var(--tr);stroke-width:2"/><path d="M590 438l8 6-8 6" style="fill:none;stroke:var(--tr);stroke-width:2"/>
<text x="606" y="376" class="svgtxt" style="font-size:12px;fill:var(--muted)">um pacote ALP</text>
<g style="stroke-width:1.5">
<rect x="606" y="388" width="70" height="40" style="fill:var(--tr);stroke:var(--tr)"/>
<rect x="676" y="388" width="60" height="40" style="fill:var(--tr-bg);stroke:var(--tr)"/>
<rect x="736" y="388" width="60" height="40" style="fill:var(--tr-bg);stroke:var(--tr)"/>
<rect x="796" y="388" width="150" height="40" style="fill:var(--tr-bg);stroke:var(--tr)"/>
<rect x="946" y="388" width="180" height="40" style="fill:var(--app-bg);stroke:var(--app)"/>
</g>
<g class="svgtxt" style="font-size:12px"><text x="626" y="413" style="fill:var(--on);font-weight:500">ALP</text><text x="696" y="413" style="fill:var(--tr)">IP</text><text x="750" y="413" style="fill:var(--tr)">UDP</text><text x="806" y="413" style="fill:var(--tr)">ROUTE — ALC/LCT</text><text x="958" y="413" style="fill:var(--app)">objeto · TOI</text></g>
<rect x="606" y="452" width="420" height="132" style="fill:var(--tr-bg);stroke:var(--tr);stroke-width:1.5"/>
<text x="618" y="474" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--tr)">LMT · Link Mapping Table</text>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)"><text x="618" y="500">PLPID</text><text x="718" y="500">endereço IP</text><text x="878" y="500">porta</text></g>
<path d="M618 508H1014" style="stroke:var(--tr);stroke-width:1"/>
<g class="svgtxt" style="font-size:12px;fill:var(--ink)"><text x="618" y="530">0</text><text x="718" y="530">…</text><text x="878" y="530">…</text><text x="618" y="556">1</text><text x="718" y="556">…</text><text x="878" y="556">…</text></g>
<text x="1040" y="500" style="font-size:13px;fill:var(--muted)">qual fluxo IP</text><text x="1040" y="518" style="font-size:13px;fill:var(--muted)">está em qual</text><text x="1040" y="536" style="font-size:13px;fill:var(--muted)">PLP</text>
</g>
<g id="m2c">
<g style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"><rect x="130" y="370" width="560" height="48"/><rect x="130" y="434" width="560" height="48"/></g>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)" text-anchor="end"><text x="118" y="399">PLP 0</text><text x="118" y="463">PLP 1</text></g>
<g style="fill:var(--tr-bg);stroke:var(--tr);stroke-width:1.2">
<rect x="146" y="380" width="44" height="28"/><rect x="200" y="380" width="44" height="28"/><rect x="254" y="380" width="44" height="28"/><rect x="308" y="380" width="44" height="28"/><rect x="362" y="380" width="44" height="28"/><rect x="416" y="380" width="44" height="28"/><rect x="470" y="380" width="44" height="28"/>
<rect x="146" y="444" width="70" height="28"/><rect x="226" y="444" width="70" height="28"/><rect x="306" y="444" width="70" height="28"/><rect x="386" y="444" width="70" height="28"/>
</g>
<g style="fill:var(--phy)"><rect x="600" y="380" width="80" height="28"/><rect x="600" y="444" width="80" height="28"/></g>
<g class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)"><text x="610" y="399">ModCod</text><text x="610" y="463">ModCod</text></g>
<g class="svgtxt" style="font-size:12px"><text x="130" y="516" style="fill:var(--muted)">multiplexação</text><text x="380" y="516" style="fill:var(--muted)">layered MIMO</text></g>
<g style="fill:none;stroke:var(--phy);stroke-width:1.5"><rect x="130" y="526" width="60" height="30"/><rect x="194" y="526" width="60" height="30"/><rect x="380" y="526" width="74" height="30"/><rect x="458" y="526" width="74" height="30"/></g>
<rect x="258" y="526" width="60" height="30" style="fill:var(--phy);stroke:var(--phy)"/>
<g class="svgtxt" style="font-size:12px" text-anchor="middle"><text x="160" y="546" style="fill:var(--phy)">TDM</text><text x="224" y="546" style="fill:var(--phy)">FDM</text><text x="288" y="546" style="fill:var(--on);font-weight:500">LDM</text><text x="417" y="546" style="fill:var(--phy)">tipo A</text><text x="495" y="546" style="fill:var(--phy)">tipo B</text></g>
<text x="130" y="590" style="font-size:13px;fill:var(--muted)">Ou TDM, ou FDM, ou LDM — com layered MIMO tipo A ou B.</text>
<path d="M700 426H760" style="stroke:var(--tr);stroke-width:2"/><path d="M754 420l8 6-8 6" style="fill:none;stroke:var(--tr);stroke-width:2"/>
<path d="M780 360h-10v132h10M1140 360h10v132h-10" style="fill:none;stroke:var(--tr);stroke-width:3"/>
<text x="790" y="380" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--tr)">STLTP · ATSC A/324</text>
<g style="fill:var(--phy-bg);stroke:var(--phy)"><rect x="790" y="394" width="340" height="38"/><rect x="790" y="440" width="340" height="38"/></g>
<g style="fill:var(--tr-bg);stroke:var(--tr)"><rect x="800" y="400" width="40" height="26"/><rect x="846" y="400" width="40" height="26"/><rect x="892" y="400" width="40" height="26"/><rect x="800" y="446" width="64" height="26"/><rect x="870" y="446" width="64" height="26"/></g>
<g id="pcap2m">
<path d="M960 492V522" style="stroke:var(--ink);stroke-width:2;stroke-dasharray:4 3"/>
<rect x="870" y="522" width="270" height="56" style="fill:var(--bg);stroke:var(--ink);stroke-width:2.5" filter="url(#g2)"/>
<text x="884" y="546" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--ink)">PCAP · suíte de testes</text>
<text x="884" y="566" style="font-size:13px;fill:var(--muted)">gravado aqui, antes do modulador</text>
</g>
</g>
<g id="m2d">
<text x="200" y="372" class="svgtxt" style="font-size:12px;fill:var(--phy)">A/321</text><text x="380" y="372" class="svgtxt" style="font-size:12px;fill:var(--phy)">A/322</text>
<rect x="200" y="382" width="100" height="72" style="fill:var(--phy);stroke:var(--phy)"/>
<rect x="300" y="382" width="120" height="72" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>
<rect x="420" y="382" width="330" height="72" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>
<rect x="750" y="382" width="330" height="72" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>
<path d="M420 418H1080" style="stroke:var(--phy);stroke-width:1;stroke-dasharray:3 3"/>
<g class="svgtxt" style="font-size:12px"><text x="212" y="422" style="fill:var(--on);font-weight:500">Bootstrap</text><text x="312" y="422" style="fill:var(--phy)">Preamble</text><text x="432" y="404" style="fill:var(--phy)">PLP 0 · Core</text><text x="432" y="442" style="fill:var(--phy)">PLP 0 · Enhanced</text><text x="762" y="404" style="fill:var(--phy)">PLP 1 · Core</text><text x="762" y="442" style="fill:var(--phy)">PLP 1 · Enhanced</text></g>
<path id="txid2" d="M300 474" style="fill:none;stroke:var(--phy);stroke-width:1.5"/>
<text x="200" y="482" class="svgtxt" style="font-size:12px;fill:var(--phy)">TxID</text>
<g style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"><rect x="200" y="520" width="380" height="64"/><rect x="600" y="520" width="380" height="64"/></g>
<g class="svgtxt" style="font-size:12px"><text x="214" y="544" style="fill:var(--ink);font-weight:500">NTP · tempo</text><text x="614" y="544" style="fill:var(--ink);font-weight:500">GPS · frequência</text></g>
<text x="214" y="566" style="font-size:13px;fill:var(--muted)">encoder, mux, scheduler e modulador</text><text x="614" y="566" style="font-size:13px;fill:var(--muted)">só o modulador</text>
</g>
<g id="m2e">
<g style="stroke:var(--phy);stroke-width:4"><path d="M120 470H220M170 420V520"/></g>
<circle cx="170" cy="470" r="6" style="fill:var(--phy)"/>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)"><text x="226" y="474">H</text><text x="176" y="414">V</text></g>
<g clip-path="url(#c2pol)"><g id="pol2" style="fill:none;stroke-width:2.5"><path d="M240 500c10-14 20-14 30 0s20 14 30 0 20-14 30 0 20 14 30 0 20-14 30 0 20 14 30 0 20-14 30 0" style="stroke:var(--phy)"/><path d="M240 440c10-14 20-14 30 0s20 14 30 0 20-14 30 0 20 14 30 0 20-14 30 0 20 14 30 0 20-14 30 0" style="stroke:var(--phy);opacity:.55;stroke-dasharray:5 3"/></g></g>
<text x="80" y="560" style="font-size:13px;fill:var(--muted)">Em MIMO, um par de antenas de polarização cruzada.</text>
<rect x="560" y="356" width="580" height="250" style="fill:var(--bg);stroke:var(--line)"/>
<g style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"><path d="M560 356H780L760 500L560 520Z"/><path d="M780 356H960L980 480L760 500Z"/><path d="M960 356H1140V606H900L980 480Z"/><path d="M560 520L760 500L980 480L900 606H560Z"/></g>
<g style="fill:var(--phy)"><path d="M660 430l-7 18h14Z"/><path d="M870 420l-7 18h14Z"/><path d="M1060 470l-7 18h14Z"/><path d="M760 560l-7 18h14Z"/></g>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)"><text x="600" y="466">txid_address 17</text><text x="808" y="456">txid_address 18</text><text x="990" y="506">txid_address 19</text><text x="700" y="594">txid_address 20</text></g>
<text x="572" y="376" class="svgtxt" style="font-size:12px;fill:var(--muted)">SFN · polígonos de melhor servidor na TBSAT</text>
</g>
</svg>
</section>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25601, Anexo A, Figuras A.1 e A.2</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig2'), $ = function(id){ return document.getElementById(id); }, T = TV3;
  if (!S) return;
  var toks = $('tok2').children, waves = $('w2').children, leds = $('leds2').children;
  var M = ['m2a','m2b','m2c','m2d','m2e'].map($), NAMES = ['Fontes','Multiplexador','Scheduler','Modulador','Amplificador e antena'];
  var X = [110, 330, 550, 790, 1050], LENS = [110, 330, 550, 790, 1050];
  var tx = 'M260 474'; for (var q = 0; q < 82; q++) tx += 'L' + (260 + q * 10) + ' ' + (474 + (q % 2 ? -4 : 4));
  $('txid2').setAttribute('d', tx);
  T.Fig({ root: S.querySelector('[data-fig]'), phases: [
    {d:4.2, pill:'fontes', title:'Fase 1 — Fontes', text:'Vídeo, áudio, legendas e língua de sinais chegam já codificados em DASH. As aplicações da 25608 e as mensagens de alerta da 25607 entram pelo mesmo ponto.'},
    {d:4.6, pill:'multiplexador', title:'Fase 2 — Multiplexador', text:'Nasce a sessão ROUTE: dados e sinalização são incorporados e passam a viajar como objetos. Aqui também se forma a camada de enlace ALP, com a Link Mapping Table.'},
    {d:5.0, pill:'scheduler', title:'Fase 3 — Scheduler', text:'ModCods de cada PLP, e TDM, FDM ou LDM, com layered MIMO tipo A ou B. A saída é o STLTP da ATSC A/324 — é deste ponto que a suíte de testes grava o PCAP.'},
    {d:4.6, pill:'modulador', title:'Fase 4 — Modulador', text:'Insere o Bootstrap da A/321 e o TxID MIMO da A/322. Encoder, mux, scheduler e modulador sincronizados no tempo por NTP; o modulador também em frequência, por GPS.'},
    {d:4.6, pill:'antena', title:'Fase 5 — Amplificador e antena', text:'Em modo MIMO, por um par de antenas de polarização cruzada. Em SFN, cada transmissor leva o seu txid_address, que a TBSAT amarra a um polígono de melhor servidor.'}
  ], render: function(i, f, u){
    var k = T.ease(T.seg(f, 0, .35)), from = i === 0 ? 110 : X[i - 1];
    var x = i === 0 ? 110 : T.lerp(from, X[i], k), y = 96 - Math.sin(Math.PI * (i === 0 ? 0 : k)) * 16;
    $('tok2').setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')');
    T.op($('tok2'), i === 0 ? T.seg(f, 0, .2) : 1);
    for (var t = 0; t < toks.length; t++){
      var o = t === i ? (i === 0 ? 1 : T.seg(f, .25, .4)) : (t === i - 1 ? 1 - T.seg(f, .25, .4) : 0);
      toks[t].style.opacity = o;
    }
    for (var l = 0; l < leds.length; l++) leds[l].style.opacity = l <= i ? 1 : .2;
    for (var m = 0; m < M.length; m++) M[m].style.opacity = m === i ? T.seg(f, .3, .5) : (m === i - 1 ? 1 - T.seg(f, .2, .3) : 0);
    if (f > .3) $('mname2').textContent = NAMES[i];
    $('lens2').setAttribute('d', 'M' + (LENS[i] - 8) + ' 290L' + LENS[i] + ' 278L' + (LENS[i] + 8) + ' 290Z');
    var tap = i > 2 ? 1 : i === 2 ? T.seg(f, .5, .7) : 0;
    T.op($('tapglow2'), i === 2 ? tap : 0);
    T.op($('pcap2m'), i === 2 ? T.seg(f, .55, .75) : 1);
    var wOn = i === 4 ? T.seg(f, .2, .4) : 0;
    for (var w = 0; w < waves.length; w++){
      var r = T.reduced() ? 30 + w * 30 : ((u * 40 + w * 30) % 120) + 14;
      waves[w].setAttribute('r', r.toFixed(1)); waves[w].style.opacity = (wOn * (1 - r / 140)).toFixed(3);
    }
    var sh = T.reduced() ? 0 : -((u * 60) % 60);
    $('pol2').setAttribute('transform', 'translate(' + sh.toFixed(1) + ' 0)');
  }});
})();
</script>

<div class="grid cards" markdown>

- **Sincronismo é requisito**

    Encoder, multiplexador, scheduler e modulador sincronizados no tempo, por exemplo via NTP. O modulador também em frequência, por exemplo via GPS. Sem isso, SFN não fecha.

- **Onde cada protocolo entra**

    A sessão ROUTE nasce no multiplexador, conforme a 25602. A camada de enlace ALP e a LMT vêm da ATSC A/330. O STLTP, da A/324. O Bootstrap, da A/321. O TxID, da A/322.

- **SFN e geolocalização**

    Cada transmissor leva o seu `txid_address` — 13 bits, de 0 a 8191. A TBSAT amarra cada um a um polígono WGS 84 de melhor servidor, o que dá ao receptor localização direto do sinal, sem GPS e sem internet.

</div>

### 2.3 Transporte: tudo é IP {#transporte}

A tecnologia central é o ROUTE/DASH da ATSC A/331. Pelo ar vai ROUTE; pela banda larga, DASH ou HLS. O mesmo serviço pode ter componentes nos dois caminhos, e o receptor costura. O que a TV 3.0 fez de mais decisivo aqui foi cortar.

#### O que foi recortado da ATSC

- **MMT/MMTP não pode ser usado.** Toda referência a ele na A/331 deve ser desconsiderada — existe um único caminho OTA.
- **Sem assinatura digital de tabela**, nem na LLS nem na SLS. A SignedMultiTable fica fora.
- **EME/CENC só na banda larga.** O DRM Data Service Type não é usado em configuração de broadcast.
- **XLink fora** para substituição de conteúdo e inserção de anúncio; no lugar, os mecanismos de Alternative MPD.
- **Só Fast Service Scan.** O Full-Service Scan não é usado.

<span class="tv3-cite">25602, 6.2, 8.1, 9.2 e Anexos A e B</span>

#### Os quatro Service Types que sobraram

| Código | Tipo de serviço |
| :--- | :--- |
| <span class="c-tr">`30`</span> | **Service Based on Bootstrap Application** — o serviço principal da TV 3.0 |
| <span class="c-tr">`31`</span> | Additional Linear A/V — só existe atrelado a um Tipo 30 |
| <span class="c-tr">`32`</span> | Additional Linear Audio-Only — idem |
| <span class="c-tr">`4`</span> | ESG — associado exclusivamente ao Tipo 30 |

<span class="tv3-cite">Os tipos 1, 2 e 3 da A/331 foram excluídos. O terceiro octeto do IP do serviço deriva da frequência central dividida pela largura do canal; `majorChannelNo` e `minorChannelNo` só valem no Tipo 30. 25602, 8.1</span>

### 2.4 Encapsulamento, camada a camada {#encapsulamento}

O mesmo segmento DASH desce ganhando um invólucro por camada e sobe no receptor perdendo todos eles. A entrega pelo ar não tem canal de retorno — daí a necessidade de FEC e de repetição, que reaparece na Parte 4 como carrossel.

<section class="figblock" id="fig4" aria-labelledby="fig4-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 4</span> NBR 25602 e 25601</p>
<p class="figtitle" id="fig4-h">Encapsulamento e desencapsulamento</p>
<p class="figdesc">Um segmento DASH desce ganhando um invólucro por camada e sobe, no receptor, perdendo todos. Daqui para baixo do IP, a transmissão de TV é indistinguível de uma rede de dados — com uma diferença: não há retorno.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 4, role na horizontal">
<svg viewBox="0 0 1200 610" style="--minw:680px" role="img" aria-label="Escada de encapsulamento. À esquerda, na emissora, o segmento DASH em ISOBMFF ganha, linha a linha, os cabeçalhos ROUTE ALC/LCT, UDP, IP, ALP e, na camada física, o PLP. Atravessa o ar. À direita, no receptor, a mesma pilha é desmontada de baixo para cima até o segmento chegar ao player como saiu. No alto, o caminho OTT por HTTP e TCP, o único em que EME/CENC é permitido.">
<defs>
<filter id="g4" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="iso4" width="8" height="40" patternUnits="userSpaceOnUse"><path d="M0 0V40" style="stroke:var(--app);stroke-width:1;opacity:.25"/></pattern>
<marker id="a4" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--tr)"/></marker>
<marker id="a4i" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--ink)"/></marker>
</defs>
<g id="ott4">
<path d="M436 58V22H1004V40" style="fill:none;stroke:var(--tr);stroke-width:2;stroke-dasharray:7 5" marker-end="url(#a4)"/>
<text x="560" y="16" class="svgtxt" style="font-size:12px;fill:var(--tr)">OTT · HTTP · TCP — só aqui EME/CENC é permitido</text>
</g>
<g id="rows4"></g>
<g class="svgtxt" style="font-size:12px;fill:var(--ink)" text-anchor="middle" id="lab4">
<text x="600" y="76">segmento DASH</text><text x="600" y="92" style="fill:var(--muted)">ISOBMFF</text>
<text x="600" y="164">ROUTE — ALC/LCT</text>
<text x="600" y="244">UDP</text>
<text x="600" y="324">IP</text>
<text x="600" y="404">ALP + LMT</text>
<text x="600" y="446">camada física</text>
</g>
<path id="air4" d="" style="fill:none;stroke:var(--phy);stroke-width:2.5"/>
<g id="ply4">
<rect x="932" y="44" width="150" height="86" style="fill:var(--off);stroke:var(--ink);stroke-width:2"/>
<path d="M996 70v34l28-17Z" style="fill:var(--ink)"/>
<text x="1092" y="92" style="font-size:13px;fill:var(--ink)">player</text>
<path d="M854 80H924" style="stroke:var(--ink);stroke-width:2" marker-end="url(#a4i)"/>
</g>
<text x="40" y="580" class="svgtxt" style="font-size:12px;fill:var(--muted)">EMISSORA · DESCE GANHANDO INVÓLUCROS</text>
<text x="1160" y="580" text-anchor="end" class="svgtxt" style="font-size:12px;fill:var(--muted)">RECEPTOR · SOBE PERDENDO TODOS</text>
<text id="no4" x="40" y="600" style="font-size:13px;fill:var(--muted)"></text>
</svg>
</section>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25602, Anexo B · NBR 25601, 4</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig4'), $ = function(id){ return document.getElementById(id); }, T = TV3, NS = 'http://www.w3.org/2000/svg';
  if (!S) return;
  var B = {
    seg:{w:170, t:'segmento DASH', c:'app', solid:false},
    route:{w:100, t:'ROUTE', c:'tr', solid:false},
    udp:{w:50, t:'UDP', c:'tr', solid:false},
    ip:{w:44, t:'IP', c:'tr', solid:false},
    alp:{w:50, t:'ALP', c:'tr', solid:true},
    plp:{w:50, t:'PLP', c:'phy', solid:true}
  };
  var ORDER = ['plp','alp','ip','udp','route','seg'];
  function blocksFor(k){ return ORDER.slice(5 - k); }
  function rowY(k){ return 60 + k * 80; }
  var rows = { L:[], R:[] }, rowsG = $('rows4');
  function mk(side, k){
    var g = document.createElementNS(NS, 'g'), bl = blocksFor(k), W = 0, y = rowY(k), html = '';
    bl.forEach(function(n){ W += B[n].w; });
    var x0 = side === 'L' ? 520 - W : 680, x = x0;
    if (k === 5) html += '<rect x="' + (x0 - 6) + '" y="' + (y - 6) + '" width="' + (W + 12) + '" height="52" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>';
    bl.forEach(function(n, idx){
      var b = B[n], isNew = (idx === 0 && k > 0) || (k === 0);
      var fill = b.solid ? 'var(--' + b.c + ')' : (n === 'seg' ? 'url(#iso4)' : 'var(--' + b.c + '-bg)');
      html += '<g' + (isNew ? ' class="nw"' : '') + '>' +
        (n === 'seg' ? '<rect x="' + x + '" y="' + y + '" width="' + b.w + '" height="40" style="fill:var(--app-bg)"/>' : '') +
        '<rect x="' + x + '" y="' + y + '" width="' + b.w + '" height="40" style="fill:' + fill + ';stroke:var(--' + b.c + ');stroke-width:1.5"/>' +
        '<text x="' + (x + 8) + '" y="' + (y + 25) + '" class="svgtxt" style="font-size:12px;' + (b.solid ? 'font-weight:500;fill:var(--on)' : 'fill:var(--' + b.c + ')') + '">' + b.t + '</text></g>';
      x += b.w;
    });
    g.innerHTML = html; rowsG.appendChild(g); return g;
  }
  for (var k = 0; k < 6; k++){ rows.L.push(mk('L', k)); }
  for (var k2 = 0; k2 < 6; k2++){ rows.R.push(mk('R', k2)); }
  var air = ''; for (var q = 0; q <= 38; q++){ var xx = 526 + q * 4; air += (q ? 'L' : 'M') + xx + ' ' + (480 + Math.sin(q / 38 * Math.PI * 6) * 10).toFixed(1); }
  $('air4').setAttribute('d', air);
  var labs = $('lab4').children;
  var LABROW = [0,0,1,2,3,4,5];
  T.Fig({ root: S.querySelector('[data-fig]'), phases: [
    {d:2.6, pill:'DASH', title:'Fase 1 — Segmento DASH (ISOBMFF)', text:'Perfil DASH-IF IOP ATSC 3.0, modificado no Anexo B da 25602.'},
    {d:2.6, pill:'ROUTE', title:'Fase 2 — ROUTE — ALC/LCT', text:'Permite entregar o objeto em canais separados por componente e recuperá-lo com FEC.'},
    {d:2.6, pill:'UDP', title:'Fase 3 — UDP', text:'Não há retorno: a entrega pelo ar é unidirecional, e é por isso que tudo precisa ser repetido.'},
    {d:2.6, pill:'IP', title:'Fase 4 — IP', text:'Daqui para baixo, a transmissão de TV é indistinguível de uma rede de dados.'},
    {d:2.6, pill:'ALP + LMT', title:'Fase 5 — ALP + LMT', text:'A Link Mapping Table diz qual fluxo IP está em qual PLP.'},
    {d:3.0, pill:'física', title:'Fase 6 — Camada física TV 3.0', text:'MIMO, LDM e TxID conforme a 25601.'},
    {d:4.2, pill:'recepção', title:'Fase 7 — Recepção', text:'Demodula, desencapsula o ALP, remonta IP e UDP, e ROUTE reconstrói o objeto.'},
    {d:3.4, pill:'player', title:'Fase 8 — Entrega ao player', text:'O segmento chega como saiu. Na entrega OTT, ROUTE e UDP dão lugar a HTTP e TCP, e só nesse caminho o EME/CENC é permitido.'}
  ], render: function(i, f, u){
    for (var k = 0; k < 6; k++){
      var g = rows.L[k], vis, cur = (i === k);
      vis = i > k ? .5 : cur ? 1 : 0;
      if (i >= 6) vis = .45;
      if (i === 5 && k === 5) vis = 1;
      g.style.opacity = vis;
      var nw = g.querySelectorAll('.nw'), sl = cur ? T.easeOut(T.seg(f, 0, .45)) : 1;
      for (var n = 0; n < nw.length; n++){ nw[n].setAttribute('transform', 'translate(' + (-50 * (1 - sl)).toFixed(1) + ' 0)'); nw[n].style.opacity = sl; }
      var dy = cur && k > 0 ? (1 - T.easeOut(T.seg(f, 0, .4))) * -80 : 0;
      g.setAttribute('transform', 'translate(0 ' + dy.toFixed(1) + ')');
      g.setAttribute('filter', cur || (i === 5 && k === 5) ? 'url(#g4)' : '');
    }
    var up = i === 6 ? f * 6 : (i > 6 ? 6 : -1);
    for (var r = 0; r < 6; r++){
      var gR = rows.R[r], step = 5 - r, v;
      if (i < 5) v = 0;
      else if (i === 5) v = r === 5 ? T.seg(f, .55, .85) : 0;
      else if (i === 6) v = up >= step ? (up < step + 1 ? 1 : .5) : 0;
      else v = r === 0 ? 1 : .45;
      gR.style.opacity = v;
      gR.setAttribute('filter', (i === 6 && up >= step && up < step + 1) || (i === 7 && r === 0) ? 'url(#g4)' : '');
      gR.setAttribute('transform', '');
    }
    var airOn = i === 5 ? T.seg(f, .2, .5) : (i > 5 ? .35 : 0);
    $('air4').style.opacity = airOn;
    $('air4').style.strokeDasharray = '10 6'; $('air4').style.strokeDashoffset = T.reduced() ? 0 : (-u * 60).toFixed(1);
    var la = i < 6 ? Math.min(i, 5) : 5 - Math.min(5, Math.floor(up));
    if (i === 7) la = 0;
    for (var l = 0; l < labs.length; l++){ var row = LABROW[l]; labs[l].style.opacity = row === la ? 1 : .45; labs[l].style.fontWeight = row === la ? 500 : 400; }
    T.op($('ply4'), i === 7 ? T.seg(f, .1, .4) : 0);
    T.op($('ott4'), i === 7 ? T.seg(f, .45, .75) : 0);
    $('no4').textContent = i === 2 ? 'Sem retorno: o receptor não pede de novo — espera a repetição.' : '';
  }});
})();
</script>

### 2.5 Retaguarda e massas de teste {#retaguarda}

Um PCAP é um cenário congelado — sinalização, mídias e aplicações, reproduzível. É o que permite a um fabricante repetir um teste meses depois e chegar ao mesmo resultado.

<div class="grid cards" markdown>

- **PCAP, não TS**

    A suíte captura o fluxo **STLTP** que o scheduler entrega ao modulador. Identificadores: `ST3_<F|C>_PCAP_XXX` para TV 3.0 e `ST3_<F|C>_TS_XXX` para TV 2.X.

- **Os XMLs são artefatos à parte**

    O que gerou o PCAP continua identificado e versionado: `ST3_BALD_XXX`, `ST3_BAMT_XXX`, `ST3_PRRD_XXX`, `ST3_AEAT_XXX`, mais os três XMLs de ESG — service, schedule e content.

- **Classes de mídia**

    `ST3_AUDIO`, `ST3_VIDEO`, `ST3_SUBTITLE`, `ST3_IMAGE`, `ST3_TEXT`, `ST3_FONT`, `ST3_MMEDIA` e `ST3_HSTREAM` — este último é streaming adaptativo: manifesto DASH ou HLS mais segmentos, empacotado.

- **Armadilhas de operação**

    A janela da BALD precisa cobrir a data de execução. Trocar o PCAP no modulador ao vivo é o mecanismo para testar DESTROY, KILL e atualização de PRRD. Em modo broadband, o pacote tem que estar acessível no endereço declarado.

</div>

## Parte 3 · Sinalização {#sinalizacao}

Tudo o que o receptor precisa saber chega em XML, em dois níveis. A LLS vale para o canal de RF inteiro, tem endereço IP e porta fixos e é a primeira coisa lida — sem descoberta prévia. A SLS descreve um serviço de cada vez e é apontada pela SLT. Em TV 3.0, nenhuma das duas usa assinatura digital de tabela.

### 3.1 LLS e SLS, tabela por tabela {#lls-sls}

Oito tabelas na LLS, dez fragmentos na SLS. O ponto que mais confunde quem vem da TV 2.X: **uma aplicação não parseia transporte** — ela pede o XML já processado aos TV 3.0 WebServices. A sinalização é superfície de programação, não só plumbing de receptor.

<section class="sigwrap">
<section class="sigcol">
<p class="sighdr" style="color:var(--sig)">Low-Level Signaling</p>
<section class="sigchips lls" id="llsChips"></section>
<p class="sighdr" style="color:var(--tr)">Service Layer Signaling</p>
<section class="sigchips sls" id="slsChips"></section>
</section>
<aside id="sigDetail" aria-live="polite"></aside>
</section>

<span class="tv3-cite">LLS_table_id conforme a Tabela 2 da NBR 25602. A CDT vem da ATSC A/360 e não consta dessa tabela. A RSAT aparece como opcional nas Tabelas A.1 e A.2 da 25602.</span>

### 3.2 Descoberta: o Fast Service Scan {#scan}

Onze passos, do primeiro sinal de RF até o mapa de canais. Quatro parsers trabalham em paralelo, e é do parser da SLT que sai o que é essencial para produzir o **Application Catalog** — a grade de emissoras que o telespectador vê ao terminar a busca. O Full-Service Scan não é usado em TV 3.0.

<section class="figblock" id="fig7" aria-labelledby="fig7-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 7</span> NBR 25602, 9.1 e 9.2</p>
<p class="figtitle" id="fig7-h">Fast Service Scan</p>
<p class="figdesc">Em cima, o sintonizador varrendo a lista predefinida de frequências. Embaixo, o diagrama de sequência da norma: da L1 do Preamble até o Application Catalog e o mapa de canais. O Full-Service Scan não é usado em TV 3.0.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 7, role na horizontal">
<svg viewBox="0 0 1200 650" style="--minw:680px" role="img" aria-label="Varredura de espectro entre 44 e 960 MHz com um marcador de sintonia percorrendo uma lista de frequências; três delas têm sinal. Diagrama de sequência com raias para sintonizador, processador de banda base, middleware, os quatro parsers — LMT, BAMT 0x90, TBSAT 0x91, SLT 0x01 — e o Application Catalog com o mapa de canais. As mensagens aparecem na ordem da norma.">
<defs>
<filter id="g7" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="sp7" x1="0" y1="1" x2="0" y2="0"><stop offset="0" style="stop-color:var(--phy);stop-opacity:.15"/><stop offset="1" style="stop-color:var(--phy);stop-opacity:.9"/></linearGradient>
<marker id="a7p" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--phy)"/></marker><marker id="a7t" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--tr)"/></marker><marker id="a7k" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--ink)"/></marker><marker id="a7s" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--sig)"/></marker>
</defs>
<text x="40" y="22" class="svgtxt" style="font-size:12px;fill:var(--muted)">LISTA PREDEFINIDA DE FREQUÊNCIAS</text>
<path d="M60 112H1140" style="stroke:var(--line);stroke-width:1.5"/>
<g id="bars7"></g>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)"><text x="60" y="132">44 MHz</text><text x="1140" y="132" text-anchor="end">960 MHz</text></g>
<g id="mk7"><path d="M0 34V112" style="stroke:var(--ink);stroke-width:2"/><path d="M-8 26H8L0 36Z" style="fill:var(--ink)"/></g>
<text id="mkl7" x="0" y="20" class="svgtxt" style="font-size:12px;fill:var(--ink)"></text>
<g style="stroke:var(--line);stroke-width:1.5;stroke-dasharray:4 4"><path d="M120 200V620M300 200V620M480 200V620M640 200V620M740 200V620M840 200V620M940 200V620M1090 200V360"/></g>
<g style="stroke-width:1.5">
<rect x="50" y="160" width="140" height="40" style="fill:var(--phy-bg);stroke:var(--phy)"/>
<rect x="230" y="160" width="140" height="40" style="fill:var(--phy-bg);stroke:var(--phy)"/>
<rect x="410" y="160" width="140" height="40" style="fill:var(--panel);stroke:var(--ink)"/>
<rect x="598" y="160" width="84" height="40" style="fill:var(--tr-bg);stroke:var(--tr)"/>
<rect x="698" y="160" width="84" height="40" style="fill:var(--sig-bg);stroke:var(--sig)"/>
<rect x="798" y="160" width="84" height="40" style="fill:var(--sig-bg);stroke:var(--sig)"/>
<rect x="898" y="160" width="84" height="40" style="fill:var(--sig-bg);stroke:var(--sig)"/>
<rect x="1010" y="160" width="160" height="40" style="fill:var(--app-bg);stroke:var(--app)"/>
</g>
<g style="font-size:13px;font-weight:600" text-anchor="middle">
<text x="120" y="185" style="fill:var(--phy)">sintonizador</text><text x="300" y="185" style="fill:var(--phy)">banda base</text><text x="480" y="185" style="fill:var(--ink)">middleware</text>
<text x="1090" y="185" style="fill:var(--app)">Application Catalog</text>
</g>
<g class="svgtxt" style="font-size:12px" text-anchor="middle">
<text x="640" y="185" style="fill:var(--tr)">LMT</text><text x="740" y="178" style="fill:var(--sig)">BAMT</text><text x="740" y="194" style="fill:var(--sig)">0x90</text><text x="840" y="178" style="fill:var(--sig)">TBSAT</text><text x="840" y="194" style="fill:var(--sig)">0x91</text><text x="940" y="178" style="fill:var(--sig)">SLT</text><text x="940" y="194" style="fill:var(--sig)">0x01</text>
</g>
<g id="s7a">
<path d="M120 236H294" style="stroke:var(--phy);stroke-width:2" marker-end="url(#a7p)"/>
<text x="130" y="228" style="font-size:13px;fill:var(--phy)">sinal detectado</text>
<path d="M300 250H340V274H306" style="fill:none;stroke:var(--phy);stroke-width:2" marker-end="url(#a7p)"/>
<text x="350" y="266" class="svgtxt" style="font-size:12px;fill:var(--phy)">L1 do Preamble</text>
</g>
<g id="s7b">
<path d="M300 330H474" style="stroke:var(--tr);stroke-width:3" marker-end="url(#a7t)"/>
<text x="310" y="306" style="font-size:13px;fill:var(--tr)">PLP com Link Layer</text><text x="310" y="322" style="font-size:13px;fill:var(--tr)">Signaling e LLS</text>
<path d="M480 366H934" style="stroke:var(--ink);stroke-width:1.5"/>
<g style="stroke:var(--ink);stroke-width:1.5" marker-end="url(#a7k)"><path d="M640 366V384"/><path d="M740 366V384"/><path d="M840 366V384"/><path d="M940 366V384"/></g>
<text x="490" y="358" style="font-size:13px;fill:var(--ink)">distribui aos módulos funcionais</text>
</g>
<g id="s7c">
<g style="stroke-width:1.5"><rect x="594" y="392" width="92" height="88" style="fill:var(--tr-bg);stroke:var(--tr)"/><rect x="694" y="392" width="92" height="88" style="fill:var(--sig-bg);stroke:var(--sig)"/><rect x="794" y="392" width="92" height="88" style="fill:var(--sig-bg);stroke:var(--sig)"/><rect x="894" y="392" width="92" height="88" style="fill:var(--sig-bg);stroke:var(--sig)"/></g>
<g class="svgtxt" style="font-size:12px">
<text x="602" y="414" style="fill:var(--tr)">PLPID</text><text x="602" y="432" style="fill:var(--tr)">endereço</text><text x="602" y="448" style="fill:var(--tr)">IP</text><text x="602" y="466" style="fill:var(--tr)">porta</text>
<text x="702" y="414" style="fill:var(--sig)">manifestos</text>
<text x="802" y="414" style="fill:var(--sig)">áreas</text>
<text x="902" y="414" style="fill:var(--sig)">serviços</text>
</g>
<g id="pp7" style="fill:var(--sig);opacity:.5"><rect x="702" y="428" width="70" height="8"/><rect x="702" y="444" width="56" height="8"/><path d="M806 452l18-20 26 6 12 26-30 8Z" style="fill:none;stroke:var(--sig);stroke-width:1.5"/><rect x="902" y="428" width="70" height="8"/><rect x="902" y="444" width="70" height="8"/><rect x="902" y="460" width="70" height="8"/></g>
</g>
<g id="s7d">
<path d="M940 480V500H1004" style="fill:none;stroke:var(--sig);stroke-width:2.5" marker-end="url(#a7s)"/>
<text x="1000" y="522" text-anchor="end" style="font-size:13px;fill:var(--sig)">essencial</text>
<path d="M640 480V560H1004" style="fill:none;stroke:var(--ink);stroke-width:1.5;stroke-dasharray:5 3" marker-end="url(#a7k)"/>
<g style="stroke:var(--ink);stroke-width:1.5;stroke-dasharray:5 3"><path d="M740 480V560M840 480V560M940 500V560"/></g>
<text x="660" y="552" style="font-size:13px;fill:var(--muted)">gravado no mapa de canais</text>
</g>
<rect x="1010" y="370" width="160" height="150" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5"/>
<g id="cat7" class="svgtxt" style="font-size:12px;fill:var(--app)"></g>
<rect x="1010" y="536" width="160" height="84" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"/>
<text x="1020" y="556" style="font-size:13px;font-weight:600;fill:var(--ink)">mapa de canais</text>
<g id="map7" class="svgtxt" style="font-size:12px;fill:var(--ink)"></g>
<text x="40" y="640" class="svgtxt" style="font-size:12px;fill:var(--muted)">Full-Service Scan: não usado em TV 3.0</text>
</svg>
</section>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25602, 9.1 e 9.2, Figura 7 · Tabela 2</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig7'), $ = function(id){ return document.getElementById(id); }, T = TV3, NS = 'http://www.w3.org/2000/svg';
  if (!S) return;
  var N = 14, FX = function(j){ return 100 + j * 76; }, SIG = { 3:1, 8:1, 11:1 }, H = [12,16,10,72,14,9,18,13,64,11,15,58,12,10];
  var bars = $('bars7'), boxes = [];
  for (var j = 0; j < N; j++){
    var g = document.createElementNS(NS, 'g'), x = FX(j);
    g.innerHTML = '<rect x="' + (x - 14) + '" y="' + (112 - H[j]) + '" width="28" height="' + H[j] + '" style="fill:' + (SIG[j] ? 'url(#sp7)' : 'var(--hatch)') + '"/>' +
      '<rect x="' + (x - 5) + '" y="140" width="10" height="10" style="fill:none;stroke:var(--muted);stroke-width:1.5"/>';
    bars.appendChild(g); boxes.push(g.children[1]);
  }
  var cat = $('cat7'), map = $('map7'), catRows = [], mapRows = [];
  for (var r = 0; r < 6; r++){
    var t = document.createElementNS(NS, 'g');
    t.innerHTML = '<rect x="1020" y="' + (382 + r * 22) + '" width="12" height="12" style="fill:var(--app)"/><text x="1040" y="' + (393 + r * 22) + '">serviço · …</text>';
    cat.appendChild(t); catRows.push(t);
  }
  var lbl = document.createElementNS(NS, 'text'); lbl.setAttribute('x', '1020'); lbl.setAttribute('y', '366'); lbl.setAttribute('style', 'font-size:12px;fill:var(--app)'); lbl.textContent = 'a partir da SLT'; cat.appendChild(lbl);
  for (var m = 0; m < 3; m++){
    var t2 = document.createElementNS(NS, 'text'); t2.setAttribute('x', '1020'); t2.setAttribute('y', 578 + m * 18); t2.textContent = 'frequência ' + (m + 1) + ' · …'; map.appendChild(t2); mapRows.push(t2);
  }
  function scanPos(i, f){
    if (i === 0) return Math.min(2.999, f * 3.2);
    if (i < 4) return 3;
    return 3 + 10 * T.seg(f, .45, 1);
  }
  T.Fig({ root: S.querySelector('[data-fig]'), phases: [
    {d:4.0, pill:'varredura', title:'Fase 1 — Varredura', text:'O sintonizador percorre uma lista predefinida de frequências e decide, em cada uma, se há sinal.'},
    {d:3.6, pill:'L1', title:'Fase 2 — Sinal detectado', text:'Detectado o sinal, o processador de banda base extrai a sinalização L1 do Preamble.'},
    {d:3.6, pill:'LLS', title:'Fase 3 — Para o middleware', text:'O PLP com Link Layer Signaling e LLS vai ao middleware, que distribui aos módulos funcionais.'},
    {d:4.2, pill:'parsers', title:'Fase 4 — Quatro parsers', text:'LMT dá PLPID, endereço IP e porta; BAMT (0x90) dá os manifestos; TBSAT (0x91) dá as áreas; SLT (0x01) dá os serviços.'},
    {d:5.0, pill:'catálogo', title:'Fase 5 — Catálogo e mapa de canais', text:'Da SLT sai o que é essencial para produzir o Application Catalog, e a informação é gravada no mapa de canais. A varredura segue para a próxima frequência.'}
  ], render: function(i, f){
    var pos = scanPos(i, f), jj = i === 0 ? Math.floor(pos) : Math.round(pos);
    var k = i === 0 ? jj + T.ease(T.seg(pos - jj, 0, .35)) : pos;
    var x = T.lerp(FX(Math.floor(k)), FX(Math.min(N - 1, Math.floor(k) + 1)), k - Math.floor(k));
    $('mk7').setAttribute('transform', 'translate(' + x.toFixed(1) + ' 0)');
    var mk = $('mkl7'); mk.setAttribute('x', (x + 12).toFixed(1));
    var cur = Math.round(k);
    mk.textContent = SIG[cur] && (i > 0 || pos >= 2.999) ? 'sinal' : (i === 4 && f > .45 ? 'próxima' : 'sem sinal');
    var done = Math.floor(k + .001);
    for (var b = 0; b < N; b++){
      var checked = b < done || (b === done && (i > 0 || f > .9));
      boxes[b].style.fill = checked ? (SIG[b] ? 'var(--phy)' : 'var(--muted)') : 'none';
      boxes[b].style.stroke = SIG[b] && checked ? 'var(--phy)' : 'var(--muted)';
    }
    T.op($('s7a'), i > 1 ? 1 : i === 1 ? T.seg(f, .1, .5) : 0);
    T.op($('s7b'), i > 2 ? 1 : i === 2 ? T.seg(f, .1, .5) : 0);
    T.op($('s7c'), i > 3 ? 1 : i === 3 ? T.seg(f, .1, .5) : 0);
    T.op($('s7d'), i === 4 ? T.seg(f, .05, .3) : 0);
    for (var c = 0; c < catRows.length; c++) catRows[c].style.opacity = i === 4 ? T.seg(f, .15 + c * .06, .25 + c * .06) : 0;
    for (var mm = 0; mm < mapRows.length; mm++){
      var at = [3, 8, 11][mm], need = mm === 0 ? (i === 4 && f > .3) : (i === 4 && pos >= at);
      mapRows[mm].style.opacity = need ? 1 : 0;
    }
  }});
})();
</script>

### 3.3 Guia de serviço: ESG, EPG e ECG {#guia}

O modelo de dados do guia é o da ATSC A/332, com extensões brasileiras no Anexo D da NBR 25602. Ele é entregue em fragmentos SGDD e SGDU, e alimenta duas superfícies diferentes no receptor.

<div class="grid cards" markdown>

- **EPG — programação on-air**

    Título, horário, descrição, gênero e classificação do que está no ar e do que vem a seguir. Ao escolher um programa on-air, o EPG inicia a Bootstrap Application do serviço correspondente. O Service Type 4 (ESG) é associado exclusivamente ao Tipo 30.

- **ECG — conteúdo sob demanda**

    O guia de conteúdo, com vista intermediária antes da reprodução. É aqui que as extensões TV 3.0 importam.

- **As extensões brasileiras**

    Dentro de `tv30ContentExtension`, dois elementos mutuamente exclusivos: `initialMediaURL`, que aponta direto para um MPD ou um M3U8, e `broadcasterApplicationDeepLinkURL`, que abre uma Broadcaster Application num ponto específico. <span class="tv3-cite">25602, Anexo D, Tabela D.1</span>

</div>

## Parte 4 · Aplicações {#aplicacoes}

O centro da TV 3.0. Em TV 2.X a aplicação era um acessório do serviço de vídeo; aqui o serviço principal *é* uma aplicação — o Service Type 30 chama-se literalmente *Service Based on Bootstrap Application*. Esta parte percorre o modelo, as duas linguagens, como o pacote chega, quem manda iniciar, e o que a plataforma oferece de API.

### 4.1 O modelo: cinco peças {#modelo}

Há uma cadeia de substituição que vale a pena fixar antes de qualquer detalhe: **channel scan → Application Catalog → Bootstrap Application → Broadcaster Application → outra Broadcaster Application**. Em toda troca, o audiovisual não pode piscar.

<div class="grid cards" markdown>

- **Application Catalog**

    A grade de emissoras, produzida no channel scan a partir da SLT e da BAMT. Tela cheia exclusiva, alcançável pela função de lista de entradas da plataforma do fabricante. Dá acesso também ao EPG e ao ECG.

- **Bootstrap Application**

    A app padrão da emissora, declarada no manifesto BAM dentro da BAMT. É o que aparece ao entrar num serviço Tipo 30, e para onde o receptor volta como *failsafe* se uma Broadcaster Application terminar ou falhar.

- **Broadcaster Application**

    A aplicação que a emissora controla pela BALD. Substitui a Bootstrap e pode ser substituída por outra. É aqui que vive o interativo de verdade.

- **Persistent Media Player**

    Garante reprodução contínua e ininterrupta do conteúdo da emissora, inclusive durante a transição entre aplicações no mesmo contexto de serviço. Continuidade é requisito, não detalhe de implementação.

- **Access Panel**

    A gaveta do telespectador: aplicações disponíveis, preferências de acessibilidade e o Privacy Manager. É onde uma aplicação sinalizada com PRESENT espera para ser aberta.

</div>

### 4.2 Duas linguagens, um ciclo de vida {#linguagens}

O `@appType` da BALD, em valores no padrão `TV30-Ginga-…`, diz ao receptor qual máquina de apresentação acionar. Tudo o mais — validade, cache, códigos de controle, APIs — é idêntico nas duas.

<div class="grid cards" markdown>

- **TV 3.0 Ginga-NCL**

    NCL 4.0 com NCLua. Modelo declarativo de sincronismo, com comandos de edição em tempo de execução, base privada e variáveis persistentes. Caminho natural para quem vem do SBTVD e para conteúdo fortemente sincronizado com o audiovisual.

- **TV 3.0 Ginga-HTML5**

    HTML5, CSS e JavaScript empacotados. Caminho natural para quem vem da web, e o que permite reaproveitar time e ferramental de front-end. As APIs da plataforma são as mesmas, expostas por REST.

- **O que não muda**

    O Application Lifecycle Manager não distingue linguagem: lê a BALD, aplica `@controlCode`, respeita `@validFrom` e `@validUntil`, e trata o cache por `@appContextId`.

</div>

### 4.3 Como o aplicativo chega {#entrega}

Não existe download sob demanda pelo ar. O pacote é fatiado em objetos, cada um com o seu **TOI**, e repetido em carrossel não-tempo-real sobre ROUTE. Quem sintoniza no meio de uma volta espera a próxima passagem — essa latência de aquisição é a consequência prática que todo desenvolvedor precisa ter na cabeça. A alternativa é o ponto de entrada por banda larga, em que o mesmo pacote é buscado por HTTP.

<section class="figblock" id="fig5" aria-labelledby="fig5-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 5</span> NBR 25608</p>
<p class="figtitle" id="fig5-h">Como o aplicativo chega ao receptor</p>
<p class="figdesc">À esquerda, o mecanismo: o carrossel NRT girando sob o receptor. À direita, o mesmo instante no tempo, raia por raia. Quem sintoniza no meio da volta só fecha o pacote no mesmo ponto da volta seguinte.</p>
</header>
<figure data-fig>
<section class="f5grid">
<section class="left">
<svg class="plate" viewBox="70 0 740 740" role="img" aria-label="Carrossel NRT como prato giratório. Anel externo: doze objetos identificados por TOI. Anel do meio: o cache do receptor, que se preenche a partir da primeira BALD depois da sintonia. Anel interno: a BALD, repetida três vezes por volta. A cabeça de leitura do receptor fica fixa no topo.">
<defs>
<filter id="f5glow" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="f5hub" cx="50%" cy="50%" r="50%"><stop offset="0" style="stop-color:var(--hub1)"/><stop offset="1" style="stop-color:var(--hub2)"/></radialGradient>
</defs>
<g style="fill:none;stroke:var(--grid);stroke-width:1.5"><circle cx="440" cy="370" r="340"/><circle cx="440" cy="370" r="236"/><circle cx="440" cy="370" r="164"/><path d="M440 30V710M100 370H780"/></g>
<g id="f5trail" style="fill:var(--ink)">
<path d="M440.0 60.0A310 310 0 0 1 546.0 78.7L474.2 276.0A100 100 0 0 0 440.0 270.0Z" style="opacity:.12"/>
<path d="M546.0 78.7A310 310 0 0 1 639.3 132.5L504.3 293.4A100 100 0 0 0 474.2 276.0Z" style="opacity:.075"/>
<path d="M639.3 132.5A310 310 0 0 1 708.5 215.0L526.6 320.0A100 100 0 0 0 504.3 293.4Z" style="opacity:.045"/>
<path d="M708.5 215.0A310 310 0 0 1 745.3 316.2L538.5 352.6A100 100 0 0 0 526.6 320.0Z" style="opacity:.02"/>
</g>
<g style="fill:none;stroke:var(--tr);stroke-width:2"><circle cx="440" cy="370" r="248"/><circle cx="440" cy="370" r="302"/></g>
<g id="f5ring">
<circle cx="440" cy="370" r="307" style="fill:none;stroke:var(--tr);stroke-width:6;stroke-dasharray:2 12;opacity:.6"/>
<g id="f5sectors" style="fill:var(--app-bg);stroke:var(--app);stroke-width:2;stroke-linejoin:round">
<path d="M295.5 109.4A298 298 0 0 1 434.8 72.0L435.6 118.0A252 252 0 0 0 317.8 149.6Z"/>
<path d="M184.6 216.5A298 298 0 0 1 286.5 114.6L310.2 154.0A252 252 0 0 0 224.0 240.2Z"/>
<path d="M142.0 364.8A298 298 0 0 1 179.4 225.5L219.6 247.8A252 252 0 0 0 188.0 365.6Z"/>
<path d="M179.4 514.5A298 298 0 0 1 142.0 375.2L188.0 374.4A252 252 0 0 0 219.6 492.2Z"/>
<path d="M286.5 625.4A298 298 0 0 1 184.6 523.5L224.0 499.8A252 252 0 0 0 310.2 586.0Z"/>
<path d="M434.8 668.0A298 298 0 0 1 295.5 630.6L317.8 590.4A252 252 0 0 0 435.6 622.0Z"/>
<path d="M584.5 630.6A298 298 0 0 1 445.2 668.0L444.4 622.0A252 252 0 0 0 562.2 590.4Z"/>
<path d="M695.4 523.5A298 298 0 0 1 593.5 625.4L569.8 586.0A252 252 0 0 0 656.0 499.8Z"/>
<path d="M738.0 375.2A298 298 0 0 1 700.6 514.5L660.4 492.2A252 252 0 0 0 692.0 374.4Z"/>
<path d="M700.6 225.5A298 298 0 0 1 738.0 364.8L692.0 365.6A252 252 0 0 0 660.4 247.8Z"/>
<path d="M593.5 114.6A298 298 0 0 1 695.4 216.5L656.0 240.2A252 252 0 0 0 569.8 154.0Z"/>
<path d="M445.2 72.0A298 298 0 0 1 584.5 109.4L562.2 149.6A252 252 0 0 0 444.4 118.0Z"/>
</g>
<g class="svgtxt" id="f5toiLabels" style="font-size:26px;font-weight:500;fill:var(--app)" text-anchor="middle" dominant-baseline="central">
<text x="368.8" y="104.4">1</text><text x="245.5" y="175.5">2</text><text x="174.4" y="298.8">3</text><text x="174.4" y="441.2">4</text><text x="245.5" y="564.5">5</text><text x="368.8" y="635.6">6</text><text x="511.2" y="635.6">7</text><text x="634.5" y="564.5">8</text><text x="705.6" y="441.2">9</text><text x="705.6" y="298.8">10</text><text x="634.5" y="175.5">11</text><text x="511.2" y="104.4">12</text>
</g>
<g class="f5ringOp" style="fill:none;stroke:var(--app);stroke-width:1.5;stroke-dasharray:4 4">
<path d="M331.4 174.1A224 224 0 0 1 436.1 146.0L436.8 186.0A184 184 0 0 0 350.8 209.1Z"/>
<path d="M248.0 254.6A224 224 0 0 1 324.6 178.0L345.2 212.3A184 184 0 0 0 282.3 275.2Z"/>
<path d="M216.0 366.1A224 224 0 0 1 244.1 261.4L279.1 280.8A184 184 0 0 0 256.0 366.8Z"/>
<path d="M244.1 478.6A224 224 0 0 1 216.0 373.9L256.0 373.2A184 184 0 0 0 279.1 459.2Z"/>
<path d="M324.6 562.0A224 224 0 0 1 248.0 485.4L282.3 464.8A184 184 0 0 0 345.2 527.7Z"/>
<path d="M436.1 594.0A224 224 0 0 1 331.4 565.9L350.8 530.9A184 184 0 0 0 436.8 554.0Z"/>
<path d="M548.6 565.9A224 224 0 0 1 443.9 594.0L443.2 554.0A184 184 0 0 0 529.2 530.9Z"/>
<path d="M632.0 485.4A224 224 0 0 1 555.4 562.0L534.8 527.7A184 184 0 0 0 597.7 464.8Z"/>
<path d="M664.0 373.9A224 224 0 0 1 635.9 478.6L600.9 459.2A184 184 0 0 0 624.0 373.2Z"/>
<path d="M635.9 261.4A224 224 0 0 1 664.0 366.1L624.0 366.8A184 184 0 0 0 600.9 280.8Z"/>
<path d="M555.4 178.0A224 224 0 0 1 632.0 254.6L597.7 275.2A184 184 0 0 0 534.8 212.3Z"/>
<path d="M443.9 146.0A224 224 0 0 1 548.6 174.1L529.2 209.1A184 184 0 0 0 443.2 186.0Z"/>
</g>
<g id="f5cache" style="fill:var(--app);stroke:none"><path/><path/><path/><path/><path/><path/><path/><path/><path/><path/><path/><path/></g>
<g class="f5ringOp">
<circle cx="440" cy="370" r="139" style="fill:none;stroke:var(--sig);stroke-width:1.5;opacity:.5"/>
<g style="fill:var(--sig-bg);stroke:var(--sig);stroke-width:2">
<path d="M399.2 227.7A148 148 0 0 1 429.7 222.4L430.9 240.3A130 130 0 0 0 404.2 245.0Z"/>
<path d="M337.2 476.5A148 148 0 0 1 317.3 452.8L332.2 442.7A130 130 0 0 0 349.7 463.5Z"/>
<path d="M583.6 405.8A148 148 0 0 1 573.0 434.9L556.8 427.0A130 130 0 0 0 566.1 401.4Z"/>
</g>
<path d="M440 236V318" style="stroke:var(--ink);stroke-width:3"/>
</g>
<path id="f5baldHi" d="M583.6 405.8A148 148 0 0 1 573.0 434.9L556.8 427.0A130 130 0 0 0 566.1 401.4Z" style="fill:var(--sig);stroke:var(--sig);stroke-width:3" filter="url(#f5glow)"/>
<path id="f5tuneRay" d="M465.9 466.6L525.4 688.8" style="stroke:var(--ink);stroke-width:2.5;stroke-dasharray:8 6"/>
<path id="f5baldRay" d="M534.0 404.2L750.1 482.9" style="stroke:var(--sig);stroke-width:2.5;stroke-dasharray:8 6"/>
</g>
<path id="f5rem" d="M0 0" style="fill:var(--ink)"/>
<circle cx="440" cy="370" r="98" fill="url(#f5hub)" style="stroke:var(--line);stroke-width:1.5"/>
<g id="f5files" style="fill:var(--app-bg);stroke:var(--app);stroke-width:2;stroke-linejoin:round">
<path d="M373 335h32l12 12v46h-44Z"/><path d="M418 335h32l12 12v46h-44Z"/><path d="M463 335h32l12 12v46h-44Z"/>
<path d="M381 356h26M381 366h26M381 376h18M426 356h10M432 366h20M432 376h14M471 372l9-10 7 6 8-9 9 13" style="fill:none;stroke-width:1.5"/>
</g>
<g id="f5hubText" text-anchor="middle">
<text x="440" y="366" style="font-size:30px;font-weight:600;fill:var(--ink)">carrossel NRT</text>
<text class="svgtxt" x="440" y="400" style="font-size:26px;fill:var(--tr)">ROUTE</text>
</g>
<path id="f5headGlow" d="M440 46V190" style="stroke:var(--ink);stroke-width:4" filter="url(#f5glow)"/>
<path d="M440 46V190" style="stroke:var(--ink);stroke-width:2.5"/>
<path d="M426 26H454L440 46Z" style="fill:var(--ink)"/>
<text class="svgtxt" x="462" y="40" style="font-size:26px;fill:var(--ink)">receptor</text>
<text class="svgtxt" id="f5remText" x="80" y="40" style="font-size:26px;fill:var(--ink)"></text>
</svg>
<section class="legend">
<span><span style="width:18px;border-top:3px dashed var(--ink)"></span>raio da sintonia</span>
<span><span style="width:18px;border-top:3px dashed var(--sig)"></span>raio da 1ª BALD</span>
<span><span style="width:18px;height:10px;background:var(--app)"></span><span>cache <span id="f5cacheCount">0</span>/12</span></span>
<span><span style="width:18px;height:3px;background:var(--ink)"></span>arco: o que falta</span>
</section>
<aside class="bald" id="f5baldCard">
<span class="head"><span style="font-weight:500">BALD</span><span id="f5baldState">ainda não recebida</span></span>
<dl>
<dt>@appType</dt><dd class="v">TV30-Ginga-…</dd>
<dt>@appContextId</dt><dd>… nome do cache</dd>
<dt><span id="f5ccA">@controlCode</span></dt><dd class="v"><span id="f5ccB">AUTOSTART</span></dd>
<dt>@bbandEntryPointUrl</dt><dd>…</dd>
</dl>
</aside>
</section>
<section style="min-width:0">
<p class="hint">A linha do tempo rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Linha do tempo da Figura 5, role na horizontal">
<svg viewBox="0 0 880 510" style="--minw:560px" role="img" aria-label="Diagrama de tempo em cinco raias, revelado da esquerda para a direita conforme a animação: carrossel NRT com os objetos TOI 1 a 12 em três voltas; BALD repetida na SLS; cache do receptor subindo em degraus da primeira BALD após a sintonia até o pacote completo; requisição por banda larga; estado do receptor de Bootstrap Application para Broadcaster Application, com o Persistent Media Player contínuo.">
<defs>
<pattern id="f5grid" x="156" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M0 0V20" style="stroke:var(--grid);stroke-width:1"/></pattern>
<linearGradient id="f5cfill" x1="0" y1="1" x2="0" y2="0"><stop offset="0" style="stop-color:var(--app);stop-opacity:.06"/><stop offset="1" style="stop-color:var(--app);stop-opacity:.4"/></linearGradient>
<pattern id="f5hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V5" style="stroke:var(--hatch);stroke-width:2"/></pattern>
<clipPath id="f5rev"><rect id="f5revRect" x="0" y="0" width="880" height="510"/></clipPath>
</defs>
<rect x="156" y="56" width="720" height="400" fill="url(#f5grid)"/>
<g style="font-size:13px;font-weight:500" text-anchor="end">
<text x="140" y="84" style="fill:var(--tr)">ROUTE · NRT</text>
<text x="140" y="100" style="fill:var(--muted);font-size:12px;font-weight:400">objetos por TOI</text>
<text x="140" y="151" style="fill:var(--sig)">SLS · BALD</text>
<text x="140" y="236" style="fill:var(--app)">cache</text>
<text class="svgtxt" x="140" y="252" style="fill:var(--app);font-size:12px;font-weight:400">@appContextId</text>
<text x="140" y="334" style="fill:var(--tr)">banda larga</text>
<text x="140" y="350" style="fill:var(--muted);font-size:12px;font-weight:400">HTTP</text>
<text x="140" y="397" style="fill:var(--ink)">receptor</text>
<text x="140" y="430" style="fill:var(--muted);font-size:12px;font-weight:400">audiovisual</text>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)" text-anchor="end"><text x="152" y="194">12/12</text><text x="152" y="290">0</text></g>
<g style="stroke:var(--ink);stroke-width:1.5"><path d="M156 30V118M396 30V118M636 30V118M876 30V118"/></g>
<g style="stroke:var(--muted);stroke-width:1"><path d="M160 48H392M400 48H632M640 48H872"/></g>
<g class="svgtxt" style="font-size:13px;fill:var(--ink)" text-anchor="middle"><text x="276" y="42">volta n</text><text x="516" y="42">volta n+1</text><text x="756" y="42">volta n+2</text></g>
<path d="M156 60H876M156 112H876" style="stroke:var(--tr);stroke-width:1.5"/>
<g style="stroke:var(--line);stroke-width:1;stroke-dasharray:2 4"><path d="M156 190H876M156 215H876M156 240H876M156 265H876"/></g>
<path d="M156 290H876" style="stroke:var(--line);stroke-width:1"/>
<g clip-path="url(#f5rev)">
<g style="fill:none;stroke:var(--tr);stroke-width:1;opacity:.4">
<rect x="157" y="66" width="18" height="40"/><rect x="177" y="66" width="18" height="40"/><rect x="197" y="66" width="18" height="40"/><rect x="217" y="66" width="18" height="40"/><rect x="237" y="66" width="18" height="40"/><rect x="257" y="66" width="18" height="40"/>
</g>
<g style="fill:url(#f5hatch);stroke:var(--muted);stroke-width:1"><rect x="277" y="66" width="18" height="40"/><rect x="297" y="66" width="18" height="40"/><rect x="317" y="66" width="18" height="40"/></g>
<g style="fill:var(--app);stroke:var(--app);stroke-width:1">
<rect x="337" y="66" width="18" height="40"/><rect x="357" y="66" width="18" height="40"/><rect x="377" y="66" width="18" height="40"/>
<rect x="397" y="66" width="18" height="40"/><rect x="417" y="66" width="18" height="40"/><rect x="437" y="66" width="18" height="40"/><rect x="457" y="66" width="18" height="40"/><rect x="477" y="66" width="18" height="40"/><rect x="497" y="66" width="18" height="40"/><rect x="517" y="66" width="18" height="40"/><rect x="537" y="66" width="18" height="40"/><rect x="557" y="66" width="18" height="40"/>
</g>
<g style="fill:var(--app-bg);stroke:var(--app);stroke-width:1;opacity:.75">
<rect x="577" y="66" width="18" height="40"/><rect x="597" y="66" width="18" height="40"/><rect x="617" y="66" width="18" height="40"/>
<rect x="637" y="66" width="18" height="40"/><rect x="657" y="66" width="18" height="40"/><rect x="677" y="66" width="18" height="40"/><rect x="697" y="66" width="18" height="40"/><rect x="717" y="66" width="18" height="40"/><rect x="737" y="66" width="18" height="40"/><rect x="757" y="66" width="18" height="40"/><rect x="777" y="66" width="18" height="40"/><rect x="797" y="66" width="18" height="40"/><rect x="817" y="66" width="18" height="40"/><rect x="837" y="66" width="18" height="40"/><rect x="857" y="66" width="18" height="40"/>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)" text-anchor="middle">
<text x="166" y="90">1</text><text x="186" y="90">2</text><text x="206" y="90">3</text><text x="226" y="90">4</text><text x="246" y="90">5</text><text x="266" y="90">6</text>
<text x="286" y="90" style="fill:var(--ink)">7</text><text x="306" y="90" style="fill:var(--ink)">8</text><text x="326" y="90" style="fill:var(--ink)">9</text>
</g>
<g class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)" text-anchor="middle">
<text x="346" y="90">10</text><text x="366" y="90">11</text><text x="386" y="90">12</text>
<text x="406" y="90">1</text><text x="426" y="90">2</text><text x="446" y="90">3</text><text x="466" y="90">4</text><text x="486" y="90">5</text><text x="506" y="90">6</text><text x="526" y="90">7</text><text x="546" y="90">8</text><text x="566" y="90">9</text>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--app)" text-anchor="middle">
<text x="586" y="90">10</text><text x="606" y="90">11</text><text x="626" y="90">12</text>
<text x="646" y="90">1</text><text x="666" y="90">2</text><text x="686" y="90">3</text><text x="706" y="90">4</text><text x="726" y="90">5</text><text x="746" y="90">6</text><text x="766" y="90">7</text><text x="786" y="90">8</text><text x="806" y="90">9</text><text x="826" y="90">10</text><text x="846" y="90">11</text><text x="866" y="90">12</text>
</g>
<path d="M156 146H876" style="stroke:var(--sig);stroke-width:1;opacity:.5"/>
<g style="fill:var(--sig-bg);stroke:var(--sig);stroke-width:1;opacity:.4"><rect x="145.7" y="134" width="34" height="24"/><rect x="225.7" y="134" width="34" height="24"/></g>
<g style="fill:var(--sig-bg);stroke:var(--sig);stroke-width:1"><rect x="385.7" y="134" width="34" height="24"/><rect x="465.7" y="134" width="34" height="24"/><rect x="545.7" y="134" width="34" height="24"/><rect x="625.7" y="134" width="34" height="24"/><rect x="705.7" y="134" width="34" height="24"/><rect x="785.7" y="134" width="34" height="24"/></g>
<rect x="305.7" y="134" width="34" height="24" style="fill:var(--sig-bg);stroke:var(--sig);stroke-width:2.5" filter="url(#f5glow)"/>
<g class="svgtxt" style="font-size:12px;fill:var(--sig)" text-anchor="middle">
<text x="162.7" y="151" style="opacity:.5">BALD</text><text x="242.7" y="151" style="opacity:.5">BALD</text><text x="322.7" y="151" style="font-weight:500">BALD</text><text x="402.7" y="151">BALD</text><text x="482.7" y="151">BALD</text><text x="562.7" y="151">BALD</text><text x="642.7" y="151">BALD</text><text x="722.7" y="151">BALD</text><text x="802.7" y="151">BALD</text>
</g>
<path d="M336 290H356V281.7H376V273.3H396V265H416V256.7H436V248.3H456V240H476V231.7H496V223.3H516V215H536V206.7H556V198.3H576V190H876V290Z" fill="url(#f5cfill)"/>
<path d="M336 290H356V281.7H376V273.3H396V265H416V256.7H436V248.3H456V240H476V231.7H496V223.3H516V215H536V206.7H556V198.3H576V190H876" style="fill:none;stroke:var(--app);stroke-width:2.5"/>
<path d="M322.7 160V334" style="stroke:var(--sig);stroke-width:1;stroke-dasharray:2 3"/>
<text class="svgtxt" x="328" y="330" style="font-size:12px;fill:var(--tr)">GET @bbandEntryPointUrl</text>
<rect x="324" y="338" width="58.7" height="14" style="fill:var(--tr-bg);stroke:var(--tr);stroke-width:1.5;stroke-dasharray:6 3"/>
<path d="M382.7 338V378" style="stroke:var(--tr);stroke-width:1.5;stroke-dasharray:4 3"/>
<path d="M156 393H286" style="stroke:var(--line);stroke-width:1;stroke-dasharray:3 4"/>
<rect x="286" y="380" width="290" height="26" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1"/>
<text class="svgtxt" x="298" y="397" style="font-size:12px;fill:var(--app)">Bootstrap Application</text>
<rect x="576" y="380" width="300" height="26" style="fill:var(--app);stroke:var(--app);stroke-width:2.5" filter="url(#f5glow)"/>
<text class="svgtxt" x="586" y="397" style="font-size:12px;font-weight:500;fill:var(--on)">Broadcaster Application · AUTOSTART</text>
<path d="M286 426H876" style="stroke:var(--pmp);stroke-width:3"/>
<circle cx="576" cy="426" r="5" style="fill:var(--bg);stroke:var(--app);stroke-width:2"/>
<text class="svgtxt" x="600" y="446" style="font-size:12px;fill:var(--pmp)">Persistent Media Player · sem corte</text>
<path d="M286 22V470" style="stroke:var(--ink);stroke-width:1.5;stroke-dasharray:4 3"/>
<path d="M576 22V470" style="stroke:var(--app);stroke-width:2"/>
<g class="svgtxt" style="font-size:12px">
<text x="282" y="14" text-anchor="end" style="fill:var(--ink)">sintonia</text>
<text x="327" y="14" style="fill:var(--sig)">1ª BALD</text>
<text x="576" y="14" text-anchor="middle" style="fill:var(--app)">pacote completo</text>
</g>
<path d="M286 450V458H382.7V450" style="fill:none;stroke:var(--tr);stroke-width:1.5"/>
<text class="svgtxt" x="392" y="462" style="font-size:12px;fill:var(--tr)">pronta por banda larga</text>
<path d="M286 474V482H576V474" style="fill:none;stroke:var(--app);stroke-width:2.5"/>
<text x="431" y="502" text-anchor="middle" style="font-size:13px;fill:var(--app)">latência de aquisição pelo ar ≈ espera pela BALD + uma volta</text>
</g>
<text class="svgtxt" id="f5anno" x="160" y="214" style="font-size:12px;fill:var(--muted)">7, 8 e 9 passaram antes da 1ª BALD</text>
<path id="f5playhead" d="M156 22V470" style="stroke:var(--ink);stroke-width:2" filter="url(#f5glow)"/>
</svg>
</section>
</section>
</section>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25608, 10.1 e A.3.22 · NBR 25602, 4</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig5'), $ = function(id){ return document.getElementById('f5' + id); }, T = TV3;
  if (!S) return;
  var ring = $('ring'), sectors = $('sectors').children, labels = $('toiLabels').children, cache = $('cache').children, ringOps = S.querySelectorAll('.f5ringOp');
  var XY = []; for (var i = 0; i < labels.length; i++) XY.push(labels[i].getAttribute('x') + ' ' + labels[i].getAttribute('y'));
  function ez(f, a){ return (f < a ? (f*f)/(2*a) : f - a/2) / (1 - a/2); }
  function frac(k, t){ return k >= 10 ? T.clamp(t - (k - 1)) : T.clamp(t - (11 + k)); }
  function sec(r1, r2, a1, a2){ return T.sec(440, 370, r1, r2, a1, a2); }
  T.Fig({ root: S.querySelector('[data-fig]'), phases: [
    {d:2.2, pill:'pacote', title:'Fase 1 — Pacote na emissora', text:'A aplicação é um conjunto de arquivos — documentos, scripts e mídias — em TV 3.0 Ginga-NCL ou TV 3.0 Ginga-HTML5.'},
    {d:2.8, pill:'fatiamento', title:'Fase 2 — Fatiamento', text:'O pacote é fatiado em objetos, cada um com o seu Transport Object Identifier. É nessa granularidade que o ar transporta arquivo.'},
    {d:3.4, pill:'carrossel', title:'Fase 3 — Carrossel NRT', text:'Os objetos entram num carrossel não-tempo-real sobre ROUTE e são repetidos sem parar. Não há pedido: quem sintoniza no meio da volta espera a próxima passagem. A alternativa é o ponto de entrada por banda larga, em que o mesmo pacote é buscado por HTTP.'},
    {d:7.5, pill:'cache', title:'Fase 4 — Cache no receptor', text:'Os objetos são acumulados no cache identificado pelo @appContextId declarado na BALD. A DWD pode descrever as janelas de distribuição desses arquivos.'},
    {d:2.6, pill:'BALD', title:'Fase 5 — BALD chega', text:'É ela que decide o que fazer com o que está em cache: iniciar, apenas oferecer, armazenar ou remover. Sem BALD, há arquivos e não há aplicação.'},
    {d:4.5, pill:'em execução', title:'Fase 6 — Aplicação em execução', text:'Com @controlCode AUTOSTART, a Broadcaster Application substitui a Bootstrap. O Persistent Media Player garante que o audiovisual não seja interrompido na troca.'}
  ], render: function(i, f){
    var n = i + 1, t = 0;
    if (n === 3) t = 6.5 * ez(f, .3); else if (n === 4) t = 6.5 + 14.5 * f; else if (n === 5) t = 21; else if (n === 6) t = 21 + 15 * (1 - ez(1 - f, .3));
    var rot = 30 * t, count = 0;
    ring.setAttribute('transform', 'rotate(' + rot.toFixed(2) + ' 440 370)');
    for (var k = 1; k <= 12; k++){
      var o = n < 2 ? 0 : n === 2 ? T.clamp((f * 1.25 - (k - 1) / 12) * 5) : 1;
      T.op(sectors[k-1], o); T.op(labels[k-1], o);
      labels[k-1].setAttribute('transform', 'rotate(' + (-rot).toFixed(2) + ' ' + XY[k-1] + ')');
      var fr = frac(k, t), la = -(k - 1) * 30 - 1;
      cache[k-1].setAttribute('d', fr > .001 ? sec(184, 224, la - 28 * fr, la) : 'M0 0');
      if (fr >= 1) count++;
    }
    var ro = n >= 3 ? 1 : n === 2 ? T.clamp((f - .6) * 2.5) : 0;
    for (var r = 0; r < ringOps.length; r++) T.op(ringOps[r], ro);
    T.op($('files'), n === 1 ? T.clamp(f * 2) : n === 2 ? 1 - T.clamp(f * 1.6) : 0);
    T.op($('hubText'), n === 1 ? 0 : n === 2 ? T.clamp((f - .55) * 2.5) : 1);
    T.op($('trail'), n >= 3 ? 1 : 0);
    T.op($('tuneRay'), t >= 6.5 ? 1 : 0); T.op($('baldRay'), t >= 8.333 ? 1 : 0); T.op($('baldHi'), t >= 8.333 ? 1 : 0);
    T.op($('headGlow'), t >= 9 && t < 21 ? 1 : 0);
    $('rem').setAttribute('d', t >= 9 && t < 21 ? sec(312, 322, -Math.min(359.5, 30 * (21 - t)), 0) : 'M0 0');
    $('remText').textContent = t < 6.5 ? '' : t < 9 ? 'esperando a BALD' : t < 21 ? 'faltam ' + (12 - count) + ' objetos' : 'pacote completo';
    $('cacheCount').textContent = count;
    $('revRect').setAttribute('width', n <= 2 ? 156 : (157 + 20 * t).toFixed(1));
    $('playhead').setAttribute('d', 'M' + (156 + 20 * t).toFixed(1) + ' 22V470');
    T.op($('playhead'), n >= 3 && t < 36 ? 1 : 0);
    T.op($('anno'), t >= 9 ? 1 : 0);
    T.op($('baldCard'), t >= 8.333 ? 1 : .4);
    $('baldState').textContent = t < 8.333 ? 'ainda não recebida' : n >= 5 ? 'decide' : 'recebida';
    $('ccA').className = $('ccB').className = n >= 5 ? 'hl' : '';
  }});
})();
</script>

#### Os atributos da BALD

Broadcaster Application **Location** Description — o fragmento da SLS que declara cada aplicação, substituindo a HELD da ATSC. Sem ela há arquivos em cache e não há aplicação.

| Atributo | O que declara |
| :--- | :--- |
| `@appId` | Identidade da aplicação |
| `@appType` | A linguagem, em valores no padrão `TV30-Ginga-…` |
| `@bcastEntryPointUrl` | Ponto de entrada por broadcast — o pacote vem pelo carrossel NRT sobre ROUTE |
| `@bbandEntryPointUrl` | Ponto de entrada por banda larga — o mesmo pacote por HTTP |
| `@appContextId` | Identifica o Application Context Cache onde os arquivos são acumulados |
| `@controlCode` | O que fazer com a aplicação agora. **Ausente, assume AUTOSTART** |
| `@validFrom` · `@validUntil` | Janela de validade. Em teste, precisa cobrir a data real de execução |
| `@clearAppContextCacheDate` | Invalida o cache a partir de uma data |

<span class="tv3-cite">25608, 10.1 e A.3.22 · obrigatória no serviço Tipo 30 quando há aplicação, conforme as Tabelas A.1 e A.2 da 25602</span>

### 4.4 Ciclo de vida: quem manda {#ciclo}

A BALD é o controle remoto da emissora sobre a aplicação. Sete códigos, dois deles capazes de gravar na memória não volátil do receptor e um de apagar. Experimente no simulador: dispare um código e veja o estado mudar.

<section class="figblock" id="fig6" aria-labelledby="fig6-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 6</span> NBR 25608, 10.1</p>
<p class="figtitle" id="fig6-h">Ciclo de vida da aplicação</p>
<p class="figdesc">O autômato e a tela são uma peça só: cada <code>@controlCode</code> que chega na BALD acende uma aresta, muda o estado e mexe no que o telespectador vê. Embaixo, a BALD repetida no tempo — o ciclo de vida é dirigido por sinalização, não por evento isolado.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 6, role na horizontal">
<svg viewBox="0 0 1200 620" style="--minw:680px" role="img" aria-label="Autômato de estados: Application Catalog, Bootstrap Application em execução, Broadcaster Application em execução, disponível no Access Panel, e a memória não volátil. Arestas rotuladas com os códigos AUTOSTART, PRESENT, STORED_AUTOSTART, STORED_PRESENT, STORED_REMOVE, DESTROY e KILL. À direita, um aparelho de TV reflete o estado. Embaixo, a BALD repetida ao longo do tempo com o código de controle em vigor.">
<defs>
<filter id="g6" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<marker id="a6m" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--muted)"/></marker>
<marker id="a6s" orient="auto" markerWidth="8" markerHeight="8" refX="4" refY="4" overflow="visible"><path d="M0 0L8 4L0 8Z" style="fill:var(--sig)"/></marker>
<clipPath id="nvm6"><path d="M400 412a80 14 0 0 0 160 0V474a80 14 0 0 1-160 0Z"/></clipPath>
<linearGradient id="vid6" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--screen2)"/><stop offset="1" style="stop-color:var(--screen)"/></linearGradient>
</defs>
<g style="fill:none;stroke:var(--muted);stroke-width:1.5" marker-end="url(#a6m)">
<path id="e6cat" d="M250 90H334"/>
<path id="e6auto" d="M380 130V224"/>
<path id="e6back" d="M580 230V136"/>
<path id="e6present" d="M360 130V170H145V224"/>
<path id="e6panel" d="M250 270H334"/>
<path id="e6nvm" d="M480 310V392"/>
</g>
<g id="hl6" style="fill:none;stroke:var(--sig);stroke-width:3;stroke-dasharray:8 6" marker-end="url(#a6s)" filter="url(#g6)">
<path data-e="auto" d="M380 130V224"/><path data-e="back" d="M580 230V136"/><path data-e="present" d="M360 130V170H145V224"/><path data-e="nvm" d="M480 310V392"/>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--sig)">
<text x="388" y="170">AUTOSTART</text><text x="388" y="186">STORED_AUTOSTART</text>
<text x="588" y="176">DESTROY</text><text x="588" y="192">KILL</text>
<text x="190" y="162">PRESENT</text>
<text x="488" y="346">STORED_AUTOSTART</text><text x="488" y="362">STORED_PRESENT</text>
<text x="572" y="452">STORED_REMOVE</text>
</g>
<text x="256" y="262" style="font-size:12px;fill:var(--muted)">telespectador</text>
<g>
<rect x="40" y="50" width="210" height="80" style="fill:var(--panel);stroke:var(--app);stroke-width:1.5"/>
<g style="stroke:var(--app);stroke-width:1;opacity:.5"><path d="M52 92h28M52 104h28M52 116h28M88 92h48M88 104h40M88 116h52"/></g>
<text x="52" y="76" style="font-size:14px;font-weight:600;fill:var(--ink)">Application Catalog</text>
</g>
<rect id="n6boot" x="340" y="50" width="280" height="80" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5"/>
<text x="356" y="84" style="font-size:14px;font-weight:600;fill:var(--app)">Bootstrap Application</text><text x="356" y="104" style="font-size:13px;fill:var(--muted)">em execução</text>
<rect id="n6bcast" x="340" y="230" width="280" height="80" style="fill:var(--app);stroke:var(--app);stroke-width:2.5" filter="url(#g6)"/>
<rect x="340" y="230" width="280" height="80" style="fill:none;stroke:var(--app);stroke-width:1.5"/>
<text id="t6bcast" x="356" y="264" style="font-size:14px;font-weight:600;fill:var(--app)">Broadcaster Application</text><text id="t6bsub" x="356" y="284" style="font-size:13px;fill:var(--muted)">em execução</text>
<rect id="n6panel" x="40" y="230" width="210" height="80" style="fill:var(--app-bg);stroke:var(--app);stroke-width:1.5;stroke-dasharray:6 4"/>
<text x="52" y="264" style="font-size:14px;font-weight:600;fill:var(--ink)">disponível, não iniciada</text><text x="52" y="284" style="font-size:13px;fill:var(--muted)">esperando no Access Panel</text>
<g>
<path d="M400 412V474a80 14 0 0 0 160 0V412" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"/>
<g clip-path="url(#nvm6)"><rect id="nvmfill6" x="396" y="490" width="168" height="0" style="fill:var(--app)"/></g>
<ellipse cx="480" cy="412" rx="80" ry="14" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"/>
<path d="M400 412V474a80 14 0 0 0 160 0V412" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>
<text x="480" y="416" text-anchor="middle" style="font-size:12px;fill:var(--ink)">memória não volátil</text>
</g>
<rect x="700" y="50" width="460" height="280" style="fill:var(--off);stroke:var(--ink);stroke-width:2"/>
<rect x="712" y="62" width="436" height="256" fill="url(#vid6)"/>
<path d="M712 276l70-44 50 26 80-64 90 70 70-36 76 48V318H712Z" style="fill:var(--screen);opacity:.9"/>
<g id="tv6boot"><rect x="724" y="74" width="190" height="28" style="fill:var(--app-bg);stroke:var(--app)"/><text x="734" y="93" class="svgtxt" style="font-size:12px;fill:var(--app)">Bootstrap Application</text></g>
<g id="tv6bcast">
<rect x="932" y="74" width="204" height="196" style="fill:var(--app-bg);stroke:var(--app);stroke-width:2.5" filter="url(#g6)"/>
<text x="946" y="100" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--app)">Broadcaster Application</text>
<g style="fill:var(--app);opacity:.45"><rect x="946" y="116" width="170" height="44"/><rect x="946" y="172" width="120" height="10"/><rect x="946" y="190" width="150" height="10"/><rect x="946" y="208" width="100" height="10"/></g>
<text id="tv6fin" x="946" y="252" class="svgtxt" style="font-size:12px;fill:var(--ink)">finalizando…</text>
</g>
<g id="tv6kill" style="opacity:0"><path d="M932 74L1136 270M1136 74L932 270" style="stroke:var(--alr);stroke-width:3"/><text x="946" y="252" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--alr)">término imediato</text></g>
<g id="tv6panel"><rect x="712" y="278" width="436" height="40" style="fill:var(--panel);opacity:.92"/><text x="724" y="303" class="svgtxt" style="font-size:12px;fill:var(--muted)">Access Panel</text><rect x="840" y="284" width="140" height="28" style="fill:var(--app-bg);stroke:var(--app);stroke-dasharray:4 3"/><text x="850" y="303" class="svgtxt" style="font-size:12px;fill:var(--app)">disponível</text></g>
<path d="M900 330v18M960 330v18M870 348h120" style="stroke:var(--ink);stroke-width:2;fill:none"/>
<text id="st6" x="700" y="382" style="font-size:14px;fill:var(--ink)"></text>
<text id="nv6" x="700" y="404" class="svgtxt" style="font-size:12px;fill:var(--muted)"></text>
<text x="40" y="530" class="svgtxt" style="font-size:12px;fill:var(--muted)">BALD REPETIDA · @controlCode</text>
<path d="M40 572H1160" style="stroke:var(--sig);stroke-width:1;opacity:.6"/>
<g id="tk6" style="stroke:var(--sig);stroke-width:1.5;opacity:.6"></g>
<g id="tags6"></g>
<path id="ph6" d="M40 540V600" style="stroke:var(--ink);stroke-width:2" filter="url(#g6)"/>
</svg>
</section>
<nav class="sim" role="group" aria-label="Simulador: disparar um código de controle"><span class="lbl">disparar @controlCode:</span></nav>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25608, 10.1 e A.3.22</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig6'), $ = function(id){ return document.getElementById(id); }, T = TV3, NS = 'http://www.w3.org/2000/svg';
  if (!S) return;
  var CODES = ['AUTOSTART','DESTROY','PRESENT','STORED_AUTOSTART','STORED_REMOVE','KILL','STORED_PRESENT'];
  var DESC = {
    AUTOSTART:'Baixa e inicia assim que recebida, substituindo a Bootstrap.',
    PRESENT:'Fica disponível, não inicia. Aparece no Access Panel e espera o telespectador.',
    STORED_AUTOSTART:'Como AUTOSTART, mas gravada na memória não volátil e passa a iniciar a partir dela.',
    STORED_PRESENT:'Carregada e armazenada, mas não inicia sozinha.',
    STORED_REMOVE:'Removida da memória não volátil. Não afeta o que está em execução.',
    DESTROY:'Término controlado: a aplicação finaliza, libera recursos, volta à Bootstrap.',
    KILL:'Término imediato, sem finalização. Nada é salvo pela aplicação.'
  };
  var EDGE = { AUTOSTART:['auto'], STORED_AUTOSTART:['auto','nvm'], DESTROY:['back'], KILL:['back'], PRESENT:['present'], STORED_PRESENT:['nvm'], STORED_REMOVE:[] };
  var INIT = { run:'boot', panel:false, nvm:false };
  function apply(s, c){
    var n = { run:s.run, panel:s.panel, nvm:s.nvm };
    if (c === 'AUTOSTART'){ n.run = 'bcast'; n.panel = false; }
    else if (c === 'STORED_AUTOSTART'){ n.run = 'bcast'; n.panel = false; n.nvm = true; }
    else if (c === 'PRESENT'){ if (n.run !== 'bcast') n.panel = true; }
    else if (c === 'STORED_PRESENT'){ n.nvm = true; }
    else if (c === 'STORED_REMOVE'){ n.nvm = false; }
    else if (c === 'DESTROY' || c === 'KILL'){ n.run = 'boot'; }
    return n;
  }
  var X0 = 120, DX = 150, tags = $('tags6'), tk = $('tk6'), tk_d = '';
  for (var x = 60; x < 1160; x += 25) tk_d += 'M' + x + ' 566V578';
  var tkp = document.createElementNS(NS, 'path'); tkp.setAttribute('d', tk_d); tk.appendChild(tkp);
  CODES.forEach(function(c, i){
    var g = document.createElementNS(NS, 'g'), w = c.length * 7.4 + 16, cx = X0 + i * DX + DX / 2;
    g.innerHTML = '<rect x="' + (cx - w / 2) + '" y="546" width="' + w + '" height="24" style="fill:var(--sig-bg);stroke:var(--sig);stroke-width:1.5"/><text x="' + cx + '" y="563" text-anchor="middle" class="svgtxt" style="font-size:12px;fill:var(--sig)">' + c + '</text>';
    g.style.opacity = .35; tags.appendChild(g);
  });
  var hl = {}; Array.prototype.forEach.call($('hl6').children, function(p){ hl[p.dataset.e] = p; });
  var last = INIT;
  function draw(s0, code, p, u){
    var s1 = apply(s0, code), e = T.ease(p);
    var b0 = s0.run === 'bcast' ? 1 : 0, b1 = s1.run === 'bcast' ? 1 : 0, bc;
    if (code === 'KILL') bc = p > .08 ? b1 : b0; else bc = T.lerp(b0, b1, e);
    T.op($('tv6bcast'), code === 'KILL' && p > .08 ? 0 : bc);
    T.op($('tv6fin'), code === 'DESTROY' && p > 0 && p < 1 ? 1 : 0);
    T.op($('tv6kill'), code === 'KILL' && p > .08 ? 1 - T.seg(p, .5, 1) : 0);
    T.op($('tv6boot'), 1 - bc);
    T.op($('tv6panel'), T.lerp(s0.panel ? 1 : 0, s1.panel ? 1 : 0, e));
    T.op($('n6bcast'), bc); $('t6bcast').style.fill = bc > .5 ? 'var(--on)' : 'var(--app)'; $('t6bsub').style.fill = bc > .5 ? 'var(--on)' : 'var(--muted)';
    T.op($('n6boot'), .35 + .65 * (1 - bc)); T.op($('n6panel'), .35 + .65 * T.lerp(s0.panel ? 1 : 0, s1.panel ? 1 : 0, e));
    var lv = T.lerp(s0.nvm ? 1 : 0, s1.nvm ? 1 : 0, e), h = 76 * lv;
    $('nvmfill6').setAttribute('y', (490 - h).toFixed(1)); $('nvmfill6').setAttribute('height', h.toFixed(1));
    for (var k in hl){ var on = EDGE[code].indexOf(k) >= 0; hl[k].style.opacity = on ? 1 : 0; hl[k].style.strokeDashoffset = T.reduced() ? 0 : (-u * 30).toFixed(1); }
    $('st6').textContent = 'em execução: ' + (s1.run === 'bcast' ? 'Broadcaster Application' : 'Bootstrap Application') + (s1.panel ? ' · uma aplicação no Access Panel' : '');
    $('nv6').textContent = 'memória não volátil: ' + (s1.nvm ? 'aplicação armazenada' : 'vazia');
    last = p >= 1 ? s1 : last;
    return s1;
  }
  var stateAt = [INIT]; for (var i = 0; i < CODES.length; i++) stateAt.push(apply(stateAt[i], CODES[i]));
  var manual = null, mraf = 0, tagEls = tags.children;
  var fig = T.Fig({ root: S.querySelector('[data-fig]'), phases: CODES.map(function(c){ return { d: 3.2, pill: c, title: c, text: DESC[c] }; }),
    onUser: function(){ manual = null; cancelAnimationFrame(mraf); },
    render: function(i, f, u){
      if (manual) return;
      draw(stateAt[i], CODES[i], T.seg(f, .12, .6), u);
      for (var t = 0; t < tagEls.length; t++) tagEls[t].style.opacity = t === i ? 1 : t < i ? .6 : .3;
      T.op($('ph6'), 1); $('ph6').setAttribute('d', 'M' + (X0 + (i + f) * DX).toFixed(1) + ' 540V600');
    }});
  var sim = S.querySelector('.sim');
  CODES.slice().sort().forEach(function(c){
    var b = document.createElement('button'); b.type = 'button'; b.textContent = c;
    b.addEventListener('click', function(){
      fig.pause(); cancelAnimationFrame(mraf);
      var s0 = last;
      manual = { s0: s0, code: c, t0: null };
      S.querySelector('[data-cap-title]').textContent = c + ' (simulador)';
      S.querySelector('[data-cap-text]').textContent = DESC[c];
      for (var t = 0; t < tagEls.length; t++) tagEls[t].style.opacity = CODES[t] === c ? 1 : .3;
      T.op($('ph6'), 0);
      var step = function(ts){
        if (!manual) return;
        if (manual.t0 == null) manual.t0 = ts;
        var p = T.reduced() ? 1 : T.clamp((ts - manual.t0) / 1400);
        draw(manual.s0, manual.code, p, ts / 1000);
        if (p < 1) mraf = requestAnimationFrame(step);
      };
      mraf = requestAnimationFrame(step);
    });
    sim.appendChild(b);
  });
})();
</script>

| Código | Efeito | Memória |
| :--- | :--- | :--- |
| <span class="c-sig">`AUTOSTART`</span> | Baixa e inicia assim que recebida, substituindo a Bootstrap | — |
| <span class="c-sig">`PRESENT`</span> | Fica disponível e não inicia. Aparece no Access Panel e espera o telespectador | — |
| <span class="c-sig">`STORED_AUTOSTART`</span> | Como AUTOSTART, mas passa a iniciar a partir da memória | grava |
| <span class="c-sig">`STORED_PRESENT`</span> | Carregada e armazenada, mas não inicia sozinha | grava |
| <span class="c-sig">`STORED_REMOVE`</span> | Remove da memória. Não afeta o que está em execução | apaga |
| <span class="c-sig">`DESTROY`</span> | Término controlado: finaliza, libera recursos, volta à Bootstrap | — |
| <span class="c-sig">`KILL`</span> | Término imediato, sem finalização. Nada é salvo pela aplicação | — |

<span class="tv3-cite">25608, 10.1 · equivale, grosso modo, ao AIT da TV 2.X, mas com persistência e cache explícitos</span>

### 4.5 TV 3.0 WebServices: a superfície de API {#webservices}

Uma API REST local, especificada no Anexo C da NBR 25608 e detalhada na NBR 15606-11. A regra prática: quase tudo o que a aplicação precisa saber sobre o mundo externo chega por aqui, não por parsing. É o que torna a camada de aplicações testável de forma relativamente isolada do transporte.

<div class="grid cards" markdown>

- **Sinalização e guia**

    Qualquer tabela da LLS ou fragmento da SLS, já processados. Guia de serviço do canal atual e dos demais. Notificações de evento por registro.

- **Alerta de emergência**

    Assinatura de notificações de AEAT, com o parâmetro `showEmergencyAlert` definindo se a aplicação assume a exibição no lugar da app nativa.

- **Plataforma**

    Capacidades e atributos da plataforma do receptor, incluindo versão da PRP e da implementação da AoP; parâmetros da camada física; geolocalização, com `tbsat` entre as fontes ao lado de `gnss`, `wifi`, `mobileNetwork`, `zip` e `ip`.

- **Estado e persistência**

    Cache de arquivos da aplicação, armazenamento persistente e perfil do telespectador — este último sob o consentimento declarado na PRRD.

- **Mídia**

    Controle do Persistent Media Player, seleção de componentes, e a propriedade `urn:sbtvd:dash:component-tag` que permite controlar um mesmo stream através de `Periods` diferentes no MPD.

- **Além da tela**

    Medição de audiência, interação multimodal, dispositivos remotos e aplicações companion, efeitos sensoriais e conteúdo 360°.

</div>

### 4.6 Middleware: onde a sua app roda {#middleware}

A plataforma do receptor (RP) tem duas metades. A **AoP** é normatizada e a sua aplicação pode contar com ela. A **PRP** — *Proprietary* Receiver Platform, não *Primary* — é do fabricante: tela inicial, menus, sintonizador. Você só alcança a PRP pelas capacidades e atributos que a plataforma expõe. Clique num componente.

<section class="mw">
<section class="mwband aop"><span class="bl">TV 3.0 AoP · APPLICATION-ORIENTED PLATFORM</span>
<section class="mwrow" style="margin-bottom:8px">
<button type="button" data-mw="bootstrap" aria-pressed="false">Bootstrap Application<small>a app padrão da emissora</small></button>
<button type="button" data-mw="bcastapp" aria-pressed="false">Broadcaster Application<small>Ginga-NCL ou Ginga-HTML5</small></button>
<button type="button" data-mw="catalog" aria-pressed="false">Application Catalog<small>a grade de emissoras</small></button>
<button type="button" data-mw="access" aria-pressed="false">Access Panel<small>painel do telespectador</small></button>
</section>
<section class="mwrow" style="margin-bottom:8px">
<button type="button" data-mw="pe" aria-pressed="false">Presentation Engine<small>apresenta a app declarativa</small></button>
<button type="button" data-mw="alm" aria-pressed="false">Application Lifecycle Manager<small>lê a BALD, decide o que roda</small></button>
<button type="button" data-mw="pmp" aria-pressed="false">Persistent Media Player<small>o vídeo não pisca na troca</small></button>
</section>
<section class="mwrow">
<button type="button" data-mw="ws" aria-pressed="false">TV 3.0 WebServices<small>REST local, Anexo C</small></button>
<button type="button" data-mw="sigman" aria-pressed="false">Signaling Manager<small>parsers de LLS e SLS</small></button>
<button type="button" data-mw="privacy" aria-pressed="false">Privacy Manager<small>consentimento e registros</small></button>
<button type="button" data-mw="amm" aria-pressed="false">Audience Measurement<small>coleta sob solicitação</small></button>
</section>
</section>
<section class="mwband prp"><span class="bl">PRP · PROPRIETARY RECEIVER PLATFORM</span>
<section class="mwrow">
<button type="button" data-mw="home" aria-pressed="false">Tela inicial e menus<small>fora do escopo da AoP</small></button>
<button type="button" data-mw="tuner" aria-pressed="false">Sintonizador e demodulador<small>até quatro processadores de PLP</small></button>
<button type="button" data-mw="prpsys" aria-pressed="false">Ajustes do fabricante<small>rede, idioma, atualização</small></button>
</section>
</section>
<section class="mwband rf"><span class="bl">RF</span>
<p style="margin:0;font-size:13.5px;line-height:19px;color:var(--muted)">Até 64 PLPs no sinal, no máximo quatro por serviço — daí a recomendação de quatro processadores de PLP no receptor.</p>
</section>
</section>

<aside id="mwDetail" aria-live="polite"></aside>

### 4.7 Receptores e perfis {#receptores}

Três tipos e nove perfis. É contra o perfil que o fabricante se certifica, e é ele que define o que a sua aplicação pode assumir como disponível no aparelho.

<div class="grid cards" markdown>

- **BDR**

    Built-in display receiver: tela integrada, sem saída de vídeo. TVs, receptores portáteis e automotivos.

- **STB**

    Set-top box: precisa de display externo, logo provê interfaces de saída de áudio e vídeo.

- **GTW**

    Gateway: recebe TV 3.0 e serve por Wi-Fi a aparelhos que não recebem, via app cliente de streaming.

- **Nove perfis**

    Cada tipo em três patamares: **4K@60fps**, **4K@120fps** e **8K@60fps**, nos Anexos A a I da 25609.

- **Decodificação exigida**

    Vídeo: VVC, HEVC, AVC, LCEVC. HDR: HDR10, SL-HDR1, SL-HDR2, HLG, SMPTE ST 2094-10 e 2094-40. Volumétrico: V3C. Áudio: MPEG-H, AAC, AC-4, E-AC-3 JOC. Legendas: IMSC1 e WebVTT.

- **Os 5 s de restart**

    Mudou Bootstrap, L1-Basic ou L1-Detail, o receptor deve voltar a demodular em até 5 s — com exceções, entre elas `ea_wake_up_1` e `ea_wake_up_2`, que não podem forçar restart. Sem essa exceção, o wake-up de emergência não funcionaria.

- **Também na 25609**

    A norma de receptores normatiza TV 3.0 Ginga-NCL, Ginga-HTML5, WebServices e NCLua na seção 13, além da recepção de RF, sensibilidade e seletividade na seção 15.

</div>

## Parte 5 · Serviços transversais {#servicos}

Três assuntos que atravessam todas as camadas e que, em TV 2.X, ou não existiam ou eram tratados por fora: emergência, acessibilidade e dados pessoais. Nos três, a aplicação tem papel ativo — e responsabilidade.

### 5.1 Alerta de emergência {#alerta}

A autoridade publica em CAP; a emissora converte para AEA-MF e transmite na AEAT, dentro da LLS. O receptor pode estar em standby — o campo de wake-up no Bootstrap resolve isso. Quem desenha a tela, no fim, pode ser a sua aplicação.

<section class="figblock" id="fig8" aria-labelledby="fig8-h">
<header class="fig-head">
<p class="figlabel"><span>FIGURA 8</span> NBR 25607</p>
<p class="figtitle" id="fig8-h">Alerta de emergência</p>
<p class="figdesc">A mensagem sai das autoridades como CAP, vira AEA-MF dentro da AEAT, e acorda um receptor que estava desligado — mas só aquele cuja localização, tirada da própria TBSAT, cai dentro da área do alerta.</p>
</header>
<figure data-fig>
<p class="hint">A figura rola na horizontal.</p>
<section class="scroll" tabindex="0" aria-label="Figura 8, role na horizontal">
<svg viewBox="0 0 1200 660" style="--minw:680px" role="img" aria-label="Fluxo do alerta: autoridades publicam em Common Alerting Protocol; a emissora converte para AEA-MF, monta a AEAT na LLS e o campo de wake-up, e transmite por ROUTE. No mapa de cobertura, quatro áreas de melhor servidor da TBSAT; o polígono do alerta cobre duas delas. O receptor dentro dessa área sai do standby e exibe o alerta; o receptor fora dela continua desligado.">
<defs>
<filter id="g8" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1700" height="1200"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="scr8"><rect x="612" y="212" width="546" height="306"/></clipPath>
<clipPath id="all8"><rect x="0" y="0" width="1200" height="660"/></clipPath>
<linearGradient id="vid8" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--screen2)"/><stop offset="1" style="stop-color:var(--screen)"/></linearGradient>
<pattern id="h8" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V7" style="stroke:var(--alr);stroke-width:1.5;opacity:.35"/></pattern>
</defs>
<g id="w8" clip-path="url(#all8)" style="fill:none;stroke:var(--phy);stroke-width:2">
<circle cx="690" cy="44" r="10"/><circle cx="690" cy="44" r="10"/><circle cx="690" cy="44" r="10"/><circle cx="690" cy="44" r="10"/><circle cx="690" cy="44" r="10"/>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--muted)"><text x="40" y="22">ORIGEM</text><text x="300" y="22">EMISSORA</text><text x="640" y="22">TRANSMISSÃO</text></g>
<path d="M62 40h54l16 16v76H62Z" style="fill:var(--alr-bg);stroke:var(--alr);stroke-width:2;stroke-linejoin:round"/>
<path d="M116 40v16h16" style="fill:none;stroke:var(--alr);stroke-width:2"/>
<text x="72" y="66" class="svgtxt" style="font-size:14px;font-weight:500;fill:var(--alr)">CAP</text>
<path d="M72 80h48M72 92h40M72 104h48M72 116h28" style="stroke:var(--alr);stroke-width:1.5;opacity:.6"/>
<text x="62" y="152" style="font-size:13px;fill:var(--ink)">autoridades</text>
<path d="M140 86H296" style="stroke:var(--muted);stroke-width:1.5"/><path d="M290 81l8 5-8 5" style="fill:none;stroke:var(--muted);stroke-width:1.5"/>
<text x="150" y="76" class="svgtxt" style="font-size:12px;fill:var(--muted)">XML · CAP</text>
<rect x="300" y="34" width="230" height="104" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.5"/>
<path d="M300 34v104M530 34v104" style="stroke:var(--ink);stroke-width:5"/>
<g style="stroke:var(--line);stroke-width:1"><path d="M304 68H526M304 102H526"/></g>
<circle id="led8a" cx="318" cy="51" r="4" style="fill:var(--alr)"/><circle id="led8b" cx="318" cy="85" r="4" style="fill:var(--sig)"/><circle id="led8c" cx="318" cy="119" r="4" style="fill:var(--app)"/>
<g class="svgtxt" style="font-size:12px">
<text x="332" y="55" style="fill:var(--alr)">CAP → AEA-MF</text>
<text x="332" y="89" style="fill:var(--sig)">AEAT · LLS + wake-up</text>
<text x="332" y="123" style="fill:var(--app)">mídias por NRT</text>
</g>
<text x="300" y="158" style="font-size:13px;fill:var(--ink)">módulo de sinalização</text>
<path d="M530 86H636" style="stroke:var(--tr);stroke-width:6"/><path d="M630 78l10 8-10 8" style="fill:none;stroke:var(--tr);stroke-width:2"/>
<text x="548" y="76" class="svgtxt" style="font-size:12px;fill:var(--tr)">ROUTE</text>
<g style="fill:none;stroke:var(--ink);stroke-width:1.5">
<path d="M690 44L664 150M690 44L716 150M670 126H710M674 104H706M679 82H701M684 62H696M670 126L706 104M674 104L701 82M679 82L696 62"/>
<path d="M690 44V30"/>
</g>
<circle cx="690" cy="28" r="4" style="fill:var(--phy)"/>
<g id="tok8">
<g id="tok8cap"><path d="M-14 -18h20l8 8v28h-28Z" style="fill:var(--alr);stroke:var(--alr);stroke-width:1.5"/></g>
<g id="tok8aeat" style="opacity:0"><path d="M-6 -14H34V14H-6L-16 4V-4Z" style="fill:var(--sig);stroke:var(--sig)"/><circle cx="-6" cy="0" r="3" style="fill:var(--panel)"/></g>
</g>
<text x="40" y="186" class="svgtxt" style="font-size:12px;fill:var(--muted)">ÁREA DE COBERTURA · TBSAT</text>
<rect x="40" y="200" width="480" height="420" style="fill:var(--panel);stroke:var(--line)"/>
<g style="stroke:var(--phy);stroke-width:1.5;stroke-linejoin:round">
<path id="p8a" d="M40 200H300L280 380L150 430L40 400Z" style="fill:var(--phy-bg)"/>
<path id="p8b" d="M300 200H520V360L400 410L280 380Z" style="fill:var(--phy-bg)"/>
<path id="p8c" d="M40 400L150 430L280 380L300 520L200 620H40Z" style="fill:var(--phy-bg)"/>
<path id="p8d" d="M280 380L400 410L520 360V620H200L300 520Z" style="fill:var(--phy-bg)"/>
</g>
<g id="p8lit" style="fill:url(#h8);stroke:var(--alr);stroke-width:2.5;stroke-linejoin:round">
<path d="M300 200H520V360L400 410L280 380Z"/><path d="M280 380L400 410L520 360V620H200L300 520Z"/>
</g>
<path id="alr8poly" d="M370 238L508 228L512 576L340 486Z" style="fill:none;stroke:var(--alr);stroke-width:2.5;stroke-dasharray:8 5"/>
<text id="alr8lbl" x="352" y="600" class="svgtxt" style="font-size:12px;fill:var(--alr)">Location@type polygon</text>
<g style="fill:var(--phy)">
<path d="M160 290l-6 16h12Z"/><path d="M410 280l-6 16h12Z"/><path d="M150 500l-6 16h12Z"/><path d="M400 500l-6 16h12Z"/>
</g>
<g class="svgtxt" style="font-size:12px;fill:var(--phy)">
<text x="172" y="304">txid_address 17</text><text x="330" y="322">txid_address 18</text><text x="60" y="540">txid_address 19</text><text x="332" y="540">txid_address 20</text>
</g>
<g>
<rect x="98" y="336" width="30" height="20" style="fill:var(--off);stroke:var(--ink);stroke-width:1.5"/><path d="M108 356v5h10v-5" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>
<text x="136" y="351" style="font-size:12px;fill:var(--muted)">fora da área</text>
<rect x="432" y="436" width="30" height="20" style="fill:var(--off);stroke:var(--ink);stroke-width:1.5"/>
<rect id="rx8on" x="433" y="437" width="28" height="18" style="fill:var(--alr)" filter="url(#g8)"/>
<path d="M442 456v5h10v-5" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>
<text x="404" y="476" style="font-size:12px;fill:var(--ink)">este receptor</text>
</g>
<rect x="600" y="200" width="570" height="330" style="fill:var(--off);stroke:var(--ink);stroke-width:2"/>
<rect x="612" y="212" width="546" height="306" style="fill:var(--off)"/>
<g clip-path="url(#scr8)">
<rect id="pw8" x="885" y="364" width="0" height="2" style="fill:#ffffff"/>
<g id="vid8g">
<rect x="612" y="212" width="546" height="306" fill="url(#vid8)"/>
<path d="M612 470l90-60 60 34 90-80 120 90 80-40 106 70V518H612Z" style="fill:var(--screen);opacity:.9"/>
</g>
<g id="ban8">
<rect x="612" y="372" width="546" height="146" style="fill:var(--alr-bg);stroke:var(--alr);stroke-width:2"/>
<rect x="612" y="372" width="546" height="6" style="fill:var(--alr)"/>
<rect x="628" y="392" width="62" height="22" style="fill:var(--alr)"/><text x="634" y="408" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)">AEA-MF</text>
<rect x="698" y="392" width="40" height="22" style="fill:none;stroke:var(--alr);stroke-width:1.5"/><text x="706" y="408" class="svgtxt" style="font-size:12px;fill:var(--alr)">Met</text>
<g style="fill:var(--alr);opacity:.55"><rect x="628" y="428" width="360" height="10"/><rect x="628" y="448" width="320" height="10"/><rect x="628" y="468" width="250" height="10"/></g>
<rect x="1020" y="392" width="120" height="96" style="fill:var(--phy-bg);stroke:var(--phy);stroke-width:1.5"/>
<path d="M1020 440L1070 430L1090 392M1070 430L1100 488" style="fill:none;stroke:var(--phy);stroke-width:1"/>
<path d="M1060 416L1132 410L1134 480L1048 462Z" style="fill:none;stroke:var(--alr);stroke-width:2;stroke-dasharray:5 3"/>
<circle cx="1102" cy="452" r="5" style="fill:var(--alr)"/>
<text x="1020" y="504" class="svgtxt" style="font-size:12px;fill:var(--muted)">via TBSAT</text>
<g id="own8n"><rect x="900" y="388" width="104" height="22" style="fill:var(--panel);stroke:var(--line)"/><text x="908" y="403" class="svgtxt" style="font-size:12px;fill:var(--ink)">app nativa</text></g>
<g id="own8b" style="opacity:0"><rect x="830" y="388" width="174" height="22" style="fill:var(--app);stroke:var(--app)"/><text x="838" y="403" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)">Broadcaster Application</text></g>
</g>
</g>
<circle id="led8tv" cx="1150" cy="524" r="3" style="fill:var(--alr)"/>
<path d="M860 530v26M910 530v26M820 556H950" style="stroke:var(--ink);stroke-width:2;fill:none"/>
<path d="M1140 200L1168 168M1140 200L1112 168" style="stroke:var(--ink);stroke-width:1.5;fill:none"/>
<text id="st8" x="600" y="586" style="font-size:14px;fill:var(--ink)">standby · sintonizador monitorando o sinal</text>
<g id="sea8" style="opacity:0">
<rect x="600" y="602" width="300" height="26" style="fill:var(--app-bg);stroke:var(--app)"/>
<text x="610" y="620" class="svgtxt" style="font-size:12px;fill:var(--app)">showEmergencyAlert = true</text>
<text x="912" y="620" style="font-size:13px;fill:var(--muted)">a nativa não exibe; os eventos seguem chegando</text>
</g>
<g id="wk8" style="opacity:0"><rect x="1078" y="140" width="72" height="22" style="fill:var(--alr)"/><text x="1085" y="155" class="svgtxt" style="font-size:12px;font-weight:500;fill:var(--on)">wake-up</text></g>
</svg>
</section>
<nav data-controls class="controls"></nav>
<figcaption class="caption"><p aria-live="polite"><b data-cap-title></b>. <span data-cap-text></span></p><span class="tv3-cite">NBR 25607, Anexo A e Tabela A.1 · NBR 25602, 8.3</span></figcaption>
</figure>
</section>

<script>
(function(){
  var S = document.getElementById('fig8'), $ = function(id){ return document.getElementById(id); }, T = TV3;
  if (!S) return;
  var waves = $('w8').children, tok = $('tok8');
  T.Fig({ root: S.querySelector('[data-fig]'), phases: [
    {d:3.0, pill:'origem', title:'Fase 1 — Origem', text:'As autoridades de segurança e defesa publicam a ocorrência, normalmente como XML em Common Alerting Protocol.'},
    {d:3.6, pill:'emissora', title:'Fase 2 — Emissora', text:'A emissora converte para AEA-MF se for relevante à sua área de cobertura. O módulo de sinalização monta a AEAT, o campo de wake-up, e disponibiliza as mídias por NRT.'},
    {d:4.0, pill:'transmissão', title:'Fase 3 — Transmissão', text:'Tudo é multiplexado e transmitido por ROUTE. O receptor em standby mantém o sintonizador monitorando o sinal à procura do wake-up.'},
    {d:4.4, pill:'receptor acorda', title:'Fase 4 — Receptor acorda', text:'Chegando alerta relevante para a localização, o receptor é ligado e a mensagem é apresentada. A localização pode vir da TBSAT, direto do sinal OTA, sem GPS e sem internet.'},
    {d:4.2, pill:'quem apresenta', title:'Fase 5 — Quem apresenta', text:'Quem apresenta pode ser a aplicação nativa ou uma Broadcaster Application registrada que tenha posto showEmergencyAlert como true — nesse caso a nativa não exibe. Os eventos continuam chegando de todo modo.'}
  ], render: function(i, f, u){
    var x, y, k;
    if (i === 0){ x = 100; y = 86; }
    else if (i === 1){ k = T.ease(T.seg(f, 0, .5)); x = T.lerp(100, 578, k); y = 86; }
    else { k = T.ease(T.seg(f, 0, .45)); x = T.lerp(578, 690, k); y = T.lerp(86, 44, k); }
    var tokVis = i < 2 || (i === 2 && f < .5) ? 1 : 0;
    if (i === 0) tokVis = T.seg(f, 0, .25);
    tok.setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')');
    T.op(tok, tokVis);
    var morph = i >= 2 ? 1 : i === 1 ? T.seg(f, .55, .75) : 0;
    T.op($('tok8cap'), 1 - morph); T.op($('tok8aeat'), morph);
    T.op($('led8a'), i > 1 || (i === 1 && f > .15) ? 1 : .2);
    T.op($('led8b'), i > 1 || (i === 1 && f > .45) ? 1 : .2);
    T.op($('led8c'), i > 1 || (i === 1 && f > .75) ? 1 : .2);
    var wOn = i >= 2 ? (i === 2 ? T.seg(f, .3, .5) : 1) : 0;
    for (var w = 0; w < waves.length; w++){
      var r = T.reduced() ? 160 + w * 140 : ((u * 120 + w * 150) % 750) + 20;
      waves[w].setAttribute('r', r.toFixed(1));
      waves[w].style.opacity = (wOn * (1 - r / 770)).toFixed(3);
    }
    var wake = i > 2 || (i === 2 && f > .65);
    T.op($('wk8'), wake ? 1 : 0);
    var lit = i > 3 ? 1 : i === 3 ? T.seg(f, .05, .3) : 0;
    T.op($('p8lit'), lit); T.op($('rx8on'), i > 3 ? 1 : i === 3 ? T.seg(f, .3, .45) : 0);
    T.op($('alr8poly'), i >= 3 ? 1 : 0); T.op($('alr8lbl'), i >= 3 ? 1 : 0);
    var p = i > 3 ? 1 : i === 3 ? T.easeOut(T.seg(f, .3, .55)) : 0, w2 = 546 * T.seg(p, 0, .4), h2 = 2 + 304 * T.seg(p, .4, 1);
    T.attr($('pw8'), 'x', (885 - w2 / 2).toFixed(1)); T.attr($('pw8'), 'width', w2.toFixed(1));
    T.attr($('pw8'), 'y', (365 - h2 / 2).toFixed(1)); T.attr($('pw8'), 'height', h2.toFixed(1));
    T.op($('pw8'), p > 0 && p < 1 ? 1 - T.seg(p, .85, 1) : 0);
    T.op($('vid8g'), i > 3 ? 1 : i === 3 ? T.seg(f, .5, .6) : 0);
    var b = i > 3 ? 1 : i === 3 ? T.easeOut(T.seg(f, .6, .85)) : 0;
    $('ban8').setAttribute('transform', 'translate(0 ' + (150 * (1 - b)).toFixed(1) + ')');
    T.op($('led8tv'), i >= 3 && !(i === 3 && f < .3) ? 0 : 1);
    var own = i === 4 ? T.seg(f, .3, .5) : 0;
    T.op($('own8n'), 1 - own); T.op($('own8b'), own); T.op($('sea8'), i === 4 ? T.seg(f, .45, .65) : 0);
    $('st8').textContent = i < 2 || (i === 2 && f <= .65) ? 'standby · sintonizador monitorando o sinal'
      : i === 2 ? 'wake-up detectado no sinal'
      : i === 3 && f < .3 ? 'localização conferida contra a área do alerta'
      : i === 3 ? 'ligado · alerta relevante para esta localização' : 'alerta apresentado';
  }});
})();
</script>

<div class="grid cards" markdown>

- **Doze categorias CAP**

    `Geo` `Met` `Safety` `Security` `Rescue` `Fire` `Health` `Env` `Transport` `Infra` `CBRNE` `Other`

- **Onde o alerta vale**

    `AEA.Header.Location@type` aceita `ZIP_BR` (CEP restrito a 8 dígitos numéricos), `polygon` e `circle`. A localização do receptor pode vir da TBSAT, direto do sinal, sem GPS e sem internet.

- **Sem sintonizador livre**

    O monitoramento é prioritariamente OTA. Sem tuner disponível, cai para a URL OTT declarada na tag `emergencyWarningTransmission` da BAM, com `@ota` e `@url`.

- **Monitoramento**

    A emissora declara que transmite alertas na tag `emergencyWarningTransmission` da BAM, com `@ota` e `@url`. OTA tem prioridade; sem sintonizador disponível, cai para a URL OTT. Vale como wake-up se `AEA@wakeup` for true, ou se um alerta em CAP tiver prioridade equivalente ao máximo.

- **Quem apresenta**

    A aplicação registra notificação de evento nos WebServices e define `showEmergencyAlert` como true: assume a exibição e a app nativa se cala. Os eventos continuam chegando de todo modo.

- **Quando não exibir**

    Se a OSN vier com `KeepScreenClear` associada ao serviço atual, o receptor **não pode** exibir a mensagem de alerta. A emissora deve evitar essa sinalização durante um alerta ativo, a menos que já esteja exibindo a mesma informação no vídeo.

</div>

### 5.2 Acessibilidade {#acessibilidade}

Quatro recursos, três normas, e um fio que os liga: todos são **preferências do telespectador** guardadas no perfil e consultáveis pela aplicação. Não são decoração do receptor — a sua aplicação precisa respeitá-los e, no caso do alerta, ativá-los.

<div class="grid cards" markdown>

- **Legendas**

    IMSC1 e WebVTT. Em HLS, os formatos MPEG-2 TS, Packed Audio e IMSC Subtitles não podem ser usados — só MPEG-4 fragmentado e WebVTT. <span class="tv3-cite">25605 · 25602, Anexo C</span>

- **Closed signing**

    Língua de sinais fechada, que o telespectador liga e desliga: stream de vídeo de Libras, stream de gloss e stream de movimento. Acabou a janela queimada no vídeo. <span class="tv3-cite">25606</span>

- **Audiodescrição e realce de diálogo**

    Componentes de áudio no MPEG-H, selecionáveis. A interface de gerenciamento de áudio MPEG-H pode ser desabilitada enquanto uma aplicação estiver no controle da apresentação. <span class="tv3-cite">25604</span>

- **No alerta, vira requisito**

    Quando `lang` é um código de gloss conhecido, como `bzs`, o conteúdo deve ser apresentado em Libras conforme o Anexo B da 25606. Em `pt-BR` com prioridade máxima, o texto deve ser sintetizado em voz. Havendo áudio ou vídeo no alerta, eles tocam primeiro e só depois vem a síntese. <span class="tv3-cite">25607, Tabela A.1</span>

</div>

<span class="tv3-cite">Os atributos básicos do perfil do telespectador são justamente estes: idioma de áudio, legendas, closed signing, audiodescrição e realce de diálogo.</span>

### 5.3 Privacidade e dados {#privacidade}

A PRRD — Privacy Record Request Description — é o fragmento da SLS em que a emissora declara, por finalidade, que dados quer e com que base. Sem consentimento sobre ela, a aplicação não toca em atributo de perfil nem em dado pessoal. O modelo foi desenhado para a LGPD.

<div class="grid cards" markdown>

- `01` **Primeira entrada**

    Ao entrar no serviço pela primeira vez, o consentimento é pedido com as informações da PRRD à vista — antes de qualquer manipulação de dado.

- `02` **Negativa**

    Negado, a operação não prossegue. A aplicação precisa degradar com elegância e o receptor segue estável.

- `03` **Atualização**

    PRRD nova força consentimento novo. Até lá, continua valendo — e bloqueando — o que foi consentido antes.

- `04` **Registro**

    A decisão fica gravada por emissora e é consultável pelo telespectador no Privacy Manager.

</div>

<div class="grid cards" markdown>

- **Medição de audiência**

    Caso particular do mesmo modelo: a coleta é delegada à AoP mediante solicitação, sob a finalidade `dpv:ServiceUsageAnalytics` declarada na PRRD. A configuração vem na BAM.

- **Para quem testa**

    A pré-condição quase sempre é *nenhum consentimento prévio*. Dois PCAPs com PRRDs distintas cobrem o ciclo de atualização. Grupo ST3_F_G_008 da suíte.

- **Onde ler mais**

    As normas citam o *Guia de Acesso a Dados e Privacidade* e o *Guia de Usabilidade* do Fórum SBTVD, que detalham o comportamento esperado da interface de consentimento.

</div>

Cheat sheet originalmente elaborado por **Carlos Eduardo Coelho Batista** (UFPB), construído sobre as ABNT NBR 25601, 25602, 25607, 25608 e 25609:2025, com as referências normativas ATSC A/321, A/322, A/324, A/330, A/331, A/332 e A/360, ISO/IEC 23009-1, IETF RFC 8216 e 1952, ITU-T X.1303 bis e ABNT NBR 15606-11.

As normas são documentos pagos: aqui há cláusula, termo e identificador — nunca reprodução de texto normativo. Em caso de divergência vale a norma e, na interpretação da versão em inglês, prevalece o texto original em português.

<script>
(function(){
  "use strict";
  var $=function(s,r){return (r||document).querySelector(s);};
  var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));};
  var LLS=[
    ['SLT','0x01','Service List Table','ATSC A/331, 6.3, modificada na NBR 25602, 8.1','Lista os serviços do canal de RF e diz onde está a SLS de cada um. Em TV 3.0, majorChannelNo e minorChannelNo só valem no Service Type 30, e o terceiro octeto do IP do serviço deriva da frequência central dividida pela largura do canal.'],
    ['RRT','0x02','Rating Region Table','ATSC A/331, Anexo F','Classificação indicativa e controle parental por região.'],
    ['SystemTime','0x03','System Time Fragment','ATSC A/331, 6.4','Hora do sistema. Sustenta as janelas validFrom e validUntil da BALD e o período de vigência dos alertas.'],
    ['AEAT','0x04','Advanced Emergency informAtion Table','ATSC A/331, 6.5, modificada na NBR 25607, A.3','Uma ou mais mensagens AEA. É o único conteúdo da LLS que pode ligar um receptor em standby, pelo wake-up.'],
    ['OSN','0x05','OnscreenMessageNotification','ATSC A/331, 6.6','Mensagem imposta pela emissora na tela. Com a tag KeepScreenClear associada ao serviço atual, o receptor fica proibido de exibir a mensagem de alerta.'],
    ['BAMT','0x90','Bootstrap Application Manifest Table','sintaxe na NBR 25602, 8.2; semântica na NBR 25608','O manifesto (BAM) das Bootstrap Applications dos serviços Tipo 30. Carrega ícone, nome, agrupamento (groupingType), configuração de medição de audiência e a tag emergencyWarningTransmission. Repete na mesma taxa da SLT.'],
    ['TBSAT','0x91','Transmitter’s Best Server Area Table','NBR 25602, 8.3','Centroide e raio da cobertura da SFN, mais uma mensagem TBSA por transmissor com o seu txid_address e o polígono em WGS 84 onde ele é o melhor servidor. Dá geolocalização direto do sinal OTA, sem GPS e sem internet.'],
    ['CDT','A/360','Certification Data Table','ATSC A/360, 5.2.2.2','Certificados. Entregue à AoP conforme a NBR 25608, 7.2.2, mas não consta da Tabela 2 de LLS_table_id da 25602 — em TV 3.0 as tabelas da LLS não usam assinatura digital.']
  ];
  var SLS=[
    ['USBD/USD','','User Service Bundle / Service Description','ATSC A/331, 7.1.3','O índice do serviço: aponta para os demais fragmentos e descreve os métodos de entrega.'],
    ['S-TSID','','Service-based Transport Session Instance Description','ATSC A/331, 7.1.4','Descreve as sessões ROUTE: qual componente do serviço viaja em qual canal LCT, com SrcFlow e RepairFlow.'],
    ['MPD','','Media Presentation Description','DASH-IF IOP ATSC 3.0, modificado na NBR 25602, Anexo B','O manifesto DASH. O XLink não é usado para substituição de conteúdo nem inserção de anúncio — no lugar entram os mecanismos de Alternative MPD. Uma SupplementalProperty com urn:sbtvd:dash:component-tag deixa a aplicação controlar um mesmo stream através de Periods diferentes.'],
    ['BALD','','Broadcaster Application Location Description','NBR 25608, 10.1','Substitui o HELD da ATSC. Declara cada Broadcaster Application: appId, appType, ponto de entrada por broadcast ou broadband, appContextId, controlCode, validFrom, validUntil e clearAppContextCacheDate. Obrigatória no Tipo 30 quando há aplicação.'],
    ['PRRD','','Privacy Record Request Description','NBR 25608, 8.8.2','Acrescentada pela TV 3.0. Declara, por finalidade, que dados a emissora pede e com que base. Sem consentimento sobre ela, a aplicação não manipula dado pessoal nem atributo de perfil.'],
    ['APD','','Associated Procedure Description','ATSC A/331, 7.1.7','Procedimentos associados ao serviço, como relatórios e callbacks.'],
    ['DWD','','Distribution Window Description','ATSC A/331, 7.1.9','Janelas de distribuição de arquivos não-tempo-real — inclusive os do pacote da aplicação.'],
    ['RSAT','','Regional Service Availability Table','NBR 25602, Tabelas A.1 e A.2','Opcional em todos os Service Types, nas duas configurações.'],
    ['SGDD','','Service Guide Delivery Descriptor','ATSC A/332, 5.4','Índice do guia de serviço, com as extensões TV 3.0 do Anexo D da NBR 25602 que habilitam acesso sob demanda e deep link para aplicação.'],
    ['SGDU','','Service Guide Delivery Unit','ATSC A/332, 5.4','As unidades do guia. É daqui que o EPG e o ECG tiram título, horário, descrição, gênero e capa.']
  ];
  var sigDetail=$('#sigDetail');
  function sigDefault(){
    if(!sigDetail) return;
    sigDetail.innerHTML='<h4>Oito tabelas, dez fragmentos</h4><p class="nm">clique numa sigla</p>'+
      '<p class="d">A LLS tem endereço IP e porta fixos, sem nenhuma descoberta prévia: é o ponto de entrada do receptor. A SLS é apontada pela SLT e descreve um serviço. Em TV 3.0 nenhuma das duas usa assinatura digital de tabela.</p>'+
      '<span class="w">25608, 7.2.2 e 7.2.3 · 25602, 8.1 Tabela 2 e Anexo A</span>';
  }
  function mkChips(arr,host){
    var el=$(host); if(!el) return;
    arr.forEach(function(it){
      var b=document.createElement('button');
      b.type='button'; b.setAttribute('aria-pressed','false');
      b.innerHTML=it[0]+(it[1]?'<span class="id">'+it[1]+'</span>':'');
      b.addEventListener('click',function(){
        var was=b.getAttribute('aria-pressed')==='true';
        $$('.sigchips button').forEach(function(x){x.setAttribute('aria-pressed','false');});
        if(was){ sigDefault(); return; }
        b.setAttribute('aria-pressed','true');
        sigDetail.innerHTML='<h4>'+it[0]+'</h4><p class="nm">'+it[2]+(it[1]?' · '+it[1]:'')+'</p><p class="d">'+it[4]+'</p><span class="w">'+it[3]+'</span>';
      });
      el.appendChild(b);
    });
  }
  mkChips(LLS,'#llsChips'); mkChips(SLS,'#slsChips'); sigDefault();
  var MW={
    bootstrap:['Bootstrap Application','A aplicação padrão da emissora, declarada no manifesto BAM dentro da BAMT. É o que aparece ao entrar num serviço Tipo 30, e é para ela que o receptor volta como failsafe quando uma Broadcaster Application termina ou falha.'],
    bcastapp:['Broadcaster Application','A aplicação que a emissora controla pela BALD. Escrita em TV 3.0 Ginga-NCL (NCL 4.0 com NCLua) ou em TV 3.0 Ginga-HTML5. O ciclo de vida é idêntico nas duas: o appType só diz ao receptor qual máquina de apresentação acionar.'],
    catalog:['Application Catalog','A grade de emissoras produzida no channel scan a partir da SLT e da BAMT. Exibida em tela cheia exclusiva, acessível pela função de lista de entradas da PRP, e dá acesso também ao EPG e ao ECG. Um ícone de Bootstrap Application pode ser fixado como atalho na tela inicial da PRP.'],
    access:['Access Panel','A gaveta do telespectador: Broadcaster Applications disponíveis, preferências de acessibilidade e o Privacy Manager. É onde uma aplicação sinalizada com PRESENT espera para ser aberta.'],
    pe:['Presentation Engine','O subsistema da AoP que processa e apresenta aplicações declarativas, incluindo áudio, vídeo e demais objetos de mídia.'],
    alm:['Application Lifecycle Manager','Lê a BALD e decide o que roda: baixar, iniciar, armazenar, encerrar ou remover. Trata validFrom, validUntil, o cache identificado por appContextId e o failsafe de volta à Bootstrap.'],
    pmp:['Persistent Media Player','Responsável pela reprodução contínua e ininterrupta do conteúdo da emissora, inclusive durante a transição entre aplicações diferentes no mesmo contexto de serviço. A continuidade do vídeo é requisito, não detalhe de implementação.'],
    ws:['TV 3.0 WebServices','API REST local. Dá à aplicação a sinalização bruta (qualquer tabela da LLS ou fragmento da SLS), o guia de serviço, o alerta de emergência, a geolocalização, parâmetros da camada física, capacidades e atributos da plataforma, perfil do telespectador, cache, medição de audiência, dispositivos remotos, efeitos sensoriais e 360°. O Ginga Common Core dessa interface tem norma própria: a NBR 15606-11.'],
    sigman:['Signaling Manager','Os parsers de LMT, SLT, BAMT e TBSAT. No channel scan, é quem alimenta o Application Catalog e o mapa de canais.'],
    privacy:['Privacy Manager','Onde o telespectador consulta e revisa o que consentiu, por emissora. Alimentado pelas decisões tomadas sobre cada PRRD.'],
    amm:['Audience Measurement Manager','A coleta de dados de audiência é delegada à AoP mediante solicitação, sob a finalidade declarada na PRRD. A configuração vem na BAM.'],
    home:['Tela inicial e menus','Parte da PRP, fora do escopo da AoP. Hospeda o ícone TV 3.0, a função de lista de entradas e os atalhos para Bootstrap Applications.'],
    tuner:['Sintonizador e demodulador','Recomenda-se ao menos quatro processadores de PLP, porque um serviço pode usar até quatro streams ALP. Com LDM, PLPs da camada Core consomem processadores para descobrir a Enhanced, mesmo quando não pertencem ao serviço desejado.'],
    prpsys:['Ajustes do fabricante','Rede, idioma, atualização de software e identificação do produto. A versão da PRP e a versão da implementação da AoP são atributos consultáveis pela aplicação.']
  };
  var mwDetail=$('#mwDetail');
  function mwDefault(){
    if(!mwDetail) return;
    mwDetail.innerHTML='<b>A divisão que importa.</b> Tudo na faixa verde é normatizado e a sua aplicação pode contar com isso. Tudo na faixa cinza é decisão do fabricante — você só a alcança pelas capacidades e atributos que a plataforma expõe pelos WebServices.';
  }
  $$('.mwrow button').forEach(function(b){
    b.addEventListener('click',function(){
      var was=b.getAttribute('aria-pressed')==='true';
      $$('.mwrow button').forEach(function(x){x.setAttribute('aria-pressed','false');});
      if(was){ mwDefault(); return; }
      b.setAttribute('aria-pressed','true');
      var m=MW[b.getAttribute('data-mw')];
      if(m) mwDetail.innerHTML='<b>'+m[0]+'.</b> '+m[1];
    });
  });
  mwDefault();
})();
</script>
