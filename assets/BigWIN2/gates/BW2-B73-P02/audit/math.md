# Fresh mathematical referee report

**Verdict: accept.**  The frozen `resolution-paper` claim is correct in its
full stated scope.  This review is bound to snapshot
`2a99216a023c7a9cfdc90150326d88f318af37372622653dccda563d6f4bf1c2`
and referee job `win-00073-p02-referee-0601432878f0`.

## Scope and integrity

I checked the SHA-256 digest of every file named in `audit/snapshot.json`.
All six files match the frozen file map, including the immutable `source.md`
hash `482b5d1916aca9fbcae82d4fbaa0069f6313a9c0b1c78e68d713ead991de6c9d`.
The claim to review is the full biconditional for every odd prime `p>3`, not a
weaker claim about only four examples.

## Reconstruction of the upper range

Let `f(x)=x^3+A*x+B`, with `A,B` represented in `{0,...,p-1}`, and let
`e=(p-1)/2`.  If `c_(p-1)` is the coefficient of `x^(p-1)` in `f(x)^e`,
Euler's criterion and the finite-field power sums give

`a_p := p-N = -sum_x chi(f(x)) = c_(p-1) (mod p)`.

The base-`2^(p^2)` digit extraction in equation (4) returns this coefficient
as an integer before the outer reduction modulo `p`: all coefficients are
nonnegative, and their sum is below the radix.  Thus equation (4) returns the
least residue `r` of `a_p` modulo `p`.  For a nonsingular cubic, Hasse's bound
gives `|a_p|<=2*sqrt(p)`; for a singular cubic, the source proves the stronger
bound `|a_p|<=1`.  When `p>=17`,

`p-2*sqrt(p) > 2*sqrt(p)`.

Consequently only one of `r` and `r-p` can be `a_p`, and `r^2<=4p` selects
`a_p=r`; otherwise `a_p=r-p`.  Equation (5) is exactly `N=p-a_p` expressed
with truncated subtraction.  I checked the live primary text of Dumitru and
Prunescu, arXiv:2609.05371v1, Lemmas 4--6 and Theorem 3.  Its equation (4),
equation (5), natural-number parameter reduction, affine count, threshold
`p>=17`, and explicit inclusion of repeated-root cubics all match the frozen
claim.  In particular, the boundary prime `17` satisfies the strict separation
because `sqrt(17)>4`.

## Independent lower-prime replay

I used a fresh implementation, `evidence/referee_independent_check.py`, which
does not import or call the submitted verifier.  It evaluates equation (4)
literally with Python integers, extracts the same coefficient independently by
the multinomial formula, and counts points using the fibre sizes of the square
map rather than enumerating `(x,y)` pairs.  Its captured output is
`evidence/referee_independent_check.txt`.

For a choice of `i` factors `x^3`, `j` factors `A*x`, and `k` factors `B`, the
coefficient conditions and contribution are

`i+j+k=e`, `3i+j=p-1`, and `e!/(i!j!k!)*A^j*B^k`.

This gives the following exact results.

| `p,A,B` | nonzero coefficient terms `(i,j,k; value)` | equation-(4) digit | `r` | complete `f(x)` vector | `N` | equation-(5) `Nhat` |
|---|---|---:|---:|---|---:|---:|
| `5,1,1` | `(1,1,0;2)` | 2 | 2 | `1,3,1,1,4` | 8 | 3 |
| `7,0,1` | `(2,0,1;3)` | 3 | 3 | `1,2,2,0,2,0,0` | 11 | 4 |
| `11,1,3` | `(3,1,1;60)` | 60 | 5 | `3,5,2,0,5,1,5,1,6,4,1` | 17 | 6 |
| `13,0,4` | `(4,0,2;240)` | 240 | 6 | `4,5,12,5,3,12,12,9,9,5,3,9,3` | 20 | 7 |

The nonzero square sets used to count the displayed vectors are respectively
`{1,4}`, `{1,2,4}`, `{1,3,4,5,9}`, and `{1,3,4,9,10,12}`.  Hence these are
complete affine counts, not samples.  In all four rows `r^2<=4p`, so the
equation-(5) lift indicator is zero and `Nhat=p-r`, producing the displayed
mismatches.  The discriminants `4A^3+27B^2 mod p` are `1,6,5,3`, so every
witness is nonsingular.  Nonsingularity is additional information rather than
a missing hypothesis, since one counterexample of either type would refute the
universal assertion.

The exact primes strictly between `3` and `17` are `5,7,11,13`.  Thus these
four mismatches disprove the universal assertion at every admissible lower
prime, while Theorem 3 proves it at every prime at least `17`.  Together they
prove the frozen biconditional.

## Adversarial checks and source comparison

- The count is affine throughout; no projective point at infinity was added.
- Canonical representatives are used, so equation (4) is evaluated on the
  same natural inputs as the source theorem.
- The divisions are by positive powers of two, and `0<=r<p`, so neither
  division by zero nor a truncated-subtraction ambiguity occurs.
- Literal big-integer digit extraction agrees with the separate multinomial
  calculation in all four rows; point counts use every `x` in each field.
- The four lower primes exhaust the lower quantified domain, and the cited
  theorem covers arbitrary parameter pairs, including singular cubics, in the
  upper quantified domain.

The author names in immutable `source.md` are bibliographically incorrect:
the linked arXiv v1 record names Bogdan Dumitru and Mihai Prunescu, not Arno
Fehm and Kurt Girstmair.  `problem.md` and the frozen research audit disclose
this, and the arXiv identifier, title, formulas, and theorem used in the proof
are the correct ones.  This metadata defect does not affect the mathematical
claim, but any manuscript bibliography must use the live record's authors.
The contribution is honestly scoped as the short sharpness completion of a
supervisor-generated question; it does not claim authorship of Theorem 3 or
unsupported literature priority.

There is no unresolved mathematical gap in the frozen candidate.  I therefore
accept the exact `resolution-paper` scope with original status `proved`.
