# Precise problem and proposed k=4 result

## Frozen original

The verbatim input remains in `source.md`, unchanged. Source: Johan Wästlund, *Moment generating functions in combinatorial optimization: Bipartite matching*, [arXiv:2602.07563v1](https://arxiv.org/pdf/2602.07563v1), Conjecture 11, printed page 25.

For every pair of positive integers m,n and every integer k satisfying 1 <= k <= min(m,n), assign independent Exp(1) costs X_ij to the mn edges of K_{m,n}. Exp(1) has rate 1 and mean 1. A k-matching is a set of k edges with no shared endpoints. Define

\[
C_{k,m,n}=\min_{M:\,|M|=k}\sum_{(i,j)\in M}X_{ij},
\qquad F_{k,m,n}(t)=\mathbb E\exp(tC_{k,m,n}).
\]

The claim is

\[
\forall m,n\in\mathbb Z_{>0}\ \forall k\in\{1,\ldots,\min(m,n)\}\
\forall t\in\mathbb C:\quad |t|<mn/k\implies F_{k,m,n}(t)\ne0.
\]

Use the ordinary d=0 generating function. The source's d>0 ghost functions are recursion auxiliaries, not normalized MGFs. The rational continuation agrees with the analytic expectation in this disk. A rational zero means a zero of its reduced numerator, with denominator nonzero. Specialize parameters before interpreting possible cancellations. The boundary |t|=mn/k is excluded from the original claim; t=mn/k is the first pole. There is no ambiguity requiring a replacement of the source claim. Cases k=0, nonintegral parameters, nonexponential costs, and matching-count partition functions are outside its scope.

## Prior results and status

Primary definitions and recursion: Sections 2.1–2.3, printed pages 7–8, equation (9). Proposition 9, page 23, gives a numerator of degree binom(k,2) and denominator of degree binom(k+1,2), before possible cancellations. Section 4.3 proves k<=3; Proposition 15 states closed-disk zero exclusion for k=3. Proposition 16, pages 30–34, gives finitely many possible exceptions for each fixed k, with no explicit cutoff. Thus none of these statements settles the full original or all of k=4.

Source status: **open-supported**, as an explicit conjecture in the current inspected arXiv version. Live record and bounded follow-up queries checked 2026-09-14; no equivalent resolution was identified in the inspected primary material. This is not a global priority guarantee. Details and query coverage: `literature/triage-validation.md`.

The supplied compact historical screen lists seven neighbors with distinct objects or predicates. No equivalent appears among those descriptions. Its reported full 2883-row/699-entry audit was not rerun: raw external registries are absent from this project. See `literature/dedup.json`; do not describe that earlier full coverage as independently verified by this worker.

## Proposed contribution and completed certificate

Nearest zero-free prior result: all k<=3 and an ineffective fixed-k finite-exception theorem. Proposed delta: zero exclusion for **k=4 and every integer m,n>=4**. The candidate is a result-note with the original still unresolved. More precisely, the primitive sextic numerator has no root in the closed disk |t|<=mn/4 for all real m,n>=4; for integer parameters this implies the MGF assertion and closed-disk exclusion for its reduced rational numerator. A pole on the boundary is not a finite nonzero value. The explicit distribution for k<=4 was already computable in Alm–Sorkin (2002); reconstructing that transform alone is not the contribution. Current comparisons and access limits are in `literature/research-validation.md`.

Equation (9) was implemented over QQ(m,n,t). The generic result, including numerator and denominator, is saved in `evidence/k4-rational.json`. Its primitive numerator P has degree 6 and leading coefficient 12. The removed content is

\[
mn(m-1)(m-2)(m-3)(n-1)(n-2)(n-3)>0
\]

throughout the intended parameter domain. Set R=mn/4 and

\[
H(z)=\frac{4^6}{(mn)^3}(1+z)^6P\!\left(R\frac{1-z}{1+z}\right).
\]

The disk |t|<R maps to Re(z)>0. Strict Hurwitz stability of H is a sufficient certificate and also excludes finite boundary roots; its leading coefficient controls the exceptional point t=-R. Write H=h_0 z^6+...+h_6. Research pass 1 completed the exact certificate after m=4+x,n=4+y: every h_i has 16 positive coefficients, and each Hurwitz determinant Delta_j has strictly positive coefficients on the entire support rectangle 0<=a,b<=3j. For j=1,...,6 the term counts are 16,49,100,169,256,361. Delta_6=h_6 Delta_5. Hence all these quantities are strictly positive on x,y>=0.

`evidence/research_k4_certificate.py` independently reconstructs the rational function with a bottom-up recurrence and computes the determinants. `evidence/verify_k4_certificate.py` uses only Python's standard library, clears the recurrence denominators in Z[m,n,t], divides exact linear factors, reconstructs the transform using binomial sums, and verifies every determinant coefficient by recursive Laplace expansion. Complete data and verification are in `evidence/research-k4-certificate.json` and `evidence/research-k4-verification.json`. Neither a finite parameter sweep nor floating-point roots are decisive.

The complete proposed argument is `evidence/k4-proof.md`: it gives the sextic, all transformed coefficient matrices, determinant certificates, the Möbius map including t=-R, a bound locating every denominator root outside the open disk, safe specialization/cancellation, and analyticity of the expectation. Its primary recursion source is copied to `evidence/external/2602.07563v1.pdf`, with accompanying primary text in `evidence/external/2602.07563v1.txt`. Known mathematical gaps in this scope: none identified by the proposer; a fresh referee audit has not occurred.

The simplest absolute-coefficient Rouché comparison with the Janson numerator fails its sufficient inequality at m=n=4: the error bound divided by the comparison lower bound is 873/10. This says nothing against the source conjecture or other Rouché estimates.

## Calibration correction and next test

Independent recursion and source-page inspection confirm that the expanded cubic terms in equations (37)–(38) should be -2t^3. There is also an omitted common normalization factor A=mn(m-1)(m-2)(n-1)(n-2) in the literal F=P/Q and J=P_J/Q formulas with denominator (36). After correcting the cubic sign, F=A P/Q matches equation (9) identically. At m=n=3 the printed P(0)/Q(0)=1/36, not 1. These corrections preserve the zero comparison and are calibration findings only.

**Next test:** a fresh referee should reconstruct the exact k=4 identity from the copied primary recursion, verify the full Hurwitz certificate and transform/domain argument, and assess the claimed contribution against the inspected primary literature. The original all-k conjecture remains unresolved.
