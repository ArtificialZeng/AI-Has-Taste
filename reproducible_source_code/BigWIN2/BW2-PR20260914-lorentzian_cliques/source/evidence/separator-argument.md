# Two-vertex cuts give a fixed-target Lorentzian obstruction

Proposer: primary-20260914-lorentzian-cliques-research-d50fb585b2a3.
Research argument, 2026-09-14; no independent referee acceptance.

## Exact statement

Let F be a finite connected simple bipartite graph with parts L,R of size
k>=2. Assume its only maximum independent sets are L and R. (The standard
name is a bistable bipartite graph; no external structural characterization
is needed below.) Put

    A = [[0,1,1],[1,0,1],[1,1,1]],   f=Z_(F,A),
    beta=(k-1,k-1,0),
    c=[x_1^(k-1) x_2^(k-1) x_3^2] f.

For distinct u,v, let q(u,v) be the number of connected components of
F-{u,v}, including isolated vertices. Let s be the number of unordered pairs
contained entirely in L or entirely in R for which q(u,v)>1. Then

    c = sum_(u in L,v in R) 2^q(u,v) + 2s,                         (1)
    Hessian(partial^beta f)
      = 2(k!)^2 [[0,1,1],[1,0,1],[1,1,c/k^2]].                  (2)

Consequently c>=2k^2, with equality if and only if F has no two-vertex cut.
F is automatically 2-connected. Thus the Hessian in (2) has two positive
eigenvalues exactly when F is not 3-connected. In that case f is not
Lorentzian, giving an admissible fixed target for this entire source class.
If F is 3-connected, this particular derivative has inertia (1,1,1), where
the entries count positive, negative, and zero eigenvalues. This says nothing
about the other derivatives or Lorentzianity of f.

## Proof

**Strict expansion.** For every nonempty proper S contained in either part,
|N(S)|>=|S|+1. Indeed, if S is contained in L and |N(S)|<=|S|, then
S union (R\N(S)) is independent and has at least k vertices. A size greater
than k contradicts maximality of L,R; equality gives a third maximum
independent set, since S is nonempty and proper. Interchange L and R for
the other side. In particular every vertex has degree at least 2.

**No cut vertex (known background, rederived).** Biconnectivity is already
Lemma 6 of de Berg--Jansen--Mukherjee, arXiv:1610.03766v1; this is not part
of the novelty claim. Delete u in L. Each component has at least one R vertex:
an L vertex retains all its neighbors. If there were several components,
each R-part R_i would be nonempty and proper in R. Its neighborhood in F
lies in L_i union {u}, so strict expansion implies |R_i|<=|L_i|. Summing
contradicts |R|=k>k-1=|L\{u}|. Thus F-u is connected; deleting a vertex
of R is symmetric. Since |V(F)|>=4, F is 2-connected.

**A cross-part deletion.** Delete u in L and v in R. Each remaining vertex
retains a neighbor by the minimum-degree bound, so every component has
nonempty parts L_i,R_i, both proper in the original parts. Expansion applied
to L_i and R_i, with neighborhoods respectively contained in R_i union {v}
and L_i union {u}, gives |L_i|<=|R_i| and |R_i|<=|L_i|. Hence every component
is balanced. It has exactly two proper colorings by spins 1 and 2, and
every independent choice of their orientations uses k-1 vertices of each
spin. This deletion contributes 2^q(u,v) to c.

**A deletion within a part.** Delete u,v in L. If the remaining graph is
connected, its unique bipartition has sizes k-2,k, so it contributes no
balanced proper coloring. If it is disconnected, every component has a
nonempty proper R_i. Expansion gives |R_i|<=|L_i|+1, since its neighbors
lie in L_i union {u,v}. When L_i is nonempty, it is proper and all its
neighbors lie in R_i; expansion gives |R_i|>=|L_i|+1. When L_i is empty,
the connected component is a single R vertex, giving the same equality.
Thus every component has |R_i|-|L_i|=1. The total difference is 2, so there
are exactly two components. Each has two color orientations, and exactly
two of the four orientation choices cancel their imbalances. This deletion
contributes 2. The proof for deletion within R is identical.

