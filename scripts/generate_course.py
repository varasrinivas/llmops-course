# -*- coding: utf-8 -*-
"""
generate_course.py — Builds course/index.html for
"Production LLMOps: AI Application Lifecycle"
  * DARK THEME
  * Domain anchor: Prior Authorization (PA) Determination Pipeline (healthcare payer)
Run:  python scripts/generate_course.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(HERE, "course", "index.html")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules_t1_4 import MODS as M1, SVGS as S1
from modules_t5_8 import MODS as M2, SVGS as S2

MODS = M1 + M2
SVGS = {}
SVGS.update(S1)
SVGS.update(S2)

# ════════════════════════════════════════════════════════════════════
#  TRACK METADATA
# ════════════════════════════════════════════════════════════════════
TRACK_META = [
    {"num":1,"name":"Foundations","color":"#4caf82","icon":"\U0001FAE7"},
    {"num":2,"name":"Eval & Testing","color":"#ec8a6e","icon":"\U0001F9EA"},
    {"num":3,"name":"Deployment & Release","color":"#6f93c9","icon":"\U0001F680"},
    {"num":4,"name":"Monitoring & Observability","color":"#e3a52c","icon":"\U0001F4CA"},
    {"num":5,"name":"Data & Feedback Loops","color":"#8fc7a8","icon":"\U0001F501"},
    {"num":6,"name":"Model Lifecycle","color":"#cf6f5f","icon":"\U0001F504"},
    {"num":7,"name":"Incident & Reliability","color":"#9486cf","icon":"\U0001F6A8"},
    {"num":8,"name":"Governance & Optimization","color":"#3f95a8","icon":"⚖️"},
]

# ════════════════════════════════════════════════════════════════════
#  HTML SHELL  (dark theme)
# ════════════════════════════════════════════════════════════════════
HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Production LLMOps: AI Application Lifecycle</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,700;1,9..144,400&family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #14161b;
  --surface: #1c1f26;
  --surface-2: #23272f;
  --text: #e9e5dc;
  --text-muted: #9aa0a8;
  --border: #2d323b;
  --gold: #d4c5a9;
  --font-display: 'Fraunces', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { background:var(--bg); color:var(--text); font-family:var(--font-body); font-size:15px; line-height:1.65; }
::selection { background:#4caf8255; }

/* ── Landing ── */
.landing { min-height:100vh; display:flex; flex-direction:column; }
.landing-hero {
  background: linear-gradient(135deg, #102027 0%, #122a22 42%, #16202f 100%);
  color: #e9e5dc; padding: 64px 24px 52px; text-align: center;
  border-bottom:1px solid var(--border);
}
.landing-hero .eyebrow {
  font-family:var(--font-mono); font-size:11px; letter-spacing:3px;
  text-transform:uppercase; color:#7fb89c; margin-bottom:16px;
}
.landing-hero h1 {
  font-family:var(--font-display); font-size:clamp(28px,5vw,44px);
  font-weight:700; line-height:1.12; margin-bottom:10px;
}
.landing-hero h1 em { font-style:italic; font-weight:300; color:var(--gold); }
.landing-hero .tagline { font-size:15px; color:#b6bcc4; max-width:600px; margin:0 auto 14px; }
.landing-hero .domain-chip {
  display:inline-block; font-family:var(--font-mono); font-size:11px; letter-spacing:1px;
  color:#cdb98f; border:1px solid #3a3327; background:#241f16; padding:5px 12px;
  border-radius:20px; margin-bottom:30px;
}
.stats-row { display:flex; justify-content:center; gap:36px; flex-wrap:wrap; }
.stat-item .num { font-family:var(--font-display); font-size:32px; font-weight:700; display:block; color:#fff; }
.stat-item .lbl { font-family:var(--font-mono); font-size:10px; letter-spacing:2px; text-transform:uppercase; color:#8b9199; }

/* ── Track List ── */
.tracks-grid { max-width:920px; margin:0 auto; padding:36px 24px 64px; width:100%; }
.track-group { margin-bottom:30px; }
.track-group-header {
  display:flex; align-items:baseline; gap:10px;
  padding-bottom:8px; border-bottom:2px solid var(--border); margin-bottom:12px;
}
.track-group-header .tnum {
  font-family:var(--font-mono); font-size:11px; letter-spacing:2px; text-transform:uppercase;
}
.track-group-header .tname { font-family:var(--font-display); font-size:20px; font-weight:500; }
.module-row {
  display:flex; align-items:center; gap:12px;
  padding:13px 16px; background:var(--surface); border:1px solid var(--border);
  border-radius:5px; margin-bottom:6px; cursor:pointer; transition:all .18s;
}
.module-row:hover { border-color:#4a515c; background:var(--surface-2); transform:translateX(2px); }
.module-row .mid { font-family:var(--font-mono); font-size:12px; min-width:34px; font-weight:500; }
.module-row .micon { font-size:18px; }
.module-row .mtitle { font-family:var(--font-display); font-size:15px; font-weight:500; flex:1; }
.module-row .mstatus { font-size:12px; color:#4caf82; }
.module-row .marrow { color:var(--text-muted); }

/* ── Module View ── */
.module-view { display:none; min-height:100vh; }
.module-view.active { display:block; }
.mv-header { padding:34px 24px 24px; text-align:center; border-bottom:1px solid var(--border); }
.mv-header .back-btn {
  display:inline-flex; align-items:center; gap:6px;
  font-family:var(--font-mono); font-size:12px; color:var(--text-muted);
  text-decoration:none; cursor:pointer; margin-bottom:18px;
  border:1px solid var(--border); padding:6px 14px; border-radius:4px; background:var(--surface);
}
.mv-header .back-btn:hover { border-color:#4a515c; color:var(--text); }
.mv-header .mv-track { font-family:var(--font-mono); font-size:11px; letter-spacing:2px; text-transform:uppercase; margin-bottom:8px; }
.mv-header h2 { font-family:var(--font-display); font-size:clamp(22px,4vw,32px); font-weight:700; margin-bottom:6px; }
.mv-header .mv-sub { font-size:14px; color:var(--text-muted); max-width:620px; margin:0 auto; }

.mv-body { max-width:780px; margin:0 auto; padding:28px 24px 72px; }

.mv-diagram { margin-bottom:28px; background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:20px; text-align:center; overflow-x:auto; }
.mv-diagram svg { max-width:100%; height:auto; }

.mv-section { margin-bottom:24px; }
.mv-section h3 { font-family:var(--font-display); font-size:19px; font-weight:500; margin-bottom:10px; padding-bottom:6px; border-bottom:1px solid var(--border); }
.mv-section p { margin-bottom:11px; }
.mv-section strong { color:#fff; font-weight:600; }
.mv-section em { color:var(--gold); font-style:italic; }

.mv-analogy {
  background:rgba(212,197,169,0.05); border-left:3px solid var(--gold); padding:16px 20px;
  border-radius:0 6px 6px 0; margin-bottom:24px;
}
.mv-analogy .analogy-title { font-family:var(--font-display); font-size:15px; font-weight:500; margin-bottom:6px; color:var(--gold); }
.mv-analogy .analogy-text { font-size:14px; color:#c4bfb5; font-style:italic; line-height:1.7; }

.mv-topics { margin-bottom:24px; }
.mv-topics .topic-item {
  padding:9px 0 9px 20px; position:relative; font-size:14px;
  border-bottom:1px solid var(--border);
}
.mv-topics .topic-item:last-child { border-bottom:none; }
.mv-topics .topic-item::before { content:'\2192'; position:absolute; left:0; font-size:13px; color:#4caf82; }

.mv-quiz {
  background:var(--surface); border:1px solid var(--border); border-radius:8px;
  padding:20px; margin-bottom:24px;
}
.mv-quiz .quiz-q { font-family:var(--font-display); font-size:15px; font-weight:500; margin-bottom:14px; }
.quiz-opt {
  display:block; width:100%; text-align:left; padding:11px 14px; margin-bottom:6px;
  background:var(--bg); border:1px solid var(--border); border-radius:4px; color:var(--text);
  font-family:var(--font-body); font-size:13px; cursor:pointer; transition:all .18s;
}
.quiz-opt:hover { border-color:#4a515c; }
.quiz-opt.correct { background:rgba(76,175,130,0.16); border-color:#4caf82; color:#bfe8d2; }
.quiz-opt.wrong { background:rgba(207,57,43,0.16); border-color:#cf6f5f; color:#f0c0b8; }
.quiz-explain { display:none; margin-top:12px; font-size:13px; color:var(--text-muted); padding:12px; background:var(--bg); border-radius:4px; border:1px solid var(--border); }

.mv-antipatterns {
  background:rgba(207,111,95,0.07); border-left:3px solid #cf6f5f; padding:16px 20px;
  border-radius:0 6px 6px 0; margin-bottom:24px;
}
.mv-antipatterns .ap-title { font-family:var(--font-mono); font-size:11px; letter-spacing:2px; text-transform:uppercase; color:#e08a78; margin-bottom:10px; }
.mv-antipatterns .ap-item { font-size:14px; padding:5px 0; color:#d6b3aa; }

.mv-crosslinks { margin-bottom:24px; }
.mv-crosslinks h3 { font-family:var(--font-display); font-size:16px; font-weight:500; margin-bottom:8px; }
.mv-crosslink-tag {
  display:inline-block; font-family:var(--font-mono); font-size:11px;
  padding:5px 11px; border-radius:3px; margin:2px 4px 2px 0;
}
.mv-crosslink-tag.ce { background:#2a3320; color:#a9c98a; }
.mv-crosslink-tag.agent { background:#1f2e25; color:#8fc7a8; }
.mv-crosslink-tag.platform { background:#1f2733; color:#8fb0d6; }
.mv-crosslink-tag.sdlc { background:#2e2535; color:#bda9cf; }

.mv-takeaway {
  background:linear-gradient(135deg,#1d2228,#1a1f26); border:1px solid #34506b; border-radius:8px;
  padding:22px; text-align:center; margin-bottom:24px;
}
.mv-takeaway .tk-label { font-family:var(--font-mono); font-size:10px; letter-spacing:2px; text-transform:uppercase; color:#7fb89c; margin-bottom:8px; }
.mv-takeaway .tk-text { font-family:var(--font-display); font-size:16px; font-weight:500; font-style:italic; color:#f0ece3; }

.mv-labs { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:24px; }
.mv-lab-card {
  background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:16px;
}
.mv-lab-card .lab-tag {
  font-family:var(--font-mono); font-size:10px; letter-spacing:1px;
  text-transform:uppercase; padding:3px 8px; border-radius:3px; display:inline-block; margin-bottom:10px;
}
.mv-lab-card.understand .lab-tag { background:rgba(76,175,130,0.16); color:#8fd9b4; }
.mv-lab-card.build .lab-tag { background:rgba(111,147,201,0.16); color:#9bbbe6; }
.mv-lab-card .lab-desc { font-size:13px; color:var(--text-muted); line-height:1.6; margin-bottom:12px; }
.mv-lab-card .lab-link {
  display:inline-flex; align-items:center; gap:5px; font-family:var(--font-mono);
  font-size:11px; text-decoration:none; padding:5px 10px; border-radius:4px;
  border:1px solid var(--border); transition:all .18s;
}
.mv-lab-card.understand .lab-link { color:#8fd9b4; }
.mv-lab-card.build .lab-link { color:#9bbbe6; }
.mv-lab-card.understand .lab-link:hover { background:rgba(76,175,130,0.14); border-color:#4caf82; }
.mv-lab-card.build .lab-link:hover { background:rgba(111,147,201,0.14); border-color:#6f93c9; }

.mv-nav { display:flex; justify-content:space-between; padding-top:20px; border-top:1px solid var(--border); }
.mv-nav button {
  font-family:var(--font-mono); font-size:12px; padding:9px 16px;
  border:1px solid var(--border); border-radius:4px; background:var(--surface);
  cursor:pointer; transition:all .18s; color:var(--text);
}
.mv-nav button:hover:not(:disabled) { border-color:#4a515c; background:var(--surface-2); }
.mv-nav button:disabled { opacity:.3; cursor:default; }

.mv-code { margin-bottom:24px; }
.mv-code pre {
  background:#0e1014; color:#d6e3d9; padding:16px; border-radius:6px;
  overflow-x:auto; font-family:var(--font-mono); font-size:12.5px; line-height:1.65;
  border:1px solid var(--border);
}
.mv-code .code-title { font-family:var(--font-mono); font-size:11px; letter-spacing:1px; text-transform:uppercase; color:var(--text-muted); margin-bottom:6px; }

@media(max-width:600px) {
  .mv-labs { grid-template-columns:1fr; }
  .landing-hero { padding:40px 16px 36px; }
  .stats-row { gap:18px; }
}
@media(prefers-reduced-motion:reduce) {
  * { transition:none !important; animation:none !important; }
}
</style>
</head>
<body>

<!-- LANDING -->
<div class="landing" id="landing">
  <div class="landing-hero">
    <div class="eyebrow">agenticai.varasrinivas.com</div>
    <h1>Production LLMOps<br><em>AI Application Lifecycle</em></h1>
    <p class="tagline">The 'day 2' discipline. 32 modules on evaluating, deploying, monitoring, upgrading, and governing LLM applications in production. Everything after 'it works on my laptop.'</p>
    <div class="domain-chip">Domain anchor: Prior Authorization Determination Pipeline</div>
    <div class="stats-row">
      <div class="stat-item"><span class="num" id="statMods">0</span><span class="lbl">Modules</span></div>
      <div class="stat-item"><span class="num">8</span><span class="lbl">Tracks</span></div>
      <div class="stat-item"><span class="num">64</span><span class="lbl">Labs</span></div>
      <div class="stat-item"><span class="num" id="statPct">0%</span><span class="lbl">Complete</span></div>
    </div>
  </div>
  <div class="tracks-grid" id="tracksGrid"></div>
</div>

<!-- MODULE VIEW -->
<div class="module-view" id="moduleView">
  <div class="mv-header">
    <button class="back-btn" onclick="showLanding()">&larr; All Modules</button>
    <div class="mv-track" id="mvTrack"></div>
    <h2 id="mvTitle"></h2>
    <div class="mv-sub" id="mvSub"></div>
  </div>
  <div class="mv-body" id="mvBody"></div>
</div>

<script>
"""

