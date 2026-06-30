path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Reduce bottom padding so text sits lower; remove extra padding-bottom
c = c.replace(
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease;padding-bottom:42px}",
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2.5rem 2rem 1.2rem 3.5rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")