# Checkpoint

Job: `bigMac-00015-p01-release-3bca604ddec1`; date: 2026-09-08;
phase: fresh citation/build/rendered-page release audit. Decision: **ready for
the supervisor's publish gate**, candidate kind: **resolution-paper**, original
status: **proved**.

The accepted mathematical snapshot remains
`ab3e4198491bf587813a4e9409d5ead91b272ae82481f039447827d825db8405`.
The current manuscript snapshot is
`60c604c24a86c3a573782df5cdf274c0d9a601a9ce8e5ff75dee92c31c2c847f`,
and the four-page PDF digest is
`4cea61bf1119db7de4fd3e05ae8e65d19fee1d55ee2cb35bf24df245a90b20b4`.
No manuscript, bibliography, evidence, or PDF content was changed during this
release review.

Citation evidence is in `audit/citations.md` and `audit/citations.json`.
The explicitly invoked citation-check workflow used a fixed extraction pass
followed by primary-source verification. The official arXiv record and supplied
primary PDF verify Zhang--Zhang's metadata, full-space definition, lower bound,
and exact `n=3,4` computations. The official PMLR record/PDF verifies the leap
paper's metadata and support-ordering definition. Both nearby attributions are
supported, all citation keys resolve, and the bounded comparison makes no
priority claim. `literature/user_bibliography_check.md` is absent, so no
user-designated workbook record was available; both references actually used
were nevertheless externally verified and are genuinely relevant.

Build evidence is in `audit/build.md` and `audit/build.json`. The bound existing
log is `manuscript/main.log`, SHA-256
`0bba46c439ceefeb4a95678821996e5f0e07e7bcc3c7554038ffba1fb8ac3e5b`.
It records a successful four-page build with zero fatal errors, warnings,
undefined citations/references, and overfull/underfull boxes. BibTeX used both
entries without warnings; all PDF fonts are embedded.

Visual evidence is in `audit/visual.md`, `audit/visual.json`, and the four
renderings under `audit/rendered/`. Pages 1--4 were individually inspected at
150 dpi. Text, equations, citations, URLs, accents, margins, and page numbers
are legible with no clipping, overlap, or missing content. The short final
page's whitespace is intentional. Optional PDF title/author metadata fields are
blank, but the visible identification is complete; this is informational, not
a build or visual defect.

The final command
`release_gate.py check /Users/mac/4prove-or-disprove-math/projects/bigMac-00015-p01`
returned `ok:true`, with kind `resolution-paper`, original status `proved`, and
pages `4`. `source.md` remains immutable at SHA-256
`d05c6b4a48e96b445089524057e53acaa3154a1fd9fe6979317c6d55c7a512d1`.

Obstacle/limitation: the literature comparison remains deliberately bounded;
the absent optional workbook-derived bibliography report prevents no local
release because every citation actually present was verified.

**One next test:** the supervisor should run `release_gate.py publish` on the
unchanged project and confirm creation of `release/manifest.json` and
`release/main.pdf` with the PDF digest above.
