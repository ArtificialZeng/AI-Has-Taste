# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen by snapshot
`838d242087a7daf3b6ee84639c29ff2422611ed9512631038d16a9e845e22e0e`.
The claim is the full original TP4 statement, together with the stronger strict
positivity assertion for admissible minors. My verdict is **accept**: the
argument establishes the claimed scope, its exact computations reproduce, and
the contribution closes the precise gap explicitly left open in the cited
source.

## Source results and hypotheses checked

I inspected the frozen primary-source PDF itself. Its indexing of the Eulerian
triangle agrees with `source.md` and `problem.md`. The following relied-on
statements occur with the needed hypotheses:

- Theorem 1.1 proves TP3 and strict positivity of every admissible minor of
  order at most three.
- Theorem 2.5 reduces strict positivity of all admissible minors through order
  `r` in a finite lower-triangular matrix to strict positivity of admissible
  minors having consecutive rows and consecutive columns; the paper explicitly
  notes the passage to an infinite matrix by finite leading truncations.
- Lemma 3.1 gives the strictly negative zeros of the Eulerian polynomial, so
  `A_n(x)=prod_i(1+r_i x)` with `r_i>0` for `n>=1`.
- Lemma 2.6 is the stated identity for the polynomials `G_j`, and Lemma 3.3 is
  the coefficient-Toeplitz multiplication and Cauchy--Binet identity used in
  the candidate.

For `n=0`, the candidate's empty product convention handles the case directly,
so no root statement is invoked outside its hypothesis. The PDF's Remark 1.2
reports a 126-minor symbolic calculation but expressly withholds a TP4 proof;
it publishes neither the template list nor universal sign certificates.

## Reconstruction of the decisive argument

Starting with `A_n(x)` and the source identity

`(1-x)G'_j=(j+1)G_(j+1)-(n-j)G_j`,

application of the Eulerian differential recurrence at step `n+t` sends a
formal term `x^a G_j` to

`(a+1)x^aG_j+(t+1-a+j)x^(a+1)G_j+(j+1)x^(a+1)G_(j+1)`.

Three iterations and unit lower-triangular row operations give

`D(n,k)=D_K(G0,xQ1,xG0+x^2Q2,x^2H2+x^3Q3)`,

with exactly the four polynomials `Q1,Q2,H2,Q3` stated in
`evidence/tp4_resolution.md`. Expanding the last two rows produces four terms
whose selected-subset caps imply that their union `U` has size at most six.
For each summand, factoring the common `f_U` from all four rows and applying
coefficient Cauchy--Binet yields

`D(n,k)=sum_U sum_L Psi_U(L) det T_(f_U)(L,K)`.

The local row degrees prove that only four-subsets `L` of `{0,...,6}` can
occur. Relabelling `U` proves that `Psi_U(L)` is the symmetric polynomial
indexed by `(m,L)`, where `m=|U|`; no dependence on `n`, `k`, or labels has
been discarded.

The support enumeration gives survivor counts
`1,3,9,19,25,34,35` for `m=0,...,6`, hence 126 templates. Of the remaining
119 slots, 118 have no support-perfect-matching and the sole structurally
possible slot `(5,{3,4,5,6})` is checked as an exact zero polynomial.

For universal signs, the sparse-polynomial audit correctly enforces
`union U` by inclusion--exclusion, expands each local row over the integers,
and forms every four-row determinant before collapsing labelled monomials into
permutation orbits. The base-five monomial encoding is valid because each row
is multiaffine and a four-row determinant has every variable exponent at most
four. This produces 120 coefficientwise-nonnegative templates. The remaining
six have exactly 18 negative symmetric-monomial orbits.

For a partition `lambda`, writing `M_lambda=m_lambda/N_lambda` for the average
of the distinct orbit monomials is the standard normalization in Muirhead's
inequality. Each coefficient `c_lambda` therefore contributes
`c_lambda N_lambda M_lambda`. Every one of the 18 transfers pairs equal total
degrees with a majorizing positive partition, covers its negative normalized
demand exactly, and never exceeds the positive normalized supply. Thus all 126
polynomials `Psi_m(L)` are nonnegative for nonnegative roots. Since every
`f_U` is a product of factors `1+r_i x`, all accompanying upper-Toeplitz minors
are nonnegative, so every consecutive admissible order-four minor is
nonnegative.

Strictness comes from the single `m=0`, `L={0,1,2,3}` summand, whose local
coefficient is one. Its Toeplitz minor is

`det[e_(k+j-i)(r_1,...,r_n)]_(1<=i,j<=4)=s_(4^k)(r_1,...,r_n)`.

For `0<=k<=n` this Schur polynomial is positive at positive roots; at
`n=k=0` it is the empty Schur polynomial, equal to one. The source's TP3
result supplies orders at most three, and Theorem 2.5 applied inside any finite
leading truncation supplies every admissible minor through order four.
Lower-triangularity makes every nonadmissible selected minor zero. This proves
both the frozen TP4 statement and the stronger strictness statement.

## Exact checks actually performed

- Recomputed SHA-256 for `claim.json` and every frozen evidence file; every
  value agrees with `audit/snapshot.json`.
- Rebuilt the 126-template manifest in memory. Its canonical JSON reproduced
  digest `927f4bc2b877ef7cec7e4ce4c62582523368e5e6a102642ab7eec860ac7ae3e3`.
- Rebuilt all 126 sparse coefficient polynomials in memory. Their canonical
  JSON reproduced digest
  `64247e35ad7e0077776645ee921d67430f962ebb885233c24bb9104a070e5650`.
- Rebuilt the Muirhead certificate in memory. Its canonical JSON reproduced
  digest `b58ca837a9139091622c6f778b7a0ec25a1e1cf9e353bee9d97ab305a1010d6f`.
- Independently formed the first four rows from the differential recurrence
  for eight arbitrary positive integer root vectors of lengths `0,...,7` and
  compared their direct consecutive determinants with the grouped
  subset/Toeplitz expansion for every `0<=k<=n`. All 36 exact integer
  comparisons agreed, including `n=0`, `k=0`, and `k=n` boundaries.
- Checked the determinant signs, inclusion--exclusion convention, orbit-size
  normalization, all majorization directions, strict Schur term, small-`n`
  empty subset behavior, and applicability of the finite-truncation criterion.

## Contribution assessment and limits

The accepted claim resolves the immutable original problem rather than a
subsidiary restriction. The nearest frozen primary source proves only TP3 and
explicitly declines to regard its hidden 126-case computation as a proof.
Here the missing coverage map, complete exact coefficient data, and universal
inequality certificates are present and reproducible, so this is a substantive
resolution-paper contribution within the frozen comparison. Literal
item-by-item identity with the source authors' unpublished template list cannot
be checked, but it is not needed: the candidate independently proves exhaustive
coverage of all consecutive order-four minors. This audit makes no broader
priority or journal-acceptance claim, and the bounded literature record is not
a comprehensive search. I found no unresolved mathematical gap in the frozen
claim.
