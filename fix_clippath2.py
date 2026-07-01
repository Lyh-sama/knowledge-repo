import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# First set (lines ~168 area): old dual-head panel rules
c = c.replace(
    ".panel{display:block;position:relative;flex:1;overflow:hidden;transform:skewX(-7deg);margin-left:-3px;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}",
    ".panel{display:block;position:relative;flex:1;overflow:hidden;clip-path:polygon(8% 0,100% 0,92% 100%,0 100%);margin-left:-3px;border-left:1px solid rgba(255,255,255,.06);text-decoration:none;color:inherit;transition:flex .65s cubic-bezier(.25,.46,.45,.94);will-change:flex}"
)
c = c.replace(
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;transform:skewX(7deg);filter:grayscale(60%) brightness(.4);transition:filter .8s ease,transform 1s ease}",
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;filter:grayscale(60%) brightness(.4);transition:filter .8s ease,transform 1s ease}"
)
c = c.replace(
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.7);transform:skewX(7deg) scale(1.05)}",
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.7);transform:scale(1.05)}"
)
c = c.replace(
    ".panel-content{position:absolute;left:0;right:0;bottom:0;padding:2rem 2.5rem 2.5rem;background:linear-gradient(transparent,rgba(0,0,0,.7) 30%,rgba(0,0,0,.95));transform:skewX(7deg);transition:padding .5s ease}",
    ".panel-content{position:absolute;left:0;right:0;bottom:0;padding:2rem 2.5rem 2.5rem;background:linear-gradient(transparent,rgba(0,0,0,.7) 30%,rgba(0,0,0,.95));transition:padding .5s ease}"
)

# Second set (lines ~205 area)
c = c.replace(
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;filter:grayscale(40%) brightness(.35);transition:filter .8s ease,transform 1s ease}",
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;filter:grayscale(40%) brightness(.35);transition:filter .8s ease}",
    count=1
)
c = c.replace(
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.72);transform:skewX(7deg) scale(1.06)}",
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.72);transform:scale(1.06)}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")