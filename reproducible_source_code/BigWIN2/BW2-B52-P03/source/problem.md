# Precise problem — the \((m,n)=(4,2)\) spectral-gap cell

## Frozen task and scope

The immutable statement is in `source.md`. The task has no free parameter: it concerns only \(m=4\) and \(n=2\). It asks for exact values of two unnormalized adjacency spectral gaps and an exact decision of their equality. It does **not** ask for the conjecture for other \((m,n)\).

## Objects and conventions

Write \(\mathbb Z_4=\mathbb Z/4\mathbb Z\). A vertex of
\[
S(4,2)=\mathbb Z_4\wr S_2
\]
is represented as a colored one-line word
\[
x=((\ell_1,a_1),(\ell_2,a_2)),
\]
where \((\ell_1,\ell_2)\) is a permutation of \((1,2)\) and \(a_1,a_2\in\mathbb Z_4\). Thus \(|S(4,2)|=2!\,4^2=32\).

For \(i\in\{1,2\}\) and \(\varepsilon\in\{-1,+1\}\), the generalized prefix reversal \(r_i^\varepsilon\) reverses the first \(i\) positions and adds \(\varepsilon\pmod 4\) to the color of every entry in that prefix. Put
\[
R(4,2)=\{r_1^-,r_1^+,r_2^-,r_2^+\}.
\]
These four maps are distinct, and \((r_i^+)^{-1}=r_i^-\), so the generator-sum adjacency operator is real symmetric and has row sum \(4\).

Let \(A_{\rm Cay}\) be the \(32\times32\) integer matrix indexed by the colored words above, with
\[
A_{\rm Cay}(x,y)=\#\{r\in R(4,2):r(x)=y\}.
\]
The full graph is \(P(4,2)=\operatorname{Cay}(S(4,2),R(4,2))\).

For the color-position Schreier action, let
\[
X=\mathbb Z_4\times\{1,2\}.
\]
A state \((a,p)\) records the color and position of a fixed distinguished label. The action is
\[
r_i^\varepsilon(a,p)=
\begin{cases}
(a+\varepsilon,\,i+1-p),&p\le i,\\
(a,p),&p>i,
\end{cases}
\]
with color arithmetic modulo \(4\). Let \(A_{\rm Sch}\) be the \(8\times8\) generator-sum matrix
\[
A_{\rm Sch}(u,v)=\#\{r\in R(4,2):r(u)=v\}.
\]
It is a Schreier multigraph adjacency matrix: a generator fixing a state contributes \(1\) to the corresponding diagonal entry. Every row therefore sums to \(4\).

For a real symmetric matrix \(A\), list eigenvalues with multiplicity as \(\lambda_1(A)\ge\lambda_2(A)\ge\cdots\). Define
\[
\psi_{4,2}=4-\lambda_2(A_{\rm Cay}),\qquad
\beta_{4,2}=4-\lambda_2(A_{\rm Sch}).
\]
The required claim is to determine both algebraic numbers exactly and prove or disprove
\[
\psi_{4,2}=\beta_{4,2}.
\]

An acceptable certificate must specify the matrices (or exact representation blocks), give exact characteristic or minimal factors that identify the second eigenvalues, and justify their ordering without relying only on decimal approximations.

## Prior result and proposed delta

The closest verified result is Saúl A. Blanco, *On the Laplacian spectral gap of generalized pancake graphs*, arXiv:2608.15398v1 (retrieved 2026-09-07). Section 2 defines the generators and Schreier convention; Corollary 3.2 gives the general squeeze
\[
\min\{\psi_{m,n-1},\beta_{m,n}\}\le \psi_{m,n}\le\beta_{m,n};
\]
Example 4.7 evaluates \((m,n)=(3,2)\); and Section 5 states that equality was then open in general. The current arXiv record is v2 dated 2026-09-03 and its abstract reports a counterexample to the unrestricted equality conjecture. No exact \((4,2)\) evaluation was found in the inspected primary records on 2026-09-07.

The bibliographic line in `source.md` misattributes arXiv:2608.15398 to Arindam Biswas; the arXiv record and paper list Saúl A. Blanco. This metadata error does not change the precise fixed-cell question above. The local PDF path named in `source.md` is not present inside this project, so its stated hash was not rechecked in this job.

Target contribution: nearest prior result = the squeeze and the \((3,2)\) worked example; proposed delta = an exact \((4,2)\) certificate; verification route = independently construct both integer adjacency matrices, factor their characteristic polynomials exactly, and prove the second-eigenvalue ordering (also checking the squeeze against the elementary \(n=1\) gap).

