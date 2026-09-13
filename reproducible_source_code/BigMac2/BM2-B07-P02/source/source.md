## DM07-02 The complete two-weight `Z/5Z` Goemans--Linial cone

Use the uniform-sparsest-cut and Goemans--Linial SDP normalization of
Stamoulis, *Integrality Gap Bounds for the Goemans-Linial SDP on Finite
Abelian Cayley Graphs*, arXiv:2609.05368v1.

For real `a,b>=0`, `a+b>0`, let `G_{a,b}` be the undirected weighted Cayley
graph on `Z/5Z` in which every edge of difference `+-1` has weight `a` and
every edge of difference `+-2` has weight `b`. Prove or disprove

`SDP_GL(G_{a,b}) = psi(G_{a,b})
                  = 5*min(a+2*b,2*a+b)/(6*(a+b))`.

Classify all optimal cuts up to the dihedral action and all optimal
translation-invariant semimetrics, including the faces `a=0`, `b=0`, and the
tie `a=b`. A complete proof must justify translation averaging without losing
the triangle inequalities, derive the full two-distance metric cone, and show
that no non-translation-invariant feasible metric improves the optimum.

The source proves exactness when a minimizing character has image size at
most four, shows that the five-gon squared-chord character metric itself is
infeasible, treats ordinary cycles, and gives a ten-vertex gap family. The
requested claim is a source-derived first complete weight cone at image size
five; it must pass a literature check for whether the formula is already an
immediate published special case.

Primary source: arXiv:2609.05368v1, Sections 4, 6, and 7.

