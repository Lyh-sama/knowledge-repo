path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Update panel onclick targets from category.html#xxx to folder/
c = c.replace("location.href='category.html#analysis'", "location.href='analysis/'")
c = c.replace("location.href='category.html#algebra'", "location.href='algebra/'")
c = c.replace("location.href='category.html#probability'", "location.href='probability/'")
c = c.replace("location.href='category.html#differential-geometry'", "location.href='geometry/'")
c = c.replace("location.href='category.html#quantum-info'", "location.href='quantum/'")

# Update sub-link hrefs
c = c.replace("href='category.html#math-analysis'", "href='analysis/'")
c = c.replace("href='category.html#real-analysis'", "href='analysis/'")
c = c.replace("href='category.html#functional-analysis'", "href='analysis/'")
c = c.replace("href='category.html#linear-algebra'", "href='algebra/'")
c = c.replace("href='category.html#abstract-algebra'", "href='algebra/'")
c = c.replace("href='category.html#probability'", "href='probability/'")
c = c.replace("href='category.html#statistics'", "href='probability/'")
c = c.replace("href='category.html#differential-geometry'", "href='geometry/'")
c = c.replace("href='category.html#quantum-info'", "href='quantum/'")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")