path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("border-radius:999px;background:rgba(0,0,0,.25)", "border-radius:2px;background:rgba(0,0,0,.25)")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")