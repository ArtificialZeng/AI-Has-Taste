# Minimum energy of odd–odd–odd complex unit gain dumbbell graphs

Primary source: Silin Huang and Kevin Pereyra, On the Extremal Energy of Complex Unit Gain Dumbbell Graphs, arXiv:2604.27785v2 (26 May 2026).
Primary version record: https://arxiv.org/abs/2604.27785
Primary full text: https://arxiv.org/html/2604.27785v2
Primary PDF: https://arxiv.org/pdf/2604.27785v2

Short original statement, Introduction, printed p.2:
> The only remaining problem is the minimum-energy problem when r, s, and ℓ are all odd.

The following is the supervisor's explicit mathematical interpretation, not an additional author quotation.

For odd integers r,s>=3 and odd integer ell>=1, take disjoint simple cycles of lengths r and s and connect one chosen vertex on each by an ell-edge path whose internal vertices are new. Denote this graph D_(r,s,ell); it has N=r+s+ell-1 vertices. A complex unit gain assigns phi_uv in the unit circle to each oriented edge, with phi_vu=conjugate(phi_uv). Its Hermitian adjacency matrix A_phi has these entries on edges and zero elsewhere. Define E(phi)=sum_(i=1)^N |lambda_i(A_phi)|.

Determine the minimum energy m(r,s,ell) over all gain assignments and characterize every minimizing assignment up to switching. Equivalently, after switching spanning-tree gains to1, classify all minimizers over (a,b) in[-1,1]^2, where a and b are the real parts of the two oriented cycle gain products. This is the full all-odd family problem, not just D_(3,3,1), the signed endpoints, or a numerical optimization.

A useful equivalent source formula (Theorem2.10, printedp4) is
P_(a,b)(x)=m_D(x)-2a m_(D-C_r)(x)-2b m_(D-C_s)(x)+4ab m_(P_(ell-1))(x),
where m_G is the ordinary matching polynomial, D-C deletes the cycle vertices, and P_0 is empty with matching polynomial1. This formula and the equality of the spectral and gain descriptions must be checked in triage.

For comparison with sourceSection4, its normalized variables are alpha=(-1)^((r+1)/2)*a and beta=(-1)^((s+1)/2)*b. Do not silently use alpha,beta as a,b when a cycle length changes modulo4.

The exact source remains open in this inspected v2; no later full resolution was found in bounded searches on2026-09-14. This is not a global priority guarantee. Sources and exclusions are recorded separately.

Known baseline, not new contributions: sourceLemma4.5 sign/simultaneous-negation reductions; Theorem4.6 fixed-t kernel minimization; Theorem4.7 claimed interior stationarity/symmetric diagonal reduction; Theorem4.8 Hessian criterion; Proposition4.9 already gives E(1/2,1/2)=2+sqrt(13)+sqrt(5)<E(0,0) for D_(3,3,1). Reproducing that inequality is a known result, not a disproof or solution of the frozen question. Other parity families and all maximum-energy cases are already treated.

A partial subclass theorem or a precisely identified correction to a subsidiary assertion may only be reported as a result-note if independently judged meaningful; the original all-odd classification must remain unresolved. A generic quantifier-elimination recipe or growing numerical table alone does not supply the intended structural classification.
