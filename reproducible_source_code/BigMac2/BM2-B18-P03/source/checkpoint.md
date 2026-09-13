# Checkpoint

Writing job provenance: `bigMac-00018-p03-write-245d5df8cb47`
(2026-09-08). `source.md` remains immutable with SHA-256
`65c11a0f7088c13b0ff6a2702bde0bc8b6b2c3c5b4626a06f291d5cedda3b646`.

## Accepted result and manuscript

The fresh mathematical audit in `audit/math.json` and `audit/math.md` accepts
the exact `resolution-paper` scope: for `A=pi^2/4`, constants `c,C,u_0>0`
exist such that

`c*u^(3/2) <= log(lambda(u))+A*u <= C*u^(3/2)` for `0<u<u_0`.

Hence the second Peano quotient tends to `+infinity` and no finite classical
right second derivative exists. No exact optimized `u^(3/2)` coefficient or
global priority claim is made.

The self-contained English manuscript is `manuscript/article.tex`, with
bibliography in `manuscript/references.bib` and clean five-page PDF at
`manuscript/article.pdf`. It was built by
`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex`; the final
LaTeX/BibTeX logs contain no warnings, undefined references, overfull boxes, or
errors. All five rendered pages were visually inspected. PDF SHA-256:
`a4d13aa84c9372f466abb5f6b0d4a4127e11b4f3499b010b68708784c29f59d9`.

`literature/user_bibliography_check.md` records the user-workbook authority and
selects worksheet row 13, Zijian Zeng's constrained spectral-constant paper,
for one narrowly qualified operator-theoretic comparison. The PDF also cites
the originating Liu--Chen preprint and the Slepian--Pollak time-frequency
limiting paper. The central proof is independent of all three citations.

`publication.json` lists the TeX/BibTeX inputs, PDF, build command, metadata
bases, and citation-scope limitation. `release_gate.py freeze-manuscript`
succeeded with manuscript digest
`eb00feeb1d21ef170e521b805881d769bca7fc11dd6ea8211719eadb6a32d36b`.

## Release audit checkpoint

Release job `bigMac-00018-p03-release-8e49cdd531eb` completed fresh citation,
build, and rendered-page reviews against the frozen manuscript and PDF.
`audit/citations.md` records the advisory citation-check skill's fixed
extraction and source-verification passes. All three references and their
nearby claims were supported at their deliberately narrow scope; the Zeng
record remains based on the user-designated workbook and independently matched
the official Preprints.org v1 page. All citation keys resolve and the authored
dependency list is complete.

`audit/build.md` binds the existing clean build log at SHA-256
`72a47380e34e1b829c7795803ff3eb095c397d510de4f69b93ed4b7fe6b7951c`.
`audit/visual.md` records actual inspection of pages 1--5: no clipping,
overlap, illegible material, broken reference marker, or other substantive
layout defect was found. The final `release_gate.py check` succeeded with
snapshot digest `541d34c4cdaca83b4396c9302a0418af32ffe4cc1fedd99b0f6b17a06c273718`,
manuscript digest `eb00feeb1d21ef170e521b805881d769bca7fc11dd6ea8211719eadb6a32d36b`,
PDF digest `a4d13aa84c9372f466abb5f6b0d4a4127e11b4f3499b010b68708784c29f59d9`,
and five pages. The accepted scope still determines only the two-sided signed
`u^(3/2)` scale, not an optimized leading coefficient.

## Obstacles and limitations

No mathematical, citation, build, dependency, or visual obstacle remains.
Local release is not peer review, journal acceptance, submission, or a claim
of global priority.

## One next test

Let the supervisor invoke `release_gate.py publish` without changing any bound
file, then verify that `release/manifest.json` and `release/main.pdf` carry the
same PDF digest.
