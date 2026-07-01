path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Fix: lower sub-link z-index and add pointer-events:none to hidden sub-links
c = c.replace(
    ".sub-link{display:inline-block;padding:4px 12px;font-size:.68rem;color:rgba(200,200,200,.65);border:1px solid rgba(200,200,200,.2);text-decoration:none;position:relative;z-index:10;transition:background .3s,color .3s,border-color .3s}",
    ".sub-link{display:inline-block;padding:4px 12px;font-size:.68rem;color:rgba(200,200,200,.65);border:1px solid rgba(200,200,200,.2);text-decoration:none;position:relative;z-index:1;transition:background .3s,color .3s,border-color .3s}"
)

# Add pointer-events:none to panel-subs (hidden state) and auto on hover
c = c.replace(
    ".panel-subs{position:absolute;bottom:8px;left:0;right:0;display:flex;flex-wrap:wrap;gap:.5rem;padding:0 3.5rem;opacity:0;transform:translateY(6px);transition:opacity .4s ease .2s,transform .4s ease .2s}",
    ".panel-subs{position:absolute;bottom:8px;left:0;right:0;display:flex;flex-wrap:wrap;gap:.5rem;padding:0 3.5rem;opacity:0;transform:translateY(6px);transition:opacity .4s ease .2s,transform .4s ease .2s;pointer-events:none}"
)
c = c.replace(
    ".panel:hover .panel-subs{opacity:1;transform:translateY(0)}",
    ".panel:hover .panel-subs{opacity:1;transform:translateY(0);pointer-events:auto}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")