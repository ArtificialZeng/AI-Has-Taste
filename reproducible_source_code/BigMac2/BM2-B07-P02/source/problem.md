# Precise reading: DM07-02

## Frozen input and provenance

- Immutable input: `source.md` (SHA-256
  `3e5ea16b71c4994ed41da59d6c974640eeb23303558f0df40da7550fab4ba6db`).
- Triage job: `bigMac-00007-p02-triage-5c4290255495`.
- The statement below interprets, but does not replace, the frozen wording.

## Objects and normalization

Let \(\Gamma=\mathbb Z/5\mathbb Z\), written additively. Quantify over every
ordered pair \((a,b)\in\mathbb R_{\ge0}^2\setminus\{(0,0)\}\). The weighted
undirected Cayley graph \(G_{a,b}\) has the five unordered edges
\(\{x,x+1\}\) of weight \(a\) and the five unordered edges \(\{x,x+2\}\) of
weight \(b\). Equivalently, its normalized random walk chooses a step

\[
 p(1)=p(-1)=\frac{a}{2(a+b)},\qquad
 p(2)=p(-2)=\frac{b}{2(a+b)}.
\]

For a nonempty proper \(A\subsetneq\Gamma\), with \(x,y\) independent uniform
vertices and \(s\) sampled from this step distribution, set

\[
 N_{a,b}(A)=\Pr[1_A(x)\ne1_A(x+s)],\quad
 D(A)=\Pr[1_A(x)\ne1_A(y)]=2\frac{|A|}{5}\left(1-\frac{|A|}{5}\right),
\]
\[
 \psi_{G_{a,b}}(A)=\frac{N_{a,b}(A)}{D(A)},\qquad
 \psi(G_{a,b})=\min_{\varnothing\ne A\subsetneq\Gamma}\psi_{G_{a,b}}(A).
\]

A GL-feasible semimetric is a function \(d:\Gamma^2\to\mathbb R_{\ge0}\)
such that \(d(x,y)=\|v_x-v_y\|_2^2\) for some Euclidean vectors, and
\(d(x,z)\le d(x,y)+d(y,z)\) for all \(x,y,z\). It may vanish on distinct
points. Put

\[
 N_{a,b}(d)=\mathbb E_{x,s}d(x,x+s),\qquad
 D(d)=\mathbb E_{x,y}d(x,y),
\]
\[
 \operatorname{SDP}_{\rm GL}(G_{a,b})=
 \inf_{d\ \mathrm{GL\text{-}feasible},\ D(d)>0}\frac{N_{a,b}(d)}{D(d)}.
\]

This is the random-walk/uniform-demand normalization of Stamoulis rather than
an unnormalized capacity convention.

## Precise claim to resolve

For every admissible \((a,b)\), prove or disprove

\[
 \operatorname{SDP}_{\rm GL}(G_{a,b})=\psi(G_{a,b})
 =\frac{5\min\{a+2b,\,2a+b\}}{6(a+b)}. \tag{C}
\]

The requested classification is read as the following simultaneous claim.
Cuts are unordered bipartitions, so \(A\) and \(A^c\) are identified; if one
instead records subsets, every orbit below has its complementary orbit too.
The dihedral group \(D_5\) acts on \(\Gamma\) by \(x\mapsto \pm x+c\).

- If \(a>b\) (including \(b=0\)), the optimal cuts should be precisely the
  \(D_5\)-orbit of the adjacent-pair cut represented by \(A=\{0,1\}\).
- If \(b>a\) (including \(a=0\)), they should be precisely the orbit of the
  difference-two pair represented by \(A=\{0,2\}\).
- If \(a=b>0\), every nontrivial cut should be optimal.

A semimetric is translation-invariant when \(d(x+c,y+c)=d(x,y)\) for all
\(c\). Write

\[
 u=d(0,1)=d(0,4),\qquad v=d(0,2)=d(0,3).
\]

The claimed complete list of optimal nonzero translation-invariant feasible
semimetrics, modulo positive scaling, is:

- \(a>b\): the single ray \(v=2u\), \(u>0\);
- \(b>a\): the single ray \(u=2v\), \(v>0\);
- \(a=b>0\): every ray in \(u,v>0\) with \(u\le2v\) and \(v\le2u\).

Finally, (C) includes the assertion that averaging an arbitrary feasible
semimetric over all five translations preserves GL feasibility, all triangle
inequalities, and both objective averages. Thus restricting to the displayed
two-distance cone loses no optimum; this must be proved, not assumed.

## Triage calculations and boundary checks

These are discriminating checks, not a reviewed resolution. If \(c_1(A)\)
and \(c_2(A)\) count crossing unordered edges of differences \(1\) and \(2\),
then

\[
 \psi_{G_{a,b}}(A)=
 \frac{5(ac_1(A)+bc_2(A))}{2(a+b)|A|(5-|A|)}.
\]

Up to complement and \(D_5\), the three cut types have representatives
\(\{0\},\{0,1\},\{0,2\}\), with crossing-count pairs respectively
\((2,2),(2,4),(4,2)\). Their values are
\(5/4\), \(5(a+2b)/(6(a+b))\), and
\(5(2a+b)/(6(a+b))\). This gives the proposed cut formula and the stated
tie/boundary behavior.

For an invariant semimetric the triangle inequalities reduce to
\(u,v\ge0\), \(u\le2v\), \(v\le2u\). Fourier diagonalization gives the weaker
squared-Euclidean restrictions
\(u\le\varphi^2v\), \(v\le\varphi^2u\), where
\(\varphi=(1+\sqrt5)/2\); hence every point of the nonzero triangle cone is
squared Euclidean. Its objective is

\[
 \frac{5(au+bv)}{2(a+b)(u+v)},
\]

whose endpoint minimizers agree with the proposed metric classification.
The remaining proof obligation is to audit every implication, especially
translation averaging and the Fourier characterization.

## Source and status triage

Retrieved 2026-09-07:

- Georgios Stamoulis, *Integrality Gap Bounds for the Goemans--Linial SDP on
  Finite Abelian Cayley Graphs*, arXiv:2609.05368v1,
  <https://arxiv.org/abs/2609.05368>. Definitions and normalization occur in
  Section 2 (PDF pp. 5--8); Lemma 4.1 (PDF p. 9) proves the regular pentagon
  squared-chord metric infeasible; Proposition 6.1 (PDF pp. 15--16) proves
  exactness for ordinary cycles, covering the faces \(a=0\) or \(b=0\) after
  relabeling.
- Searches for the exact displayed formula, the exact two-weight phrase, and
  equivalent weighted-\(C_5\)/translation-invariant GL terminology returned
  no matching primary source. This is only a limited screen, not evidence of
  priority.

Source status: **new-question; novelty unverified**. Nearest prior result:
Stamoulis Proposition 6.1 for the one-weight cycle faces. Proposed delta: the
entire two-weight cone plus equality classifications. Verification route:
finite cut-orbit enumeration, translation symmetrization, exact Fourier/CND
description of the two-distance cone, and a one-variable endpoint
optimization.
