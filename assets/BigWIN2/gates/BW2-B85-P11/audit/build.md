# Build audit

Verdict: **accept**.

A clean `latexmk -C` rebuild followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed successfully and produced `manuscript/main.pdf` with four pages. BibTeX ran against the canonical `manuscript/references.bib`, and the final log contains no fatal error, undefined citation, undefined reference, overfull box, or underfull box diagnostic.

The ordinary body citation set, BibTeX entry set, and final AUX citation set are identical: `FuLiWangWang2026`, `KolountzakisRevesz2006`, and `ZengLiuRatnavelu2026`. The deterministic exact verifier reported `all exact assertions passed`; the accepted-audit recheck reported a unique Sturm root, certified alternating root-isolation signs, and positive leading moment minors.

The log and PDF recorded by this audit are the outputs of the final source tree frozen in `audit/manuscript-snapshot.json`.

