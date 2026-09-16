# Build audit

Verdict: accept.

- Build: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
  from `manuscript/`; exit status 0 and converged as up to date.
- PDF: five letter-size pages, SHA-256
  `fb76446a1d3a37b3c9aa6b92c93dee82a9ec81e77f5298343f1a513379da0794`.
- Log scan: no undefined citation/reference, missing database entry, BibTeX
  warning, duplicate entry, LaTeX error, fatal error, emergency stop,
  undefined control sequence, runaway argument, overfull box, or underfull box.
- Bibliography checker: three cited keys, three BibTeX entries, three AUX
  bibcite keys; no missing or unused keys.
- Fonts: `pdffonts` reports every font embedded and subsetted.
- PDF metadata: title, author (Xiaojian Zeng), subject, and keywords are set.
- Frozen mathematical inputs retain the SHA-256 values in
  `audit/snapshot.json`; `source.md` remains
  `e90eced4876d95f100aff8e5c2579b4c35555939a27f7593366b48bdd25b7a5a`.
- Exact formula verifier: 620 orbits representing all 4,278 configurations.
