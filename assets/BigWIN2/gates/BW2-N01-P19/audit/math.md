# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Referee job: `newwin-00001-p19-referee-f7b236903823`.
Review date: 2026-09-12.
Snapshot digest: `f6e26cd2153e23fdfbc5be1822272e0031a1a19a7c9717f8d44555b03e6c3e02`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The argument proves nonconvergence of the original sequence `s_2(n)/n`.
Acceptance includes both asserted inequalities for every integer `t>=1`,
all the stated rational constants, and the common separated bounds for every
`t>=203`. It does not assert a result for higher iterates, exact global
liminf/limsup values, or optimality of the finite threshold.

## Inputs and independence

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and
the snapshot's listed proof, verifier, arithmetic output, primary PDF/text,
and literature comparison. All nine frozen file hashes and the canonical
snapshot digest were independently verified. In particular, `source.md`
retains SHA-256
`06bb18541ed5c313de4681fcc61eebb42d73353add1b3dc546c441aa8a9015b6`.
No owner checkpoint, scheduling state, earlier review, earlier job transcript,
or unlisted handoff was read. No agents or additional model processes were used.

The separate verifier `audit/referee_verify.py` was written in this referee
context and run successfully. It imports no proposer code and does not execute
the supplied verifier, which would write into the frozen evidence tree. The
new verifier computes its results before comparing with the frozen arithmetic
output. Its output is `audit/referee-verification.json`.

This is a fresh mathematical review pass, not a claim of statistical
independence or external peer review. No proof-assistant verification is claimed.

## Reconstructed decisive argument

### Positive membership

For `r>0`, membership in the second remainder set is equivalent to existence
of `q>=3` and a prime `p<q` such that

    (q+1)r <= n-q,       pq | (q-1)n+r.                 (1)

For the forward direction, write `n=qk+r`, `0<r<k`, with `k` in the first
set. Then `n=ah+k` for `1<=h<=floor(n/2)`, `h>k`, and `a>=2`.
The bound `n>=2(k+1)+k` ensures `q>=3`. A prime divisor `p` of `a`
satisfies `(n-k)/p>=h>k`, hence
`p<n/k-1=q-1+r/k<q`. Also
`q(n-k)=(q-1)n+r`, yielding the divisibility in (1). Finally `k>=r+1`
gives precisely its endpoint inequality.

Conversely, (1) implies `q|(n-r)`, so `k=(n-r)/q` is an integer with
`k>=r+1`. Cancellation in the integer divisibility
`pq | q(n-k)` gives `p|(n-k)`, including when `p|q`. Put `h=(n-k)/p`.
Since `p<=q-1` and `r>0`,
`n-k=(q-1)k+r>pk`, so `h>k`; also `h<=floor(n/2)` because `p>=2`
and `k>0`. These give both required Euclidean divisions and recover
membership from the definitions. There is no modular inversion assumption.

The zero value is outside (1) and contributes at most one to the cardinality.
For `n=1` the original sets are empty. The proof never divides by a zero
remainder or uses zero as a modulus.

### Fixed cutoff and a uniform count

Let `T_Q(n)` count positive witnesses in (1) having `3<=q<=Q`.
A missed positive value must have a witness `q>=Q+1`, hence
`r<n/(Q+2)`. Consequently

    0 <= s_2(n)-T_Q(n) <= floor(n/(Q+2))+1.             (2)

For fixed `n congruent to b (mod L_Q)`, every divisibility condition in
(1) depends only on `r mod L_Q`. Its smallest valid `q` is decisive:
the endpoint `H_q(n)=floor((n-q)/(q+1))` decreases with `q`. Thus a later
witness cannot contribute a larger representative from the same class.

For `n>=Q`, all these endpoints are nonnegative. Represent residue zero
by `L_Q` and the other residues by `1,...,L_Q-1`. The number of positive
representatives of a class `c` up to `H` is
`floor((H+L_Q-c)/L_Q)`. Its error from `H/L_Q` is at most one, and
`|H_q(n)-n/(q+1)|<2`. Summing over at most `L_Q` eligible classes gives

    |T_Q(n)-n C_Q(b)| <= L_Q+2.                        (3)

Combining (2) and (3) proves the stated lower error `(L_Q+2)/n` and
upper error `1/(Q+2)+(L_Q+3)/n`. The extra upper unit accounts for zero.
The proof fixes `Q` before letting `n` grow, so no exchange of limits or
unproved uniformity in a growing period is involved.

### Coefficients and the prime-power cases

For `b=1`, direct inspection of every representative in `1,...,75600`
gives the following least-witness counts for `q=3,...,10`:

    12600, 12600, 6930, 7770, 4110, 3540, 165, 1128.

This independent enumeration tests the defining congruences on each
representative; it does not use the proposer's residue-marking loop.
The weighted sum gives

    C_10(1) = 1182869/9979200 = beta.

For `b=0`, the conditions become `pq|r`. The proposed classification of
the smallest witness is correct. A composite quotient with a prime divisor
different from `p` has an earlier witness from that prime and `p`. If it
has no such divisor, it is a power of `p` with exponent at least two, and
the witness `p^2` is available because `p^3|r`. Thus only the second
smallest distinct prime divisor and prime squares with cubic divisibility
can be minimal.

For a prime witness `ell`, exactly one smaller prime `p` may divide `r`.
When `p^2<ell`, its cube must be absent; when `p^2>ell`, no cube
restriction is needed. Equality cannot occur because `ell` is prime.
For witness `p^2`, its cube must divide `r` and every other prime below
`p^2` must be absent. Larger prime factors are unrestricted. Each required
prime or prime cube divides the period, so CRT gives exact residue
proportions, including the zero class represented by `L_Q`. This validates
the two density formulas and all their boundary cases.

