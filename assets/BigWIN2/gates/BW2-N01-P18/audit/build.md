# Clean build review

Verdict: accept. Job `newwin-00001-p18-release-ecb3e56853b6`, attempt 2, launch `4d1f8672-f643-46f1-a0ca-d3a703cd0153`.
Clean and build commands recorded in `audit/release-build-commands.json` both
returned zero. The PDF is six pages. The final TeX log contains no fatal
diagnostics, missing references, undefined citations, overfull boxes or
underfull boxes. The final AUX and BibTeX key checker reports seven keys
in every set, zero omissions, zero extras and zero unused entries.

There is one understood BibTeX warning: `Warning--empty journal in Zeng_2026`.
It comes from the verbatim official Crossref @article export for a deposited
preprint. No nonexistent journal was added. The rendered reference retains
the exact versioned DOI and the body identifies it as a preprint. This is a
metadata-format warning, not an unresolved citation or failed build.

PDF metadata identifies the title and Xiaojian Zeng. `pdffonts` was inspected:
all fonts are embedded Type 1 with Unicode mappings, with no Type 3 font.
FLS project-authored dependencies and the canonical bibliography are complete;
see `audit/release-dependencies.json`. Exact standalone supplement replays
match all packaged output bytes, as recorded in the supplement inspection.

Manuscript digest: `260f9e3032adc94ed40a9d4684bb3542d018ea567b648eaa5f628dbf55afdcf4`.
PDF digest: `b3635986e7c3be508b7917c1a6d04675ff0cbd3674b388c0aae4fe3c87004b72`.
TeX log SHA-256: `883a28af8068a41dbfe6de07c940a3982e3ca662181682b6d0cb8317ec6454af`.
BibTeX log SHA-256: `23220e523712ec0b71e856a8b8360826e29dadbe9059db2699b84bab9a245918`.
