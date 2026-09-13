# Fresh mathematical referee report

## Frozen scope and evidence binding

I reviewed the exact `result-note` claim frozen in `claim.json`: every
five-label moment system with exactly three distinct direction values, of
multiplicities (3,1,1), has an attained admissible selection on at most
three labels with (C(q)\le 5E/8).  The claim does not purport to prove the
five-atom assertion for other direction multiplicities, the six-atom
assertion, or Conjecture 7.8.  The original problem therefore remains
unresolved.

I recomputed the SHA-256 hashes of `claim.json` and every enumerated evidence
file.  They agree with `audit/snapshot.json`, whose digest is
`5482579d7b8e056581fe37df26d7a304bc29991b2846a927bd385d5a38be0186`.

## Reconstruction of the decisive argument

Let (G_1) be the three-label direction class and (G_2,G_3) the singleton
classes.  Write their distinct unit directions as (	au_g), their original
mass totals as (P_g), and their response means as (m_g).  The two vectors


\[
  (\sqrt{P_g})_{g=1}^3,\qquad
  (\sqrt{P_g}\tau_g)_{g=1}^3
\]

are orthonormal.  The two response moment equations put
((\sqrt{P_g}m_g)_g) in their one-dimensional orthogonal complement.  The
diagonal of the corresponding rank-one projection is (1-2P_g).  Hence,
with (E_m=\sum_gP_g|m_g|^2),

\[
 P_g|m_g|^2=(1-2P_g)E_m,
 \qquad E=E_m+P_1V_1,
\]

where (V_1) is the conditional variance in (G_1).  Because the three
directions are distinct and all (P_g) are positive, (0<P_g<1/2); thus all
later denominators (1-2P_g) are positive.

Put (r_i=p_i/P_1) and (w_i=z_i-m_1) on (G_1).  Then
(\sum_i r_iw_i=0) and (V_1=\sum_i r_i|w_i|^2).  Choosing one (G_1)
label and both singleton labels, with masses (P_1,P_2,P_3), gives
(mu=0) and the attained certificate

\[
 A_0=2P_1^2d_*^2,
 \qquad d_*^2=\min_i|w_i|^2.
\]

I independently checked the second certificate.  For (g\in\{2,3\}), let
(h) be the other singleton class.  Interpolation between
((\tau_1,m_1)) and ((\tau_g,m_g)) has coefficient vector (A_g).
Changing the first response by (w) changes that vector by

\[
 v_gw,\qquad v_g=\frac{(-\tau_g,1)}{\tau_1-\tau_g}.
\]

Eliminating class (h) from the two aggregate response equations gives

\[
 (1+\overline{\tau_g}\tau_1)m_g
   =-\frac{1-2P_g}{P_g}m_1.
\]

Direct projection then yields

\[
 \|A_g+v_gw\|^2
 =\frac{|m_g|^2}{2}
  +\frac{2}{|\tau_1-\tau_g|^2}
       \left|w+\frac{m_1}{2P_g}\right|^2.
\]

Splitting positive mass in direction (	au_1) between any two (G_1)
labels realizes every point of the corresponding closed segment.  Giving
positive mass to the singleton realizes the two-direction interpolant and
makes (|\mu|<1).  Endpoint minimizers use only one (G_1) label, so the
minimum is attained even there.  Finally,

\[
 P_1P_g|\tau_1-\tau_g|^2=1-2P_h
\]

follows by taking squared moduli in
(P_1\tau_1+P_g\tau_g=-P_h\tau_h).  Thus the exact attained certificate is

\[
 S_g=\frac{1-2P_g}{2P_g}E_m
 +\frac{2P_1P_g}{1-2P_h}\delta_g^2,
\]

where (delta_g) is the distance from (-m_1/(2P_g)) to the union of the
three edges joining the (w_i).

The remaining geometric lemma is valid.  For a nondegenerate weighted
triangle with barycentre (0), let (ell_i,h_i,n_i) be the opposite-side
length, distance from (0), and inward unit normal.  With

\[
 Z=\sum_i\frac{r_i}{h_i^2},\quad
 \alpha_i=\frac{r_i/h_i^2}{Z},\quad
 M=\sum_i\alpha_i n_in_i^{\mathsf T},
\]

the barycentric and polygon identities give
(\sum_i\alpha_ih_in_i=0) and (1/Z=V\det M).  I checked the latter from
the weighted variance identity and the (2\times3) Cauchy--Binet formula.
For an interior target (u), averaging its three signed side distances
therefore bounds the squared distance to the boundary by

