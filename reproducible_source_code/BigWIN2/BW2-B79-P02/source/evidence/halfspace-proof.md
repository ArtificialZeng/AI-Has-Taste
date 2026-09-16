# Half-space counterexample: complete research proof

Provenance: `win-00079-p02-research-4421f0915749`  
Checked: 2026-09-09

## Proposition (exact frozen scope)

Let \(H\) be any infinite-dimensional complex Hilbert space, with no
separability assumption.  There is a point-ultraweakly closed convex cone
\(\mathsf K\subsetneq\mathsf{CP}^{\sigma}\) such that

\[
   \mathsf K_{Q,P}=\mathsf{CP}_{Q,P}
\]

for every pair of finite-rank orthogonal projections \(P,Q\) on \(H\).
Moreover, \(\mathsf K\) is not cut--pad stable.

This proposition disproves the frozen assertion in `source.md` under the
precise interpretation in `problem.md`.

## Construction

Fix a unit vector \(e\in H\), let

\[
 E=|e\rangle\langle e|,\qquad A=2E-I,
\]

For a unit vector \(z\), write \(\omega_z\) for its normal vector state.
Thus \(\omega_z(T)=\langle Tz,z\rangle\) under the convention in which the
inner product is linear in its first variable, and
\(\omega_z(T)=\langle z,Tz\rangle\) under the other convention.  This
notation prevents a complex-linearity ambiguity in the provisional formula
for \(\Theta_z\) in `source.md`.  For a normal map \(\Phi\), put

\[
 f(\Phi)=\omega_e(\Phi(A))=\operatorname{Tr}(E\Phi(A)).
\]

Define

\[
 \mathsf K=\{\Phi\in\mathsf{CP}^{\sigma}:f(\Phi)\leq 0\}.
\]

The inequality is meaningful because a positive map preserves adjoints, so
\(\Phi(A)\) is self-adjoint and \(f(\Phi)\in\mathbb R\) for every
\(\Phi\in\mathsf{CP}^{\sigma}\).  On these maps this is exactly the frozen
scalar \(\langle e,\Phi(A)e\rangle\), independently of which inner-product
convention is used.

## Normality and complete positivity of the auxiliary maps

For a unit vector \(z\in H\), define

\[
 \Theta_z(T)=\omega_z(T)E \quad(T\in\mathcal B(H)).
\]

This map is normal: for every trace-class \(S\),

\[
 \operatorname{Tr}(S\Theta_z(T))
   =\operatorname{Tr}(SE)\omega_z(T),
\]

which is an ultraweakly continuous functional of \(T\).  It is completely
positive at every matrix level.  Indeed, if
\([T_{ij}]\in M_n(\mathcal B(H))_+\), compression to the subspace
\(\{(c_1z,\ldots,c_nz):c_i\in\mathbb C\}\) shows that
\([\omega_z(T_{ij})]\in M_n(\mathbb C)_+\).  Consequently
\([\Theta_z(T_{ij})]=[\omega_z(T_{ij})]\otimes E\geq0\) on
\(\mathbb C^n\otimes H\).

Now fix finite-rank \(P,Q\) and
\(\psi\in\mathsf{CP}_{Q,P}\).  Regard the output of \(\psi\) as acting by
zero on \((QH)^\perp\), and define

\[
 \widehat\psi(T)=\psi(PTP)\in Q\mathcal B(H)Q.
\]

(Equivalently, this is the formula
\(Q\psi(PTP)Q\) in `source.md`.)  For every \(n\), positivity of
\([T_{ij}]\) implies positivity of its compression
\([PT_{ij}P]\) on \((PH)^n\); complete positivity of \(\psi\) then gives
\([\psi(PT_{ij}P)]\geq0\) on \((QH)^n\), and extension by zero preserves
positivity on \(H^n\).  Thus \(\widehat\psi\) is completely positive at
every matrix level.

It is also normal.  If \(T_\alpha\to T\) ultraweakly, every matrix entry of
\(PT_\alpha P\) on the finite-dimensional space \(PH\) converges.  Hence
\(PT_\alpha P\to PTP\) in the unique finite-dimensional linear topology;
applying the linear map \(\psi\) and then the fixed zero embedding into
\(\mathcal B(H)\) gives ultraweak convergence of the outputs.

## Point-ultraweak closedness and properness

First, \(\mathsf{CP}^{\sigma}\) is point-ultraweakly closed in the stated
ambient space of normal maps.  To see this directly, suppose a net
\(\Phi_\alpha\in\mathsf{CP}^{\sigma}\) converges point-ultraweakly to a
normal map \(\Phi\).  For \([T_{ij}]\in M_n(\mathcal B(H))_+\), entrywise
ultraweak convergence implies
\([\Phi_\alpha(T_{ij})]\to[\Phi(T_{ij})]\) ultraweakly in
\(\mathcal B(H^n)\): a trace-class block matrix has only finitely many
trace-class entries.  Every matrix on the left is positive, and the positive
cone of \(\mathcal B(H^n)\) is ultraweakly closed.  Thus
\([\Phi(T_{ij})]\geq0\) for every \(n\), so \(\Phi\) is completely positive.

