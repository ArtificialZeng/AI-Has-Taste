# Research pass 1: exact continuation and an infinite edge certificate

Job: `primary-20260913-subsum-denominator-research-c627858a54d2`.
Date: 2026-09-13 Asia/Shanghai / 2026-09-12 UTC.
Decision: **continue**, candidate kind **none**, original status **unresolved**.
No claim.json, manuscript, or research PDF is proposed. The restricted result
below has a complete computer-assisted argument and a separate implementation
check; it has not received a fresh mathematical referee or novelty clearance.
The arbitrary fixed edge cutoff is not by itself claimed to justify publication.

## Sources and immutable scope

The source SHA256 is unchanged:
`3d8e6928f3bd250dbdfde723603903f527d4ec0da8f85f5ac628b232991e240a`.
The original target and all its quantifiers remain as recorded in `problem.md`.
All literature filenames were enumerated; no `literature/*handoff*.md` existed.
`literature/outer-intake.md` was read and its dyadic recurrence checked against
the primary text, rather than accepted as a conclusion.

Read cached BBFM text at Proposition 3.8, Proposition 3.9, Proposition 3.10,
and Conjecture 4, and revisited the live
[journal article](https://link.springer.com/article/10.1007/s11139-026-01419-0).
The live [Chen--Ono--Zhang v2 text](https://arxiv.org/html/2605.21718v2),
Conjecture 4 and Table 1, continues to list this ordinary-denominator shape
problem as open. The correction to the binary-numerator conjecture is separate.
Bounded searches included `"log-concavity" "subsum" denominator`,
`"log-concave" "1+x^i" product`, and distinct/colored-partition and shifted
binomial-mixture queries. No resolution or equivalent quantitative recurrence
bound was identified in the inspected primary sources. This is not exhaustive
priority or novelty clearance. No additional theorem is imported from snippets.

## Assigned test: finite observation

`research_h_probe.py` uses Python integers, caches exact adjacent minors between
stages, and preserves all triage files. Its output covers every support index,
without symmetry sampling, for every ascending dyadic stage in 257<=n<=512:

- 512 stages; 52,893,866 tests of H, all nonnegative.
- The stronger `9 T_new >= 5 (T_old + shifted T_old)` also passes all these tests.
- All 26,228,480 internal minors of the final D_n in this new range are
  nonnegative. No new exception to the original claim was found.
- Exact degree, palindromicity, and evaluation at 1 are checked for every n.
  The D_256 coefficient digest agrees with the immutable triage output.

Together with triage this gives H through n=512 at 60,553,416 stage/index pairs
and full original-coefficient checks at 30,000,042 internal indices. These are
finite observations. The smallest previously attained ratio 5/9 remains the
minimum in the combined range: triage establishes its minimum through 256 and
the new probe explicitly checks the 5/9 lower bound thereafter.

The independent FLINT direct product in `research_verify.py` recomputes every
coefficient at n=256 and n=512; both complete coefficient digests agree with the
Python recurrence. It also directly rechecks their original minors. This is
separate implementation verification, not an independent model referee.

## A precise obstruction to a generic induction shortcut

**Exact-counterexample / proved-obstruction.** Symmetry, strict log-concavity,
and the first-overlap bound `T_(s-1)(a)>=2 a_(s-2) a_0` do not imply H, even if
the polynomial after multiplication remains log-concave.

Take `a(x)=(1+x)^16`, s=4, and b(x)=a(x)(1+x^4). The complete coefficient
arrays and all checks are in `research_verify.json`. At j=10,

\[
T_{10}(a)=T_6(a)=14,158,144,\qquad T_{10}(b)=6,619,392,
\]
\[
2T_{10}(b)-T_{10}(a)-T_6(a)=-15,077,504.
\]

The boundary margin `T_3(a)-2a_2a_0` is 94,960, and every minor of b is
nonnegative. This example is not an A_(n,k) and refutes neither H on that family
nor the original denominator conjecture.

There is also an unbounded obstruction to deducing any fixed positive minor
ratio from just these old-sequence assumptions. For even s>=4 set N=s^2 and
`a_j=binom(N,j)`. At j=(N+s)/2, with b=a+shift_s(a), direct binomial identities
give

\[
\frac{T_j(b)}{T_j(a)+T_{j-s}(a)}
=\frac{4(s^2+2)}{s^4+3s^2+4}\longrightarrow0.
\]

For completeness, put t=N/2, q=s/2 and d=(t+1)^2-q^2. The two old minors
equal `a_j^2 (2t+1)/d`; the new minor divided by their sum equals
`2(t+1)(t+1-2q^2)/d`, yielding the displayed formula. The old sequence is
strictly log-concave, symmetric, and has degree s^2. Its boundary ratio is

\[
\frac{T_{s-1}(a)}{a_{s-2}a_0}
=\binom{N}{s-1}\frac{N+1}{s(s-1)}>2,
\]

since `binom(N,s-1)>=N`. No assertion about all new minors for this entire
family is needed; only the explicit N=16 example has that extra checked property.

## Computer-assisted restricted theorem

**Statement.** For every n>=9 and every stage in `problem.md`, H holds at all
indices `0<=j<=32`, and at their reflections in the degree of the new stage.
Consequently, for every positive n outside {3,5,6,7}, the original minors are
nonnegative whenever `1<=j<L_n` and `min(j,L_n-j)<=32`.

This is an infinite-n restricted theorem, not an inference from a long prefix.
Here is the reduction that makes its finite certificates decisive.

Fix an integer B=32. A stage adding `1+x^s` occurs exactly at
`n=s*2^t`, t>=0. Before that stage the earlier new factors are
`1+x^o,1+x^(2o),...,1+x^(s/2)`, where o is the odd part of s (the list is empty
if s is odd). Write the resulting old polynomial as a_(s,t).
Let

\[
F_{s,j}(t)=2T_j(a_{s,t}(1+x^s))-T_j(a_{s,t})-T_{j-s}(a_{s,t}).
\]

Only factors of degrees at most B+1 affect these quantities for j<=B. Choose
the least t0>=0 such that `s*2^t0>=max(9,B+1)`. For every i<=B+1 the exponent
of `1+x^i` in a_(s,t0+u) is `E_i+u`, u>=0, with E_i a fixed nonnegative
integer. Indeed its exponent in D_(n-1) counts the q>=0 with `2^q i<n`, and
doubling n adds exactly one when i<=n; the earlier-stage factors stay fixed.

The coefficient of x^r in `(1+x^i)^(E_i+u)` is either zero or
`binom(E_i+u,r/i)`. Thus a coefficient of degree r in the whole old polynomial
is a polynomial in u of degree at most r. The same is true after adding s.
It follows that `F_(s,j)(t0+u)` has degree at most 2j. This is a proved degree
bound from the product formula, not a degree guessed from data.

Every polynomial P(u) of degree at most 2j has the exact Newton expansion

\[
P(u)=\sum_{h=0}^{2j}\Delta^hP(0)\binom{u}{h}.
\]

For integer u>=0 the binomial factors are nonnegative. Therefore nonnegative
integer coefficients `Delta^h P(0)` prove P(u)>=0 for every integer u>=0.

The complete certificate `research_edge_probe.json` contains all 561 cases
`1<=s<=33`, `s-1<=j<=32`, and all their 24,497 Newton coefficients. Every
coefficient is nonnegative. It additionally checks the 968 earlier (s,t,j)
cases with n>=9 and t<t0. The script checks 1,122 evaluations outside the
interpolation grids as consistency tests; the mathematical degree bound is
what makes the certificate conclusive.

The verifier constructs coefficients by binomial convolution instead of repeated
shift/add and recomputes every Newton coefficient by

\[
\Delta^hP(0)=\sum_{v=0}^{h}(-1)^{h-v}\binom hv P(v).
\]

It independently reproduces all 24,497 coefficients and 968 earlier checks.
Domain completeness is checked again in the final integrity pass.

To cover stages with s>=j+2, observe that their coefficient triple at j is
unchanged and `T_(j-s)=0`. In this case H reduces to the old nonnegative
minor. Induct through all stages starting with the exactly verified D_8.
For s<=j+1 the certificate supplies H; its right side involves only old
indices <=j, so the same induction proves nonnegativity of every new minor
with j<=32. The initial D_8 checks, and n=1,2,4, are independently recomputed
in the final integrity pass. This closes the induction without assuming the
original full conjecture.

Every stage is palindromic. If the old degree is L, the H margin satisfies
`F_j=F_(L+s-j)` by zero extension and `T_j(a)=T_(L-j)(a)`. This proves the
reflected range. The remaining original minors have `32<j<L_n-32`; nothing
here settles that unbounded region for n>512.

## Minimal next kernel and one next test

The following **working-hypothesis K** is explicitly stronger than the
restricted calculation and is not claimed proved. For every j>=0 and
1<=s<=j+1, let t0(s,j) be the least nonnegative t with
`s*2^t>=max(9,j+1)`. Require

\[
\Delta^h[F_{s,j}(t_0+u)]_{u=0}\ge0\qquad(0\le h\le2j).
\tag{K}
\]

`research_kernel_probe.py` and `.json` check the design range j<=32 at these
smaller, j-dependent starting points: 561 polynomials and 24,497 coefficients,
all nonnegative. This was chosen after discovering the certificate method and
is not held-out support for K. A negative Newton coefficient would refute K
but need not make F negative or refute H. Even uniform K would directly cover
only the stages with n>=max(9,j+1); the n<j+1 region is a separate gap, so K
is not asserted equivalent to H or the original conjecture.

A structural formulation useful for attacking K is the following coefficient
identity. Put `A(x)=a_(s,t0)(x)`, `P_m(x)=prod_(i=1)^m(1+x^i)`, m=j+1, and
`R(x,y)=P_m(x)P_m(y)-1`. Then

\[
\Delta^hF_{s,j}(t_0)=
[x^jy^j](1-x/y)A(x)A(y)
\bigl(1+2x^s+2y^s+(xy)^s\bigr)R(x,y)^h.
\]

This follows from the affine exponent identity modulo x^(j+2) and y^(j+2).
The multiplier `(1-x/y)` creates signed coefficients; ordinary coefficient
positivity of R is not a proof of K.

**One next test:** freeze K as above and execute
`python3 evidence/research_kernel_probe.py --B 64`, isolating the previously
untested 33<=j<=64, every 1<=s<=j+1 and 0<=h<=2j. Save the first negative
integer Newton coefficient, if any, and then evaluate its F polynomial to
distinguish failure of K from failure of H. If it survives, the bivariate
coefficient identity is the named uniform proof target, rather than another
full-n prefix extension.

## Reproduction

From the project root, in a single foreground process per command:

```
python3 evidence/research_h_probe.py --max-n 512
python3 evidence/research_edge_probe.py --B 32
python3 evidence/research_verify.py
python3 evidence/research_kernel_probe.py --B 32
python3 evidence/research_integrity.py
```

The first, second and fourth scripts use the Python standard library. The
verifier additionally uses python-flint 0.9.0 for two full direct products;
the integrity script imports its independent coefficient implementation.
No random sampling, floats, external workers, or formal-proof system were used.
