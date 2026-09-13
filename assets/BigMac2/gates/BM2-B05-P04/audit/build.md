# Fresh build audit

Release job: `bigMac-00005-p04-release-6b0c3be4a6a2`.

The existing build log `manuscript/article.log` is nonempty (22,601 bytes),
ends with `Output written on article.pdf (5 pages, 291189 bytes)`, and has
SHA-256 `a8a9d9be003b258d560d44917ef1e5f64121c6f7fc7ff13ac90dbe6fe0a6c11a`.
The PDF digest agrees with `audit/manuscript-snapshot.json`.

I inspected the complete LaTeX and BibTeX diagnostics.  There are no fatal
errors, undefined citations or references, multiply defined labels, rerun
requests, package warnings, or overfull/underfull boxes.  BibTeX reports three
used entries and zero warnings.  The PDF has a valid text layer (10,380 bytes
from `pdftotext`) and all 18 listed fonts are embedded and subsetted.

`pdfinfo` reports a five-page, unencrypted letter-size PDF produced by pdfTeX.
Its optional Title, Author, Subject, and Keywords metadata fields are blank;
the visible title and author are correct.  This is a disclosed metadata
polish item, not a compilation, reference, font, text-extraction, or layout
failure.

Verdict: the recorded build is clean.  No rebuild or manuscript-source edit
was made during this audit, and the final full release gate accepted the
current evidence and manuscript bindings.
