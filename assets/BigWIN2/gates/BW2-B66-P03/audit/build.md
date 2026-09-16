# Clean build report

Verdict: accept

The manuscript was cleaned with `latexmk -C main.tex`, the orbit table was
regenerated from the canonical classification JSON, and the publication command
was run in `manuscript/`:

`python3 generate_orbits_table.py ../evidence/bondage5_classification.json orbits-table.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

The source hashes remained identical to the accepted manuscript snapshot, and
the build converged to a six-page PDF with SHA-256
`9b1e2288dcba4da257093451a63bfcf21de1029476dc504612b63fc66b4a4183`.
The final log SHA-256 is
`8827f99d7d2462e9f6562efc173ebf7b1ebe9f3d8a6156fa36bfc5ccb7dfe0c0`.

The final LOG and BLG contain no undefined citation/reference, missing or
repeated bibliography entry, LaTeX error, fatal stop, undefined control
sequence, runaway argument, overfull box, or underfull box. The bibliography
checker found three cited keys, three canonical entries, no missing or unused
entries, and exact AUX agreement. `pdfinfo` confirms a valid, unencrypted,
text-extractable, six-page letter-size PDF; `pdffonts` reports every font
embedded and Unicode mappings present.
