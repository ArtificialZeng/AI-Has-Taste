# Checkpoint

Job provenance: bigMac-00008-p04-research-cad23325b5f2 (research pass 1).

## Current claim

- Candidate outcome: **resolution-paper**; proposed original status: **proved**.
- Exact statement: over every field, every $(x,y,z)$-primary monomial ideal
  in $K[x,y,z]$ with at most four minimal generators, each of total degree at
  most four, satisfies $v(\overline I)\leq v(I)$.
- Field scope is unrestricted: the certificate uses only exponent
  divisibility, rational/integer Newton-polyhedron tests, and monomial socles.

## Decisive evidence

- The complete labeled parameter set contains 517 ideals: 64 pure-power
  triples and 453 triples plus one incomparable mixed generator. No
  variable-permutation quotient was used.
- evidence/enumerate_lp.py decides all integral-closure memberships by exact
  rational active-set vertex feasibility and computes both v-numbers by the
  three-neighbor socle test.
- evidence/enumerate_facets.py independently decides Newton membership by
  exact integer dual-cone rays. It computes the input socle by a closed formula
  and the closure socle as the globally maximal points of its standard
  down-set.
- Each method checks 31,922 expanded-grid exponents, covering all 13,270
  standard-box exponents. evidence/compare_runs.py finds exact agreement on
  every membership bitmap, complete socle list, and v-number. The common
  distribution of $v(\overline I)-v(I)$ is
  $-6:1,-5:6,-4:19,-3:82,-2:194,-1:124,0:91$; there are no violations.
- Both methods recover $v(I)=2<v(\overline I)=3$ for the degree-five control
  $(x^2,y^2,z^5,xyz)$. The canonical admissible-record hash is
  ffdd460fb7212673c7d8168be996eb8498d0ad1654527ce3590164e718c4753c.
- evidence/exhaustive_proof.md proves input completeness, correctness of both
  exact membership algorithms, completeness of the finite boxes, and the
  field-independent conclusion. evidence/verification.json records hashes.
- source.md remains byte-for-byte unchanged with SHA-256
  ef9b49c782c4ea63b2df51f5da7e2856e06aebf72b9f721bace16feb074e033e.

## Remaining gate and one next test

No mathematical gap is asserted by the proposer, but this is not yet accepted:
a fresh referee must audit the parameterization and the dual-ray completeness
argument, rerun the three documented commands, compare the output hashes, and
check that the degree-five positive control is recovered. Any failed audit
returns the precise disputed lemma or record to research.
