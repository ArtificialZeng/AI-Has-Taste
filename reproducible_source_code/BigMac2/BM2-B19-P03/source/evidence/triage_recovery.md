# Triage recovery record

The first triage worker reached its eight-minute wall-clock ceiling before it
could write `problem.md` or return the required structured result.  A formally
requeued second triage did the same: repeated response-stream timeouts consumed
its opening minutes, and its two attempted checkpoint patches targeted the
obsolete pristine template rather than the recovered file.  It returned no
`result.json` and changed no research artifact.  These are operational
timeouts, not mathematical decisions about the frozen CSP.

## Material verified before timeout

- Immutable `source.md` has SHA-256
  `29441258d1fb9526154bab4ea6f8c973728e4ab25b86dc18932baa2b03e5e596`.
- The local Zenodo deposit `batches/literature/bigMac-19/supplement.zip` has
  MD5 `2a3ac93eaa5c9e6dc72d4bc3d42bdcb6`, agreeing with the deposited record,
  and SHA-256
  `5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4`.
  ZIP integrity and its member inventory were checked.
- Member `agl_29_g14.g6` is one CRLF-terminated graph6 record (54,884 bytes;
  payload length 54,882 bytes) with SHA-256
  `8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e`
  and CRC32 `b19efdef`.  A completed pure-Python decode, independently
  replayed with the deposited `egtools.py`, establishes 812 vertices, 1,218
  edges, simplicity, connectedness, degree set `{3}`, and girth 14.
- The supplied paper (arXiv:2609.04686v1, pp. 3--4 and 6--7) and deposited
  scripts support the precise orientation inequality and report the `p=29`
  instance as left open.  This supports intake only; it does not prove the
  CSP is still unresolved beyond the searched sources.
- The archive includes pure-Python graph6 and short-cycle utilities
  (`egtools.py`, `gadget_design.py`) and a PySAT-based orientation encoding
  (`f6_construct.py`, `f6_lean.py`).  The current machine has
  `/opt/homebrew/bin/cadical` 3.0.1 and `/opt/homebrew/bin/kissat` 4.0.4; its selected
  Python environment does not currently provide `pysat`, `z3`, or `networkx`.
  No package installation is required for the next validation step.

## Exact scope still missing

No 14--16 cycle census, satisfiability result, assignment, or UNSAT
certificate was produced during either triage attempt.  The graph decode and
basic property checks are complete.  The outer supervisor has now normalized
the already-admitted frozen statement in `problem.md` without changing
`source.md`, so another short context need not repeat this clerical step.

## One next test

At the next clean owner boundary, officially requeue directly to research
without resetting history.  Deterministically enumerate and canonicalize the
14-, 15- and 16-cycles, record a complete census, and independently reconstruct
the three-choice capacity CNF.  Emit DIMACS directly for CaDiCaL/Kissat, so
the absent optional Python packages do not block the test.  A SAT result must
retain the 812 choices and pass an exhaustive cycle check; an UNSAT result
must retain a proof accepted by an independent checker.
