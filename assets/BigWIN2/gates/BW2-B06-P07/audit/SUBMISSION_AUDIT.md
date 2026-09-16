# Submission audit

Date: 2026-08-30 UTC

Final status: PASS for submission as a partial theorem.  This is not a claim
that the arbitrary-tree conjecture has been solved.

## Contribution gate

- The manuscript does not claim the arbitrary-tree conjecture.
- It proves a nontrivial infinite-family theorem: the short-arm capacity
  inequalities characterize finite multiset dimension for every starlike
  tree, and every finite case satisfies the conjectured diameter bound.
- The class has unbounded order and degree, and known starlike constructions
  have unbounded ID-number.
- It also gives an independently certified finite result through order 15.

## Mathematical gate

- Formal statement and conventions agree with the frozen source problem.
- Builder, Breaker, Certifier, and Referee records were maintained serially.
- The main proof has no computational premise.  The capacity obstruction,
  binary construction, odd-modulus depth recovery, polynomial arm recovery,
  binary-weight budget, and exceptional four-arm cases are closed.
- The source sharpness family is recovered exactly.
- Failed stronger routes and the still-fatal arbitrary-tree gap are disclosed
  outside and inside the manuscript as appropriate.

## Novelty and citation gate

- The 2018 conference slides defeat novelty of the preliminary three-leaf and
  two-stem observations; neither is presented as a new contribution.
- Kono--Zhang's 2021 necessary capacity condition is cited at the point of
  comparison.
- Exact post-result searches under both multiset-dimension and ID-coloring
  terminology did not locate the general sufficiency theorem or its diameter
  corollary.  This is a bounded search conclusion, not a claim of exhaustive
  absence.
- The July 2026 surveys and the later July 30, 2026 primary paper were checked;
  none resolves the frozen tree conjecture or contains the starlike theorem.
- Every bibliography entry supports a cited statement and has a verified
  title, author list, year, and arXiv identifier or DOI.

## Presentation and ethics gate

- Title and abstract state the partial scope and the open global limitation.
- Author, affiliation, and both requested emails are present.
- The paper contains no internal role IDs, route IDs, confidence scores,
  hashes, or internal audit language.
- Exact computation is separated from the symbolic proof, and bounded checks
  are not described as infinite proofs.
- Code/data availability and generative-AI assistance are disclosed plainly;
  responsibility remains with the author.

## Final artifact gate

- The final eight-page PDF was built without warnings and inspected page by
  page after the last bibliography change.
- The LaTeX ZIP was independently extracted and rebuilt; the resulting PDF
  has the same eight-page structure and clean final log.
- The archive's evaluator test and fail-closed report comparison both pass.
- Artifact hashes are confined to the independent manifest and do not appear
  in the manuscript.

Decision: the work clears the submission threshold as a nontrivial infinite
subclass theorem plus a certified finite result.

## Continuation freeze

The new round proves a useful hull-center deletion lemma, refutes its first
local iteration, and derives an exact rooted-attachment shell identity.  It
does not prove a strictly stronger infinite subclass or the arbitrary-tree
conjecture, and its open cancellation gap prevents a new submission claim.

Accordingly:

- `paper/main.tex`, `paper/references.bib`, the accepted PDF, and the LaTeX ZIP
  were not edited or rebuilt;
- their bytes match the pre-continuation manifest entries;
- the existing starlike submission remains valid under its original scope;
- the continuation material remains a separate audited research record.

Continuation manuscript decision: preserve the accepted partial-theorem
artifacts byte-for-byte; do not generate a replacement paper.
