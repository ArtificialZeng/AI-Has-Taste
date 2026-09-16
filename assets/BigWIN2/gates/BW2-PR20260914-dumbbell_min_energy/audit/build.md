# Build audit — accept

Job: primary-20260914-dumbbell-min-energy-release-d0dcdbfc65d4

Manuscript digest: `684f969d232c6e203ffd7fb7ee7866b0792f2879556277493b9cc223f4180229`  
PDF digest: `2c59c283fc319ae3992c6615f0593ca4e74baabd685856808187e3403ed5eb1f`  
Frozen mathematical snapshot: `c54ee1930645183cb069fba12fb9fd382eddca737522332f05cf84b9349a0cae`

Clean rebuild command:

```sh
BIBINPUTS=/home/ailab/4math-open-problems/projects/primary-20260914-dumbbell-min-energy/manuscript: latexmk -pdf -gg -interaction=nonstopmode -halt-on-error -outdir=build manuscript/main.tex
```

The forced latexmk rebuild completed successfully and regenerated the bibliography and nine-page PDF. Canonical references.bib was found through BIBINPUTS. The final build/main.log has no errors, undefined citations/references, duplicate labels, overfull/underfull boxes or other warnings. The direct BibTeX/aux consistency checker passes with eight cited entries, no missing or unused keys and no differences. PDF metadata and embedded-font inspection are saved in release-pdfinfo.txt and release-pdffonts.txt. Recorder inputs, source completeness and exact build-log hash are in release-build-inspection.json. The companion table and verifier remain explicitly listed publication sources although the table is now inline. No extra local style or hidden bibliography dependency was found.
