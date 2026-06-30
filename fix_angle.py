import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Increase slant from 5% to 8%, increase overlap from -2.5% to -3.5%
c = c.replace(
    "clip-path:polygon(5% 0,100% 0,95% 100%,0 100%);margin-left:-2.5%",
    "clip-path:polygon(8% 0,100% 0,92% 100%,0 100%);margin-left:-3.5%"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")