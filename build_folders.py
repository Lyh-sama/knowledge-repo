# -*- coding: utf-8 -*-
import json, os

def C(*a): return "".join(chr(x) for x in a)

# Exact data from original category.html
cats = {
  'math-analysis': {
    'name': C(0x6570,0x5B66,0x5206,0x6790), 'icon': 'fa-chart-line',
    'desc': C(0x6781,0x9650)+'\u3001'+C(0x5BFC,0x6570)+'\u3001'+C(0x79EF,0x5206)+'\u3001'+C(0x7EA7,0x6570)+'\uFF0C'+C(0x5206,0x6790,0x5B66,0x7684,0x57FA,0x7840,0x4E0E,0x6838,0x5FC3)+'\u3002',
    'docs': [
      {'name': C(0x6885,0x52A0,0x5F3A)+' \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790,0x8BB2,0x4E49), 'meta': 'PDF \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790), 'file': 'Mei-Jiaqiang-Mathematical-Analysis.pdf'},
      {'name': C(0x5F90,0x68EE,0x6797)+' \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790)+' ('+C(0x7B2C)+'2'+C(0x518C)+')', 'meta': 'PDF \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790), 'file': 'Xu-Senlin-Mathematical-Analysis-2.pdf'},
      {'name': C(0x5F90,0x68EE,0x6797)+' \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790)+' ('+C(0x7B2C)+'3'+C(0x518C)+')', 'meta': 'PDF \u00B7 '+C(0x6570,0x5B66,0x5206,0x6790), 'file': 'Xu-Senlin-Mathematical-Analysis-3.pdf'},
    ]
  },
  'real-analysis': {
    'name': C(0x5B9E,0x5206,0x6790), 'icon': 'fa-sigma', 'docs': []
  },
  'linear-algebra': {
    'name': C(0x7EBF,0x6027,0x4EE3,0x6570), 'icon': 'fa-calculator',
    'desc': C(0x5411,0x91CF,0x7A7A,0x95F4)+'\u3001'+C(0x77E9,0x9635,0x53D8,0x6362)+'\u3001'+C(0x7279,0x5F81,0x503C)+'\uFF0C'+C(0x73B0,0x4EE3,0x6570,0x5B66,0x7684,0x57FA,0x77F3)+'\u3002',
    'docs': []
  },
  'abstract-algebra': {
    'name': C(0x62BD,0x8C61,0x4EE3,0x6570), 'icon': 'fa-shapes', 'docs': []
  },
  'probability': {
    'name': C(0x6982,0x7387,0x8BBA), 'icon': 'fa-dice',
    'desc': C(0x968F,0x673A,0x53D8,0x91CF)+'\u3001'+C(0x5206,0x5E03)+'\u3001'+C(0x6781,0x9650,0x5B9A,0x7406)+'\uFF0C'+C(0x4E0D,0x786E,0x5B9A,0x6027,0x7684,0x6570,0x5B66,0x8BED,0x8A00)+'\u3002',
    'docs': [
      {'name': 'Durrett \u00B7 '+C(0x6982,0x7387,0x8BBA)+' ('+C(0x7B2C)+'5'+C(0x7248)+')', 'meta': 'PDF \u00B7 '+C(0x6982,0x7387,0x8BBA), 'file': 'durrett.pdf'},
      {'name': 'Durrett \u00B7 '+C(0x4E60,0x9898,0x89E3,0x7B54)+' ('+C(0x7B2C)+'5'+C(0x7248)+')', 'meta': 'PDF \u00B7 '+C(0x6982,0x7387,0x8BBA), 'file': 'durrett-5e-solutions.pdf'},
    ]
  },
  'statistics': {
    'name': C(0x6570,0x7406,0x7EDF,0x8BA1), 'icon': 'fa-chart-simple',
    'desc': C(0x4F30,0x8BA1)+'\u3001'+C(0x68C0,0x9A8C)+'\u3001'+C(0x56DE,0x5F52)+'\uFF0C'+C(0x4ECE,0x6570,0x636E,0x4E2D,0x63D0,0x53D6,0x4FE1,0x606F,0x7684,0x65B9,0x6CD5,0x8BBA)+'\u3002',
    'docs': [
      {'name': 'Casella & Berger \u00B7 '+C(0x7EDF,0x8BA1,0x63A8,0x65AD), 'meta': 'PDF \u00B7 '+C(0x6570,0x7406,0x7EDF,0x8BA1), 'file': 'Casella-Berger-Statistical-Inference.pdf'},
    ] + [
      {'name': 'HW '+str(i)+' '+C(0x7B54,0x6848), 'meta': 'PDF \u00B7 '+C(0x6570,0x7406,0x7EDF,0x8BA1), 'file': 'hw'+str(i)+'-ans.pdf'} for i in range(1,16)
    ] + [
      {'name': C(0x9648,0x5BB6,0x9F0E)+' \u00B7 '+C(0x8BB2,0x4E49)+' part'+str(i), 'meta': 'PDF \u00B7 '+C(0x6570,0x7406,0x7EDF,0x8BA1), 'file': 'Chen-Jiading-Statistics-Lecture-3rd-part'+str(i)+'.pdf'} for i in range(1,11)
    ] + [
      {'name': C(0x8865,0x5145,0x8D44,0x6599), 'meta': 'PDF \u00B7 '+C(0x6570,0x7406,0x7EDF,0x8BA1), 'file': 'stat.pdf'},
    ]
  },
  'differential-geometry': {
    'name': C(0x5FAE,0x5206,0x51E0,0x4F55), 'icon': 'fa-draw-polygon',
    'desc': C(0x6D41,0x5F62)+'\u3001'+C(0x66F2,0x7387)+'\u3001'+C(0x8054,0x7EDC)+'\uFF0C'+C(0x51E0,0x4F55,0x7684,0x73B0,0x4EE3,0x8BED,0x8A00)+'\u3002',
    'docs': [
      {'name': C(0x5FAE,0x5206,0x51E0,0x4F55,0x8BB2,0x4E49), 'meta': 'PDF \u00B7 '+C(0x5FAE,0x5206,0x51E0,0x4F55), 'file': 'Differential-Geometry-Lecture.pdf'},
      {'name': C(0x9648,0x7EF4,0x6853)+' \u00B7 '+C(0x5FAE,0x5206,0x51E0,0x4F55), 'meta': 'PDF \u00B7 '+C(0x5FAE,0x5206,0x51E0,0x4F55), 'file': 'Chen-Weihuan-Differential-Geometry.pdf'},
    ]
  },
  'functional-analysis': {
    'name': C(0x6CDB,0x51FD,0x5206,0x6790), 'icon': 'fa-infinity',
    'desc': C(0x65E0,0x9650,0x7EF4,0x7A7A,0x95F4)+'\u3001'+C(0x7B97,0x5B50,0x7406,0x8BBA)+'\uFF0C'+C(0x5206,0x6790,0x7684,0x51E0,0x4F55,0x5316,0x89C6,0x89D2)+'\u3002',
    'docs': [
      {'name': 'Ch 0 '+C(0x5F15,0x8A00), 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt0-Intro-ppt.pdf'},
      {'name': 'Ch 6 Sec 1', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec01-ppt.pdf'},
      {'name': 'Ch 6 Sec 2', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec02-ppt-No-Pause.pdf'},
      {'name': 'Ch 6 Sec 3', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec03-ppt.pdf'},
      {'name': 'Ch 6 Sec 4', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec04-ppt.pdf'},
      {'name': 'Ch 6 Sec 5', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec05-ppt.pdf'},
      {'name': 'Ch 6 Sec 6', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt06-Sec06-ppt.pdf'},
      {'name': 'Ch 7 Sec 1', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt07-Sec01-ppt.pdf'},
      {'name': 'Ch 7 Sec 2', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt07-Sec02-ppt.pdf'},
      {'name': 'Ch 7 Sec 3', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt07-Sec03-ppt.pdf'},
      {'name': 'Ch 7 Sec 4', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt07-Sec04-ppt.pdf'},
      {'name': 'Ch 8 Sec 1', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect01-ppt.pdf'},
      {'name': 'Ch 8 Sec 2', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect02-ppt.pdf'},
      {'name': 'Ch 8 Sec 3', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect03-ppt.pdf'},
      {'name': 'Ch 8 Sec 4', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect04-ppt.pdf'},
      {'name': 'Ch 8 Sec 5', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect05-ppt.pdf'},
      {'name': 'Ch 8 Sec 6', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect06-ppt.pdf'},
      {'name': 'Ch 8 Sec 7', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-chpt08-sect07-ppt.pdf'},
      {'name': 'Ch 9 Sec 1-2', 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Chpt09-Sec01-Sec02-ppt.pdf'},
      {'name': C(0x671F,0x672B,0x590D,0x4E60), 'meta': 'PDF \u00B7 '+C(0x6CDB,0x51FD,0x5206,0x6790), 'file': '2026-Final-Review.pdf'},
    ]
  },
  'quantum-info': {
    'name': C(0x91CF,0x5B50,0x4FE1,0x606F,0x4E0E,0x91CF,0x5B50,0x8BA1,0x7B97), 'icon': 'fa-atom',
    'desc': C(0x91CF,0x5B50,0x6BD4,0x7279)+'\u3001'+C(0x91CF,0x5B50,0x95E8)+'\u3001'+C(0x91CF,0x5B50,0x7EA0,0x9519)+'\uFF0C'+C(0x4FE1,0x606F,0x4E0E,0x7269,0x7406,0x7684,0x4EA4,0x6C47)+'\u3002',
    'docs': [
      {'name': 'Nielsen \u00B7 '+C(0x91CF,0x5B50,0x7EA0,0x9519), 'meta': 'PDF \u00B7 '+C(0x91CF,0x5B50,0x4FE1,0x606F,0x4E0E,0x91CF,0x5B50,0x8BA1,0x7B97), 'file': 'Nielsen.pdf'},
      {'name': 'QECCbook 2026 \u00B7 '+C(0x91CF,0x7EA0,0x9519,0x7801,0x6559,0x6750), 'meta': 'PDF \u00B7 '+C(0x91CF,0x5B50,0x4FE1,0x606F,0x4E0E,0x91CF,0x5B50,0x8BA1,0x7B97), 'file': 'QECCbook-2026.pdf'},
    ]
  },
}

# Folder-to-category-key mapping
folders = {
    'analysis': ['math-analysis', 'real-analysis', 'functional-analysis'],
    'algebra': ['linear-algebra', 'abstract-algebra'],
    'probability': ['probability', 'statistics'],
    'geometry': ['differential-geometry'],
    'quantum': ['quantum-info'],
}

folder_names = {
    'analysis': C(0x5206,0x6790),
    'algebra': C(0x4EE3,0x6570),
    'probability': C(0x6982,0x7387,0x4E0E,0x7EDF,0x8BA1),
    'geometry': C(0x51E0,0x4F55),
    'quantum': C(0x91CF,0x5B50),
}

base = r'C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI'

def make_html(folder_key):
    sub_keys = folders[folder_key]
    all_docs = []
    sections = []
    for sk in sub_keys:
        cat = cats[sk]
        sections.append({'name': cat['name'], 'docs': cat['docs']})
        all_docs.extend(cat['docs'])
    
    docs_json = json.dumps(sections, ensure_ascii=False)
    cat_name = folder_names[folder_key]
    
    html = u'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + cat_name + ''' — りく様の世界</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
:root{--bg-dark:#0a0a1a;--accent-pink:#ff6b9d;--accent-purple:#c084fc;--text-primary:#f1f0fb;--text-secondary:#a5a3c4;--glass-bg:rgba(255,255,255,.04);--glass-border:rgba(255,255,255,.06)}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei","Hiragino Sans GB","WenQuanYi Micro Hei",sans-serif;background:var(--bg-dark);color:var(--text-primary);min-height:100vh}
::selection{background:var(--accent-pink);color:#fff}

.navbar{display:flex;align-items:center;gap:1rem;padding:1rem 2rem;background:rgba(10,10,26,.9);backdrop-filter:blur(12px);border-bottom:1px solid var(--glass-border);position:sticky;top:0;z-index:10}
.nav-back{display:inline-flex;align-items:center;gap:.4rem;color:var(--text-secondary);font-size:.85rem;text-decoration:none;transition:color .3s}
.nav-back:hover{color:var(--accent-purple)}
.nav-title{font-family:"Noto Serif SC",serif;font-size:1.1rem;font-weight:600;color:var(--text-primary)}

.hero{position:relative;padding:4rem 2rem 3rem;text-align:center;background:linear-gradient(to bottom,rgba(192,132,252,.08),transparent)}
.hero-icon{width:64px;height:64px;margin:0 auto 1rem;background:linear-gradient(135deg,rgba(192,132,252,.15),rgba(255,107,157,.15));border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:1.6rem;color:var(--accent-purple)}
.hero h1{font-family:"Noto Serif SC",serif;font-size:2rem;font-weight:700;margin-bottom:.25rem;background:linear-gradient(135deg,#d4b0ff,var(--accent-purple) 35%,var(--accent-pink) 65%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero .count{color:var(--text-secondary);font-size:.85rem}

main{max-width:900px;margin:0 auto;padding:0 2rem 5rem}
.sub-section{margin-bottom:2.5rem}
.sub-title{font-family:"Noto Serif SC",serif;font-size:1.25rem;font-weight:600;color:var(--text-primary);margin-bottom:.75rem;padding-left:.75rem;border-left:3px solid var(--accent-purple)}
.doc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:.6rem}
.doc-card{display:flex;align-items:center;gap:.8rem;padding:.85rem 1rem;background:var(--glass-bg);border:1px solid var(--glass-border);border-radius:6px;text-decoration:none;color:inherit;transition:border-color .3s,background .3s}
.doc-card:hover{border-color:rgba(192,132,252,.3);background:rgba(255,255,255,.06)}
.doc-icon{width:36px;height:36px;background:rgba(192,132,252,.12);border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--accent-purple);font-size:1rem;flex-shrink:0}
.doc-info{flex:1;min-width:0}
.doc-info .doc-name{font-size:.85rem;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:2px}
.doc-info .doc-meta{font-size:.68rem;color:var(--text-secondary)}
.doc-dl{color:var(--accent-purple);font-size:.8rem;opacity:0;transition:opacity .3s}
.doc-card:hover .doc-dl{opacity:1}
.empty{text-align:center;padding:2rem;color:var(--text-secondary);font-size:.85rem;border:1px dashed var(--glass-border);border-radius:6px}

@media(max-width:480px){main{padding:0 1rem 4rem}.hero{padding:3rem 1rem 2rem}}
</style>
</head>
<body>
<nav class="navbar">
  <a href="../index.html#categories" class="nav-back"><i class="fa-solid fa-arrow-left"></i> ''' + C(0x8FD4,0x56DE) + '''</a>
  <span class="nav-title">''' + cat_name + '''</span>
</nav>
<div class="hero">
  <div class="hero-icon"><i class="fa-solid fa-folder-open"></i></div>
  <h1>''' + cat_name + '''</h1>
  <p class="count" id="docCount"></p>
</div>
<main id="content"></main>
<script>
var sections = ''' + docs_json + ''';
var total = 0;
var html = "";
sections.forEach(function(sec){
  html += '<div class="sub-section"><h2 class="sub-title">' + sec.name + '</h2>';
  if (sec.docs.length === 0) {
    html += '<div class="empty">''' + C(0x6682,0x65E0,0x8D44,0x6599) + '''</div>';
  } else {
    html += '<div class="doc-grid">';
    sec.docs.forEach(function(d){
      total++;
      html += '<a href="../' + d.file + '" class="doc-card" target="_blank">';
      html += '<div class="doc-icon"><i class="fa-solid fa-file-pdf"></i></div>';
      html += '<div class="doc-info"><div class="doc-name">' + d.name + '</div><div class="doc-meta">' + d.meta + '</div></div>';
      html += '<span class="doc-dl"><i class="fa-solid fa-download"></i></span>';
      html += '</a>';
    });
    html += '</div>';
  }
  html += '</div>';
});
document.getElementById("content").innerHTML = html;
document.getElementById("docCount").textContent = total + " ''' + C(0x4EFD,0x8D44,0x6599) + '''";
</script>
</body>
</html>'''
    return html

for folder_key in folders:
    html = make_html(folder_key)
    path = os.path.join(base, folder_key, 'index.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Written {folder_key}/index.html ({len(html)} bytes)")

print("ALL DONE")