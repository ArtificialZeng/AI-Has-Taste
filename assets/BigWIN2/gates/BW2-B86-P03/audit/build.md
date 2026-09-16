# Build audit

**Verdict: accept.** Release job
`win-00086-p03-release-6700fccf9f2a` ran
`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex` from the
canonical `manuscript/` directory.  The forced rebuild removed generated
outputs, ran pdfLaTeX, BibTeX, and the required converging pdfLaTeX passes,
and exited successfully with a four-page PDF.

The final `manuscript/main.log` has SHA-256
`b84e4c1e329931bfc240742c29959df828d1d268ecffbf04371c4eba89d1a180`.
The converged log and `.blg` contain no undefined citation or reference,
missing database entry, repeated entry, LaTeX error, fatal error, emergency
stop, undefined control sequence, runaway argument, or unresolved rerun
diagnostic.  The bibliography checker found six body citation keys and six
canonical BibTeX entries, with no missing or unused key and exact agreement
with the final `.aux` set.

The independent exact checker also exited successfully and reproduced the
frozen projective images and both difference histograms before the release
snapshot was frozen.  The final PDF SHA-256 is
`3c0c758fb84ce6bef582a0a5b5a09c231959cead555192f097cd2f7cf0d7cafd`.
