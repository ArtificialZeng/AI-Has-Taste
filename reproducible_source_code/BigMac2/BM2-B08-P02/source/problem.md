# Precise problem statement

## Frozen source and interpretation

The immutable statement is in `source.md` (SHA-256
`93dae429fcc298c6e538247a4cdaa8e4d6dbaddc20ed8cb4bc7fe60f9cc8d088`).
The conventions below are those of the cited local copy of
Tamura--Yamagami, *Hadamard Rigidity of Positive Sojourn Time Distributions
for Rotation Coins*, arXiv:2609.05033v1 (PDF SHA-256
`5703bbf648949e50aa49140adece707fa4b8dda128f1d4b850569fa01c495193`).

Fix
\[
 \phi_* = 2^{-1/2}(1,i)^T\in\mathbb C^2
\]
and an arbitrary coin
\[
 U=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in U(2).
\]
Decompose it, with the chirality basis and spatial labels held fixed, as
\[
 P=\begin{pmatrix}a&b\\0&0\end{pmatrix},\qquad
 Q=\begin{pmatrix}0&0\\c&d\end{pmatrix}.
\]
Here `P` is a step to the left and `Q` a step to the right. Matrix products
act from right to left.

For a length-\(n\) step sequence
\(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_n)\in\{-1,+1\}^n\), put
\[
 x_0=0,\qquad x_j=\sum_{r=1}^j\varepsilon_r,
 \qquad M_{-1}=P,\quad M_{+1}=Q,
\]
and
\[
 A_U(\varepsilon)=M_{\varepsilon_n}\cdots M_{\varepsilon_1}.
\]
The positive-sojourn count is Konno's interval count
\[
 K(\varepsilon)=\sum_{j=0}^{n-1}
 \mathbf 1\{x_j>0\ \text{or}\ (x_j=0\ \text{and}\
 \varepsilon_{j+1}=+1)\}.
\]
Thus an interval beginning at the origin is assigned according to the next
step; this is not the count of the indices for which \(x_j>0\).

For \(0\leq k\leq n\), coherently sum all amplitudes having the same return
and sojourn outcome:
\[
 \Gamma_n(k;U)=
 \sum_{\substack{\varepsilon\in\{-1,+1\}^n\\x_n=0\\K(\varepsilon)=k}}
 A_U(\varepsilon),
 \qquad
 w_n(k;U)=\|\Gamma_n(k;U)\phi_*\|_2^2.
\]
Let
\[
 R_n(U)=\sum_{j=0}^n w_n(j;U).
\]
Only when \(R_n(U)>0\) is the return-conditioned distribution defined, by
\[
 \mu_n(k;U)=\frac{w_n(k;U)}{R_n(U)}.
\]

## Classification target and quantifiers

Determine exactly the set
\[
 \mathcal S=\left\{U\in U(2):R_8(U)>0,\quad
 \mu_8(k;U)=
 \begin{cases}
 1/3,&k\in\{2,4,6\},\\
 0,&k\in\{0,1,3,5,7,8\}
 \end{cases}\right\}.
\]
Equivalently, determine all \(U\in U(2)\) for which there is a real
\(q>0\) such that
\[
 w_8(2;U)=w_8(4;U)=w_8(6;U)=q
\]
and \(w_8(k;U)=0\) for every other \(k\in\{0,\ldots,8\}\). Any parameter
faces with \(R_8(U)=0\) must be identified but are excluded from
\(\mathcal S\); conditional probabilities must not be assigned there.
The answer must cover all of \(U(2)\), including coins with zero entries and
other degenerate parameter faces, rather than only a generic chart.

Let
\[
 H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
The cited paper proves that, for every diagonal unitary \(D\), left
multiplication \(U\mapsto DU\) multiplies every length-\(n\) return amplitude
by one common phase and hence preserves all \(w_n(k)\) and \(\mu_n(k)\).
Global phase is the special case \(D=e^{i\eta}I\), although it is retained in
the wording to match the source. Accordingly, the proved restricted
Hadamard-type orbit is
\[
 \mathcal H_{\rm left}=\{DH:D\text{ is diagonal unitary}\}.
\]

Raw classification of \(\mathcal S\) comes before quotienting. No right
diagonal multiplication, conjugation, arbitrary change of coin basis, or
swap of left/right labels is presumed to be an equivalence: these operations
can change the fixed vector \(\phi_*\), the chirality projectors, or the
positive-side statistic. A further proposed basis/geometry map may be used in
the quotient only after a pathwise or unitary calculation proves that it
preserves this fixed experiment (in particular, with \(\phi_*\), `P/Q`, the
positive half-line, and the reported \(k\)-labels fixed). Determining any such
additional admissible equivalences is part of the requested classification.
The final question is whether every equivalence class in \(\mathcal S\) meets
\(\mathcal H_{\rm left}\); if not, one must give an exact non-Hadamard family
and the complete corrected classification.

## Nearest prior result and proposed delta

The inspected primary PDF gives the walk and conditional distribution on
pp. 3--4; proves global-phase and left-diagonal invariance in Lemmas 3.1--3.2
on pp. 5--6; and proves in Definition 3.1 and Theorem 3.1 on pp. 13--14 that,
for
\[
 U(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\
 \sin\theta&-\cos\theta\end{pmatrix},\qquad 0<\theta<\pi/2,
\]
the stated time-eight law holds exactly if \(\theta=\pi/4\). Section 5
(pp. 16--17) explicitly proposes extension to general two-state unitary
coins while accounting for equivalences and the fixed initial state.

Thus the proposed delta is the exact extension from the one-real-parameter
rotation family to all of \(U(2)\), with degenerate/zero-return branches and
only proved experiment-preserving equivalences. A bounded verification route
is to enumerate the 70 return paths at time eight exactly, parameterize
\(U(2)\) on complete charts modulo the proved left-diagonal action, factor the
equal-weight and zero-weight equations, and certify every real branch plus
the excluded \(R_8=0\) locus. The first discriminating test is to derive and
factor these exact time-eight weights in a complete two-parameter normal form
and compare the resulting branches with \(\mathcal H_{\rm left}\).

## Scope/status at intake

The original general-\(U(2)\) classification is unresolved here. The cited
paper supports it as a future problem but proves only the rotation subfamily.
No novelty or completeness claim beyond that inspected boundary is made at
triage.
