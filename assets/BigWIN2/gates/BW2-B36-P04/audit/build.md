# Fresh build audit

Job: `win-00036-p04-release-23764c16e129`

A clean rebuild ran with
`cd manuscript && latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
Latexmk converged after BibTeX and the required rerun, producing a four-page
PDF. Only the converged final logs were assessed.

- `python3 manuscript/check_certificate.py` returned `PASS`, certified prime
  `108099707`, 22 transitions, `a22_mod_q 0`, and `a5 228947163`.
- The bibliography checker found four cited keys and four BibTeX entries, no
  missing/unused key, and exact final AUX agreement.
- The final diagnostic scan found no undefined citation/reference,
  missing/repeated BibTeX entry, warning, LaTeX error, fatal stop, runaway
  argument, or overfull/underfull box.
- `pdffonts` reports every font embedded and subsetted.
- `pdfinfo` reports four US-letter pages, no encryption, and explicit title,
  author, subject, and keyword metadata.

Final SHA-256 values: `manuscript/main.log` is
`48eff40e7aea610e79512b81d60b6baa7c097ef1cdf41060579182e5285aa7f1`;
`manuscript/main.pdf` is
`3e171d8f22032e1e035fbc42bc6b9705a29f6f99b1acd69f970e990ab36000b9`.
Verdict: **accept**.
