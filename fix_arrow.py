path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Increase hero bottom padding to compensate for removed button
c = c.replace("padding:6rem 2rem 8rem", "padding:6rem 2rem 11rem")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")