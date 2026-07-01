import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace margin-left:-4px with margin-left:-2.5% (covers 5% clip on each side)
c = c.replace(
    "clip-path:polygon(5% 0,100% 0,95% 100%,0 100%);margin-left:-4px",
    "clip-path:polygon(5% 0,100% 0,95% 100%,0 100%);margin-left:-2.5%"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")