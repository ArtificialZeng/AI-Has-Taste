# Fresh citation and bibliography audit

## Method and frozen extraction

I used a non-interactive two-pass audit.  Pass 1 froze every manuscript
claim/citation pair in `audit/claim-ledger.json`; Pass 2 verified only those
four entries against the primary-source locations in
`audit/source-locations.md`.  No subagent was used because the release job
explicitly prohibited agents and background workers.

## Claim-level verification

| Claim | Key | Source support | Result |
|---|---|---|---|
| CIT-01 | `Bhardwaj2026` | Section 3.1, Lemma 1, printed p. 7 describes the vertex split and intermediate NAE equality clauses. The displayed proof has no explicit four-ary clause list or projection table. | Verified, exact/paraphrase |
| CIT-02 | `Bhardwaj2026` | Section 3.2, printed p. 7 says the linear clause hypergraph makes the K6 subgraphs edge-disjoint. | Verified, paraphrase |
| CIT-03 | `DarmannDocker2019` | Lemma 3, pp. 9--10 contains 12 arity-three clauses and the exact all-four-terminals-equal extension property; Theorem 2, p. 10 performs occurrence replacement and proves linearity. | Verified, exact/paraphrase |
| CIT-04 | `ZengEtAl2026` | Section 1, p. 2 explicitly separates encoding soundness, whole-instance termination, and independent checking of a proof trace. | Verified, paraphrase |

The DOI/title/author/year data of each retained entry agrees with its source
record or title page.  The final key `ZengEtAl2026` intentionally differs from
the registry's `Zeng2026SSRN7334758`; this is recorded in
`audit/user-bibliography-selection.json`.  No manuscript citation key changed
during this audit, and no retained citation is decorative.

## Coverage and closest-work screen

The bibliography is not Excel-only: it cites the frozen problem's primary
arXiv source and the closest explicit NAE linearization construction inspected,
in addition to the one genuinely relevant active-library paper.  Targeted
searches for “linear NAE-4 equality gadget,” “monotone NAE-4 gadget
linearization,” and four-uniform NAE equality constructions found no equivalent
explicit four-uniform terminal gadget.  That limited negative search supports
only the manuscript's qualified phrase “closest ... we found”; the paper makes
no priority claim.

No further external dependency requires a citation.  The projective incidence
argument is elementary and proved in the manuscript.  The finite claims rely
on the supplied inspectable verifier and a completeness proof, not on a cited
solver theorem.  Adding another user-library entry would be padding rather than
natural scholarly coverage.

## Mechanical consistency

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` found three
cited keys, three unique bibliography entries, no missing bibliography, no
missing key, no unused entry, and exact agreement with the final auxiliary
file.  The final `.log` and `.blg` contain no undefined citation, undefined
reference, missing database entry, repeated entry, BibTeX warning, LaTeX error,
fatal error, emergency stop, undefined control sequence, or runaway argument.

**Verdict: accept.** All nearby citation claims are supported, bibliography
coverage is proportionate and primary-source based, and citation compilation is
clean.  This is a release audit, not a priority or peer-review certification.
