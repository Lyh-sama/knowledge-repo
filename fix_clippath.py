import re
path = r"C:\Users\lyh\Documents\Codex\2026-06-29\https-lyh-sama-github-io-riku-2\work\Riku_sama_no_SEKAI\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace transform:skewX approach with clip-path for sharp text rendering
# .panels stays the same

# .panel: remove skewX, add clip-path for slant
c = c.replace(
    ".panel{flex:1;position:relative;overflow:hidden;transform:skewX(-6deg);margin-left:-2px;transition:flex .6s cubic-bezier(.25,.46,.45,.94);border-right:1px solid rgba(255,255,255,.08);cursor:pointer;text-decoration:none;color:inherit;display:block}",
    ".panel{flex:1;position:relative;overflow:hidden;clip-path:polygon(7% 0,100% 0,93% 100%,0 100%);margin-left:-2px;transition:flex .6s cubic-bezier(.25,.46,.45,.94);border-right:1px solid rgba(255,255,255,.08);cursor:pointer;text-decoration:none;color:inherit;display:block}"
)

# .panel-bg: remove skewX
c = c.replace(
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;transform:skewX(6deg);filter:grayscale(40%) brightness(.35);transition:filter .8s ease,transform 1s ease}",
    ".panel-bg{position:absolute;top:-10%;left:-10%;width:140%;height:130%;background-size:cover;background-position:center;filter:grayscale(40%) brightness(.35);transition:filter .8s ease,transform 1s ease}"
)
c = c.replace(
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.65);transform:skewX(6deg) scale(1.05)}",
    ".panel:hover .panel-bg{filter:grayscale(0%) brightness(.65);transform:scale(1.05)}"
)

# .panel-overlay: remove skewX
c = c.replace(
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transform:skewX(6deg);transition:padding .5s ease;will-change:transform}",
    ".panel-overlay{position:absolute;bottom:0;left:0;right:0;padding:2rem 2rem 2rem;background:linear-gradient(transparent,rgba(0,0,0,.75) 30%,rgba(0,0,0,.96));transition:padding .5s ease}"
)

# Fix mobile part: remove transform:none for panel-bg and panel-overlay since we no longer use transform
c = c.replace(
    "@media(max-width:768px){.panels,.panel{transform:none;margin-left:0;height:220px;border-right:none;border-bottom:1px solid rgba(255,255,255,.08)}.panel-bg,.panel-overlay{transform:none}.panel:hover{flex:1}.panel:last-child{border-bottom:none}}",
    "@media(max-width:768px){.panels,.panel{clip-path:none;margin-left:0;height:220px;border-right:none;border-bottom:1px solid rgba(255,255,255,.08)}.panel:hover{flex:1}.panel:last-child{border-bottom:none}}"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("DONE")