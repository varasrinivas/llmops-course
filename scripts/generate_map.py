# -*- coding: utf-8 -*-
"""
generate_map.py — Builds llmops-course-map.html from the module data.
Dark theme + Prior Authorization domain, consistent with course/index.html.
Run:  python scripts/generate_map.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(HERE, "llmops-course-map.html")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules_t1_4 import MODS as M1
from modules_t5_8 import MODS as M2
from generate_course import TRACK_META
MODS = M1 + M2

TRACK_DESC = {
 1:"What LLMOps is, how it differs from traditional MLOps, and the lifecycle stages every LLM application moves through — from prototype to production to retirement.",
 2:"You can't improve what you can't measure. This track builds the evaluation infrastructure that tells you whether the prior-authorization model is right — before and after every change.",
 3:"Getting LLM applications from 'works in dev' to 'serving determinations safely' — CI/CD, canaries, feature flags, and rollback designed for non-deterministic systems.",
 4:"LLM applications degrade silently — quality drops, costs creep, turnaround slips — with no 500 errors to alert on. This track builds the monitoring that catches what traditional APM misses.",
 5:"The virtuous cycle — collecting reviewer feedback, curating eval data, and building the data flywheel that makes the pipeline improve over time instead of decaying.",
 6:"Models change — providers release new versions, deprecate old ones, and alter behavior. This track builds the systems to manage model transitions without breaking determinations.",
 7:"LLM applications fail in unique ways — hallucinated criteria, prompt injection, silent quality drift, cost explosions. This track builds the reliability practices for a regulated AI workflow.",
 8:"The long game — optimizing cost, automating compliance, building institutional knowledge, and the capstone that operates the complete prior-authorization pipeline in production.",
}

XREF = [
 ("M04–M07 Eval & Testing","CE M29 Context A/B Testing","LLMOps automates evals at scale; CE designs what to evaluate"),
 ("M05 LLM-as-Judge","Platform M10 Prompt Eval","Same technique, LLMOps focuses on production automation"),
 ("M08–M11 Deployment","Platform M11, AI-SDLC CI/CD","LLMOps deploys the full app; Platform deploys prompts"),
 ("M12–M15 Monitoring","Platform M28 Observability","App-level monitoring vs Platform's infra-level"),
 ("M13 Quality Drift","CE M14 Context Decay","Same concept — LLMOps detects it; CE prevents it"),
 ("M16–M19 Feedback Loops","Agent M15 HITL","LLMOps systematizes feedback; Agents implement HITL flows"),
 ("M20–M23 Model Lifecycle","Platform M05 Multi-Provider","LLMOps manages upgrades; Platform routes across providers"),
 ("M24–M27 Reliability","Platform M07, M29","App-level reliability vs Platform's infra-level"),
 ("M28–M30 Governance","Platform M16–M19 Cost","App-level optimization vs org-level budgets"),
 ("M31 Capstone","All capstones","LLMOps capstone operates the prior-authorization pipeline others build"),
]

def build_tracks():
    tracks = []
    for tm in TRACK_META:
        mods = [m for m in MODS if m["track"] == tm["num"]]
        tracks.append({
            "id": f"t{tm['num']}", "color": tm["color"],
            "num": f"Track {tm['num']}", "title": tm["name"], "icon": tm["icon"],
            "desc": TRACK_DESC[tm["num"]],
            "modules": [{
                "id": m["id"], "name": m["title"],
                "topics": m["topics"],
                "analogy": f"{m['analogy']['title']}. {m['analogy']['text']}",
                "labs": [m["labUnderstand"], m["labBuild"]],
                "crosslinks": m["crosslinks"],
            } for m in mods]
        })
    return tracks

def nav_buttons():
    out = ['<button class="active" data-track="all">All Tracks</button>']
    for tm in TRACK_META:
        out.append(f'<button data-track="t{tm["num"]}">T{tm["num"]} {tm["name"]}</button>')
    return "\n  ".join(out)

def xref_rows():
    return "\n".join(f"      <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in XREF)

TRACKS = build_tracks()
total_links = sum(len(m["crosslinks"]) for m in MODS)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Production LLMOps — AI Application Lifecycle (Course Map)</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,700;1,9..144,400&family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg:#14161b;--surface:#1c1f26;--surface-2:#23272f;--text:#e9e5dc;--text-muted:#9aa0a8;--border:#2d323b;--gold:#d4c5a9;
    --font-display:'Fraunces',serif;--font-body:'Inter',sans-serif;--font-mono:'JetBrains Mono',monospace;
  }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:var(--bg);color:var(--text);font-family:var(--font-body);font-size:15px;line-height:1.65}}
  ::selection{{background:#4caf8255}}
  .hero{{background:linear-gradient(135deg,#102027 0%,#122a22 42%,#16202f 100%);color:#e9e5dc;padding:56px 32px 48px;text-align:center;border-bottom:1px solid var(--border)}}
  .hero-eyebrow{{font-family:var(--font-mono);font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#7fb89c;margin-bottom:16px}}
  .hero h1{{font-family:var(--font-display);font-size:clamp(26px,5vw,42px);font-weight:700;line-height:1.15;margin-bottom:12px}}
  .hero h1 em{{font-style:italic;font-weight:300;color:var(--gold)}}
  .hero-sub{{font-size:16px;color:#b6bcc4;max-width:640px;margin:0 auto 18px;line-height:1.6}}
  .domain-chip{{display:inline-block;font-family:var(--font-mono);font-size:11px;letter-spacing:1px;color:#cdb98f;border:1px solid #3a3327;background:#241f16;padding:5px 12px;border-radius:20px;margin-bottom:20px}}
  .launch-row{{margin-bottom:26px}}
  .launch-btn{{display:inline-block;font-family:var(--font-mono);font-size:12px;letter-spacing:.5px;color:#0c1418;background:#4caf82;border:1px solid #4caf82;padding:11px 22px;border-radius:6px;text-decoration:none;transition:all .2s}}
  .launch-btn:hover{{background:#5fc497;border-color:#5fc497}}
  .module-open{{font-family:var(--font-mono);font-size:11px;color:var(--track-color);text-decoration:none;border:1px solid var(--border);padding:3px 9px;border-radius:4px;margin-right:8px;white-space:nowrap;transition:all .2s}}
  .module-open:hover{{border-color:var(--track-color);background:var(--surface-2)}}
  .hero-stats{{display:flex;justify-content:center;gap:36px;flex-wrap:wrap}}
  .hero-stat .num{{font-family:var(--font-display);font-size:32px;font-weight:700;display:block;color:#fff}}
  .hero-stat .label{{font-family:var(--font-mono);font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8b9199}}
  .positioning{{max-width:860px;margin:0 auto;padding:40px 24px 0}}
  .ecosystem-box{{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:28px;margin-bottom:32px}}
  .ecosystem-box h2{{font-family:var(--font-display);font-size:20px;font-weight:500;margin-bottom:16px}}
  .ecosystem-flow{{display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;margin-bottom:20px}}
  .eco-pill{{padding:10px 18px;border-radius:6px;font-family:var(--font-mono);font-size:12px;font-weight:500;text-align:center;line-height:1.4}}
  .eco-pill.active{{background:#3f95a8;color:#0c1418;border:2px solid #3f95a8}}
  .eco-pill.linked{{background:var(--bg);color:var(--text-muted);border:1px solid var(--border)}}
  .eco-arrow{{font-size:18px;color:var(--text-muted)}}
  .ecosystem-note{{font-size:13px;color:var(--text-muted);text-align:center;font-style:italic}}
  .track-nav{{max-width:860px;margin:0 auto;padding:0 24px 16px;display:flex;flex-wrap:wrap;gap:6px}}
  .track-nav button{{font-family:var(--font-mono);font-size:11px;letter-spacing:.5px;padding:6px 14px;border:1px solid var(--border);border-radius:4px;background:var(--surface);color:var(--text-muted);cursor:pointer;transition:all .2s}}
  .track-nav button:hover{{border-color:#4a515c;color:var(--text)}}
  .track-nav button.active{{background:var(--text);color:var(--bg);border-color:var(--text)}}
  .tracks-container{{max-width:860px;margin:0 auto;padding:0 24px 60px}}
  .track{{margin-bottom:36px;display:none}}.track.visible{{display:block}}
  .track-header{{display:flex;align-items:baseline;gap:12px;margin-bottom:4px;padding-bottom:10px;border-bottom:2px solid var(--track-color)}}
  .track-num{{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--track-color)}}
  .track-title{{font-family:var(--font-display);font-size:22px;font-weight:500}}
  .track-desc{{color:var(--text-muted);font-size:14px;margin:12px 0 20px;line-height:1.6}}
  .module-card{{background:var(--surface);border:1px solid var(--border);border-left:3px solid var(--track-color);border-radius:4px;padding:20px 22px;margin-bottom:12px;cursor:pointer;transition:border-color .2s,background .2s}}
  .module-card:hover{{border-color:var(--track-color);background:var(--surface-2)}}
  .module-card.expanded{{border-color:var(--track-color)}}
  .module-top{{display:flex;align-items:baseline;gap:12px}}
  .module-id{{font-family:var(--font-mono);font-size:12px;color:var(--track-color);font-weight:500;min-width:32px}}
  .module-name{{font-family:var(--font-display);font-size:17px;font-weight:500;flex:1}}
  .module-expand{{font-size:14px;color:var(--text-muted);transition:transform .2s}}
  .module-card.expanded .module-expand{{transform:rotate(90deg)}}
  .module-detail{{display:none;margin-top:16px;padding-top:14px;border-top:1px solid var(--border)}}
  .module-card.expanded .module-detail{{display:block}}
  .detail-section{{margin-bottom:14px}}
  .detail-label{{font-family:var(--font-mono);font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-muted);margin-bottom:4px}}
  .detail-content{{font-size:14px;line-height:1.6}}
  .detail-content ul{{list-style:none;padding:0}}
  .detail-content li{{padding:2px 0 2px 16px;position:relative;font-size:13.5px}}
  .detail-content li::before{{content:'\\2192';position:absolute;left:0;color:var(--track-color);font-size:12px}}
  .crosslink{{display:inline-block;font-family:var(--font-mono);font-size:11px;padding:2px 8px;border-radius:3px;margin:2px 4px 2px 0}}
  .crosslink.ce{{background:#2a3320;color:#a9c98a}}.crosslink.agent{{background:#1f2e25;color:#8fc7a8}}
  .crosslink.sdlc{{background:#2e2535;color:#bda9cf}}.crosslink.platform{{background:#1f2733;color:#8fb0d6}}
  .lab-tag{{display:inline-block;font-family:var(--font-mono);font-size:10px;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:3px;margin-right:6px}}
  .lab-tag.understand{{background:rgba(76,175,130,0.16);color:#8fd9b4}}.lab-tag.build{{background:rgba(111,147,201,0.16);color:#9bbbe6}}
  .analogy-box{{background:rgba(212,197,169,0.05);border-left:3px solid var(--gold);padding:10px 14px;border-radius:0 4px 4px 0;font-size:13.5px;color:#c4bfb5;font-style:italic;margin-top:8px}}
  .appendix{{max-width:860px;margin:0 auto;padding:0 24px 48px}}
  .appendix h2{{font-family:var(--font-display);font-size:20px;font-weight:500;margin-bottom:16px}}
  .xref-table{{width:100%;border-collapse:collapse;font-size:13px}}
  .xref-table th{{font-family:var(--font-mono);font-size:10px;letter-spacing:1.5px;text-transform:uppercase;text-align:left;padding:8px 12px;border-bottom:2px solid var(--text-muted);color:var(--text-muted)}}
  .xref-table td{{padding:8px 12px;border-bottom:1px solid var(--border);vertical-align:top}}
  .xref-table tr:hover{{background:var(--surface)}}
  @media(max-width:600px){{.hero{{padding:36px 20px 32px}}.track-nav{{gap:4px}}.track-nav button{{font-size:10px;padding:5px 10px}}.ecosystem-flow{{flex-direction:column;gap:4px}}.eco-arrow{{transform:rotate(90deg)}}}}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-eyebrow">New Course — agenticai.varasrinivas.com</div>
  <h1>Production LLMOps<br><em>AI Application Lifecycle</em></h1>
  <p class="hero-sub">The "day 2" discipline — evaluating, deploying, monitoring, upgrading, and governing LLM applications in production. Everything that happens after "it works on my laptop."</p>
  <div class="domain-chip">Domain anchor: Prior Authorization Determination Pipeline</div>
  <div class="launch-row"><a class="launch-btn" href="course/index.html">Launch the interactive course &#8594;</a></div>
  <div class="hero-stats">
    <div class="hero-stat"><span class="num">{len(MODS)}</span><span class="label">Modules</span></div>
    <div class="hero-stat"><span class="num">{len(TRACK_META)}</span><span class="label">Tracks</span></div>
    <div class="hero-stat"><span class="num">{len(MODS)*2}</span><span class="label">Labs</span></div>
    <div class="hero-stat"><span class="num">{total_links}</span><span class="label">Ecosystem Links</span></div>
  </div>
</div>

<div class="positioning">
  <div class="ecosystem-box">
    <h2>Agentic AI Five-Pillar Curriculum</h2>
    <div class="ecosystem-flow">
      <div class="eco-pill linked">Context Eng.<br><span style="font-size:10px;opacity:.7">Science</span></div>
      <span class="eco-arrow">&#8594;</span>
      <div class="eco-pill linked">AI Agents<br><span style="font-size:10px;opacity:.7">Applied</span></div>
      <span class="eco-arrow">&#8594;</span>
      <div class="eco-pill linked">AI Platform<br><span style="font-size:10px;opacity:.7">Infrastructure</span></div>
      <span class="eco-arrow">&#8594;</span>
      <div class="eco-pill active">LLMOps<br><span style="font-size:10px;opacity:.7">Operations</span></div>
      <span class="eco-arrow">&#8594;</span>
      <div class="eco-pill linked">AI-SDLC<br><span style="font-size:10px;opacity:.7">Process</span></div>
    </div>
    <p class="ecosystem-note">LLMOps is the operational discipline — it runs on the AI Platform, operates the Agents, and integrates into the AI-SDLC.<br>Target audience: ML engineers, SREs, DevOps engineers, and engineering managers running AI in production.</p>
  </div>
</div>

<div class="track-nav" id="trackNav">
  {nav_buttons()}
</div>

<div class="tracks-container" id="tracksContainer"></div>

<div class="appendix" id="appendix">
  <h2>Ecosystem Cross-Reference Map</h2>
  <table class="xref-table">
    <thead><tr><th>LLMOps Module</th><th>Other Course</th><th>Relationship</th></tr></thead>
    <tbody>
{xref_rows()}
    </tbody>
  </table>
</div>

<script>
const TRACKS = {json.dumps(TRACKS, ensure_ascii=False)};
function renderTracks(){{const c=document.getElementById('tracksContainer');c.innerHTML='';TRACKS.forEach(track=>{{const el=document.createElement('div');el.className='track visible';el.dataset.track=track.id;el.style.setProperty('--track-color',track.color);let mhtml='';track.modules.forEach(mod=>{{const cl=mod.crosslinks.map(x=>`<span class="crosslink ${{x.type}}">${{x.label}}</span>`).join('');const topics=mod.topics.map(t=>`<li>${{t}}</li>`).join('');const labs=mod.labs.map((l,i)=>`<span class="lab-tag ${{i===0?'understand':'build'}}">${{i===0?'Understand':'Build'}}</span> ${{l}}`).join('<br>');mhtml+=`<div class="module-card" onclick="this.classList.toggle('expanded')"><div class="module-top"><span class="module-id">${{mod.id}}</span><span class="module-name">${{mod.name}}</span><a class="module-open" href="course/index.html#${{mod.id}}" onclick="event.stopPropagation()" title="Open this module in the course">Open &#8594;</a><span class="module-expand">&#9654;</span></div><div class="module-detail"><div class="detail-section"><div class="detail-label">Key Topics</div><div class="detail-content"><ul>${{topics}}</ul></div></div><div class="detail-section"><div class="detail-label">Everyday Analogy</div><div class="analogy-box">${{mod.analogy}}</div></div><div class="detail-section"><div class="detail-label">Dual-Path Labs</div><div class="detail-content">${{labs}}</div></div>${{cl?`<div class="detail-section"><div class="detail-label">Cross-links</div><div class="detail-content">${{cl}}</div></div>`:''}}</div></div>`;}});el.innerHTML=`<div class="track-header"><span class="track-num">${{track.num}}</span><span class="track-title">${{track.icon}} ${{track.title}}</span></div><p class="track-desc">${{track.desc}}</p>${{mhtml}}`;c.appendChild(el);}});}}
document.getElementById('trackNav').addEventListener('click',e=>{{if(e.target.tagName!=='BUTTON')return;document.querySelectorAll('.track-nav button').forEach(b=>b.classList.remove('active'));e.target.classList.add('active');const f=e.target.dataset.track;document.querySelectorAll('.track').forEach(t=>{{t.classList.toggle('visible',f==='all'||t.dataset.track===f);}});document.getElementById('appendix').style.display=f==='all'?'block':'none';}});
renderTracks();
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("Wrote %s (%d modules, %d KB)" % (OUT, len(MODS), len(HTML)//1024))
