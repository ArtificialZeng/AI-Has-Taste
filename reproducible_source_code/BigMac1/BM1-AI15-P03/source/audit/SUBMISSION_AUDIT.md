# Submission audit

**Result: PASS**  
**Audit date:** 2026-08-29 (Asia/Shanghai)  
**Terminal mathematical state:** PROVED

## Mathematical and scope checks

- The title, abstract, theorem, and conclusion all state the same quantified
  result for every \(n\ge6\), with zero set exactly \(\{7,8,12,16\}\).
- The graph definition specifies the vertex set, all three edge types, labelled
  colours, and identification of repeated unordered edges.  The \(n=6\)
  offset-three/diameter collision is handled explicitly.
- Every infinite residue class is covered by one of four literal colour-word
  families.  All endpoint exponents and seams have been checked.
- Nonexistence at the four exceptions is proved structurally.  Exhaustive
  enumeration is supplemental and is not used as a substitute for the proof.
- The independent referee's remediation recheck ends in a clean PASS with no
  fatal, major, local, or expository issue left open.
- The supplementary transfer route proves a two-way colouring/automaton
  correspondence with the mandatory track-swap seam.  Its independent
  implementation/cone recheck ends in PASS with no unresolved item.

## Novelty and citation checks

- A pre-result claim ledger and search log were frozen before the proof route
  was accepted; a second search was run after the exact theorem wording and
  blocks were known.
- The manuscript makes only a bounded search-scope novelty statement and does
  not claim absolute priority.
- All externally attributed factual claims are supported by nearby citations.
  The dedicated citation audit verified 10/10 fixed claims with zero
  numerical errors, hallucinations, or misleading attributions.
- `audit_latex.py` reports `cited=4 bib=4 missing=0 unused=0`; every bibliography
  entry is cited and DOI metadata were checked against the DOI record.

## Authorship, disclosure, and publication hygiene

- The author name, affiliation, and email in the manuscript were inherited
  from the project scaffold and were not inferred from the literature.
- There is no invented funding, acknowledgement, conflict-of-interest,
  institutional-approval, or data-availability claim.
- The manuscript includes an accurate computational/AI disclosure and says
  explicitly that no proof assistant was used.
- No journal-specific formatting or submission-policy compliance is claimed;
  no target journal was specified.  The source uses standard `amsart` and an
  internally consistent `amsplain` bibliography.

## Source, build, and visual checks

- The main LaTeX source, bibliography, formal statement, proof notes,
  serialized certificates, and verifiers are present and named consistently.
- The release manuscript retains only the shorter \(A=01,B=21202\) proof as
  its main argument.  The one-flip construction is explicitly marked as a
  supplementary appendix, and the transfer/cone route is a separate exact
  audit artifact, avoiding competing manuscript proofs.
- A clean out-of-tree `latexmk`/BibTeX build produced the release PDF.  Its
  final log has no warning, undefined reference, overfull/underfull box, or
  error match.
- The five-page PDF was rendered with Poppler at 144 dpi.  Every page was
  inspected at original rendered resolution; no clipping, overlap, missing
  glyph, broken table, black box, or unreadable text was found.
- The final PDF SHA-256 is
  `29d3ce3524c49628d613a749d5c05673eb47b8c69749107f74e8dc8efccce83b`.

## Reproducibility checks

- The builder verifier checks 9,991 constructed orders through \(n=10000\)
  and exhausts all \(2^n\) sign words at \(n=7,8,12,16\).
- A second verifier reconstructs exact colouring counts through \(n=20\) in
  two independent engines and stress-checks the constructions.
- A third verifier rebuilds the alternate serialized sign-word certificate.
  After its optimization-mode defect was reported, all correctness assertions
  were replaced by explicit failures.  A 12-cell adversarial matrix now passes
  in normal, `-O`, and `-O -I` modes.
- A fourth verifier reconstructs the 12/54-state matrices, their twisted
  closure, the strictly positive powers \(O^{10}\) and \(E^{13}\), and a
  separate direct-graph finite certificate through \(n=25\).  It passes in
  normal and optimized isolated modes; an independent referee also rejected
  positive-power, threshold, and acceptance-text tampering.
- The release manifest is generated only after the final status, audits, and
  source archive have been fixed; its independent verification command is
  recorded in `FINAL_STATUS.md`.

- The final source archive and manifest use explicit static whitelists rather
  than a recursive directory scan.  They contain no `logs/`, `tmp/`, build
  directories, caches, bytecode, or TeX auxiliary files.  Both archive and
  manifest member sets are checked for exact whitelist equality.
- `TASK_STATUS.json`, `FINAL_STATUS.md`, and `research_state.json` remain
  outside the frozen payload because they record the final ZIP and manifest
  hashes; including them would create a self-referential hash.  This control
  plane exclusion is documented in `release/frozen/README.md`.

No unresolved submission blocker remains within the declared scope.