**Coefficient formula.** In the fixed target A, spins 1 and 2 must each
occupy an independent set, while spin 3 is unrestricted. All admissible
assignments have weight 1. Choose the unordered pair occupying spin 3 and
apply the preceding two cases. This proves (1), including isolated-vertex
components and k=2. Since q>=1, every cross-part summand is at least 2.
It exceeds 2 exactly for a cross-part cut. The remaining term is positive
exactly when there is a same-part cut. This proves the equality criterion.

For completeness, without the maximum-independent-set assumption the
general deletion expression is

    c = sum_(D subset V, |D|=2) [z^(k-1)] product_(C component of F-D)
                                      (z^|C intersect L|+z^|C intersect R|).

The assumption is what simplifies this elementary coloring identity to (1).

**Hessian normalization and inertia.** The independence number is k, so
c_(k+1,k-1,0)=c_(k-1,k+1,0)=0. Connectedness gives c_(k,k,0)=2. A color-1
class of size k must be L or R; omitting one vertex of the other part for
spin 3 shows c_(k,k-1,1)=2k, and symmetry gives c_(k-1,k,1)=2k.
For each Hessian entry multiply c_(beta+e_i+e_j) by the product of the
three exponent factorials. This gives (2), with the factor 2 in the (3,3)
entry coming from 2!.

The target characteristic polynomial is (lambda+1)(lambda^2-2lambda-1),
so A has spectrum -1,1-sqrt(2),1+sqrt(2) and is entrywise nonnegative with
exactly one positive eigenvalue. In the normalized Hessian M, (1,-1,0)
is an eigenvector of eigenvalue -1. On its orthogonal complement, in the
orthonormal basis ((1,1,0)/sqrt(2),(0,0,1)), the matrix is

    [[1,sqrt(2)],[sqrt(2),t]],    t=c/k^2>=2.

Its determinant is t-2 and trace 1+t>0. It has two positive eigenvalues
if t>2, and eigenvalues 3 and 0 if t=2. The order of beta is 2k-2, so the
two-positive-eigenvalue case violates the defining necessary quadratic
derivative condition for a Lorentzian polynomial. No support claim is used.

## Boundary checks and scope

For C_(2k), deleting an adjacent cross-part pair leaves one component;
deleting a nonadjacent cross-part pair leaves two. Every same-part pair
is a cut. Hence (1) gives 4k+4(k^2-2k)+2k(k-1)=6k(k-1), recovering the
all-even-cycle result for every k>=2.

For K_(k,k), k>=3, every two-vertex deletion is connected, so c=2k^2.
For K_(2,2)=C4, the two same-part pairs are cuts and c=8+4=12. Equality
is therefore a 3-connectivity criterion, not a complete-bipartite criterion.

The proof resolves a subsidiary class of sources and does not settle the
original connected-clique characterization. It does not assert that the
fixed target works for all bistable graphs. The structural counting proof is
self-contained. Novelty/significance screening and a fresh mathematical
referee remain necessary. No mathematical gap is presently identified in
the stated argument. `separator-check.py` and `separator-check.json` verify
all six needed coefficients, the general and simplified deletion formulas,
and the predicted inertia by exact arithmetic for every qualifying graph
among all labeled fixed-part bipartite graphs with k=2,3,4. The qualifying
counts are 1,34,6785, totaling 6820. They also check 22 structured cases:
cycles and complete bipartite graphs for k=2..7, and odd theta graphs and
complete bipartite graphs minus a perfect matching for k=3..7. Some small
structured cases coincide; they are not counted as distinct graphs. These
finite checks corroborate the proof and are not an independent referee audit.

The graph without a two-cut need not be complete bipartite: K_(4,4) minus
a perfect matching (the cube) is an explicit tested equality example.
The complete literature comparison and its limitations are recorded in
`literature/separator-comparison.md`.
