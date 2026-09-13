# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: every
finite simple 2-connected noncycle graph (G) of order (n) satisfies
(s^+(G)>n), so the equality class requested in `source.md` is empty.  This is
the full scope of the original classification problem, not a subsidiary or
finite-order claim.

All eight hashes in `audit/snapshot.json` match the current frozen files.  I
also recomputed the canonical SHA-256 digest of its `files` mapping and obtained
`3db9027967184b976645ce811287ded594b4bc772eb97bf04f0eed20b3676bf9`,
equal to the recorded snapshot digest.  The immutable source hash remains
`ed872b78b52d5cc0ddc57d8a49aaf786dbcf1e0b5091c4967d207fa60f97295a`.

## Reconstruction of the decisive argument

Let (A=P-N), where (P=A_+\succeq0), (N=A_-\succeq0), and
(PN=0).  For a triangle on vertex set (S), put (X=P[S]) and

\[
 \tau_v=P_{vv}^2+2\sum_{u\in S\setminus\{v\}}P_{vu}^2.
\]

Because (P-A=N\succeq0), its principal block gives

\[
 \mathbf 1^T X\mathbf 1\geq
 \mathbf 1^T A[S]\mathbf 1=6.
\]

Cauchy--Schwarz applied to the three numbers (P_{vv}) and the three
numbers (2P_{uv}) gives

\[
 (\mathbf 1^T X\mathbf 1)^2\leq 6\sum_{v\in S}\tau_v.
\]

Suppose every (v\in S) had

\[
 \mu_v(P)=P_{vv}^2+2\sum_{u\ne v}P_{vu}^2\leq2.
\]

Then (36\leq(\mathbf 1^TX\mathbf 1)^2\leq6\sum\tau_v\leq36), so
every inequality is equality.  Thus all six quantities used in
Cauchy--Schwarz equal (1), each (	au_v=mu_v(P)=2), and

\[
 X=\begin{pmatrix}1&1/2&1/2\\1/2&1&1/2\\1/2&1/2&1\end{pmatrix},
 \qquad P[S,V\setminus S]=0.
\]

The eigenvalues of (X) are (2,1/2,1/2), so (X) is invertible.  The
(S\)-by-(S) block of (PN=0) is therefore
(XN[S,S]=0), whence (N[S,S]=0).  But (N=P-A) has
(N_{vv}=P_{vv}-A_{vv}=1) on (S), a contradiction.  Hence every triangle
contains a vertex (v) with (mu_v(P)>2).  I checked that this step uses no
connectedness, no hidden induced-triangle hypothesis (three triangle vertices
induce (K_3) in a simple graph), and no limiting or division argument.

Now let (G) be 2-connected and not a cycle.  Then (n\geq4) and
(\Delta(G)\geq3).  If (G) has a triangle, choose the vertex above.
The definition of 2-connectivity makes (G-v) connected.  Theorem 2.1 and
Lemma 2.4 in the frozen Akbari--Hu--Liu PDF state, with the required
hypotheses and inequality directions,

\[
 s^+(G-v)\geq |V(G-v)|-1=n-2,
 \qquad
 s^+(G)\geq s^+(G-v)+\mu_v(P).
\]

Consequently (s^+(G)>n).  If (G) is triangle-free, a maximum-degree
vertex belongs to no triangle, and the strict clause of their Theorem 3.4
directly gives (s^+(G)>n).  These two cases exhaust the domain.  The proof
therefore establishes strictness for every graph quantified in the frozen
claim, and the requested equality class is indeed empty.

## Attacks and computational checks

- I checked the edge cases (n=3), degree two, zero adjacency eigenvalues,
  and disconnected graphs.  The first two are excluded by the quantified
  domain; zero eigenvalues do not affect either spectral part; the triangle
  lemma itself does not need connectedness.
- I examined all equality steps in the triangle lemma.  Equality in the two
  scalar bounds forces equality term-by-term, including vanishing of every
  outside-block entry of (P); thus the block use of (PN=0) omits no term.
- I reran `evidence/enumerate_n4_n8.py` in a fresh process.  Its output was
  byte-for-byte identical to the frozen JSON (SHA-256
  `fe2f26ccaf120205fb7fae21beb0932f42c146d75d236ea7ee66620836e22f82`):
  7,655 noncycle biconnected isomorphism classes through order 8, no equality
  candidate, and exact strict certificates for all ten recorded near-gap
  graphs.  This is corroboration only, not a proof of the all-orders claim.
- As a separate numerical falsification test, I computed (P=A_+) for every
  unlabeled graph through order 8 (13,598 graphs) and tested every triangle
  instance (97,680 instances).  None violated the strict triangle lemma; the
  smallest observed value of
  `max(mu_v(P) over the triangle) - 2` was approximately
  (0.222222222222217).  This floating-point test is not used in the proof.

## Source comparison and contribution

The frozen source PDF's Theorem 3.4 proves (s^+(G)\geq n) for the full
2-connected noncycle class and strictness only when a maximum-degree vertex
belongs to no triangle.  Its Corollary 3.2 supplies only the non-strict local
bound (mu_v(P)\geq2) on a triangle.  The audited spectral-orthogonality
argument rules out equality in that local bound for at least one vertex of
every triangle and thereby closes precisely the case left open by the source.
This is a substantive all-orders strengthening and resolves the frozen
classification rather than imposing a toy restriction.

The frozen literature screen is explicitly bounded and reports no equivalent
theorem in the inspected current primary sources.  I accept only the narrow
source-derived delta above; this audit makes no global novelty, priority, or
journal-acceptance claim.  No mathematical gap remains in the exact frozen
scope.

## Verdict

**ACCEPT.**  The frozen claim has the correct full scope, its proof is complete,
and the stated contribution relative to the frozen source is supported.
