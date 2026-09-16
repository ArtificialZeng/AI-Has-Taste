# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the frozen `resolution-paper` claim that, for the single cell
\((m,n)=(4,2)\), both specified generator-sum adjacency operators have second
eigenvalue \(2\sqrt2\), hence
\(\psi_{4,2}=\beta_{4,2}=4-2\sqrt2\). This is exactly the full scope of the
original fixed-cell question, rather than a subsidiary or weakened claim.

All files named in `audit/snapshot.json` have the recorded SHA-256 digests. I
also recomputed the canonical hash of its `files` mapping and obtained the
declared snapshot digest
`edbdc4da6f0d9402df1a061830f441c960f1ba9e24b5c26c03746e09d4de6b5f`.

## Reconstruction of the decisive argument

For the Cayley operator, encode a colored word as \((t,a,b)\), where
\(t\in\{0,1\}\) is its label order and \(a,b\in\mathbb Z_4\) are its positional
colors. Directly from the frozen generator rule,
\[
 r_1^\varepsilon(t,a,b)=(t,a+\varepsilon,b),\qquad
 r_2^\varepsilon(t,a,b)=(1-t,b+\varepsilon,a+\varepsilon).
\]
Thus these coordinates enumerate all \(2\cdot4^2=32\) vertices. Put
\(\zeta=i\), \(d_j=\zeta^j+\zeta^{-j}\), so
\((d_0,d_1,d_2,d_3)=(2,0,-2,0)\), and define
\[
 F_{s,k,l}(t,a,b)={\bf1}_{t=s}\zeta^{ka+lb}.
\]
Applying the four transitions to this function gives, with indices modulo
four,
\[
 A_{\rm Cay}F_{s,k,l}
   =d_kF_{s,k,l}+d_{k+l}F_{1-s,l,k}.
\]
Consequently each
\(W_{k,l}=\operatorname{span}\{F_{0,k,l},F_{1,l,k}\}\) is invariant and has
the exact block
\[
 B_{k,l}=\begin{pmatrix}d_k&d_{k+l}\\d_{k+l}&d_l\end{pmatrix}.
\]
The sixteen spaces are mutually orthogonal and exhaustive: their first basis
vectors give every Fourier character on the \(t=0\) slice exactly once, and
their second basis vectors do the same on the \(t=1\) slice. Hence the blocks
account for all 32 eigenvalues, with no missing representation.

Enumerating \(k,l\in\mathbb Z_4\) using the four exact values of \(d_j\) gives
\[
 \chi_{\rm Cay}(x)=
 x^{10}(x-4)(x-2)^8(x+2)^8(x+4)(x^2-8)^2.
\]

For the Schreier operator, the frozen action on \((a,p)\in\mathbb Z_4\times
\{1,2\}\) gives directly
\[
 (A_{\rm Sch}f)(a,1)=\sum_{\varepsilon=\pm1}
       \bigl(f(a+\varepsilon,1)+f(a+\varepsilon,2)\bigr),
\]
\[
 (A_{\rm Sch}f)(a,2)=2f(a,2)+
       \sum_{\varepsilon=\pm1}f(a+\varepsilon,1).
\]
On color Fourier mode \(j\), this is the exact block
\[
 S_j=\begin{pmatrix}d_j&d_j\\d_j&2\end{pmatrix}.
\]
The four modes exhaust the eight-dimensional space, and their determinant
factors yield
\[
 \chi_{\rm Sch}(x)=x^3(x-4)(x-2)^2(x^2-8).
\]

It follows, including multiplicities, that the top of the Cayley spectrum is
\(4,2\sqrt2,2\) (with \(2\sqrt2\) occurring twice), while the top of the
Schreier spectrum is also \(4,2\sqrt2,2\). The exact inequalities
\(4>2\sqrt2>2\) follow from \(1<\sqrt2<2\). Therefore in both cases
\(\lambda_2=2\sqrt2\), and subtracting from the common generator degree four
proves the claimed equality and exact gap.

## Adversarial checks actually performed

- I checked the four generators are distinct for \(m=4\), the \(+\) and \(-\)
  maps are inverse pairs, and both integer matrices are symmetric with row sum
  four. The two loops at a Schreier state with position two are correctly
  counted separately; there are no Cayley loops.
- The source's operator uses inverse action on functions, while the displayed
  reconstruction uses forward transitions. This causes no discrepancy because
  the generator set is inverse-closed.
- I checked block exhaustiveness, characteristic-polynomial degrees and root
  multiplicities. In particular, eigenvalue four is simple in each polynomial,
  so the root \(2\sqrt2\) really is the second eigenvalue rather than merely a
  listed spectral value.
- I executed both snapshotted exact scripts successfully. One checks the
  Gaussian-integer Fourier intertwining identities entry by entry and compares
  the block product with the direct 32-by-32 and 8-by-8 characteristic
  polynomials; the other independently enumerates colored-word transitions and
  obtains the same polynomials. No floating-point eigenvalues are used.
- There are no free parameters, empty domains, limiting operations, divisions,
  or imported lemmas on which the proof could fail. The optional semi-recursive
  squeeze is not needed for the conclusion.

## Source comparison and contribution

The snapshotted primary PDF has SHA-256
`49cf3770084b724debc4cf4cb29403ed23f14fb9b102a10344e7a48bc0fcdb79`
and identifies the author as Saúl A. Blanco, correcting the author metadata in
`source.md`. Its definitions confirm the four prefix reversals, the
inverse-closed convention, the color-position action, and generator-counting
loops. Corollary 3.2 gives the cited squeeze; Example 4.7 treats \((3,2)\); and
Conjecture 5.1 predicts equality for \(2\le m\le5\), \(n\ge2\). The paper does
not state an exact \((4,2)\) evaluation. The frozen candidate supplies exactly
that missing full-scope certificate and expressly makes no bibliographic
priority claim. The metadata correction has no mathematical effect.

## Verdict

**Accept.** The frozen claim matches the original scope, its exact proof is
complete, the matrices and representation blocks are specified and exhaustive,
and the exact ordering establishes both second eigenvalues. I found no
unresolved mathematical or scope gap.
