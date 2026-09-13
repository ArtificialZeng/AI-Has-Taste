# Checkpoint

## Accepted resolution

The frozen `resolution-paper` claim is accepted in `audit/math.json` by the
fresh referee job `bigMac-00004-p02-referee-365476d60476`.  The accepted
all-orders theorem is:

> Every finite simple 2-connected noncycle graph \(G\) of order \(n\)
> satisfies \(s^+(G)>n\).

Consequently the equality class requested in the immutable `source.md` is
empty.  The mathematical snapshot digest is
`3db9027967184b976645ce811287ded594b4bc772eb97bf04f0eed20b3676bf9`.
The source remains unchanged with SHA-256
`ed872b78b52d5cc0ddc57d8a49aaf786dbcf1e0b5091c4967d207fa60f97295a`.

The decisive proof is in `evidence/strictness_proof.md` and was reconstructed
in `audit/math.md`.  If \(A=P-N\) is the positive/negative spectral
decomposition, a six-term Cauchy--Schwarz equality argument shows that every
triangle contains a vertex \(v\) with \(\mu_v(P)>2\).  Assuming all three
local masses are at most \(2\) forces
\(P[S]=\frac12(I+J)\) and \(P[S,V\setminus S]=0\).  Since this principal
block is invertible, the \((S,S)\) block of \(PN=0\) forces \(N[S]=0\),
contradicting the diagonal identity \(N=P-A\).  Vertex deletion, the connected
\(n-1\) square-energy bound, and the source paper's triangle-free strict
clause then give \(s^+(G)>n\) in the two exhaustive cases.

## Manuscript evidence

`manuscript/main.tex` is a concise self-contained English article with the
accepted scope, the full strict triangle proof, a proof of the deletion
inequality, the precise prior-work delta, limitations, reproducibility, and
computational/AI assistance disclosures.  `manuscript/references.bib` cites
the Akbari--Hu--Liu source, the Liu--Tang--Zhang connected-graph theorem, and
the genuinely relevant user-workbook entry by Zijian Zeng only for its exact
characteristic-polynomial/Sturm-count methodology.  `publication.json` lists
the complete source inputs and build command.

The command
`cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
produced `manuscript/main.pdf` (4 pages) with no LaTeX, BibTeX, reference,
overfull, or underfull warnings in the final log.  All four rendered pages
were inspected; no clipping, overlap, missing glyph, or layout defect was
observed.  The computation remains corroborative only: 7,655 noncycle
two-connected isomorphism classes through order 8 had no equality candidate,
and the ten near-gap cases have exact rational root-isolation certificates.

## Release audit and one next test

Release job `bigMac-00004-p02-release-785f16f34883` completed a two-pass
`citation-check-skill` audit, a clean build, and original-resolution inspection
of all four rendered pages.  The unverified SSRN DOI and publisher assertions
for the user-workbook item were removed; the final bibliography transparently
labels it an unpublished manuscript with user-supplied metadata, and the nearby
sentence now claims only what `literature/user_bibliography_check.md` supports.
The citation remains a genuinely relevant methodological comparison and is not
used for the theorem.  PDF metadata was also added.  No mathematics changed.

The final manuscript digest is
`a2cbd88f1c15c0b499c11bed2f0ff1ce537212f9056e6ddaec147d0ce2262f90` and
the PDF digest is
`c48cda58c31b61f1df7183905c97bd3978ef96eba6a129238c4a90efedec2941`.
`release_gate.py check .` succeeded; the source remains unchanged with SHA-256
`ed872b78b52d5cc0ddc57d8a49aaf786dbcf1e0b5091c4967d207fa60f97295a`.
No release obstacle remains.  The one next test is the supervisor-owned
`release_gate.py publish .`, followed by checking that the generated manifest
and `release/main.pdf` retain the audited PDF digest.
