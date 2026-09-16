# Triage evidence

Provenance: `win-00079-p02-triage-426731f718a2`  
Inspection date: 2026-09-09

## Immutable input and handoffs

- `source.md` had SHA-256 (identical before and after triage)
  `50d4f6c867198e9386f01791d6d68e230eaa0c3f673014b91a4193b773adda26`
  before triage.
- No `literature/` directory, hence no `literature/*handoff*.md`, was present.

## Primary-source and literature check

The official arXiv abstract and HTML for
<https://arxiv.org/abs/2609.04889> and
<https://arxiv.org/html/2609.04889v1> were inspected live.  The arXiv record
lists only v1, submitted 2026-09-04.  The inspected locations were:

- Definition 3.1 (HTML lines 110--128): compression and cut--pad formulas;
- Definition 3.3 (lines 129--143): cut--pad stable convex cones and
  point-ultraweak closedness;
- Theorem 3.9 (lines 235--250): reconstruction under both hypotheses;
- Theorem 4.1 (lines 455--475): corner bipolar/separation under both
  hypotheses;
- Example 5.1 (lines 516--560): normal CP maps are closed and cut--pad stable,
  with every finite CP corner characterized by Choi positivity;
- Remark 5.4 and Proposition 5.5 (lines 751--809): compression-image notation
  and the failure caused by dropping closedness while retaining cut--pad
  stability.

Exact and equivalent-language web searches for “same finite-corner cones,”
“finite corner cones point-ultraweakly closed,” “finite-corner reconstruction
normal maps counterexample,” and “cut-pad stable cones normal maps” returned
the source paper but no distinct primary paper settling the complementary
closed/non-cut--pad case.  This narrow check is not proof of novelty or open
status.  The source itself does not state the target as open, so its intake
status is `new-question`, with priority unverified.

## Cheapest exact screening of the proposed cone

Fix a unit vector \(e\), let \(E=|e\rangle\langle e|\), \(A=2E-I\), and put

\[
f(\Phi)=\langle e,\Phi(A)e\rangle,\qquad
\mathsf K=\{\Phi\in\mathsf{CP}^{\sigma}:f(\Phi)\leq0\}.
\]

The value of \(f\) is real on CP maps.  The following identities survived the
triage check.

1. `Closed cone`: \(f\) is point-ultraweakly continuous, so \(\mathsf K\) is
   the intersection of the point-ultraweakly closed CP cone with a closed
   homogeneous half-space.  This also gives convexity.
2. `Strictness`: for
   \(\Theta_e(T)=\langle e,Te\rangle E\), one has
   \(f(\Theta_e)=1\), so \(\Theta_e\in\mathsf{CP}^{\sigma}\setminus\mathsf K\).
3. `All finite corners`: fix finite-rank \(P,Q\) and
   \(\psi\in\mathsf{CP}_{Q,P}\).  Its zero extension
   \(\widehat\psi(T)=Q\psi(PTP)Q\) is normal CP.  Choose a unit
   \(v\perp(\operatorname{ran}P+\mathbb Ce)\), possible because \(H\) is
   infinite-dimensional, and set
   \(\Theta_v(T)=\langle v,Tv\rangle E\).  Then
   \((\Theta_v)_{Q,P}=0\) and
   \(f(\Theta_v)=\langle v,Av\rangle=-1\).  Hence, with
   \(t=\max\{0,f(\widehat\psi)\}\),
   \(\widehat\psi+t\Theta_v\in\mathsf K\) and its \((Q,P)\)-corner is
   \(\psi\).  The reverse corner inclusion follows from
   \(\mathsf K\subseteq\mathsf{CP}^{\sigma}\).
4. `Explicit cut--pad failure`: take a unit \(u\perp e\),
   \(w=(e+u)/\sqrt2\), and \(\Phi=\Theta_w\).  Then
   \(f(\Phi)=\langle w,Aw\rangle=0\), so \(\Phi\in\mathsf K\).  For
   \(P=Q=E\), however,
   \(f(\Phi^{(E,E)})=\langle w,Ew\rangle=1/2>0\), so the cut--pad map is not
   in \(\mathsf K\).

Normality and complete positivity of the scalar-output maps and of the zero
extension still require a fully written proof rather than reliance on these
screening labels.  No mathematical acceptance is asserted at triage.
