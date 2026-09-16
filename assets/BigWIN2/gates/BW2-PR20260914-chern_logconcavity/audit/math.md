# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` candidate.
The frozen `original_status` remains **unresolved**.

Referee job: `primary-20260914-chern-logconcavity-referee-bc38d9ae2dd8`.
Snapshot: `c7a3ce92d5a241cbc4872e171dadffe3e04b62c10715996352a37acb1320381b`.
Review date: 2026-09-14.

The accepted assertion is the following. With the original definitions of
the Schur coefficients, for every integer \(k\geq4\), set

\[
\begin{aligned}
R_k(x)={}&(x-k+2)A_{k-1,1}(x)
+\frac{(x-k+3)(x-k+2)}2 A_{k-2,0}(x)\\
&+(x+1)(x-k+3)A_{k-2,1}(x)
+\frac{(x+1)(x-k+4)(x-k+3)}2 A_{k-3,0}(x).
\end{aligned}
\]

Its Newton coefficients \(\rho_{k,r}\) have strict positive support
\([k-2,2k-1]\), vanish elsewhere, and obey
\(\rho_{k,r}^2\geq\rho_{k,r-1}\rho_{k,r+1}\) for every integer
\(r\geq0\), with the stated zero extension. This acceptance includes
all \(k\geq4\), not just the computed range. It does not resolve the
original Conjecture 3.3 or its \(j=2\) restriction.

## Reconstructed proof

Let \(D(N,K)\) count fixed-point-free permutations with \(N-K\) cycles.
Deleting the distinguished letter or its transposition gives

\[
D(N,K)=(N-1)\{D(N-1,K-1)+D(N-2,K-1)\}.
\]

For \(K\geq1\), its strict support is \(K+1\leq N\leq2K\).
Necessity follows from the number and minimum lengths of the cycles.
For sufficiency, with \(c=N-K\), use \(c-1\) transpositions and a final
cycle of length \(2K-N+2\geq2\).

Writing \(S_h=A_{h,0}\), the rising factorial and decomposition by
nonfixed support give

\[
[\tbinom{x}{r}]S_h=D(r,h)+D(r+1,h),\qquad
A_{n,1}=x(x+2-n)S_{n-1}-(n+1)S_n.
\]

These are polynomial identities: they follow at all sufficiently large
nonnegative integers from the defining Chern product and then extend
identically. Substitution into the defining four terms of \(R_k\), using
the Newton multiplication rule

\[
[\tbinom{x}{r}]((x-c)F)=(r-c)f_r+r f_{r-1},
\]

and reduction to \(K=k-3\), gives

\[
2\rho_{k,r}=\sum_{i=-5}^{1}p_i(k,r)D(r+i,k-3).
\]

I independently reconstructed all seven polynomials \(p_i\). They are
exactly the serialized polynomials in the frozen certificate and have
total degree at most four.

The strict-support argument in `evidence/auxiliary-proof.md` also checks
out. The four-term expression for \(B_{n,1,r}\) has nonnegative active
multipliers. For its third multiplier, substitution \(r=n+1+t\) gives

\[
2n+2+(3n+4)t+3t^2>0\quad(t\geq0).
\]

The other three multipliers are positive on the required active indices.
They give strict support \([n-1,2n]\) for every \(n\geq2\), including
\(n=2\). The zeroth mode has support \([h,2h]\) for \(h\geq1\).
Multiplication by each displayed linear factor then gives, respectively,

\[
[k-1,2k-1],\quad[k-1,2k-2],\quad[k-2,2k-2],\quad[k-2,2k-3].
\]

All coefficients of these terms are nonnegative, and their union is the
claimed support of \(R_k\). No cancellation is invoked for this step.

For the quadratic inequality, put \(D_i=D(r+i,k-3)\). Expansion produces

\[
4(\rho_{k,r}^2-\rho_{k,r-1}\rho_{k,r+1})
=\sum_{a\leq b}q_{a,b}(k,r)D_aD_b.
\]

The complete pair set has 41 elements, including both the central
product and the shifted adjacent product. For each fixed \(a+b\), order
the pairs from the center outward. The products \(U_i=D_{a_i}D_{b_i}\)
are nonincreasing: the recurrence gives

\[
P_K(t)=t^2\big((1+t)P_{K-1}(t)\big)',\qquad P_0=1.
\]

Rolle's theorem inductively gives real nonpositive roots. Newton's
inequalities, together with interval support, give the required strong
coefficient inequalities, including zero-boundary cases.

Abel summation with \(U_{t+1}=0\) expresses the minor as the sum of
\(W_i(U_i-U_{i+1})\), where \(4W_i\) is the corresponding prefix sum
of \(q\). If a difference is positive, then \(U_i>0\). Thus

\[
X=r+a_i-(k-2)\geq0,\qquad
Y=2k-6-(r+b_i)\geq0.
\]

Solving yields exactly

\[
k=X+Y+b_i-a_i+4,\qquad r=2X+Y+b_i-2a_i+2.
\]

The fresh verifier expanded every prefix under this substitution and
compared the full polynomial coefficients with the frozen arrays.
All 41 identities hold. Their 1,506 serialized nonzero coefficients
are strictly positive, and no prefix polynomial is zero. Consequently
every active Abel summand is nonnegative. Inactive terms vanish. This
establishes the infinite-range claim without extrapolation.

