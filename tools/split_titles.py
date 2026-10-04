"""Split data/titles.txt (one title per line, points.bin order) into
data/titles/NNN.txt chunks of CHUNK lines, loaded on demand by index.html
(hover / card / beacon labels) instead of one ~54 MB download.
Re-run after re-baking titles.txt:  python tools/split_titles.py
"""
import os

CHUNK = 10_000  # must match TITLE_CHUNK in index.html
src = os.path.join(os.path.dirname(__file__), "..", "data", "titles.txt")
out = os.path.join(os.path.dirname(__file__), "..", "data", "titles")
os.makedirs(out, exist_ok=True)
with open(src, encoding="utf-8", newline="\n") as f:
    lines = f.read().split("\n")
for k in range(0, len(lines), CHUNK):
    with open(os.path.join(out, "%03d.txt" % (k // CHUNK)), "w", encoding="utf-8", newline="\n") as g:
        g.write("\n".join(lines[k:k + CHUNK]))
print(len(lines), "titles ->", (len(lines) + CHUNK - 1) // CHUNK, "chunks")
