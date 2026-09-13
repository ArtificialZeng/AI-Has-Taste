# Checkpoint

## Accepted result and writing status

The frozen original statement is proved. The fresh referee accepted the exact
scope in `audit/math.json` and `audit/math.md`: for every connected non-tree
simple graph \(G\) on eight vertices, every genuine nonedge \(uv\), and every
start \(s\),

\[
t_{\rm cov}(G+uv,s)\ne t_{\rm cov}(G,s).
\]

This is a `resolution-paper` candidate and says nothing about trees, other
orders, worst-start cover time, the sign of the change, or the unrestricted
conjecture.

Writing provenance: `bigMac-00026-p02-write-80370fd25a3d`. The mathematical
gate passed again against accepted snapshot
`9d187ad65fc4f91f8917a488d7a8505255d5d1118baaed63f542cd964662a043`.

## Manuscript and decisive evidence

- `source.md` remains unchanged with SHA-256
  `e8d3f12668e1311cc09c0fb6df882dfb0726e649e17c394b04813b8d6b92fe1a`.
- `manuscript/main.tex` and `manuscript/references.bib` form a concise,
  self-contained five-page article. `manuscript/main.pdf` is the clean build.
- The proof presents grounded-Laplacian nonsingularity, the visited-set and
  absorbing-hitting-time formulations, the good-prime exactness lemma, and the
  isomorphism transfer from the exhaustive inventory.
- The article reports all 11,094 connected cyclic order-eight representatives,
  150,573 nonedges, and 1,204,584 marked comparisons, with zero singular
  systems and zero equality residues under both designated exact methods.
- The primary source PDF was checked at pp. 24--26. The initially missing
  project bibliography note was created as
  `literature/user_bibliography_check.md` from the authoritative user workbook.
  Its two cited records are used only for accurately delimited methodological
  comparison; they support no cover-time or priority claim.
- A clean `latexmk`/pdfLaTeX/biber build completed with no unresolved
  citations, references, overfull boxes, or logged warnings. All five rendered
  pages were visually inspected without finding clipping, overlap, or
  illegible content.
- `publication.json` lists every TeX/BibTeX input and the PDF. This job
  clean-built and visually inspected the five-page PDF, then froze the
  manuscript successfully with manuscript digest
  `a3dcc5c255b51d98765bd7c59f9d82e4ade371ff02af82501fb43f5100116920`
  and PDF digest
  `dc102f63d6dc4ffc9bc1270646396ea16bab9b24ca7d673df5e21ff80c9961bd`.

## Fresh release audit status

Release job `bigMac-00026-p02-release-dea508a61244` completed the advisory
two-pass citation check, a clean latexmk/pdfLaTeX/Biber rebuild, and visual
inspection of every rendered page. The rebuild retained manuscript digest
`a3dcc5c255b51d98765bd7c59f9d82e4ade371ff02af82501fb43f5100116920`
and produced PDF digest
`94a4ec58d8f02cf5890a7d395d83580460494266512ad076a5199b5ae4d8a6da`.
The final compiler log has no warning, undefined citation/reference, layout,
or fatal diagnostic; all five pages are clear and complete.

Si's arXiv v1 full text confirms the two cited scope statements. The first
user-workbook paper refreshed successfully at Preprints.org. The second is
preserved from the authoritative workbook with
`metadata_basis=user_designated_workbook` and external refresh unavailable;
its supplied abstract supports only the manuscript's narrow methodological
comparison. No unsupported citation or priority claim remains.

## Obstacles and limitations

No mathematical, citation-support, build, or visual obstacle remains. The one
external metadata refresh limitation above is disclosed and does not affect
the clean submission-ready PDF. The supervisor, not this release worker, owns
publication of the active local deliverable.

## One next test

The fresh `release_gate.py check` succeeded for the current five-page PDF,
all three release audits, and their exact snapshot/manuscript/PDF/build-log
digests. Return `ready`; the one next test is for the supervisor to run
`release_gate.py publish` and verify the resulting active manifest/PDF pair.
