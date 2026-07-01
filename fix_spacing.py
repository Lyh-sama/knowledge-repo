path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add tighter letter-spacing for first panel's number
old = ".panel:first-child .panel-overlay{padding-left:2rem}"
new = ".panel:first-child .panel-overlay{padding-left:2rem}.panel:first-child .panel-number{letter-spacing:.15em}"
c = c.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")