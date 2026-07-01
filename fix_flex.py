path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Make overlay fill full panel height with flex to bottom-align content
old = ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease}.panel:first-child .panel-overlay{padding-left:2rem}"
new = ".panel-overlay{position:absolute;top:0;bottom:0;left:0;right:0;display:flex;flex-direction:column;justify-content:flex-end;padding:2rem 2rem 2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease}.panel:first-child .panel-overlay{padding-left:2rem}"
c = c.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")