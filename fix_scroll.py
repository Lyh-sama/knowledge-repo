path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Fix broken scroll hint HTML
c = c.replace(
    '<a href="#about" class="hero-scroll"><span>\u5411\u4e0b\u63a2\u7d22</a><i class="fa-solid fa-chevron-down"></i></a>',
    '<a href="#about" class="hero-scroll"><span>\u5411\u4e0b\u63a2\u7d22</span><i class="fa-solid fa-chevron-down"></i></a>'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")