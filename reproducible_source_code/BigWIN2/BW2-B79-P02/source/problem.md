# Precise problem statement

## Ambient objects and topology

Fix an arbitrary infinite-dimensional complex Hilbert space \(H\); no
separability assumption is made.  Write \(\mathcal B(H)\) for the bounded
operators on \(H\), and let

\[
\mathsf{CP}^{\sigma}
=\{\Phi:\mathcal B(H)\to\mathcal B(H):
  \Phi\text{ is complex-linear, normal, and completely positive}\}.
\]

Here normal means ultraweakly continuous.  The ambient space of normal maps is
given the point-ultraweak topology: a net \((\Phi_\alpha)\) converges to
\(\Phi\) precisely when, for every \(T\in\mathcal B(H)\) and every trace-class
\(S\),

\[
\operatorname{Tr}(S\Phi_\alpha(T))\longrightarrow
\operatorname{Tr}(S\Phi(T)).
\]

A convex cone is closed under addition and multiplication by nonnegative real
scalars.  In this problem, “proper” means a strict subset of
\(\mathsf{CP}^{\sigma}\).

## Finite corners and cut--pad maps

For finite-rank orthogonal projections \(P,Q\) on \(H\), identify
\(\mathcal B(\operatorname{ran}P)\) with \(P\mathcal B(H)P\).  For a normal map
\(\Phi\), its \((Q,P)\)-compression is

\[
\Phi_{Q,P}(X)=Q\Phi(X)Q,
\qquad X\in P\mathcal B(H)P.
\]

For any set \(\mathsf K\) of normal maps, use the compression-image notation
from Remark 5.4 of the source,

\[
\mathsf K_{Q,P}=\{\Phi_{Q,P}:\Phi\in\mathsf K\}.
\]

Thus this notation remains meaningful when \(\mathsf K\) is not cut--pad
stable.  Let \(\mathsf{CP}_{Q,P}\) denote the cone of all completely positive
maps
\(\mathcal B(\operatorname{ran}P)\to\mathcal B(\operatorname{ran}Q)\).
The cut--pad map is

\[
\Phi^{(Q,P)}(T)=Q\Phi(PTP)Q,
\qquad T\in\mathcal B(H).
\]

Cut--pad stability would require
\(\Phi^{(Q,P)}\in\mathsf K\) for every \(\Phi\in\mathsf K\) and every
finite-rank \(P,Q\), but it is deliberately not assumed below.

## Frozen target, made fully quantified

For every infinite-dimensional complex Hilbert space \(H\), construct a
point-ultraweakly closed convex cone

\[
\mathsf K\subsetneq\mathsf{CP}^{\sigma}
\]

such that, for every pair of finite-rank orthogonal projections \(P,Q\),

\[
\mathsf K_{Q,P}=\mathsf{CP}_{Q,P}.
\]

This is a counterexample to reconstruction without cut--pad stability: any
\(\Psi\in\mathsf{CP}^{\sigma}\setminus\mathsf K\) has every finite
compression in the corresponding corner cone \(\mathsf K_{Q,P}\), while
\(\Psi\notin\mathsf K\).  Equality is required for all finite corners, not
merely along a cofinal sequence.  The task does not ask for a cone stable under
other pre- or post-compositions, and it makes no novelty or open-problem claim.

## Nearest verified source result and proposed delta

Kian--Kittaneh, arXiv:2609.04889v1, Definition 3.3 and Theorem 3.9, prove
finite-corner reconstruction when both cut--pad stability and
point-ultraweak closedness hold.  Theorem 4.1 gives the associated corner
bipolar separation.  Proposition 5.5 exhibits the complementary failure after
dropping closedness while retaining cut--pad stability.  The proposed delta is
to retain closedness and complete positivity, drop cut--pad stability, and
give an explicit cone with all the same finite corner cones as
\(\mathsf{CP}^{\sigma}\).

## Admitted construction lead (not yet a reviewed result)

Fix a unit vector \(e\in H\), set \(E=|e\rangle\langle e|\) and
\(A=2E-I\), and test

\[
\mathsf K=\{\Phi\in\mathsf{CP}^{\sigma}:
\langle e,\Phi(A)e\rangle\leq0\}.
\]

The exact calculations in `evidence/triage.md` make this a bounded research
target.  They are triage evidence, not an independently audited proof.