At \(k=4\), \(K=1\) and \(P_1=t^2\), so the same reasoning applies.
Negative indices in the formal expansions have zero \(D\)-values.
At \(r=0\), and outside the strict support, the required minors are
zero; at the support endpoints they are positive squares. There are no
unjustified divisions by zero, limits, or additional large-parameter
assumptions.

## Checks actually performed

Reproduction command: `python3 audit/referee_verify.py`.
The saved result is `audit/referee-verification.json`.

The new verifier uses only the Python standard library and imports none
of the submitted programs. It implements sparse bivariate polynomial
arithmetic, applies Newton multiplication before reducing permutation
defects, and compares polynomial dictionaries exactly. It verifies all
seven \(p_i\), all 41 complete prefix identities, their degree bounds,
pair completeness, and all coefficient signs. This also confirms the
finite algebra underlying the submitted interpolation proof; that
proof's separate degree bound of eight is sufficient for its 9-by-9 grid.

As an independent connection to the original definition, I recomputed
the Chern product for \(0\leq d\leq90\), extracting the first three
\(u\)-coefficients. For \(4\leq k\leq44\), the verifier checked 3,690
residual Newton entries and their minors, and 3,690 evaluations of the
recurrence. This includes held-out values \(33\leq k\leq44\).
The first row is

\[
(\rho_{4,r})_{r=0}^{8}=(0,0,27,212,660,1000,735,210,0).
\]

The documented failed-method witness was independently recovered:
at \(k=8,r=10\), the full \(B_{k,2}\) minor is
\(23405794555448176>0\), while the specified defect-\(k-3\), trace-\(-7\)
contribution is \(-1196776183680\). It refutes that intermediate
nonnegativity assertion only. The earlier aggregate probe counts are
not needed for acceptance of the residual theorem.

I also attacked the stated remaining mixed inequality at all 2,000
points \(5\leq k\leq44, 0\leq r\leq2k\); no negative value occurred.
This is a finite observation, not an all-\(k\) proof or an additional
accepted conjecture. The algebra showing its sufficiency for induction
is correct: the minor of \(g+\rho\) is the sum of the two separate
minors and the displayed mixed term. The submitted proof that
\(g_r=(r+1)a_r+ra_{r-1}\) preserves nonnegative interval-supported
log-concavity is valid, including \(r=0,1\).

The canonical snapshot digest and all 26 listed file hashes were checked
before and after the computations. All remained unchanged; in particular,
`source.md` retains SHA-256
`3881581fc17206c48f171c064afbfde3d9f85b5b150104077b657eadb7ddd25f`.

## Source comparison and contribution

The nearest result is Bérczi–Fehér, Theorem 5.4: \(j=1\) log-concavity
using 17 Abel prefixes. Their equation (5.2) supplies precisely this
forcing polynomial; Theorem 5.2 proves positivity, not its
log-concavity. Sections 3–5 supply the permutation identities and method.
Figure 1's \(j=2\) label conflicts with the formal \(j=1\) theorem and
proof; I confirmed the discrepancy in the frozen HTML. The live
[primary paper](https://arxiv.org/html/2605.25271v1) and
[version history](https://arxiv.org/abs/2605.25271) were checked; only
v1 was listed. The
[Patel contribution](https://mathdb.com/p/374934/rank-two-binomial-positivity-conjecture-for-schur-coefficien)
claims all-index positivity and support, with no residual log-concavity
theorem. The accepted proof does not depend on that claim.

Fresh queries combined the arXiv identifier, author names, rank-two
binomial log-concavity, lower modes, residuals, forcing, and Schur
coefficients. No equivalent theorem for this explicit \(R_k\) was found
in the inspected sources on 2026-09-14. This is bounded negative-search
evidence, not a priority guarantee. I compared the supplied focused and
broader match titles and available object/quantifier fields: the displayed
neighbors concern other families. The underlying complete registry and
spreadsheet corpora were not independently searched.

I judge the increment sufficient for a modest result note. It concerns
the entire natural forcing family in the first unresolved Schur-mode
recurrence. Positivity of the summands and log-concavity of lower modes
do not by themselves give log-concavity of their sum. For example,
the positive log-concave rows \((1,1,1,1)\) and \((1,2,4,8)\) have a sum
\((2,3,5,9)\) that is not log-concave. The certificate establishes a
specific additional property needed to isolate the mixed induction
term. This is a nontrivial infinite-family application of the prior
method, with a precise potential use; it is not a new general method.
The source comparison supports the contribution at exactly that scope.

## Remaining gaps and disposition

There is no remaining gap in the frozen residual theorem after these
checks. The all-\(k\) mixed inequality and the original higher-mode
log-concavity problem remain unresolved here. Any manuscript should
retain that distinction, attribute the recurrence and Abel method to
the primary source, and include or accompany the complete certificate.

**Accept the frozen `result-note` scope.** No change to the claim or its
decisive evidence is requested. The next workflow step is writing within
this accepted scope after the runner's provenance/integrity gate. This
report is a separate mathematical review pass, not journal peer review
or a proof-assistant formalization.
