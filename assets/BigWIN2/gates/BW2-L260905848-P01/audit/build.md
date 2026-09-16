# Build audit

**Verdict: accept.** A clean `latexmk` rebuild of the canonical `manuscript/main.tex` completed with `-interaction=nonstopmode -halt-on-error` and produced the frozen six-page `manuscript/main.pdf`.

- PDF SHA-256: `4590bf991a6642ed36b183e9845cd4e616d3b574c0061a6cdb700361bce5afee`
- Build-log SHA-256: `737868428df3c8a2f58185e57606af9a8a20e7927351c1917132bd5f9f4f7400`
- Canonical key check: 7 cited keys, 7 BibTeX keys, 7 AUX keys; zero missing or uncited keys
- Fatal diagnostic scan: no LaTeX error, fatal error, emergency stop, undefined control sequence, runaway argument, undefined reference, or undefined citation
- BibTeX scan: no missing database entry, repeated entry, or warning
- PDF checks: valid 1.5 PDF, letter size, six extractable-text pages, all fonts embedded

The log has two `Underfull \hbox` warnings at source lines 335--336 and 339--340. They arise from long filenames in the certificate-component table. Page 5 was inspected at rendered resolution: the entries wrap within their cells and no text clips, overlaps, or becomes illegible. These warnings do not affect acceptance.
