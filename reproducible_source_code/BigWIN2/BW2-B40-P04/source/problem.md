# Precise reading — seven points on \(S^3\)

## Frozen target

Interpret the source through the notation of Zlatanov, arXiv:2608.25805v1. Let

\[
\mathcal M=(S^3)^7,\qquad S^3=\{x\in\mathbb R^4:\|x\|_2=1\}.
\]

A codebook is a labeled tuple \(C=(c_1,\ldots,c_7)\in\mathcal M\). This is the
paper's compact parameter space; relabeling and applying a common orthogonal
transformation do not change the objective. Although ordinary set notation
suggests distinct points, the paper's optimization includes coincident entries.
Such entries are allowed in the precise reading so that the displayed minimum is
literally the cited one; they cannot occur in a bounded-energy family for all
sufficiently large \(\gamma\).

Put

\[
E_7=\{(i,j):1\le i,j\le7,\ i\ne j\},\qquad
\rho_{(i,j)}(C)=c_i^Tc_j,
\]

so all 42 **ordered** off-diagonal pairs are counted. Define

\[
\rho_{\max}(C)=\max_{e\in E_7}\rho_e(C),\qquad
\rho^*_{7,4}=\min_{C\in\mathcal M}\rho_{\max}(C)=0.
\]

The equality is the orthoplex bound plus feasibility of any seven vertices of
the four-dimensional cross-polytope. For every real \(\gamma>0\), define

\[
G_\gamma(C)=\sum_{e\in E_7}e^{\gamma\rho_e(C)},\qquad
V_\gamma(7,4)=\min_{C\in\mathcal M}G_\gamma(C),
\]

and

\[
K^*_{7,4}=\lim_{\gamma\to\infty}V_\gamma(7,4).
\]

The minimum exists by compactness and continuity. The limit exists by Theorem 2
of the source paper. Equation (27) of that paper has exponent
\((n\gamma/4)(\rho_e-\rho^*_{M,n})\); for \(n=4\) and \(\rho^*_{7,4}=0\), it is
exactly the \(G_\gamma\) frozen above, with no rescaling discrepancy.

The claim is

\[
\boxed{K^*_{7,4}=24}.
\]

Equivalently, the missing proof direction is the global quantified assertion

\[
\forall\varepsilon>0\ \exists\Gamma>0\ \forall\gamma\ge\Gamma\
\ \forall C\in(S^3)^7:\quad G_\gamma(C)\ge24-\varepsilon.
\]

A disproof in the scope fixed by the source is supplied by a rigorously feasible
family \(C_\gamma\in(S^3)^7\), defined for all sufficiently large \(\gamma\),
with \(\limsup_{\gamma\to\infty}G_\gamma(C_\gamma)<24\). Floating-point
optimization alone proves neither alternative.

## Source status and nearest result

Primary source inspected on 2026-09-06:
<https://arxiv.org/html/2608.25805v1> (version 1, 2026-08-26).

- Equations (4), (6), (27), (30), and (35) give the ordered-pair correlation,
  packing optimum, soft energy, finite-\(\gamma\) minimum, and limiting
  coefficient used above.
- Equation (66) proves \(\rho^*_{n+k,n}=0\) in the orthoplex range.
- Proposition 4 gives the nearest fixed-code result
  \(K^{\mathrm{fix}}_{7,4}=4n(k-1)=32\).
- Proposition 5, equations (69)--(76), constructs a feasible SNR-indexed family
  and proves \(K^*_{7,4}\le4k(k-1)=24\).
- Conjecture 1, equation (92), explicitly asserts equality for
  \(n\ge4\), \(3\le k\le n-1\); \((n,k)=(4,3)\) is its smallest instance. The
  paragraph immediately before it says that a matching global lower bound has
  not been proved.

Exact-phrase and notation searches on 2026-09-06 for the conjecture title,
\(K^*_{7,4}\), `4k(k-1)`, and `Gaussian soft-packing energy` located the source
paper but no distinct primary paper resolving this instance. This narrow search
supports the intake label **open-supported**, not a claim of exhaustive priority.

## Proposed contribution and scope

Nearest prior result X: the explicit construction proves the sharp candidate
upper bound 24, while the source's global converse is known only at the endpoint
\(k=2\). Proposed delta Y: prove the missing global liminf lower bound 24 for
seven unit vectors in \(\mathbb R^4\), or find an exact feasible multiscale
family with limiting energy below 24. Verification route Z: work with the
\(7\times7\) correlation Gram matrix (positive semidefinite, diagonal one, rank
at most four), first localize bounded-energy families near the optimal
zero-correlation packing set, and then derive or falsify a uniform weighted
ordered-pair inequality at the \(1/\gamma\) scale.

