# Checkpoint

- Job: `bigMac-00027-p03-release-be7e61976cd6` (release phase).
- Frozen source: `source.md` is unchanged at SHA-256
  `4bbc9b373dd34a149fe4e10b662d96d60386a356aeced534d189fd9856e08f5c`.
- Accepted mathematics: the `result-note` proves, globally over every starting
  position, that adjacent positive-length factors of total length at most 2745
  have distinct normalized Parikh vectors. The original infinite claim remains
  unresolved; the evidence supplies no control at total length at least 2746.
- Publication repair: the abstract's unsupported current-status wording was
  narrowed from “remains unresolved” to the document-relative statement “This
  note does not resolve that infinite problem.” No mathematical claim changed.
- Current publication binding: manuscript digest
  `82323397713c1a4e2b0f6cabbf4c9f9b92e0451d318f396c0823c94fcdde45c8`;
  PDF digest
  `ff88f4f1cd608d26134d5ed87844085916170e844a65e79d7fa88364cf8396f9`;
  four pages.
- Citation audit: `$citation-check-skill` was used as an advisory two-pass
  check. Shallit, Avgustinovich--Puzynina, Fici--Puzynina, and the relevant
  user-workbook Zeng et al. record were verified at the claims' restrained
  scope. `metadata_basis=user_designated_workbook` is recorded, and the
  accessible official Preprints record matched the workbook. Dependency scope
  is complete and there are no undefined citations.
- Build audit: a clean `latexmk` build and forced confirmation build succeeded.
  `evidence/release_build.log` has SHA-256
  `fd8083c79f65b34deb20b8ba224e8037aa19092d19d0e4a445ccc343f7af5ca4`
  and no unresolved reference, warning, box, or fatal diagnostic. The PDF is
  text-extractable and all fonts are embedded.
- Visual audit: current PDF pages 1, 2, 3, and 4 were rendered at 160 dpi and
  inspected at original image resolution. No clipping, overlap, missing glyph,
  illegible equation, or margin defect was found.
- Release gate: `release_gate.py check` passed with `ok:true` for the current
  snapshot, manuscript, PDF, build log, and fresh audit records.
- Obstacles: none for local release. The remaining obstacle is mathematical,
  namely the absent argument for total length at least 2746; it is not converted
  into a resolution claim.
- Next test: the supervisor should run `release_gate.py publish` and verify that
  `release/manifest.json` binds `release/main.pdf` to the PDF digest above.
