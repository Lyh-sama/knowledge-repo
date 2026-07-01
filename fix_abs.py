path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add position:relative to panel-overlay
c = c.replace(
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease}",
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease;padding-bottom:42px}"
)

# Change .panel-subs to absolute positioning (no layout space)
c = c.replace(
    ".panel-subs{display:flex;flex-wrap:wrap;gap:.5rem;opacity:0;transform:translateY(10px);transition:opacity .4s ease .2s,transform .4s ease .2s}",
    ".panel-subs{position:absolute;bottom:8px;left:0;right:0;display:flex;flex-wrap:wrap;gap:.5rem;padding:0 3.5rem;opacity:0;transform:translateY(6px);transition:opacity .4s ease .2s,transform .4s ease .2s}")

# First panel subs also need matching padding
c = c.replace(
    ".panel:first-child .panel-overlay{padding-left:2rem}",
    ".panel:first-child .panel-overlay{padding-left:2rem}.panel:first-child .panel-subs{padding:0 2rem}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")