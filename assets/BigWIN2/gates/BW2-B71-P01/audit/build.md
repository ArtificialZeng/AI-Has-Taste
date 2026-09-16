# Clean build audit

Release job `win-00071-p01-release-74f5b2e2a4db`, checked 2026-09-08.

The unchanged canonical manuscript was cleaned and rebuilt in `manuscript/`
with
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  BibTeX and
the required reruns converged successfully to a four-page PDF.  The final log
and BibTeX log contain no undefined citation or reference, missing database
entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined
control sequence, or runaway argument.  The bibliography key checker reports
four cited keys, four database keys, no missing or unused entries, and exact
agreement with `main.aux`.

The resulting PDF was refrozen with `release_gate.py freeze-manuscript`.  The
manuscript digest remains
`59949e6f61c07e339acdafb3d2b1218608f0dbf50a6cbee1fd5f263a051e2d24`
and the current PDF digest is
`cfffd20a9694d43fecee03f34859ba16ceb47cbb47a163c480dc8375936d387d`.
