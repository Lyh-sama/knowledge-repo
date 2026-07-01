path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Increase hero min-height to push arrow down
c = c.replace("min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden",
              "min-height:110vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")