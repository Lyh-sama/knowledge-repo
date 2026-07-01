# -*- coding: utf-8 -*-
import os

def C(*args):
    return "".join(chr(a) for a in args)

# Category data: sub-topics and their materials
cats = {
    "analysis": {
        "name": C(0x5206, 0x6790),  # 分析
        "bg": "card-bg-7.jpg",
        "subs": [
            {
                "name": C(0x6570, 0x5B66, 0x5206, 0x6790),  # 数学分析
                "id": "math-analysis",
                "docs": [
                    {"name": C(0x6885,0x52A0,0x5F3A)+" - "+C(0x6570,0x5B66,0x5206,0x6790), "file": "Mei-Jiaqiang-Mathematical-Analysis.pdf"},
                    {"name": "Chpt0 "+C(0x5BFC,0x8A00), "file": "2026-Chpt0-Intro-ppt.pdf"},
                ]
            },
            {
                "name": C(0x5B9E, 0x5206, 0x6790),  # 实分析
                "id": "real-analysis",
                "docs": [
                    {"name": C(0x5F90,0x68EE,0x6797)+" - "+C(0x5B9E,0x53D8,0x51FD,0x6570,0x8BBA), "file": "Xu-Senlin-Mathematical-Analysis-Exercises.pdf"},
                ]
            },
            {
                "name": C(0x6CDB, 0x51FD, 0x5206, 0x6790),  # 泛函分析
                "id": "functional-analysis",
                "docs": [
                    {"name": C(0x9648,0x7EF4,0x6853)+" - "+C(0x5FAE,0x5206,0x51E0,0x4F55,0x521D,0x6B65), "file": "Chen-Weihuan-Differential-Geometry.pdf"},
                ]
            },
        ]
    },
    "algebra": {
        "name": C(0x4EE3, 0x6570),  # 代数
        "bg": "card-bg-5.jpg",
        "subs": [
            {
                "name": C(0x7EBF, 0x6027, 0x4EE3, 0x6570),  # 线性代数
                "id": "linear-algebra",
                "docs": []
            },
            {
                "name": C(0x62BD, 0x8C61, 0x4EE3, 0x6570),  # 抽象代数
                "id": "abstract-algebra",
                "docs": []
            },
        ]
    },
    "probability": {
        "name": C(0x6982,0x7387,0x4E0E,0x7EDF,0x8BA1),  # 概率与统计
        "bg": "card-bg-1.jpg",
        "subs": [
            {
                "name": C(0x6982, 0x7387, 0x8BBA),  # 概率论
                "id": "probability",
                "docs": [
                    {"name": "Durrett - Probability: Theory and Examples", "file": "durrett.pdf"},
                    {"name": "Durrett 5e Solutions", "file": "durrett-5e-solutions.pdf"},
                ]
            },
            {
                "name": C(0x6570, 0x7406, 0x7EDF, 0x8BA1),  # 数理统计
                "id": "statistics",
                "docs": [
                    {"name": "Casella & Berger - Statistical Inference", "file": "Casella-Berger-Statistical-Inference.pdf"},
                    {"name": C(0x9648,0x5E0C,0x5B9A)+" - "+C(0x6570,0x7406,0x7EDF,0x8BA1)+" I-VIII", "file": "Chen-Jiading-Statistics-Vol1.pdf"},
                ]
            },
        ]
    },
    "differential-geometry": {
        "name": C(0x51E0, 0x4F55),  # 几何
        "bg": "card-bg-6.jpg",
        "subs": [
            {
                "name": C(0x5FAE, 0x5206, 0x51E0, 0x4F55),  # 微分几何
                "id": "differential-geometry",
                "docs": [
                    {"name": C(0x5FAE,0x5206,0x51E0,0x4F55)+" Notes", "file": "Differential-Geometry-Notes.pdf"},
                ]
            },
        ]
    },
    "quantum-info": {
        "name": C(0x91CF, 0x5B50),  # 量子
        "bg": "card-bg-2.jpg",
        "subs": [
            {
                "name": C(0x91CF,0x5B50,0x4FE1,0x606F,0x4E0E,0x91CF,0x5B50,0x8BA1,0x7B97),  # 量子信息与量子计算
                "id": "quantum-info",
                "docs": [
                    {"name": "Nielsen & Chuang", "file": "Nielsen.pdf"},
                    {"name": "QECC Book 2026", "file": "QECCbook-2026.pdf"},
                ]
            },
        ]
    },
}

