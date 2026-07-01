import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add font-smoothing to .panel-number to fix blur on skew
c = c.replace(
    ".panel-number{font-size:.6rem;letter-spacing:.3em;color:rgba(200,200,200,.35);margin-bottom:.5rem}",
    ".panel-number{font-size:.6rem;letter-spacing:.3em;color:rgba(200,200,200,.35);margin-bottom:.5rem;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}"
)

# Also add will-change:transform to .panel-overlay to stabilize during flex animation
c = c.replace(
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transform:skewX(6deg);transition:padding .5s ease}",
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transform:skewX(6deg);transition:padding .5s ease;will-change:transform}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")