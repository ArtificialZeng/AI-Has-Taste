# A321614 exact proof release

Terminal result: **PROVED** for the fixed four-operation rectangle group
`{identity, horizontal flip, vertical flip, 180-degree rotation}` at every
index, including `n=2`.

Run `make verify` from the project root to reconstruct and verify the exact
certificate, both independent audits, the no-import verifier, the paper, and
its bibliography.  Run `python3 code/test_fail_closed.py` for optimized-mode
tamper rejection; repeat `--python` for cross-interpreter testing.
See `FINAL_STATUS.md` for the theorem and the necessary full-`D4` caveat.

The source archive contains the proof, exact certificates, independent
verifiers, audit trail, literature ledger, and LaTeX sources.  No proof
assistant was used.

The final hash manifest is intentionally rooted at `release/frozen`, which
contains only immutable release artifacts.  This excludes the scheduler's
continuously written `logs/` file from the trust boundary.