base = "https://lyh-sama.github.io/Riku_sama_no_SEKAI/"

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>知识分类 — りく様の世界</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
:root{--bg-dark:#0a0a1a;--bg-card:rgba(255,255,255,.03);--text-primary:#e8e6f0;--text-secondary:rgba(200,200,210,.6);--accent-purple:#c084fc;--accent-pink:#ff6b9d;--accent-gold:#f0c060;--glass-bg:rgba(255,255,255,.04);--glass-border:rgba(255,255,255,.06);--transition:.3s ease}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei","Hiragino Sans GB","WenQuanYi Micro Hei",sans-serif;background:var(--bg-dark);color:var(--text-primary);min-height:100vh}
a{color:inherit;text-decoration:none}

.cat-hero{position:relative;min-height:35vh;display:flex;align-items:center;justify-content:center;overflow:hidden}
.cat-hero-bg{position:absolute;top:0;left:0;width:100%;height:100%;background-size:cover;background-position:center;filter:brightness(.35) grayscale(30%)}
.cat-hero::after{content:"";position:absolute;bottom:0;left:0;right:0;height:60%;background:linear-gradient(transparent,var(--bg-dark))}
.cat-hero-content{position:relative;z-index:1;text-align:center;padding:2rem}
.cat-back{display:inline-flex;align-items:center;gap:.5rem;color:var(--text-secondary);font-size:.85rem;margin-bottom:1.5rem;transition:color var(--transition)}
.cat-back:hover{color:var(--accent-purple)}
.cat-hero h1{font-family:"Noto Serif SC",serif;font-size:clamp(2.2rem,5vw,3.5rem);font-weight:700;background:linear-gradient(135deg,#d4b0ff,var(--accent-purple) 35%,var(--accent-pink) 65%,var(--accent-gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:.5rem}
.cat-hero .cat-sub{font-size:1.1rem;color:var(--text-secondary);font-weight:300}

.container{max-width:1000px;margin:0 auto;padding:3rem 2rem 6rem}

.section-header{margin-bottom:2.5rem}
.section-header h2{font-family:"Noto Serif SC",serif;font-size:1.6rem;font-weight:600;color:var(--text-primary);margin-bottom:.4rem}
.section-header p{color:var(--text-secondary);font-size:.9rem}

.doc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem}
.doc-card{background:var(--glass-bg);border:1px solid var(--glass-border);border-radius:6px;padding:1.2rem;display:flex;align-items:center;gap:1rem;transition:border-color var(--transition),background var(--transition)}
.doc-card:hover{border-color:rgba(192,132,252,.3);background:rgba(255,255,255,.06)}
.doc-icon{width:42px;height:42px;background:rgba(192,132,252,.12);border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--accent-purple);font-size:1.2rem;flex-shrink:0}
.doc-info{flex:1;min-width:0}
.doc-info .doc-name{font-size:.9rem;font-weight:500;color:var(--text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:2px}
.doc-info .doc-type{font-size:.7rem;color:var(--text-secondary)}
.doc-dl{display:flex;align-items:center;gap:.35rem;padding:8px 16px;background:rgba(192,132,252,.1);border:1px solid rgba(192,132,252,.2);border-radius:4px;color:var(--accent-purple);font-size:.75rem;transition:background var(--transition),border-color var(--transition);white-space:nowrap}
.doc-dl:hover{background:rgba(192,132,252,.2);border-color:rgba(192,132,252,.4)}

.empty-hint{color:var(--text-secondary);font-size:.9rem;padding:2rem;text-align:center;background:var(--glass-bg);border-radius:6px;border:1px dashed var(--glass-border)}

@media(max-width:768px){.doc-grid{grid-template-columns:1fr}.cat-hero{min-height:25vh}}
</style>
</head>
<body>

<div class="cat-hero" id="catHero">
  <div class="cat-hero-bg" id="catBg"></div>
  <div class="cat-hero-content">
    <a href="index.html" class="cat-back"><i class="fa-solid fa-arrow-left"></i> """ + C(0x8FD4,0x56DE,0x9996,0x9875) + """</a>
    <h1 id="catTitle"></h1>
    <p class="cat-sub id="catSub"></p>
  </div>
</div>

<div class="container" id="contentArea"></div>

<script>
const CATS = """ + cats.__repr__().replace("'", '"') + """;
const BASE = '""" + base + """';

function render(hash) {
  const key = (hash || 'analysis').replace('#','');
  const cat = CATS[key] || CATS['analysis'];
  document.title = cat.name + ' \u2014 \u308A\u304F\u69D8\u306E\u4E16\u754C';
  document.getElementById('catBg').style.backgroundImage = "url('"+BASE+cat.bg+"')";
  document.getElementById('catTitle').textContent = cat.name;
  document.getElementById('catSub').textContent = cat.subs.length + ' \u5B50\u4E13\u9898';
  
  let html = '';
  cat.subs.forEach(sub => {
    html += '<div class="section-header"><h2>'+sub.name+'</h2></div>';
    if (sub.docs.length === 0) {
      html += '<div class="empty-hint">\u6682\u65E0\u8D44\u6599</div>';
    } else {
      html += '<div class="doc-grid">';
      sub.docs.forEach(doc => {
        const ext = doc.file.split('.').pop().toUpperCase();
        html += '<a href="'+BASE+doc.file+'" class="doc-card" target="_blank">';
        html += '<div class="doc-icon"><i class="fa-solid fa-file-pdf"></i></div>';
        html += '<div class="doc-info"><div class="doc-name">'+doc.name+'</div><div class="doc-type">'+ext+'</div></div>';
        html += '<span class="doc-dl"><i class="fa-solid fa-download"></i> \u4E0B\u8F7D</span>';
        html += '</a>';
      });
      html += '</div>';
    }
  });
  document.getElementById('contentArea').innerHTML = html;
}

window.addEventListener('hashchange', function(){ render(location.hash); });
render(location.hash);
</script>

</body>
</html>"""

path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\category.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("DONE - category.html written,", len(html), "bytes")