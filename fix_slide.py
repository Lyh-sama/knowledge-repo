path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add transform transition to panel-number and panel-title
c = c.replace(
    ".panel-number{font-size:.6rem;letter-spacing:.3em;color:rgba(200,200,200,.35);margin-bottom:.5rem;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}",
    ".panel-number{font-size:.6rem;letter-spacing:.3em;color:rgba(200,200,200,.35);margin-bottom:.5rem;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;transition:transform .4s ease}"
)
c = c.replace(
    ".panel-title{font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.08em;margin-bottom:.4rem}",
    ".panel-title{font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.08em;margin-bottom:.4rem;transition:transform .4s ease}"
)

# On hover, move number and title up
c = c.replace(
    ".panel:hover .panel-subs{opacity:1;transform:translateY(0)}",
    ".panel:hover .panel-number,.panel:hover .panel-title{transform:translateY(-24px)}.panel:hover .panel-subs{opacity:1;transform:translateY(0)}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")