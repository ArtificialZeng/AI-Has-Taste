# Mathematical referee report

Job: `win-00079-p02-referee-83070b0bdb6b`  
Frozen snapshot: `11a066578b8a6d99a678be172a2d5271ff864cdd86f6e457d884db17ea9ba4f5`

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
infinite-dimensional complex Hilbert space \(H\), the displayed half-space
cone is a point-ultraweakly closed proper convex subcone of the normal
completely positive maps, has every finite corner equal to the full
corresponding completely positive cone, and is not cut--pad stable. The claim
therefore supplies the counterexample requested by the frozen original
problem, rather than a result about a restricted class of corners or Hilbert
spaces.

**Verdict: accept.** The proof is exact and covers the full quantified scope.

## Reconstruction of the decisive argument

Fix a unit vector \(e\), let \(E=|e\rangle\langle e|\), and set
\(A=2E-I\). For a unit vector \(z\), let \(\omega_z\) be its normal vector
state and define

\[
  \Theta_z(T)=\omega_z(T)E,
  \qquad
  f(\Phi)=\omega_e(\Phi(A)).
\]

The map \(\Theta_z\) is normal because, for every trace-class \(S\),
\(\operatorname{Tr}(S\Theta_z(T))=\operatorname{Tr}(SE)\omega_z(T)\).
It is completely positive: if \([T_{ij}]\geq0\), then compression to vectors
of the form \((c_i z)_i\) gives \([\omega_z(T_{ij})]\geq0\), and hence
\([\Theta_z(T_{ij})]=[\omega_z(T_{ij})]\otimes E\geq0\).

Consider

\[
  \mathsf K=\{\Phi\in\mathsf{CP}^{\sigma}:f(\Phi)\leq0\}.
\]

For a completely positive \(\Phi\), the operator \(\Phi(A)\) is
self-adjoint, so \(f(\Phi)\) is real. The functional \(f\) is
point-ultraweakly continuous: it is evaluation at the fixed operator \(A\)
followed by pairing with the trace-class operator \(E\). The cone
\(\mathsf{CP}^{\sigma}\) is point-ultraweakly closed in the stated ambient
space of normal maps. Indeed, at every matrix level an entrywise ultraweak
limit of positive block operators remains positive. Thus \(\mathsf K\) is a
point-ultraweakly closed convex cone. It is proper because

\[
  f(\Theta_e)=\omega_e(A)\omega_e(E)=1,
\]

so \(\Theta_e\in\mathsf{CP}^{\sigma}\setminus\mathsf K\).

Now fix arbitrary finite-rank projections \(P,Q\), and an arbitrary
\(\psi\in\mathsf{CP}_{Q,P}\). Extend \(\psi\) by zero via

\[
  \widehat\psi(T)=\psi(PTP),
\]

where its output acts on \(QH\) and is zero on \((QH)^\perp\). Compression by
\(P\), application of the finite-dimensional CP map \(\psi\), and the zero
embedding into \(\mathcal B(H)\) show directly that \(\widehat\psi\) is CP.
It is normal because \(T\mapsto PTP\) has finite-dimensional range and all
subsequent maps are continuous in the relevant finite-dimensional topology.

The subspace \(PH+\mathbb Ce\) is finite-dimensional. Since \(H\) is
infinite-dimensional, choose a unit vector
\(v\perp(PH+\mathbb Ce)\). For every \(X\in P\mathcal B(H)P\), one has
\(Xv=0\), so the \((Q,P)\)-corner of \(\Theta_v\) is zero. Also \(Ev=0\),
and therefore

\[
  f(\Theta_v)=\omega_v(A)\omega_e(E)=-1.
\]

Writing \(b=f(\widehat\psi)\in\mathbb R\), take
\(t=\max\{0,b\}\) and \(\Phi=\widehat\psi+t\Theta_v\). Then \(\Phi\) is
normal CP,

\[
  f(\Phi)=b-t\leq0,
  \qquad
  \Phi_{Q,P}=\psi.
\]

This proves \(\mathsf{CP}_{Q,P}\subseteq\mathsf K_{Q,P}\). The reverse
inclusion follows by compressing a CP map, so equality holds for every finite
pair \((Q,P)\).

Finally, choose a unit \(u\perp e\), set \(w=(e+u)/\sqrt2\), and let
\(\Phi=\Theta_w\). Since \(\omega_w(A)=0\), this map lies in \(\mathsf K\).
For \(P=Q=E\), however,

\[
  \Phi^{(E,E)}(T)
  =E\Theta_w(ETE)E
  =\tfrac12\omega_e(T)E
  =\tfrac12\Theta_e(T),
\]

and hence \(f(\Phi^{(E,E)})=1/2>0\). Thus \(\mathsf K\) is explicitly not
cut--pad stable.

## Checks and attacks performed

- I checked the quantifiers without assuming separability. The only dimension
  step is that the orthogonal complement of the finite-dimensional space
  \(PH+\mathbb Ce\) is nonzero.
- The zero-projection cases cause no exception: the relevant corner map is the
  unique zero map, while the same extension-and-perturbation construction
  remains valid.
- The vector state notation makes every auxiliary map complex-linear under
  either inner-product convention. All signs are fixed by \(Ae=e\) and
  \(Av=-v\) for \(v\perp e\).
- The perturbing vector is allowed to depend on the selected corner. Corner
  membership only requires a representative in \(\mathsf K\) for each corner;
  it does not require one representative to serve all corners simultaneously.
- Normality was checked separately for both auxiliary map types. Closedness is
  relative to the problem's declared ambient space of normal maps, so no
  unproved assertion that normality itself survives arbitrary pointwise limits
  is being used.
- There is no division, limiting exchange, compactness claim, numerical
  certificate, or equality case left implicit in the decisive construction.

## Source comparison and remaining gaps

I checked the cited local PDF at its frozen SHA-256 digest. Definition 3.1 gives
the compression and cut--pad formulas used above; Definition 3.3 makes
cut--pad stability a separate hypothesis. Theorem 3.9 requires convexity,
point-ultraweak closedness, and cut--pad stability for its converse
reconstruction statement. Remark 5.4 explicitly explains that the local
representatives may depend on the corner. Proposition 5.5 keeps cut--pad
stability and instead drops point-ultraweak closedness. The accepted example
keeps closedness and drops cut--pad stability, so it has exactly the
complementary scope claimed.

No priority, novelty, or open-status assertion is part of the frozen claim, and
none is needed for this mathematical verdict. I found no mathematical gap or
scope mismatch requiring revision.
