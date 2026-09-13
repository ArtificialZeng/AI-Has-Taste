# Checkpoint

## Accepted mathematical scope

The frozen k=2 claim is disproved at its least admissible index:
`b(5)=25056=5*5011+1`. The accepted kind is `resolution-paper` and original
status is `disproved`. The distinct k=4 conjecture in Thejitha--Fathima is
unaffected. The manuscript maintains this limitation throughout.

`source.md` is unchanged, SHA-256
`b891202372ba5c77b5b7f18fe5ac0bd99b438bb6d9f8e159d26070cf649c979e`.
The authoritative actual source digest is also recorded below in the fresh
validation artifact; all snapshot-bound files match the accepted snapshot.
Decisive evidence remains `evidence/research_b5_audit.md`, both frozen integer
programs, and the independent recurrence in `audit/math.md`.

## Completed release audit

Release job: `bigMac-00006-p03-release-45c673bd9503`, 2026-09-08.
The main math skill and release role/contract were read; no workers were
spawned. The explicitly invoked `$citation-check-skill` was used as advisory
with separate fixed extraction and verification passes. The accepted evidence,
complete manuscript sources, real final build logs, and all PDF pages were
reviewed. Both frozen coefficient programs and an exact recurrence calculation
were executed again; see `evidence/release-coefficients.json` and
`evidence/release-validation.json`.

`audit/citations.md` and `audit/citations.json` accept the citation scope.
Version-1 primary arXiv text confirms equation (1.2), metadata, and the k=4
parameter in Conjecture 7.1. The supplied Excel BibTeX record is preserved
verbatim and supplies one genuinely relevant methods comparison. Its DOI and
metadata use `metadata_basis=user_designated_workbook`; external refresh
unavailable. The supplied workbook extract/relevance assessment is
`literature/user_bibliography_check.md`. The complete workbook and Zeng full
text were not independently inspected here; no stronger claim is attributed
to that reference. Searches and limits: `audit/release-web-check.md`.

`audit/build.md` and `audit/build.json` accept the existing clean four-command
build after fresh inspection of its actual final TeX/Biber logs and complete
transcript. Final diagnostics are clean, and all 25 PDF fonts are embedded.
No source or PDF edit or new compilation was necessary.

`audit/visual.md` and `audit/visual.json` accept the unchanged three-page PDF.
Pages 1, 2, and 3 were freshly rendered and each opened as an image. No clipping,
overlap, unreadable formulas, missing glyphs, or unresolved references was
found. Images: `evidence/release-render/page-1.png` through `page-3.png`.
The final PDF remains `manuscript/main.pdf`.

Every fresh release audit binds the assigned release job and current evidence,
manuscript, and PDF digests. `release_gate.py check` passed; its exact result is
saved in `evidence/release-gate-check.json`. `source.md`, claim/evidence,
manuscript, bibliography, PDF, and their snapshots remain unchanged. No
mathematical/build/visual blocker remains; the disclosed external-refresh
limit does not prevent local release. No publish or external submission was
performed by this worker.

## One next test

The supervisor should run `release_gate.py publish` on this project to activate
the exact validated PDF and manifest; publication rechecks current bindings.