ENGINE = r"""
function renderVisual(moduleId) {
  switch(moduleId) {
__SVG_CASES__
    default: return '';
  }
}

const STORAGE_KEY = 'llmops-pa-course-progress';
let progress = {};
try { progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch(e) {}
function saveProgress() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); } catch(e) {} }
function markComplete(id) { progress[id] = true; saveProgress(); updateStats(); }
function updateStats() {
  document.getElementById('statMods').textContent = MODS.length;
  const pct = Math.round((Object.keys(progress).length / 32) * 100);
  document.getElementById('statPct').textContent = pct + '%';
}
function showLanding() {
  document.getElementById('landing').style.display = '';
  document.getElementById('moduleView').classList.remove('active');
  buildLanding();
  try { history.replaceState(null, '', location.pathname + location.search); } catch(e) { location.hash = ''; }
  window.scrollTo(0, 0);
}
function showModule(id) {
  const mod = MODS.find(m => m.id === id);
  if (!mod) return;
  const track = TRACK_META[mod.track - 1];
  document.getElementById('landing').style.display = 'none';
  const mv = document.getElementById('moduleView');
  mv.classList.add('active');
  document.getElementById('mvTrack').textContent = `Track ${track.num} — ${track.name}`;
  document.getElementById('mvTrack').style.color = track.color;
  document.getElementById('mvTitle').textContent = `${mod.icon} ${mod.id}: ${mod.title}`;
  document.getElementById('mvSub').textContent = mod.subtitle;
  let html = '';
  const svg = renderVisual(mod.id);
  if (svg) html += `<div class="mv-diagram">${svg}</div>`;
  if (mod.analogy) {
    html += `<div class="mv-analogy"><div class="analogy-title">💡 ${mod.analogy.title}</div><div class="analogy-text">${mod.analogy.text}</div></div>`;
  }
  if (mod.topics && mod.topics.length) {
    html += `<div class="mv-topics"><h3>Key Topics</h3>`;
    mod.topics.forEach(t => { html += `<div class="topic-item">${t}</div>`; });
    html += `</div>`;
  }
  if (mod.sections) {
    mod.sections.forEach((sec, si) => {
      if (sec.type === 'content') {
        html += `<div class="mv-section"><h3>${sec.title}</h3>${sec.body}</div>`;
      } else if (sec.type === 'analogy') {
        html += `<div class="mv-analogy"><div class="analogy-title">💡 ${sec.title}</div><div class="analogy-text">${sec.body}</div></div>`;
      } else if (sec.type === 'code') {
        html += `<div class="mv-code"><div class="code-title">${sec.title} (${sec.language || ''})</div><pre><code>${escHtml(sec.code)}</code></pre></div>`;
      } else if (sec.type === 'quiz') {
        const qid = `quiz-${mod.id}-${si}`;
        html += `<div class="mv-quiz" id="${qid}"><div class="quiz-q">🧪 ${sec.question}</div>` +
          sec.options.map((o, oi) => `<button class="quiz-opt" onclick="handleQuiz('${qid}',${oi},${sec.correct})">${String.fromCharCode(65+oi)}. ${o}</button>`).join('') +
          `<div class="quiz-explain">${sec.explanation}</div></div>`;
      } else if (sec.type === 'antipattern') {
        html += `<div class="mv-antipatterns"><div class="ap-title">⚠️ ${sec.title}</div>` +
          sec.items.map(it => `<div class="ap-item">• ${it}</div>`).join('') + `</div>`;
      }
    });
  }
  if (mod.crosslinks && mod.crosslinks.length) {
    html += `<div class="mv-crosslinks"><h3>Cross-Links</h3>`;
    mod.crosslinks.forEach(cl => { html += `<span class="mv-crosslink-tag ${cl.type}">${cl.label}</span>`; });
    html += `</div>`;
  }
  if (mod.takeaway) {
    html += `<div class="mv-takeaway"><div class="tk-label">LLMOps Takeaway</div><div class="tk-text">${mod.takeaway}</div></div>`;
  }
  const LAB_BASE = "https://github.com/varasrinivas/llmops-course/blob/main/labs";
  html += `<div class="mv-labs"><div class="mv-lab-card understand"><span class="lab-tag">🔍 Understand It</span><div class="lab-desc">${mod.labUnderstand || ''}</div><a class="lab-link" href="${LAB_BASE}/${mod.id}-lab-understand.md" target="_blank" rel="noopener">Open lab →</a></div><div class="mv-lab-card build"><span class="lab-tag">🔨 Build It with AI</span><div class="lab-desc">${mod.labBuild || ''}</div><a class="lab-link" href="${LAB_BASE}/${mod.id}-lab-build.md" target="_blank" rel="noopener">Open lab →</a></div></div>`;
  const idx = MODS.findIndex(m => m.id === id);
  const prev = idx > 0 ? MODS[idx-1] : null;
  const next = idx < MODS.length - 1 ? MODS[idx+1] : null;
  html += `<div class="mv-nav"><button ${prev ? `onclick="showModule('${prev.id}')"` : 'disabled'}>← ${prev ? prev.id : ''}</button><button onclick="markComplete('${mod.id}'); this.textContent='✓ Complete'; this.style.background='rgba(76,175,130,0.16)'; this.style.borderColor='#4caf82'; this.style.color='#bfe8d2';">Mark Complete</button><button ${next ? `onclick="showModule('${next.id}')"` : 'disabled'}>${next ? next.id : ''} →</button></div>`;
  document.getElementById('mvBody').innerHTML = html;
  try { if (location.hash.replace(/^#/,'') !== id) history.replaceState(null, '', '#' + id); } catch(e) {}
  window.scrollTo(0, 0);
}
function handleQuiz(qid, selected, correct) {
  const quiz = document.getElementById(qid);
  const opts = quiz.querySelectorAll('.quiz-opt');
  opts.forEach((o, i) => {
    o.disabled = true;
    if (i === correct) o.classList.add('correct');
    else if (i === selected && selected !== correct) o.classList.add('wrong');
  });
  quiz.querySelector('.quiz-explain').style.display = 'block';
}
function escHtml(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function buildLanding() {
  const grid = document.getElementById('tracksGrid');
  grid.innerHTML = '';
  TRACK_META.forEach(track => {
    const trackMods = MODS.filter(m => m.track === track.num);
    if (!trackMods.length) return;
    const group = document.createElement('div');
    group.className = 'track-group';
    group.innerHTML = `<div class="track-group-header"><span class="tnum" style="color:${track.color}">Track ${track.num}</span><span class="tname">${track.icon} ${track.name}</span></div>` +
      trackMods.map(m => `<div class="module-row" onclick="showModule('${m.id}')" style="border-left:3px solid ${track.color}"><span class="mid" style="color:${track.color}">${m.id}</span><span class="micon">${m.icon}</span><span class="mtitle">${m.title}</span><span class="mstatus">${progress[m.id] ? '✓' : ''}</span><span class="marrow">→</span></div>`).join('');
    grid.appendChild(group);
  });
  updateStats();
}
document.addEventListener('keydown', e => {
  if (document.getElementById('moduleView').classList.contains('active')) {
    const cur = document.getElementById('mvTitle').textContent;
    const idx = MODS.findIndex(m => cur.includes(m.id + ':'));
    if (e.key === 'ArrowRight' && idx < MODS.length - 1) showModule(MODS[idx+1].id);
    if (e.key === 'ArrowLeft' && idx > 0) showModule(MODS[idx-1].id);
    if (e.key === 'Escape') showLanding();
  }
});
// Deep-linking: course/index.html#M14 opens that module; supports back/forward.
function route() {
  const id = (location.hash || '').replace(/^#/, '');
  if (id && MODS.some(m => m.id === id)) showModule(id);
  else showLanding();
}
window.addEventListener('hashchange', route);
buildLanding();
{ const id = (location.hash || '').replace(/^#/, ''); if (id && MODS.some(m => m.id === id)) showModule(id); }
</script>
</body>
</html>
"""

def build():
    svg_cases = []
    for mid, svg in SVGS.items():
        svg_cases.append('    case "%s": return %s;' % (mid, json.dumps(svg)))
    engine = ENGINE.replace("__SVG_CASES__", "\n".join(svg_cases))
    parts = []
    parts.append(HEAD)
    parts.append("const MODS = " + json.dumps(MODS, indent=2, ensure_ascii=False) + ";\n")
    parts.append("const TRACK_META = " + json.dumps(TRACK_META, indent=2, ensure_ascii=False) + ";\n")
    parts.append(engine)
    html = "".join(parts)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote %s  (%d modules, %d KB)" % (OUT, len(MODS), len(html)//1024))

if __name__ == "__main__":
    build()
