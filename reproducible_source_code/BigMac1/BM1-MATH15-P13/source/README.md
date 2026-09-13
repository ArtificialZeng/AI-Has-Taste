# Submission package

This package accompanies **The small Ramsey degree of an edge in ordered
split graphs is three** by Zijian Zeng.

## Contents

- `main.tex`, `references.bib`, and `main.bbl`: manuscript sources.
- `main.pdf`: compiled five-page manuscript.
- `certificates/split_witness.json`: machine-readable lower-bound witness.
- `code/verify_split_witness.py`: independent exact witness verifier.
- `MANIFEST.json`: byte counts and checksums for the packaged files.

## Build

From the package root, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Exact witness check

From the package root, run:

```sh
python code/verify_split_witness.py certificates/split_witness.json
```

The exact theorem in the manuscript concerns ordered split graphs.  The full
ordered chordal-graph question remains open; the manuscript gives only a lower
bound and structural obstructions for that larger class.
