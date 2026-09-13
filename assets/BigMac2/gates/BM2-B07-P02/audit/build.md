# Fresh build audit

Release job: `bigMac-00007-p02-release-e3e9934bb4ec`  
Build log: `manuscript/main.log`  
Build-log SHA-256:
`6519274d582fdcea6eac1bf1aa86c17e4545f1d75d1bd83e21dc6dec0a320184`

The publication was force-rebuilt with
`latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex` in the
`manuscript` directory.  Biber 2.21 found both citekeys and completed without
an error; pdfTeX completed two passes; latexmk exited zero and reported all
targets up to date after convergence.

The final compiler log is nonempty and contains no fatal error, emergency
stop, undefined citation, undefined reference, multiply-defined label,
overfull box, underfull box, or LaTeX/package warning.  The `.aux`, `.bcf`,
`.bbl`, extracted PDF text, and rendered reference list all resolve the two
citations.  `evidence/check_finite.py` also ran successfully and exactly
verified the 30 subsets, 10 triples, and two endpoint averaged metrics stated
in the paper.

The output begins with `%PDF-`, contains four letter-size pages and nonempty
extractable text, and has embedded fonts.  PDF metadata now records the full
title, author Xiaojian Zeng, subject, and keywords.  The output PDF is
`manuscript/main.pdf`, SHA-256
`e8e4681269c10271d5d861b1a4cd311df05506a161abd8767b18c6e2c7fc393c`.

**Verdict: accept; clean build.**
