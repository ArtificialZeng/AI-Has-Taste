# Mathematical referee report

Verdict: **accept** the exact frozen candidate.

Referee job: `primary-20260913-multiset-rook-referee-16d847d36008`.
Review date: 2026-09-13 UTC.
Snapshot digest: `504145184b080ede72dcc81b550b2532dd2735ee8c192cc934b26a38d9154ba3`.
Frozen kind: `resolution-paper`. Frozen original status: `disproved`.

The counterexample disproves the interlacing clause of AJQ Conjecture 28,
and hence the conjunction frozen in `source.md`. It does not decide the
separately quantified total real-rootedness clause. This is the submitted
scope itself; acceptance does not substitute a weaker contribution.

## Inputs and independent checks

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and
the listed proof, source audit, verifier, numerical certificate, both TSV
certificates, literature screen and relevant portions of both primary HTML
sources. I did not use checkpoint/state files, earlier transcripts or owner
confidence as evidence. No additional agents or workers were used.

The fresh verifier `audit/referee-verify.py` imports no research code. It
visits every string in `{1,2,3,4}^6`, tests the exact content and row bounds,
and counts strict comparisons in positions 1 through 5. Among 4096 strings,
180 have the specified content and exactly 60 satisfy the board bounds.
Every serialized word, first letter and ascent count in the 60-row TSV
agrees. All 30 rows of the base-insertion certificate also agree; their
two insertions recover the same complete word set. The refined and split
counts in the frozen JSON agree as well.

The verifier checks the factorizations and sign evaluations using integer
and rational arithmetic. It independently reproduces source Example 26:
12 legal words with total polynomial `3t+8t^2+t^3`. All 12 snapshot file
hashes, the exact evidence-file set, and the canonical mapping digest match,
both before and after verification. `source.md` retains SHA-256
`2a88f14a8f18991b1253ef13abad929e8b00f48326545c52911ef89a6707f18f`.
Results are saved in `audit/referee-verification.json`.

The research verifier was inspected but not rerun, since its entry point
rewrites two frozen evidence files. This review relies on the separate
enumeration and the mathematical argument below, not on an earlier program's
success flag. The original 720-labeled-order method was inspected in code;
the independent method actually executed here was the Cartesian product.

## Reconstructed argument

The witness has six rows of lengths `(3,3,3,3,4,4)` and content `(2,2,1,1)`.
The row lengths are positive and nondecreasing. It is a non-skew,
nonrectangular Ferrers board. Its words use two copies each of 1 and 2
and one copy each of 3 and 4. The multiset definition permits column
repetitions, and the source's own board `22233` shows that the staircase
restriction from the nonattacking setting is inapplicable here.

The unique 4 can occupy only position 5 or 6. Deleting it gives a
permutation of `11223`; conversely either insertion into any such base is
legal. This is a bijection. There are `5*binomial(4,2)=30` bases, hence
exactly 60 words. For a base `v`, insertion in position 5 has ascent count
`1+asc(v_1 v_2 v_3 v_4)`, while insertion in position 6 has ascent count
`1+asc(v)`. The complete checked table gives:

| First letter | 4 in position 5 | 4 in position 6 |
| --- | --- | --- |
| 1 | `5t^2+7t^3` | `2t^2+8t^3+2t^4` |
| 2 | `t+9t^2+2t^3` | `6t^2+6t^3` |
| 3 | `2t+4t^2` | `t+4t^2+t^3` |

Consequently

```
R3 = t(t^2+8t+3),
R2 = t(8t^2+15t+1),
R1 = t^2(t+7)(2t+1).
```

AJQ Definition 9 requires every pair of earlier and later entries to
interlace, not just adjacent entries. Thus `(R3,R2,R1)` requires
`R3 preceq R1`. In Definition 8, if `f` has degree 3 and `g` degree 4,
the root chain starts `b4 <= a3 <= b3 <= a2 <= b2 <= a1 <= b1`, where
the `a` roots belong to `f` and the `b` roots to `g`.

Here `R3` has roots `0,-4+sqrt(13),-4-sqrt(13)`, and `R1` has roots
`0,0,-1/2,-7`. Since `sqrt(13)>3`, its required initial inequality is
false: `-7 > -4-sqrt(13)`. As an independent exact check, the quadratic
`t^2+8t+3` takes values 3 and -4 at -8 and -7, respectively, placing
a root strictly below the least root of `R1`. The quadratic's other
root lies in `(-1,0)`. This also verifies the identity of the least root
without a numerical root routine.

All polynomials in the failed pair are nonzero, have positive leading
coefficients, and have only nonpositive real roots. The roots at zero
were retained with multiplicity. No choice of zero-polynomial convention
or cancellation of common factors is involved. `R2` is also real-rooted:
its quadratic discriminant is 193, with `0<193<225`, so both quadratic
roots are real and negative.

Finally, summation yields

```
R = 2t(t^3+12t^2+15t+2).
```

For its cubic factor, the values at `-11,-10,-2,-1,0` are respectively
`-42,52,12,-2,2`. The intermediate value theorem gives one root in each
of `(-11,-10)`, `(-2,-1)`, and `(-1,0)`. Degree three exhausts the roots;
the additional root of `R` is zero. Thus the claim's affirmative
real-rootedness statements for this particular witness are proved too.

## Source comparison and contribution

The relevant primary definitions and conjecture were read directly from
the frozen AJQ HTML and checked against the live
[arXiv v1 source](https://arxiv.org/html/2502.05939v1#S3.SS3).
Theorem 12 covers the distinct-letter setting; the source attributes the
rectangular cases to Simion and Ma--Pan. Those older proofs are not
dependencies of this self-contained disproof.

The frozen Yan v1 Introduction and its Theorems 1.4/1.5 concern
unrestricted colored words and interlacing of totals as content changes.
The live record also has v2, dated 2026-08-20; I checked its
[Introduction and the same theorem statements](https://arxiv.org/html/2608.15682v2#S1),
which retain that scope. This does not supply the arbitrary row-flagged
first-entry assertion or the candidate counterexample. The v2 check is
a source-comparison update, not a change to the candidate mathematics.

Fresh bounded searches found no equivalent primary counterexample among
the inspected results. Full queries, source locators and access limits
are recorded in `audit/referee-literature.md`. This is not a worldwide
priority certification. The explicit failure of the proposed general
extension is a useful correction beyond the preceding distinct-letter
and rectangular results, and the exact witness provides a reproducible
test for future interlacing claims. Its short proof does not diminish
that contribution.

## Scope limits and disposition

No unresolved mathematical gap was found in the frozen statement. The
universal total-polynomial clause, minimality, larger computational ranges
and exhaustive priority remain outside the claimed result. None is needed
to refute the original conjunction. No limit, division, compactness or
uniformity argument occurs; the nontrivial checks are the full finite
domain and the exact root direction.

Accept for the next workflow gate with the exact frozen kind and status.
Any subsequent manuscript must state explicitly that the interlacing
clause fails and that this example's total remains real-rooted. This job
does not create or certify a manuscript, citations/build/visual audits,
or a released PDF. The runner remains responsible for the provenance
and `check-math` gate before dispatching writing.
