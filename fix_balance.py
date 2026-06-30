import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Active set (third CSS block): add flex:0.75 to first-child and last-child
# .panel:first-child line
old_first = ".panel:first-child{clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:0}"
new_first = ".panel:first-child{flex:0.75;clip-path:polygon(0 0,100% 0,calc(100% - 120px) 100%,0 100%);margin-left:0}"
c = c.replace(old_first, new_first)

# .panel:last-child (on the hover line)
old_last = ".panel:last-child{clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)}"
new_last = ".panel:last-child{flex:0.75;clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)}"
c = c.replace(old_last, new_last)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")