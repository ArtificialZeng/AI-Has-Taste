# Certified source bundle contents

The release ZIP contains the exact certificate and no-import verifier,
fail-closed regression suite, formal/source statements, proof and route
records, discovery scripts and retained diagnostics, two-pass literature
ledger/search logs, all audits, final status, manuscript source/bibliography/
PDF, and reproducibility metadata.

The bundle omits temporary rendered PNGs, Python bytecode caches, LaTeX
scratch files other than the generated `.bbl`, and locally archived copies of
third-party papers.  Stable source links and source hashes remain in the
literature/audit records.

`MANIFEST.json` uses this `release/` directory as its root and binds the
curated ZIP plus this contents note.  This scope intentionally excludes the
live project session log, whose append-only growth would make a whole-working-
directory manifest unstable after creation.
