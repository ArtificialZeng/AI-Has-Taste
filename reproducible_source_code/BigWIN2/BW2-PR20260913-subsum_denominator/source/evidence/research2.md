# Research pass 2: held-out K, a uniform band, and the affine boundary

Job: `primary-20260913-subsum-denominator-research-983c87564404`.
Date: 2026-09-13 Asia/Shanghai / 2026-09-12 UTC.
Decision: **continue**; candidate kind **none**; original status **unresolved**.
No claim, manuscript, fresh referee, novelty certification, or research PDF.

## Scope and sources

The original statement in `source.md` is unchanged, SHA256
`3d8e6928f3bd250dbdfde723603903f527d4ec0da8f85f5ac628b232991e240a`.
The all-n, all-internal-index claim in `problem.md` remains the target.
Pass-1 scripts, certificates and dossier have been preserved without edits.
No literal `literature/*handoff*.md` files were present. `outer-intake.md`
was read and its substantive assertions were checked against primary text.

The live [BBFM journal article](https://link.springer.com/article/10.1007/s11139-026-01419-0),
Propositions 3.8--3.10, agrees with the saved product, symmetry/unimodality,
and full dyadic recurrence. Its Conjecture 4 has the stated four exceptions.
The live [Chen--Ono--Zhang v2](https://arxiv.org/html/2605.21718v2),
Conjecture 4 and Table 1, retains this ordinary-denominator shape claim as
open. The binary-numerator correction is a different claim. Relevant cached
primary passages were reread. Searches included `"subsum" "log-concavity"
denominator`, `"restricted partitions" "log-concavity" colored`, and
`"plane partitions" "polynomial" "log-concavity" coefficients Newton`.
No original-claim resolution was identified in the inspected primary results;
this is bounded source checking, not exhaustive priority or novelty clearance.
No theorem is imported from a search snippet. The generic auxiliary band
below is not proposed as a new publishable result.

## Assigned frozen test and independent verification

The frozen definition of F and K is in `research.md`. In particular,
\(F_{s,j}(t)=2T_j(a_{s,t}(1+x^s))-T_j(a_{s,t})-T_{j-s}(a_{s,t})\),
where \(a_{s,t}\) is the old stage adding s at n=s*2^t, with every earlier
ascending dyadic factor included. K starts at the least t with
n>=max(9,j+1) and asks for all 2j+1 Newton coefficients to be nonnegative.

`research2_kernel_probe.py --B 64` executes the pass-1 algorithm with
separate output and current provenance; only the metadata and output path
were changed. `research2_kernel_probe.json` records:

- All 2,145 polynomials and 185,185 integer Newton coefficients for j<=64.
- No negative coefficient. Exactly 1,584 polynomials and 160,688
  coefficients belong to the held-out range 33<=j<=64.
- The entire design range j<=32 agrees exactly with the original certificate.

`research2_verify.py` independently constructs the old coefficients using
\(r a_r=\sum_{k=1}^r b_k a_{r-k}\), where
\(b_k=\sum_{i\mid k}i E_i(-1)^{k/i-1}\).
It obtains each exponent by counting powers of two, and every division is
checked exact. It recomputes every Newton coefficient by the signed binomial
sum, without importing the producer's coefficient or difference functions.
All 185,185 agree. It also checks all 3,068 triples (s,t,j) with j<=64,
s<=j+1, n=s*2^t>=9 and t below K's local start, with nonnegative H margin.
Complete domains are checked again by `research2_integrity.py`.

The pass-1 polynomial-degree proof and induction now apply verbatim with
B=64: every affected stage at j<=64 has either a nonnegative Newton
certificate or an earlier finite check. An unaffected shift s>=j+2 reduces
H to the old minor. Starting with D_8, induction propagates nonnegativity;
reflection uses palindromicity. Thus the following is a **restricted
computer-assisted theorem**, not a finite-n inference:

> For every n>=9, H holds at every stage through j=64 and at its reflected
> indices. For every positive n outside {3,5,6,7}, the original minor is
> nonnegative when min(j,L_n-j)<=64.

The bases n=1,2,4,8 are rechecked by a sparse-product implementation. This
extends the previous fixed edge result; it does not settle the remaining
unbounded indices or establish publication value.

## Uniform positivity from the bivariate identity

The complete proof is in `research2_band.md`. Set h=2j-k. For every j,k>=0
with h>=0, every s in the K domain, and every old polynomial A with
nonnegative coefficients and A(0)=1,

\[
 j\ge2k^2+k-1\quad\Longrightarrow\quad
 [x^jy^j](1-x/y)A(x)A(y)
 (1+2x^s+2y^s+(xy)^s)(P_{j+1}(x)P_{j+1}(y)-1)^h\ge0.
\]

This proves an unbounded band of the highest Newton orders in K. It follows
from a binomial smoothing lemma for symmetric homogeneous polynomials,
not from computed data. The two highest rows have explicit Catalan formulas.
The proof leaves the low and middle Newton orders uncontrolled.

`research2_bivariate_verify.py` directly multiplies bivariate arrays and
checks the identity at all 1,547 coefficients in 91 polynomials for j<=12.
It also checks 24,923 finite instances of the smoothing identity. These
are consistency tests of the written algebra, not its proof. With A=1,
s=3, j=2, the generic bivariate expressions at h=1,2 are -3 and -1;
ordinary coefficient positivity alone is insufficient. That A is not an
actual recurrence stage, so this does not refute K or H.

## Sharper affine threshold: K_sharp_v1

The pass-1 sufficient condition n>=j+1 was not minimal. Write
\(e_i(n)=\#\{q\ge0:2^q i<n\}\). For every i<2n,
\(e_i(2n)=e_i(n)+1\). Indeed, q>=1 contributes e_i(n), and q=0
contributes one exactly when i<2n. At all subsequent doublings the same
condition holds. Earlier-stage factors are independent of t.

Consequently, the old exponents through degree j+1 are affine in u>=0
already when **2n>j+1**. The degree bound deg F<=2j and the bivariate
Newton identity are valid from this earlier point.

Freeze the following **working hypothesis K_sharp_v1**, distinct from the
original frozen K:

> For every j>=0 and 1<=s<=j+1, let tau(s,j) be the least nonnegative t
> with s*2^t>=9 and 2*s*2^t>j+1. Then
> Delta^h F_(s,j)(tau)>=0 for every integer 0<=h<=2j.

This is structurally motivated by exact polynomiality. Its design range
j<=64 is **not held-out confirmation**. Uniform K_sharp would imply K,
because shifting a nonnegative Newton expansion forward preserves its
nonnegative differences. It would imply H directly in 2n>j+1, but would
still leave the indices j>=2n-1. No equivalence with H or the original is
claimed.

`research2_sharp_probe.py` translates the original Newton polynomials back
one step whenever tau is earlier: if c is the old coefficient vector, the
new vector satisfies c'_h=c_h-c'_(h+1), starting at its top. It separately
recomputes every translated coefficient using the independent exact
recurrence and signed binomial sums. `research2_sharp_probe.json` contains
all 2,145 templates and 185,185 coefficients, all nonnegative. In 1,956
templates, the start moves one doubling earlier; all their 175,492
coefficients are independently recomputed. Unchanged templates inherit the
fully verified original certificate.

## Proved obstruction at the excluded boundary

The strict inequality in 2n>j+1 cannot be relaxed as a uniform claim of
polynomiality. At n=9, s=9, j=17, one has 2n=j+1. The old polynomial is
A=D_8. The tail F(t) is polynomial of degree at most 34 for t>=1. Its
extrapolation to t=0 differs from the actual value because the factor of
degree 18 would have exponent -1 in the extrapolation and 0 in A.
Modulo x^19, the extrapolated old polynomial is A/(1+x^18).

Hence, writing P for the polynomial tail extended to t=0,

\[
 F_{9,17}(0)-P(0)=-a_{16}-2a_7=-899-2(114)=-1127.
\]

The exact values are F(0)=19668 and P(0)=20795. Since F(t)=P(t) for all
t>=1, for every h>34,
\(\Delta^hF(0)=(-1)^h(-1127)\). In particular the 36th difference is
**-1127**. The script recomputes this signed binomial sum from all 37
actual margins. The sparse-product integrity check verifies A and F(0).

This is a **proved-obstruction** to extending the polynomial/Newton method
unchanged through that boundary. The actual H margin is positive. The
witness is outside the starting-point hypotheses of K and K_sharp and
refutes neither of them nor the original denominator conjecture.

## Remaining gap and one next test

No proof of the low/middle orders of K or K_sharp is known here. Even a
proof of K_sharp leaves the separate region j>=2n-1 before reflection.
The fixed edge certificate, generic high-order band, and method obstruction
are retained as useful partial evidence without a claim of novelty or
publication qualification.

**One next test:** attack the now-frozen K_sharp_v1 on the held-out range
65<=j<=96, every 1<=s<=j+1 and 0<=h<=2j, at the exact start tau above.
Use an independent implementation or the verified logarithmic-derivative
recurrence. Save the first negative integer coefficient, if any; evaluate
its entire F polynomial on u>=0 as needed to distinguish a failure of
Newton positivity from a negative H margin. This is a test of the revised
kernel, not another full-n calibration and not evidence already used to
design K_sharp_v1.

## Reproduction

From the project root, run each as a foreground command:

```
python3 evidence/research2_kernel_probe.py --B 64
python3 evidence/research2_verify.py
python3 evidence/research2_sharp_probe.py
python3 evidence/research2_bivariate_verify.py
python3 evidence/research2_integrity.py
```

All new computations use Python arbitrary-precision integers and the standard
library. No random sampling, floating-point tests, spawned agents, additional
Codex processes, formal checker, or fresh referee were used.