The functional \(f\) is point-ultraweakly continuous because it evaluates
the map at the fixed operator \(A\) against the trace-class operator \(E\).
It follows (or follows directly by taking nets) that
\(\mathsf K=\mathsf{CP}^{\sigma}\cap\{f\leq0\}\) is point-ultraweakly
closed.  Linearity of \(f\), together with closure of
\(\mathsf{CP}^{\sigma}\) under addition and nonnegative scalar
multiplication, proves that \(\mathsf K\) is a convex cone.

It is a strict subcone.  The auxiliary map \(\Theta_e\) is normal and
completely positive by the calculation above, whereas

\[
 f(\Theta_e)=\omega_e(A)\omega_e(E)=1>0.
\]

Hence \(\Theta_e\in\mathsf{CP}^{\sigma}\setminus\mathsf K\).

## Equality of every finite corner cone

Fix arbitrary finite-rank \(P,Q\), including the possible zero projections.
If \(\Phi\in\mathsf K\), then its compression is completely positive, so

\[
 \mathsf K_{Q,P}\subseteq\mathsf{CP}_{Q,P}.
\]

Conversely, fix arbitrary \(\psi\in\mathsf{CP}_{Q,P}\) and form the normal
CP zero extension \(\widehat\psi\) above.  Since
\(\operatorname{ran}P+\mathbb Ce\) is finite-dimensional while \(H\) is
infinite-dimensional, choose a unit vector

\[
 v\perp(\operatorname{ran}P+\mathbb Ce).
\]

This uses no countability or separability.  For every
\(X\in P\mathcal B(H)P\), one has \(Xv=0\), whence
\((\Theta_v)_{Q,P}(X)=0\).  Also \(Ev=0\), so \(Av=-v\), and therefore

\[
 f(\Theta_v)=\omega_v(A)\omega_e(E)=-1.
\]

Because \(f(\widehat\psi)\) is real, set

\[
 t=\max\{0,f(\widehat\psi)\},\qquad
 \Phi=\widehat\psi+t\Theta_v.
\]

Then \(\Phi\) is normal and completely positive,

\[
 f(\Phi)=f(\widehat\psi)-t\leq0,
\]

and hence \(\Phi\in\mathsf K\).  On the prescribed corner,

\[
 \Phi_{Q,P}=\widehat\psi_{Q,P}+t(\Theta_v)_{Q,P}=\psi.
\]

Thus \(\mathsf{CP}_{Q,P}\subseteq\mathsf K_{Q,P}\).  Since \(P,Q\) and
\(\psi\) were arbitrary, equality holds for every finite corner.

## Explicit failure of cut--pad stability

Choose a unit vector \(u\perp e\), put
\(w=(e+u)/\sqrt2\), and take \(\Phi=\Theta_w\).  Since

\[
 \omega_w(A)=0,
\]

we have \(f(\Phi)=0\), so \(\Phi\in\mathsf K\).  For the rank-one pair
\(P=Q=E\), however, the source's cut--pad formula gives, for every
\(T\in\mathcal B(H)\),

\[
 \begin{aligned}
 \Phi^{(E,E)}(T)
 &=E\Theta_w(ETE)E\\
 &=\omega_w(ETE)E\\
 &=\tfrac12\omega_e(T)E
 =\tfrac12\Theta_e(T).
 \end{aligned}
\]

Consequently \(f(\Phi^{(E,E)})=1/2>0\), and
\(\Phi^{(E,E)}\notin\mathsf K\).  This is the required explicit failure of
cut--pad stability.

Finally, the excluded map \(\Theta_e\) has every finite compression in
\(\mathsf K_{Q,P}=\mathsf{CP}_{Q,P}\), but \(\Theta_e\notin\mathsf K\).
Thus the global cone is not reconstructed from its finite corner cones.

## Audit ledger

- Quantifiers: arbitrary infinite-dimensional complex \(H\); arbitrary
  finite-rank \(P,Q\); arbitrary \(\psi\in\mathsf{CP}_{Q,P}\).
- Exactness: all witnesses and identities are analytic; no numerical evidence
  is used.
- Convention check: every auxiliary rank-one map is defined using the
  complex-linear vector state \(\omega_z\); this removes the inner-product
  convention ambiguity in the provisional triage notation.
- Source match: Definition 3.1 and Remark 5.4 of arXiv:2609.04889v1 give the
  compression-image and cut--pad formulas used here.  Theorem 3.9 assumes
  cut--pad stability; Proposition 5.5 instead drops closedness.
- Current-source check: the official arXiv record inspected on 2026-09-09
  listed only v1 (submitted 2026-09-04).  Narrow exact/equivalent-language
  searches found no separate primary source for this complementary example.
  This is not a priority, novelty, or open-status claim.
- Literature handoffs: none were present.
- Known proof gaps: none identified in this research pass; fresh mathematical
  review is still required by the workflow.