\[
 V\det M+u^{\mathsf T}Mu.
\]

If the eigenvalues of (M) are (lambda,1-lambda), with
(0\le\lambda\le1/2), maximizing
((1-\lambda)(V\lambda+|u|^2)) gives

\[
 \operatorname{dist}^2(u,\Gamma)\le
 \begin{cases}
 (V+|u|^2)^2/(4V),&|u|^2\le V,\\
 |u|^2,&|u|^2\ge V.
 \end{cases}
\]

For an exterior target, (0) belongs to the triangle and the nearest point
of the triangle lies on its boundary, so the bound by (|u|^2) suffices.
For a collinear triangle, one edge contains (0), giving the same conclusion.
Thus no compactness, projection-to-an-edge, or degenerate-triangle gap is
present.

For the final scalar comparison, set (x_k=1-2P_k), choose
(x=x_1), (y=\max(x_2,x_3)), and (z=\min(x_2,x_3)).  If (A_0>5E/8),
then (0<x<3/8).  Choosing (h) with (x_h=y) gives
(y\ge(1-x)/2) and (z=1-x-y).  When (E_m=0), the geometric lemma gives

\[
 \frac{S_g}{P_1V_1}\le\frac{x+y}{4y}<\frac58.
\]

When (E_m>0), normalize it to one.  The failed (A_0) alternative implies

\[
 V>V_0=\frac{10}{(1-x)(3-8x)}.
\]

For the chosen target,

\[
 U=\left|\frac{m_1}{2P_g}\right|^2
 =\frac{2x}{(1-x)(1-z)^2},\qquad \frac UV<\frac12.
\]

Consequently the geometric bound gives
(delta_g^2\le V/4+5U/8).  Substitution in (S_g) gives

\[
 S_g\le \frac{z}{1-z}+\frac{5x}{8y(1-z)}
       +\frac{(1-x)(1-z)}{8y}V.
\]

The coefficient of (V) in (5(1+(1-x)V/2)/8-S_g) is
((1-x)(3y-2x)/(16y)>0), so it is enough to use (V=V_0).  I independently
expanded the resulting numerator as

\[
 N=30x^2-15x-24y+108xy+54y^2-104xy(x+y).
\]

Writing (y=(1-x)/2+q), (q\ge0), reproduces

\[
 N=\left(\frac32-2x-\frac{21}{2}x^2+26x^3\right)
 +(30-50x)q+(54-104x)q^2.
\]

All three displayed coefficients are positive for (0<x<3/8); for the
constant term this follows from the two elementary bounds recorded in the
evidence on (2N|_{q=0}=3-4x-21x^2+52x^3).  Hence (S_g<5E/8).  Together
with the attained (A_0) alternative, this proves the frozen claim.

## Attacks, boundary cases, and contribution assessment

- If (E=0), all (z_i=0); selecting one label from each direction class
  with masses (P_g) gives an admissible attained zero-cost selection.
- If (V_1=0) while (E>0), then (A_0=0), so the proof never divides by
  (V_1).  In the branch using the geometric lemma, failure of (A_0)
  forces (V_1>0).
- All segment minima are on compact segments and are realized by probability
  vectors.  Distinct unit directions with positive mass make every such
  two-direction selection strictly admissible; the proof establishes an
  existential minimum, not merely a boundary infimum.
- The strict inequalities used after assuming (A_0>5E/8) are harmless:
  equality is already covered by the attained (A_0) branch.
- As a supplementary falsification check, I sampled 50,000 random weighted
  centred triangles and targets against the edge-distance inequality; no
  violation occurred.  This numerical check is not used as proof.

The nearest-result comparison available under the imposed frozen-evidence
scope is the one in `problem.md`: the cited source covers the three-point
budget for at most four atoms, whereas this theorem treats a complete natural
five-label stratum and also proves literal attainment.  The result is not a
routine restatement of that layer; the exact segment reduction and weighted
triangle inequality do substantive work and can be reused in attacks on the
remaining direction patterns.  No claim of global literature priority is
certified here, because the primary paper itself is not among the frozen
evidence files.

## Verdict

**Accept**, at exactly the frozen `result-note` scope.  Correctness, attained
evidence, and nontrivial local contribution pass.  The original two-part
problem remains unresolved.
