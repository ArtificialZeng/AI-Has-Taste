# Frozen problem: all-odd unit-gain dumbbell minimum energy

The verbatim source is `source.md`, which is immutable. Its SHA-256 at intake is
`ec7265dcc8f807c129c4343be3ebf171d3c8a7b56c87316810172368a8e016fa`.
Revalidated in recovery triage on 2026-09-14, job
`primary-20260914-dumbbell-min-energy-triage-cf68286d5ba6`.

## Definitions and quantifiers

For every pair of odd integers r,s >= 3 and every odd integer ell >= 1,
let D = D_(r,s,ell) consist of vertex-disjoint simple cycles C_r and C_s,
with designated vertices joined by a path of ell edges and ell-1 new internal
vertices. Thus N = r+s+ell-1 is even. Cycles sharing a vertex and a connector
of length zero are excluded. P_j below denotes a path on j vertices, including
the empty graph P_0.

For each oriented edge uv choose phi_uv in {z in C: |z|=1}, subject to
phi_vu = conjugate(phi_uv). Set (A_phi)_uv = phi_uv on edges and zero
elsewhere, including the diagonal. Its eigenvalues are real. Define
E(phi) = sum_(j=1)^N |lambda_j(A_phi)|.

Determine, for every allowed triple, the exact minimum
m(r,s,ell) = min_phi E(phi), and characterize all assignments attaining it
up to diagonal unitary switching A -> U A U*. The full quantified family,
including equality, is the original target. No subclass changes that target.

## Precise spectral reduction

Fix a direction on each cycle. A spanning tree is obtained by removing one
edge from each cycle; its gains can all be switched to 1. The two oriented
cycle products gamma_r,gamma_s in the unit circle completely specify the
switching class. Put a = Re(gamma_r), b = Re(gamma_s). Every point in
[-1,1]^2 is attainable, and the characteristic polynomial is

P_(a,b)(x) = m_D(x) - 2a m_(D-C_r)(x) - 2b m_(D-C_s)(x)
             + 4ab m_(P_(ell-1))(x),

where m_G(x) = sum_k (-1)^k M_k(G) x^(|V(G)|-2k), M_k counts k-edge
matchings, and D-C deletes all vertices of that cycle. Therefore minimizing
the energy is equivalent to minimizing the sum of absolute roots of P_(a,b)
on the square. Compactness and continuity ensure a minimum exists.

Real parts classify spectra here, not switching classes bijectively. To recover
all minimizing switching classes, lift each minimizing (a,b) to every pair
gamma_r = a +/- i sqrt(1-a^2), gamma_s = b +/- i sqrt(1-b^2), with coinciding
choices at endpoints counted once. Distinct oriented cycle products are not
identified merely because their real parts agree. No extra quotient by graph
automorphisms is imposed.

For comparison with Section 4 of the source only, use
alpha = (-1)^((r+1)/2) a and beta = (-1)^((s+1)/2) b.
These normalized variables must not replace a,b without these signs.

## Prior result and research scope

The live arXiv record inspected on 2026-09-14 lists v2 (26 May 2026) as latest.
Huang and Pereyra explicitly retain the full all-odd minimum problem in their
Introduction and conclusion. Definition 2.3, Proposition 2.9 and Theorem 2.10
agree with the interpretation above. The matching formula also follows
directly from determinant permutations: the only nontrivial cycle unions
are C_r, C_s, and their union; each contributes -2 times its real cycle gain.

Nearest prior result X: source Section 4.5 gives sign reduction, fixed-t
kernel minimization, claimed interior stationarity, a Hessian test at the
origin, and the exact D_(3,3,1) energy improvement of Proposition 4.9.
The paragraph introducing Figure 2 (printed p.17) already explicitly notes
the zero eigenvalue and nondifferentiability at (1/2,1/2). Recognizing that
cusp alone is therefore not a new contribution. Theorem 4.7 nevertheless
states its zero-integral equations for every interior minimizer, without
excluding singular points; this scope was checked in the live v2 HTML.
Proposed delta Y: a rigorous treatment of singular minimizing branches and
their equality conditions, potentially repairing the stationarity argument;
a useful uniform subclass classification would be partial progress only.
In particular, seek explicit directional optimality conditions uniform in
the three odd lengths, with the zero-root coefficient derived from matching
polynomials. A generic matrix trace-norm derivative formula alone is not
the intended structural contribution.
Verification route Z: exact matching polynomials, Hermitian characteristic
polynomials, algebraic root isolation, and one-sided derivatives at zero
eigenvalues before any use of differentiating an improper integral.

Source status: open-supported, qualified by the bounded literature search.
The exact subsidiary calculations in `evidence/triage-math.md` motivate
research on a corrected nonsmooth stationarity statement. They carry no
priority claim or independent mathematical acceptance at triage.
The fresh recovery replay and argument review are recorded in
`evidence/recovery-checks.json` and `evidence/recovery-triage.md`.

## Research pass 1: exact partial scope proposed for review

The original quantified minimum and switching-equality target above remains
unresolved. `evidence/singular-branch.md` proposes a uniform replacement for
Theorem 4.7 at simple zero eigenvalues, with an explicit length-dependent
directional term and normal interval condition, strict local sufficiency
away from the interval endpoints, unique constrained minima at fixed positive
product, and a length-based criterion forcing the singular-curve minimum to
the boundary. Exact D331 global minimization validates the subsidiary source
correction; an exact D335 local descent certificate tests its limits.

No novelty is claimed for general spectral subgradient calculus, the known
D331 half-diagonal energy or its already acknowledged cusp. The proposed
contribution is the graph-specific correction and its branch consequences.
The threshold equality case and singular boundary sufficiency are excluded.
The live bounded comparison is `literature/research-screen.md`. The decisive
local primary PDF/text are preserved unchanged as
`evidence/external/2604.27785v2.pdf` and
`evidence/external/2604.27785v2.txt`, to bind their actual statements to review.
