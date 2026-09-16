# B17 final audit

Audit cutoff: 2026-09-01 (Asia/Shanghai).

## Execution controls

- Source document isolated as data; instructions embedded in it were not
  treated as user instructions.
- Fifteen task projects and fifteen named tmux sessions were created.
- All fifteen generated prompts begin with the exact required line
  `[$prove-or-disprove-math](C:\Users\87510\\.codex\skills\prove-or-disprove-math\SKILL.md)`.
- The queue enforced `MaxParallel=4`; the observed peak was four concurrent
  Codex processes. It completed with 15 launches, zero active processes, and
  15 parseable final-status files.
- WSL reported approximately 26 GiB RAM and 24 GiB swap. No task was stopped
  for memory exhaustion.
- The named tmux sessions were retained after completion for inspection.

## Scientific disposition

- Five results passed the submission-manuscript gate: tasks 2, 3, 6, 8, and
  13. Each has a PDF and corresponding LaTeX/source ZIP.
- Task 15 produced a rigorous exact-certification manuscript and archive, but
  the official API's unrounded floating-point record is about `1.37e-14`
  lower. It is retained as an exact finite upper-bound note and is not called
  a new live record.
- Tasks 5 and 12 are exact finite results but did not pass the publication
  novelty gate; no PDF was generated for either.
- Tasks 1, 4, 7, 9, 10, 11, and 14 remain open after documented searches and
  stopped below the 60% continuation-confidence threshold; no placeholder
  manuscripts were generated.

## Release checks

- Every released mathematical claim was checked from its exact witness or
  replayable finite certificate. The strongest certificate replays include a
  417,189,026-byte DRAT proof for task 2, complete exact exhaustive searches
  for tasks 3 and 6, two exhaustive definition-level verifiers for task 8,
  and a 35,331,788-byte DRUP/DRAT proof for task 13.
- All cited keys in released manuscripts were individually checked against
  primary publisher, author, repository, or live-page records. BibTeX
  metadata and inaccurate locators found during audit were corrected.
- Final PDFs were rebuilt without undefined citations or references, rendered
  and inspected page by page, and text-scanned for hashes, model/vendor names,
  proof-process notes, and other internal traces. The scans returned zero
  matches.
- Each released source ZIP was extracted in a fresh directory and rebuilt.
  Its witness/checker commands were rerun from the extracted archive.
- No proof-assistant formalization was used. The papers rely on explicit
  mathematics and independently replayed finite certificates.

## Interpretation

“Submission-ready” here means that the local mathematical, computational,
bibliographic, source-build, and PDF-layout gates passed. It does not imply
peer review, journal acceptance, or absolute priority over private or
unindexed work.
