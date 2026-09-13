# Checkpoint

## Accepted result and scope

The fresh mathematical referee accepted the frozen full resolution
`nu(4,4)=15` under Shin's literal-interval label definition; see
`audit/math.json` and `audit/math.md`. The accepted snapshot digest is
`6103d3338e01807a90cdcdf1de4d1dcd19827711615d8f91d115fe1dbc0e6640`.
The result settles only `(h,k)=(4,4)`, not the all-`h` endpoint question and
not a weak-type or order-type radius.

## Writing evidence

- The writing-stage `check-math` gate passed against the accepted snapshot.
- `manuscript/main.tex` is a concise self-contained resolution paper. It
  states the exact scope in the title and abstract, gives the finite reduction,
  proves the 35-vector equivalence, records both full frequency maps, supplies
  an ordered-tuple replay, and includes computational/AI assistance disclosure.
- `manuscript/references.bib` cites the two directly relevant frozen primary
  records, Shin arXiv:2609.01690v1 and Zhang arXiv:2609.08915v1, only for the
  definitions, bounds, and broader question they actually support.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` cleanly built
  the four-page `manuscript/main.pdf`. The final log has no undefined
  references, citation warnings, overfull boxes, or underfull boxes; PDF text is
  extractable and all fonts are embedded. The pages were also rendered and
  inspected for gross layout defects.
- `publication.json` lists every TeX/BibTeX input and the draft PDF path.
  `release_gate.py freeze-manuscript` succeeded and wrote
  `audit/manuscript-snapshot.json` with manuscript digest
  `0497ba06c140c8bf1dd752e62348ce9084e8ae2f27e7f003e4c2a209d9b95183`
  and PDF digest
  `e3f58a99faa9a912351ae3d80ac81dd4f128e4595759e1444ec4d0f391103386`
  after the release-stage forced clean rebuild.
  `source.md` remains byte-for-byte unchanged at SHA-256
  `093883054c665b367e5363739e6d5a5563e0959b8a39c6d2b288fc3401932be6`.

## Citation limitation

`literature/user_bibliography_check.md` was absent when inspected, so no
Excel-derived DOI/BibTeX record was available to apply. This is recorded in
`literature/citation_limitations.md` and `publication.json`; it did not suppress
the clean PDF. The manuscript makes no priority or exhaustive-literature
claim.

## Fresh release evidence

- The citation-check skill was explicitly invoked. Its fixed extraction is
  `audit/citation_claims.md`; all 18 claims were then checked separately.
  Official arXiv records and full HTML verified both bibliography entries and
  the exact cited passages. No citation limitation remains.
- A forced `latexmk -gg` rebuild succeeded. The bound final log is
  `manuscript/main.log`, SHA-256
  `d538b8de9a36c2c38a12501ce6972a84393af07ba7d14e61bf286f2a621966a2`,
  with no unresolved citations/references or box warnings.
- All four 170-dpi page renders in `audit/rendered-pages/` were opened and
  inspected; no clipping, overlap, illegibility, or substantive layout defect
  was found.
- Fresh bound records are `audit/citations.json`, `audit/build.json`, and
  `audit/visual.json`, all using release job
  `bigMac-00028-p04-release-4ebd396e9585`.
- The authoritative `release_gate.py check` passed on the current evidence,
  manuscript, PDF, compiler log, reports, audit records, and role provenance;
  it reported four pages and the PDF digest above.

The project has no local `scripts/release_gate.py`; the authoritative skill
copy is available and is invoked with the mandated exact research interpreter.

## One next test

The supervisor may invoke `release_gate.py publish` to activate the exact
validated PDF, then verify the resulting release manifest and copied digest.
