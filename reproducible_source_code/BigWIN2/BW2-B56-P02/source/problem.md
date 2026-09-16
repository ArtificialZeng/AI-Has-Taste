# Precise reading: exact condition-number asymptotics in Sylvester Example 6

## Frozen data and notation

Let \(\delta\in(0,1]\),
\[
A=\operatorname{diag}(1,4,7),\qquad
B_\delta=\operatorname{diag}(10,1-\delta,20).
\]
Let \(E_{12}\in\mathbb R^{3\times3}\) have its sole nonzero entry, equal to one, in position \((1,2)\), and let \(\mathbf 1\) denote the \(3\times3\) all-ones matrix. Define
\[
C_1=I+E_{12},\quad C_2=\mathbf 1,\quad
C_3=\mathbf 1-E_{12},\quad C_4=I.
\]
For each \(i\in\{1,2,3,4\}\), \(X_i(\delta)\) is the unique real \(3\times3\) solution of
\[
AX_i-X_iB_\delta=C_i.
\]
Uniqueness holds throughout \((0,1]\): the spectra \(\{1,4,7\}\) and \(\{10,1-\delta,20\}\) are disjoint because \(1-\delta\in[0,1)\). Entrywise,
\[
(X_i)_{jk}=\frac{(C_i)_{jk}}{a_j-b_k},\qquad X_i=C_i\circ R_\delta,
\]
where
\[
R_\delta=
\begin{pmatrix}
-1/9&1/\delta&-1/19\\
-1/6&1/(3+\delta)&-1/16\\
-1/3&1/(6+\delta)&-1/13
\end{pmatrix}.
\]
Thus
\[
X_1=\begin{pmatrix}-1/9&1/\delta&0\\0&1/(3+\delta)&0\\0&0&-1/13\end{pmatrix},
\quad X_2=R_\delta,
\]
\[
X_3=\begin{pmatrix}-1/9&0&-1/19\\-1/6&1/(3+\delta)&-1/16\\-1/3&1/(6+\delta)&-1/13\end{pmatrix},
\quad
X_4=\operatorname{diag}\!\left(-1/9,1/(3+\delta),-1/13\right).
\]

For a real matrix \(M\) of rank \(r>0\), order its nonzero singular values as \(\sigma_1(M)\ge\cdots\ge\sigma_r(M)>0\) and use the paper's convention
\[
\kappa_2(M)=\frac{\sigma_1(M)}{\sigma_r(M)}.
\]
In fact all four matrices have rank three for every \(\delta\in(0,1]\). Direct exact expansion gives
\[
\det X_1=\det X_4=\frac1{117(\delta+3)},
\]
\[
\det X_2=\frac{5(\delta+9)(\delta+19)}{5928\,\delta(\delta+3)(\delta+6)},\qquad
\det X_3=-\frac{5(17\delta+115)}{11856(\delta+3)(\delta+6)},
\]
and none vanishes on the prescribed domain. Consequently \(\kappa_2(X_i)=\sigma_1(X_i)/\sigma_3(X_i)\) everywhere in scope; the rank-deficient convention is not activated.

## Required quantified result

For every \(i\in\{1,2,3,4\}\), determine an exponent \(p_i\in\mathbb R\) and an exact constant \(K_i>0\) such that
\[
\lim_{\delta\to0^+}\delta^{p_i}\kappa_2(X_i(\delta))=K_i,
\quad\text{equivalently}\quad
\kappa_2(X_i(\delta))\sim K_i\delta^{-p_i}.
\]
The constants must be exact algebraic numbers or exact formulas, not decimal fits. For the two cases identified numerically as bounded, \(i=3,4\), this includes determining the exact finite limits \(K_i=\lim_{\delta\to0^+}\kappa_2(X_i(\delta))\) (so \(p_i=0\) if the reported boundedness is proved).

Each asserted asymptotic must also have a rigorous remainder statement or explicit two-sided bounds. A rigorous remainder statement means, for example, explicit \(q_i>0\), \(M_i>0\), and \(\delta_i>0\) for which
\[
\left|\frac{\kappa_2(X_i(\delta))}{K_i\delta^{-p_i}}-1\right|
\le M_i\delta^{q_i}\qquad(0<\delta\le\delta_i),
\]
or an equally precise bound implying the displayed limit. Extending valid bounds to all \(\delta\in(0,1]\) is optional. A classification for arbitrary \(C\) is also optional and cannot replace proofs for these four fixed matrices.

## Prior result, status, and proposed delta

The relevant primary source is Massimiliano Fasi and Behnam Hashemi, *Conditioning of solutions to the Sylvester equation*, arXiv:2609.04050v1 (submitted 3 September 2026), <https://arxiv.org/abs/2609.04050>. Equation (2) defines the nonzero-singular-value convention, Proposition 1 gives the diagonal/Hadamard representation, and Example 6 on PDF page 21 tests 30 logarithmically spaced \(\delta\)-values in \([10^{-6},1]\). It reports only numerical orders \(\delta^{-2}\), \(\delta^{-1}\), bounded, bounded for \(C_1,C_2,C_3,C_4\), respectively; it supplies neither exact leading constants nor proofs or error bounds for those orders.

The source file's attribution of arXiv:2609.04050 to Froilán M. Dopico, Enrique S. Quintana-Ortí, and Paul Van Dooren is bibliographically incorrect. The arXiv record and the hash-matched local PDF identify Fasi and Hashemi. This correction does not alter the mathematical statement because the arXiv identifier, example, matrices, and local-PDF hash all identify the intended source unambiguously.

Triage status is **new-question**: the exact refinement is not presented by the paper as an open theorem, although it is a precise strengthening of its numerical observation. Searches of the exact assertion and equivalent Example 6 language on 2026-09-07 found no primary source beyond this paper; that limited search is not a claim of priority.

Nearest prior result \(X\): Example 6's four empirical orders. Proposed delta \(Y\): exact exponents and leading constants for all four fixed cases, with proofs and controlled errors. Verification route \(Z\): exact characteristic polynomials of \(X_i(\delta)^T X_i(\delta)\), scaled eigenvalue limits and exterior-power/minor identities, followed by exact or arbitrary-precision interval checks at rational held-out values. Numerical slopes alone are not proof.

