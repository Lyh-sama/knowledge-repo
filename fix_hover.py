path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace the hover + last-child line to add hover overrides for first/last
old = ".panel:hover{flex:3.2;z-index:2}.panel:last-child{flex:0.75;clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)}"
new = ".panel:hover{flex:3.2;z-index:2}.panel:last-child{flex:0.75;clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)}.panel:first-child:hover,.panel:last-child:hover{flex:3.2;z-index:2}"
c = c.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")