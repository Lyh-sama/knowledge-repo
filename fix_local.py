path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("location.href='analysis/'", "location.href='analysis/index.html'")
c = c.replace("location.href='algebra/'", "location.href='algebra/index.html'")
c = c.replace("location.href='probability/'", "location.href='probability/index.html'")
c = c.replace("location.href='geometry/'", "location.href='geometry/index.html'")
c = c.replace("location.href='quantum/'", "location.href='quantum/index.html'")

# Also fix sub-links
c = c.replace("href='analysis/'", "href='analysis/index.html'")
c = c.replace("href='algebra/'", "href='algebra/index.html'")
c = c.replace("href='probability/'", "href='probability/index.html'")
c = c.replace("href='geometry/'", "href='geometry/index.html'")
c = c.replace("href='quantum/'", "href='quantum/index.html'")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")