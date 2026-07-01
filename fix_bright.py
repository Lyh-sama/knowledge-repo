path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Increase brightness: non-hover .35 -> .5, hover .65 -> .8
c = c.replace("filter:grayscale(40%) brightness(.35);transition:filter .8s ease,transform 1s ease",
              "filter:grayscale(40%) brightness(.5);transition:filter .8s ease,transform 1s ease")
c = c.replace(".panel:hover .panel-bg{filter:grayscale(0%) brightness(.65);transform:scale(1.05)}",
              ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.8);transform:scale(1.05)}")

# Also fix the older panel sets
c = c.replace("filter:grayscale(60%) brightness(.4);transition:filter .8s ease,transform 1s ease",
              "filter:grayscale(50%) brightness(.55);transition:filter .8s ease,transform 1s ease")
c = c.replace(".panel:hover .panel-bg{filter:grayscale(0%) brightness(.7);transform:scale(1.05)}",
              ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.85);transform:scale(1.05)}")
c = c.replace(".panel:hover .panel-bg{filter:grayscale(0%) brightness(.72);transform:scale(1.06)}",
              ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.85);transform:scale(1.06)}")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")