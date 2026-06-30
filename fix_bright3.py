path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Fix the ACTIVE panel-bg (line 238) - this is the one the categories section actually uses
c = c.replace("filter:grayscale(40%) brightness(.35);transition:filter .8s ease}",
              "filter:grayscale(25%) brightness(.7);transition:filter .8s ease}")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")