I also recomputed every density at `Q=50` **without using that
classification**. Starting with the raw clauses `pq|r`, the verifier forms
an exact signed divisibility indicator of their union. To add a modulus
`m`, it uses `U'=U+1_(m|r)-U*1_(m|r)`, with intersections represented
by least common multiples. A clause is skipped only when its modulus is
a multiple of an already processed modulus, making its containment exact.
The increment after each quotient is its first-witness event.

Of the 422 raw clauses, 109 remain after these direct containment tests.
The largest signed union has 98,288 nonzero terms. Each denominator
divides `M`, so summing integer counts `c*(M/d)` evaluates a whole period
exactly; the period itself is not scanned. Every resulting density agrees
with the frozen table. The independent weighted sum is

    C_50(0) = 6191714756605250456368/69244275641746488908625.

### Exact separation and quantified conclusions

Independent least-common-multiple and rational calculations reproduce

    L = 75600,
    M = 691374732709966591241323368000,
    alpha = C_50(0)+1/52
          = 30093341768093808664597/276977102566985955634500,
    beta-alpha
          = 131410063319607383019139/13294900923215325870456000 > 0.

Apply (2)-(3) at `(Q,b,n)=(50,0,Mt)` and at `(10,1,Lt+1)`.
Both inputs exceed their cutoff for every integer `t>=1`. This proves
exactly the two inequalities in `claim.json`, with their stated errors.
Both index sequences are strictly increasing and unbounded. Their limiting
upper and lower bounds are incompatible with convergence of the original
sequence, proving the full frozen `j=2` assertion.

For the additional finite claim, set `A=(M+3)/M` and `B=(L+2)/L`.
The inequality `(L+2)/(Lt+1)<=B/t` has the required direction. For
`t>=203` the two bounds therefore separate by at least

    (beta-alpha)-(A+B)/203
      = 559612671694976819161613011/
        17543633842515402252748580463000 > 0.

The independently calculated integer `floor((A+B)/(beta-alpha))+1`
is 203. At 202 the same coarse allowance has negative gap. This verifies
the stated threshold without asserting optimality for actual counts.

## Additional checks actually performed

The fresh exact verifier completed successfully with Python 3.10.12.
Beyond the decisive coefficient recomputations above, it checked:

- Full positive-membership equality against literal remainder sets for every
  `1<=n<=768`, extending beyond the proposer's exhaustive range `1<=n<=256`.
  The complete quotient range follows from `r>=1`, which forces `2q+1<=n`.
- 5,376 cutoff-tail tests at cutoffs `3,4,6,9,10,17,50` in that range.
- Literal sets at `4095,4096,4097,10007,30029,30030,30031,75601,151201`.
  For example, `s_2(75601)=9611`, while `T_10(75601)=8962` and
  `T_50(75601)=9558`.
- 34,848 positive-residue endpoint counts, including residue zero represented
  by the period and the empty interval `H=0`.
- 1,530 progression-counting tests covering every residue class for cutoffs
  `3,4,5,6` at three positive inputs per class.
- Exact truncated counts on both claimed progressions for
  `t=1,202,203,204,1000,10^12`; these independently reproduce all six
  frozen count records and respect the claimed counting errors.
- The unchanged frozen hashes after all computations.

These finite tests are falsification and arithmetic checks. Universally
quantified membership, truncation and counting statements are justified by
the arguments reconstructed above. No literal computation of `S_2(Mt)`
and no enumeration of all `M` residue classes is claimed.

## Source comparison and contribution

The local primary PDF was checked directly with `pdftotext` on pages
3, 4 and 16, as well as by reading the listed text. Its definitions agree
with the frozen original. Baraskar and Vukusic's Theorem 1 concerns the
first iterate; Theorem 3 supplies general bounds, giving `1/24` and `1/4`
at the second iterate. Their Problem 2 asks for nonconvergence for every
fixed `j>=2`. The present proof settles exactly its `j=2` specialization
by an explicit positive separation, a substantive advance beyond those
bounds. No theorem from that paper is a logical premise of this proof.
[Publisher PDF](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.pdf).

The live [publisher record](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.html)
confirms JIS 29 (2026), Article 26.1.4 and January 26, 2026 publication.
The live [arXiv record](https://arxiv.org/abs/2508.20853) lists v1 of
August 28, 2025. The journal version governs page and theorem references.

A separate bounded web screen on 2026-09-12 used:

1. `"Bounds for Sets of Remainders" nonconvergence proof`
2. `"Baraskar" "Vukusic" "Problem 2"`
3. `"iterated remainder sets" nonconvergence`
4. `"second remainder set" limit`
5. `"2508.20853" nonconvergence proof`
6. `"Vukusic" "remainders" "non-convergence"`

The relevant primary results retrieved were the publisher article and its
arXiv record. No equivalent separation or subsequent resolution was found
in these results. Secondary summaries and unrelated uses of “remainder
sets” were not used as authority. This supports the candidate's bounded
novelty statement, not an exhaustive priority guarantee.

## Gaps, scope and disposition

No unresolved mathematical gap was found in the exact frozen candidate.
Correctness, original-problem scope, and contribution all pass. The proof's
finite error estimates are coarse but valid. No substantive revision is
required, and no theorem has been weakened or repaired in this review.

The remaining step is the runner's structural `check-math` against this
unchanged snapshot before manuscript work. This report makes no claim
about manuscript, citation-layout, build, visual, or release checks, which
belong to subsequent phases.
