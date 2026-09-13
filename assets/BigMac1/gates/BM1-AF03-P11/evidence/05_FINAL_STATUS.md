# Final status

**Terminal category:** `CERTIFIED_FINITE_RESULT`  
**Original prompt complete:** yes  
**Scope:** the requested first unverified relation `n=7`, not the all-`n`
Conjecture 4.4.

## Exact conclusion

For the generalized stack-sorting map `s_{123,132}`,

```text
|M_13| = 47,265,120,
|M_14| = 378,120,960 = 8 |M_13|.
```

Moreover, deletion of the last entry followed by standardization maps
`M_14` onto `M_13` with exactly eight preimages, corresponding to terminal
insertions of the values 7 through 14.

## Certificate and independent audit

- Exact certificate:
  `certificates/n1_to_n7_counts.json`, SHA-256
  `1a3580a593bf6e5a640f0347f0c8ab385e7a5af559949b399925c2936891903e`.
- Independent no-import verifier:
  `code/verify_certificate.py`, SHA-256
  `c9d2df5bd7b28f17da0e28f09e277812a0f3a661c71af38174d5c44c2dfea46f`.
- Full verifier output:
  `experiments/independent_verifier_full.json`, SHA-256
  `ea7559795d8bb2d7e53011b8d7c2b7991363bf2b9dc2fbee1f11992ef81051cf`.
- Six malformed-certificate mutations were rejected with structured failure;
  362,879 exact literal factorization comparisons passed.

Reproduction from the source archive:

```text
python3 -I code/verify_certificate.py certificates/n1_to_n7_counts.json
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Release artifacts

- PDF: `output/pdf/generalized_stack_sorting_n7_Zeng.pdf`, SHA-256
  `76997d53c15fe7d7890f3e46a8276d3d5a00e5faf73ecb775d1ae8277f8ee17d`.
- LaTeX/source ZIP:
  `output/source/generalized_stack_sorting_n7_Zeng_source.zip`, SHA-256
  `8da2417940767f692f71e7cb8889413393c648c172e189b11f1e6c3731eadece`.
- `output/RELEASE_MANIFEST.json` verifies both files; the ZIP's internal
  `MANIFEST.json` verifies all 15 packaged source and audit files.

Both citations were checked against primary DOI/arXiv records; a separate
post-result fingerprint search found no earlier matching result in the
recorded sources. The search conclusion is date-bounded, not a claim of
absolute worldwide priority.

No Lean, Coq, Isabelle, or other proof assistant was used.
