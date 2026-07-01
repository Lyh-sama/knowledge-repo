# -*- coding: utf-8 -*-
import re

path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

def C(*args):
    return ''.join(chr(a) for a in args)

# Panel data: (onclick_href, bg_image, number, title, [(sub_name, sub_href), ...])
panels = [
    ("category.html#analysis", "card-bg-7.jpg", "01 / "+C(0x5206,0x6790), C(0x5206,0x6790), [
        (C(0x6570,0x5B66,0x5206,0x6790), "category.html#math-analysis"),
        (C(0x5B9E,0x5206,0x6790), "category.html#real-analysis"),
        (C(0x6CDB,0x51FD,0x5206,0x6790), "category.html#functional-analysis"),
    ]),
    ("category.html#algebra", "card-bg-5.jpg", "02 / "+C(0x4EE3,0x6570), C(0x4EE3,0x6570), [
        (C(0x7EBF,0x6027,0x4EE3,0x6570), "category.html#linear-algebra"),
        (C(0x62BD,0x8C61,0x4EE3,0x6570), "category.html#abstract-algebra"),
    ]),
    ("category.html#probability", "card-bg-1.jpg", "03 / "+C(0x6982,0x7387,0x4E0E,0x7EDF,0x8BA1), C(0x6982,0x7387,0x4E0E,0x7EDF,0x8BA1), [
        (C(0x6982,0x7387,0x8BBA), "category.html#probability"),
        (C(0x6570,0x7406,0x7EDF,0x8BA1), "category.html#statistics"),
    ]),
    ("category.html#differential-geometry", "card-bg-6.jpg", "04 / "+C(0x51E0,0x4F55), C(0x51E0,0x4F55), [
        (C(0x5FAE,0x5206,0x51E0,0x4F55), "category.html#differential-geometry"),
    ]),
    ("category.html#quantum-info", "card-bg-2.jpg", "05 / "+C(0x91CF,0x5B50), C(0x91CF,0x5B50), [
        (C(0x91CF,0x5B50,0x4FE1,0x606F,0x4E0E,0x91CF,0x5B50,0x8BA1,0x7B97), "category.html#quantum-info"),
    ]),
]

base = "https://lyh-sama.github.io/Riku_sama_no_SEKAI/"

new_panels = ""
for onclick, bg, num, title, subs in panels:
    subs_html = "".join('<a href="{}" class="sub-link" onclick="event.stopPropagation()">{}</a>'.format(sub_href, sub_name) for sub_name, sub_href in subs)
    panel = '''        <div class="panel" onclick="location.href='{onclick}'">
          <div class="panel-bg" style="background-image:url('{base}{bg}')"></div>
          <div class="panel-overlay">
            <div class="panel-number">{num}</div>
            <div class="panel-title">{title}</div>
            <div class="panel-subs">{subs}</div>
          </div>
        </div>
'''.format(onclick=onclick, base=base, bg=bg, num=num, title=title, subs=subs_html)
    new_panels += panel

# Replace the entire <section id="categories"> block
section_label = C(0x4E16,0x754C,0x7684,0x77E5,0x8BC6,0x5E93)
section_title = C(0x77E5,0x8BC6,0x5206,0x7C7B)

new_section = '''<section id="categories">
  <div class="section-inner">

    <div class="section-label reveal">{label}</div>
    <h2 class="section-title reveal" style="display:inline-block">{title}</h2>

    <div class="panels-wrap">
      <div class="panels">
{panels}
      </div>
    </div>

  </div>
</section>'''.format(label=section_label, title=section_title, panels=new_panels.rstrip())

# Replace from <section id="categories"> to </section>
c = re.sub(r'<section id="categories">.*?</section>', new_section, c, flags=re.DOTALL)

# Also remove any remaining "hover for subjects" hints
c = re.sub(r'<div class="panel-hint">[^<]*</div>\n?', '', c)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")