# Primary-source dependency map for the grade-six exclusion

## Frozen source artifact

- Matthew J. Colbrook, George Stepaniants, and Alex Townsend, *A Complete
  Resolution of Forsythe's Conjecture for Restarted Conjugate Gradients*,
  arXiv:2609.04659v1.
- Local evidence file:
  `evidence/Colbrook-Stepaniants-Townsend-2609.04659v1.pdf`.
- SHA-256:
  `a8eddb4d369949f3410bc711f657c06725fcbd4e6d8b20ff93a8ddced99244ee`.
- The PDF has 146 physical pages and is unencrypted. The relevant common-core
  material is on physical PDF pages 6--9 (printed pages 6--9).

This note is a locator and normalization audit. The PDF, rather than this
paraphrase, is the primary evidence.

## Hypotheses and conventions checked

Physical page 6 fixes arbitrary restart length \(s\geq1\), orthogonally reduces
a real symmetric positive-definite matrix to the distinct active eigenvalues
\(0<\lambda_1<\cdots<\lambda_N\), writes a normalized residual direction as
\(y=(\eta_i)\), and sets \(w_i=\eta_i^2\). For support larger than \(s\), it
defines the unique monic degree-\(s\) orthogonal polynomial \(P_w\) and
\(H(w)=\langle P_w,P_w\rangle_w>0\). Equation (G.5) gives the normalized
one-block map. Its signed factor is \((-1)^s\), hence is \(+1\) for the present
case \(s=4\). The same page states that block termination is equivalent to
active grade at most \(s\).

For a nonterminating orbit the source uses block-boundary index \(k\) and
defines

\[
 P_k=P_{w_k},\qquad H_k=H(w_k),\qquad q_k=P_kP_{k+1}.
\]

These are exactly the monic-polynomial, squared-weight, and block-index
conventions used in `evidence/grade6_exclusion.md`. The polynomial \(p_k\) in
`problem.md` instead has constant term one; it is the unnormalised-residual
factor \(P_k/P_k(0)\). No step of the grade-six dossier identifies these two
normalizations with one another.

## Exact imported results and their use

- Physical page 7, (G.7), is the signed two-block recurrence used to pass from
  polynomial products to signed residual directions.
- Physical page 7, (G.8)--(G.10), gives monotonicity and a positive finite limit
  for \(H_k\), summability of the energy increments, and summability (hence
  vanishing) of same-parity squared chords. The boundary argument uses the
  last conclusion to make each parity omega-limit set connected.
- Physical pages 8--9, Proposition 1.4, gives coefficientwise convergence
  \(P_{2n}\to P_e\), \(P_{2n+1}\to P_o\), and
  \(q_k\to q_\infty=P_eP_o\). It also states that every omega-limit state is
  fixed by the signed two-block map, has support between \(s+1\) and \(2s\),
  and is supported on nodes where \(q_\infty(\lambda_i)=h\).

At \(s=4\), these statements supply precisely the global-dynamics package
listed in the "Imported degree-independent facts" section of the grade-six
dossier: limiting parity factors, asymptotic same-parity regularity, and the
five-to-eight-node resonant support description. The new six-node
annihilator, drift, completion-functional, and sign-transport arguments are
not imported from this source.

## Scope check

A diagonal positive-definite matrix is a special case of the source's real
symmetric positive-definite hypothesis. Repeated diagonal entries and zero
initial spectral coordinates are handled by the source's active spectral
reduction, matching `problem.md`. The imported statements assume only that
the orbit never terminates; the grade-six proof separately handles finite
termination. Thus no extra simplicity, full-support-at-all-times, or
normalization hypothesis has been introduced through the citation.
