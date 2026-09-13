# Fresh mathematical referee report

**Review job:** `bigMac-00002-p11-referee-3950e4626323`  
**Frozen snapshot:** `5d159c2593246597489d9bf5267fcb50843d2c04bb2bebd51d7e0e61fb6e0ce5`  
**Candidate:** result-note, “Strict planar L2 Rogers-Shephard inequality for centrally symmetric hexagons”  
**Verdict:** **accept** at exactly the frozen scope. The original Conjecture 5 remains unresolved.

## Scope and integrity checks

I reviewed the immutable statement, its precise reading, `claim.json`, the
snapshot, and the snapshot-listed decisive proof, verifier, and bibliography
check. The SHA-256 values of all snapshot files agree with
`audit/snapshot.json`; for the prohibited progress summary `checkpoint.md`, I
checked only its hash and did not inspect its contents. In particular,
`source.md` still has SHA-256
`65c0c9c9aa70c5da4ba3bd2c5ccc71d7eab7d419ba7910a442578cd7ff22fec5`.

The frozen candidate is only the following subsidiary theorem: at (p=2), a
genuine centrally symmetric hexagon containing the origin cannot attain the
constant (2+\pi/2). It does not assert the original equality
classification for polygons with eight or more vertices, nonpolygons, or any
(p\ne2). Thus the stated `original_status: unresolved` is necessary and
correct.

## Reconstruction of the decisive argument

Write (K=a+S), where (S=-S). Since (0\in K), one has
(-a\in S), equivalently (a\in S). For (p=2), if
(M_a=2^{-1/2}(K\oplus_2(-K))), then

\[
h_{M_a}(u)^2=h_S(u)^2+\langle a,u\rangle^2,
\qquad |K\oplus_2(-K)|=2|M_a|.                 \tag{1}
\]

The translation family used in the second proof of Corollary 29 is a shadow
system, and that proof explicitly states that its Firey sum with its negative
has convex volume along every admissible translation segment. Hence
(F(a)=|(a+S)\oplus_2(-a-S)|) is convex on the polygon (S). A convex
function on a polygon is bounded above by its largest value at a vertex.
Because there are finitely many vertices, strictness at every vertex implies
strictness throughout (S); no strict-convexity assumption is being used.

Every genuine origin-symmetric hexagon is a three-generator zonotope. At any
chosen vertex, orient the three generators toward that vertex, choose the two
extreme generator rays as a basis, and apply a nonsingular linear map. The
body and chosen translation become

\[
S=[-e_1,e_1]+[-e_2,e_2]+[-d,d],\qquad
d=(r,s),\quad r,s>0,\qquad a=(1+r,1+s).         \tag{2}
\]

The strict inequalities are exactly what exclude a collapsed generator or a
parallelogram. The area is

\[
|S|=4(1+r+s).                                   \tag{3}
\]

Put (\alpha=\arctan(r/s)). On the half-circle
([ -\pi/2,\pi/2]), the successive support vertices of (S) are

\[
v_1=(1-r,-1-s),\quad v_2=(1+r,s-1),\quad a,
\]

on ([ -\pi/2,-\alpha]), ([ -\alpha,0]), and
([0,\pi/2]), respectively. On a cone with support vertex (v), writing
(g=h_{M_a}) and (Q_v=vv^T+aa^T), one has

\[
g^2=u^TQ_vu,qquad
g^2-g'^2={\det(Q_v)\over g^2}-(gg')'.           \tag{4}
\]

If (t=\tan\theta), (Q_v=(\begin{smallmatrix}A&E\\E&B\end{smallmatrix})),
and (\delta=|\det(v,a)|), direct differentiation gives the primitive

\[
\delta^2\int{d\theta\over g^2}
=\delta\arctan{Bt+E\over\delta}.               \tag{5}
\]

For (v_1), (\delta=2(1+s)) and (5) contributes
(2(1+s)(\pi/2-\alpha)). For (v_2),
(\delta=2(1+r)); its two arctangent arguments are
(s) and (z=(s^2-r)/((1+r)s)). Here

\[
{s-z\over1+sz}={r\over s},\qquad
1+sz={1+s^2\over1+r}>0,
\]

so the difference is on the correct branch and equals (\alpha). This cone
therefore contributes (2(1+r)\alpha). The last cone is rank one. The
endpoint terms from (4), including the switch jump at (-\alpha), sum to
(4(1+r+s)=|S|). Consequently

\[
|M_a|=|S|+\pi(1+s)+2(r-s)\arctan(r/s).          \tag{6}
\]

Combining (1), (3), and (6), half of the sharp-bound deficit is

\[
D(r,s)=\pi r-2(r-s)\arctan(r/s).                \tag{7}
\]

If (r\le s), then (D=\pi r+2(s-r)\alpha>0). If (r>s), then
(0<\alpha<\pi/2), whence
(D>\pi r-\pi(r-s)=\pi s>0). This proves strictness at every vertex
translation and, by the preceding convexity argument, for every allowed
origin location.

## Adversarial checks actually performed

- Checked the normal fan directly from
  (h_S(u)=|u_1|+|u_2|+|ru_1+su_2|); its switches are exactly
  (-\alpha) and (0) on the chosen half-circle.
- Recomputed both determinants, the arctangent branch condition, all endpoint
  terms, the factor of two in (1), and the area factor (1/2) in the planar
  support-function formula. They reproduce (6) and (7).
- Checked the edge cases (r=s), (r<s), and (r>s). Division by (s)
  is safe because a genuine hexagon has (s>0); limits (r=0) or (s=0)
  leave the six-vertex scope and correctly approach a lower-complexity case.
- Checked that interior, edge, and vertex placements of the origin are all
  covered by (a\in S) and translation convexity. Compactness is finite here,
  and no limiting passage from polygons to arbitrary bodies is claimed.
- Ran `evidence/verify_p2_hexagon.py`; all four independent quadratures agreed
  with (6) to at most (7.11\times10^{-15}), and all sampled exact-form
  deficits were positive. I also evaluated the unsplit formula using
  (h_S=|u_1|+|u_2|+|ru_1+su_2|) on six additional log-spaced random pairs;
  it agreed to the expected mesh error and found no sign failure. These are
  diagnostics only; acceptance rests on the exact reconstruction above.

## Source comparison and contribution

The primary source, Fradelizi--Manui--Meyer--Ndiaye,
[arXiv:2607.03582v1](https://arxiv.org/abs/2607.03582v1), states the exact
planar inequality in Corollary 29, states sufficiency of parallelograms with a
vertex at the origin, and poses necessity as Conjecture 5. Its second proof
also supplies the translation-shadow-system convexity used above. A fresh
targeted arXiv/web search on 2026-09-06 located that source, the authors'
separate paper arXiv:2606.07887 on equality in the *unrestricted* planar
inequality, and a formal-conjecture transcription, but no primary source with
this centrally symmetric six-vertex exclusion. This limited negative search
does not establish priority.

The nearest prior result is therefore Corollary 29. The precise delta is an
exact strict inequality for the first possible non-parallelogram centrally
symmetric polygon class at (p=2), uniform over every permitted origin
placement. The closed deficit (7) is more than a finite experiment or a
routine restatement of the source proof: that proof only reduces maximizers
to parallelograms and deliberately leaves equality propagation unresolved.
The result gives a concrete base case and formula for further equality or
stability analysis. It is narrow but mathematically nontrivial and coherent
enough for a short result-note.

No mathematical revision is required. Any manuscript must preserve this
scope, explicitly say that Conjecture 5 remains unresolved, cite the primary
source for the shadow-system input, and avoid claiming priority from the
negative search.
