import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Current clip-path: polygon(7% 0, 100% 0, 93% 100%, 0 100%)
# Change to tighter overlap: smaller clip % and larger negative margin
c = c.replace(
    "clip-path:polygon(7% 0,100% 0,93% 100%,0 100%);margin-left:-2px",
    "clip-path:polygon(5% 0,100% 0,95% 100%,0 100%);margin-left:-4px"
)

# Also fix the older panel rules (first set: 8% / 92%)
c = c.replace(
    "clip-path:polygon(8% 0,100% 0,92% 100%,0 100%);margin-left:-3px",
    "clip-path:polygon(5% 0,100% 0,95% 100%,0 100%);margin-left:-4px"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")