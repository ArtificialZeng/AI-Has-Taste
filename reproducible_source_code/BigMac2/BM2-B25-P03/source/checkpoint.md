# Checkpoint

Job: `bigMac-00025-p03-release-3e0a1365b5bd` (release phase, 2026-09-09).

## Accepted result and manuscript

- `release_gate.py check-math` passes for accepted mathematical snapshot
  `3aa1730abde890254c3a46f9864a0d812eb7ead0d7258a09fb0634060fc5da1e`.
- The accepted scope is preserved exactly: every \(4+5\) partition of the
  additive group \(\mathbb F_3^2\) admits four vertex-disjoint cross edges whose
  oriented differences are all eight nonzero group elements. No claim is made
  for a larger group.
- `manuscript/main.tex` is a concise, self-contained computer-assisted proof.
  It gives the injection reduction, proves equivalence of the four-direction
  predicate to the required multiset condition, documents complete coverage of
  all \(126\cdot120=15120\) candidates, reports the 54/72 exact count
  distribution, supplies reproduction commands, and discloses computational
  and AI assistance.
- `manuscript/main.pdf` is a clean three-page pdfLaTeX/BibTeX build. The build
  log has no warnings, undefined references, or overfull/underfull boxes; all
  fonts are embedded. All three pages were rendered and visually inspected for
  clipping, overlap, and legibility.
- The exact search and separate checker were rerun with the mandated
  `/Users/mac/4prove-or-disprove-math/.research-venv/bin/python`. They again
  produced 126 witnesses, checked 15,120 injections, and returned
  `verification: pass`; the accepted certificate digest is unchanged.
- `publication.json` lists the complete TeX/BibTeX and computational source
  bundle plus the PDF and exact build command. `release_gate.py
  freeze-manuscript` passes; `audit/manuscript-snapshot.json` records manuscript
  digest `63e01e3cc54f75e390f8fa0c1437d9a15e73a1cd9e295f833d94e0172ab3c535`
  and PDF digest
  `bb19403925b73a6c5481cf58cf36c33990d5ff5f5118efd933fb90a07e4a6099`.
- `source.md` remains unchanged with SHA-256
  `16978696725ccc1e0c9f92862888d9e2ca24fb0e6a790353906b4b3c13f43e34`.

## Fresh release evidence

- `audit/citations.md` applies the requested citation checker in two passes.
  Springer's version of record verifies Open Problem 2 and all metadata for
  DOI `10.1007/s40590-025-00772-2`; arXiv v3 verifies its three authors,
  version date, Problem 1.6, Theorem 1.7, and the stated cross-part method
  limitation. Both nearby attributions are supported, and no priority claim
  is made. The requested project-local
  `literature/user_bibliography_check.md` remains absent; because both cited
  records are externally verified, this is disclosed but leaves no unverified
  citation.
- The exact search and independent checker were rerun using the mandated
  `/Users/mac/4prove-or-disprove-math/.research-venv/bin/python`. Their
  regenerated outputs are byte-identical to the frozen evidence, including
  certificate SHA-256
  `cf3589e80b12bdf59e737e073cb690a0f01d99fb9ba4b6b4e2258c18f73d449e`.
- `audit/build.md` binds `manuscript/main.log` at SHA-256
  `64975a79fbc3aa1aa4a1b567dd7d6ba6e5d60a0a3099b4a5e3d5553d1158815c`.
  The compiler/BibTeX records contain no errors, warnings, unresolved
  citations/references, or box warnings; all fonts are embedded.
- `audit/visual.md` records fresh inspection of rendered pages 1--3 at
  original image resolution. No clipping, overlap, bad glyph, illegible
  material, or other presentation defect was found.
- Fresh `audit/citations.json`, `audit/build.json`, and `audit/visual.json`
  use job ID `bigMac-00025-p03-release-3e0a1365b5bd` and bind the current
  evidence, manuscript, PDF, and build-log digests.
- The final structural/provenance command `release_gate.py check` returned
  `ok: true`, `kind: resolution-paper`, `original_status: proved`, and
  `pages: 3` for the current digests.

## Next test

The supervisor should run `release_gate.py publish` to atomically activate
the already checked PDF and manifest; no further manuscript change is needed.
