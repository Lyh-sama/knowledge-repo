# -*- coding: utf-8 -*-
import re

path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Fix panel numbers to English upppercase
numbers = [
    ("01 / ANALYSIS", "01 / "+chr(0x5206)+chr(0x6790)),  # was 01 / 分析
    ("02 / ALGEBRA", "02 / "+chr(0x4EE3)+chr(0x6570)),   # was 02 / 代数
    ("03 / PROB & STATS", "03 / "+chr(0x6982)+chr(0x7387)+chr(0x4E0E)+chr(0x7EDF)+chr(0x8BA1)),  # was 03 / 概率与统计
    ("04 / GEOMETRY", "04 / "+chr(0x51E0)+chr(0x4F55)),   # was 04 / 几何
    ("05 / QUANTUM", "05 / "+chr(0x91CF)+chr(0x5B50)),    # was 05 / 量子
]

for eng, cn in numbers:
    c = c.replace('<div class="panel-number">'+cn+'</div>', '<div class="panel-number">'+eng+'</div>')

# 2. Fix panel-title font-family: change 'Noto Serif SC',serif to match body font
body_font = '"PingFang SC","Microsoft YaHei","Hiragino Sans GB","WenQuanYi Micro Hei",sans-serif'
c = c.replace("font-family:'Noto Serif SC',serif;font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.08em;margin-bottom:.4rem",
               "font-family:"+body_font+";font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.08em;margin-bottom:.4rem")

print("Panel numbers before:", sum(1 for _ in re.finditer(r'<div class="panel-number">', c)))
with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")