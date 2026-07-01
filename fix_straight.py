import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace the active panels CSS (third set, has .panels ancestor)
# Change: only right edge slanted, fixed pixel cut using calc(), left edge straight
old_panel = ".panel{flex:1;position:relative;overflow:hidden;clip-path:polygon(18% 0,100% 0,82% 100%,0 100%);margin-left:-7%;transition:flex .6s cubic-bezier(.25,.46,.45,.94);border-right:1px solid rgba(255,255,255,.08);cursor:pointer;text-decoration:none;color:inherit;display:block}"
new_panel = ".panel{flex:1;position:relative;overflow:hidden;clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;transition:flex .6s cubic-bezier(.25,.46,.45,.94);cursor:pointer;text-decoration:none;color:inherit;display:block}"
c = c.replace(old_panel, new_panel)

# Add last-child rule to remove slant on the last panel
# Insert after .panel:hover{flex:3.2;z-index:2}
insert_after = ".panel:hover{flex:3.2;z-index:2}"
last_child_rule = ".panel:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}"
c = c.replace(insert_after, insert_after + last_child_rule)

# Also remove border-right from .panel since we don't need separator lines anymore
c = c.replace(
    ".panel:first-child{margin-left:0}",
    ".panel:first-child{margin-left:0;border-right:1px solid rgba(255,255,255,.08)}"
)

# Fix the old panel rules too (first and second sets)
old1 = ".panel{display:block;position:relative;flex:1;overflow:hidden;clip-path:polygon(18% 0,100% 0,82% 100%,0 100%);margin-left:-7%;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}"
new1 = ".panel{display:block;position:relative;flex:1;overflow:hidden;clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:-120px;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}"
c = c.replace(old1, new1)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")