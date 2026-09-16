# win-00071-p02 — The first stabilization kernel for the Horváth–Kania Motakis space

## Immutable primary-source record

- Primary source: Bence Horváth and Tomasz Kania, *Twisting exponential spectra*, arXiv:2609.05362v1 [math.FA], 4 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.05362v1>.
- Official PDF: <https://arxiv.org/pdf/2609.05362v1>.
- Relevant locations: Theorem 4.1, printed pp.7–9; Lemma 4.5, pp.9–10; Theorem 5.1, pp.10–11; component group and stabilization map, p.21; Lemma 7.1 and Proposition 7.3, pp.21–22; Calkin-order discussion, p.23; Question 9.1, p.26.
- Access record: official arXiv text and PDF were inspected on 2026-09-08. The PDF is archived as `bigWin-71-materials/2609.05362.pdf`, SHA256 `5e8416e39b443dd1976edf7353f9d1652decac39873975328f00c42e53d99886`.

## Frozen assertion

Let \(X\) be the complex Motakis realization over \(S^4\) used in Theorem 4.1 of the source, let \(E=X\oplus X\), and let \(S,T\in\mathcal B(E)\) be exactly the operators constructed in Theorem 5.1/Theorem A. Put
\[
\mathfrak I(A)=\operatorname{Inv}(A)/\operatorname{Inv}_0(A),
\qquad
s_A([u])=\left[\begin{pmatrix}u&0\\0&1\end{pmatrix}\right].
\]
Determine
\[
\ker\!\left(s_{\mathcal B(E)}:\mathfrak I(\mathcal B(E))
\longrightarrow\mathfrak I(M_2(\mathcal B(E)))\right),
\]
and determine the order of \([I_E-2ST]\).

The quantifiers are restricted to the exact \(X,E,S,T\) of the source. No assertion is made for arbitrary Motakis realizations or arbitrary lifts.

## Source result and proposed delta

The source proves that \([I_E-2ST]\) is nontrivial and is killed by the first stabilization. Its image in the relevant Calkin component group has order two, while the text says the upstairs order is unknown. Question 9.1 asks for both the full kernel and the order.

The proposed contribution is a complete answer to that exact question. During desktop screening the following candidate answer emerged, but it is not accepted evidence until independently proved:
\[
\mathfrak I(\mathcal B(E))\cong\mathbb Z/2,
\qquad
\mathfrak I(M_2(\mathcal B(E)))=1,
\]
and therefore
\[
\ker s_{\mathcal B(E)}=\{1,[I_E-2ST]\}\cong\mathbb Z/2,
\qquad \operatorname{ord}[I_E-2ST]=2.
\]

## Proof route requiring independent verification

Audit and, if valid, prove the general lemma: for a complex Banach space \(Y\) with a Schauder basis, the Calkin quotient \(q_Y:\mathcal B(Y)\to\mathcal Q(Y)\) induces an injection
\[
(q_Y)_*:\mathfrak I(\mathcal B(Y))\hookrightarrow\mathfrak I(\mathcal Q(Y)).
\]
The proposed proof must include explicit norm control for:

1. approximation of compact operators by finite-rank operators via the basis projections;
2. path connectedness of the invertible fiber \(I+\mathcal K(Y)\), reducing an invertible \(I+F\) to a finite-dimensional complex general linear group;
3. lifting a quotient path from \(q(v)\) to 1 by finitely many increments whose lifts have norm below 1, followed by the fiber path.

Then check from the source, without extrapolating its notation, that
\[
\mathcal Q(E)\cong C(S^4,M_2(\mathbb C)),\quad
\pi_4(GL_2(\mathbb C))\cong\mathbb Z/2,
\]
that \(I_E-2ST\) maps to the nonzero component, and that
\[
\mathcal Q(E^2)\cong C(S^4,M_4(\mathbb C)),\quad
\pi_4(GL_4(\mathbb C))=0.
\]

## Failure and novelty risks

- A quotient path need not admit a global arbitrary lift; the proposed small-increment construction must be written and checked, not cited vaguely.
- Verify the exact approximation property supplied by the Schauder basis and every matrix/Calkin identification.
- If a standard theorem already gives this component injection and the source's own hypotheses make Question 9.1 immediate, the mathematical answer can still be recorded, but publication value and literature novelty require a separate current search.
- Do not let the desktop candidate answer bias the fresh referee; freeze the proof and evidence before review.

## Semantic boundary

No registered project used arXiv:2609.05362, the component group \(\mathfrak I(\mathcal B(E))\), this stabilization map, or the Motakis realization over \(S^4\). Other stabilization entries concern unrelated finite-dimensional or combinatorial thresholds.
