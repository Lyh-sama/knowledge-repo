import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Target the active panel CSS (third set, ~line 235 area)
# Replace the .panel base rule
old_panel = ".panel{flex:1;position:relative;overflow:hidden;clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;transition:flex .6s cubic-bezier(.25,.46,.45,.94);cursor:pointer;text-decoration:none;color:inherit;display:block}"
new_panel = ".panel{flex:1;position:relative;overflow:hidden;clip-path:polygon(120px 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;transition:flex .6s cubic-bezier(.25,.46,.45,.94);cursor:pointer;text-decoration:none;color:inherit;display:block}"
c = c.replace(old_panel, new_panel)

# Fix first-child: straight left edge
old_first = ".panel:first-child{margin-left:0;border-right:1px solid rgba(255,255,255,.08)}"
new_first = ".panel:first-child{clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:0}"
c = c.replace(old_first, new_first)

# Fix last-child: straight right edge + keep last-child rule
# Current: .panel:hover{flex:3.2;z-index:2}.panel:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}
old_hover_last = ".panel:hover{flex:3.2;z-index:2}.panel:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}"
new_hover_last = ".panel:hover{flex:3.2;z-index:2}.panel:last-child{clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)}"
c = c.replace(old_hover_last, new_hover_last)

# Fix mobile: clip-path:none for all panel variants
old_mobile = "@media(max-width:768px){.panels,.panel{clip-path:none;margin-left:0;height:220px;border-right:none;border-bottom:1px solid rgba(255,255,255,.08)}.panel:hover{flex:1}.panel:last-child{border-bottom:none}}"
new_mobile = "@media(max-width:768px){.panels,.panel,.panel:first-child,.panel:last-child{clip-path:none;margin-left:0;height:220px;border:none;border-bottom:1px solid rgba(255,255,255,.08)}.panel:hover{flex:1}.panel:last-child{border-bottom:none}}"
c = c.replace(old_mobile, new_mobile)

# Also fix the older panel CSS sets (first and second sets)
# First set
old1 = ".panel{display:block;position:relative;flex:1;overflow:hidden;clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}"
new1 = ".panel{display:block;position:relative;flex:1;overflow:hidden;clip-path:polygon(120px 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}"
c = c.replace(old1, new1)

# Also fix first-child in first set
old1f = ".panel:first-child{margin-left:0;border-left:none}"
new1f = ".panel:first-child{clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:0;border-left:none}"
c = c.replace(old1f, new1f)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")