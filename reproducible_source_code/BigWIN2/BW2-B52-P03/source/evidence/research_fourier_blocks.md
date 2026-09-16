# Exact Fourier-block certificate for \((m,n)=(4,2)\)

Provenance: `win-00052-p03-research-fb952e179868`  
Date: 2026-09-07

This is an independent reconstruction of the exact observation in
`evidence/triage_exact_check.py`.  Run

```text
python3 evidence/research_fourier_blocks.py
```

to check the integer adjacency matrices, the exact Fourier intertwining
identities over the Gaussian integers, and both characteristic polynomials.

## Schreier blocks

Put \(\zeta=i\) and
\[
d_j=\zeta^j+\zeta^{-j}=2\cos(\pi j/2),\qquad
(d_0,d_1,d_2,d_3)=(2,0,-2,0).
\]
For a Fourier function \(F(a,p)=\zeta^{ja}f(p)\), the transition rules in
`problem.md` give, in the position order \((1,2)\), the exact block
\[
S_j=\begin{pmatrix}d_j&d_j\\d_j&2\end{pmatrix}.
\]
Indeed, from position 1 the two length-one reversals contribute \(d_j\) at
position 1 and the two length-two reversals contribute \(d_j\) at position
2.  From position 2 the length-one reversals give two loops and the
length-two reversals contribute \(d_j\) at position 1.  The four block
determinants are
\[
\det(xI-S_j)=x(x-4),\quad x(x-2),\quad x^2-8,\quad x(x-2).
\]
Thus
\[
\chi_{\rm Sch}(x)=x^3(x-4)(x-2)^2(x^2-8).
\]

## Cayley blocks

Represent a colored word by \((t,a,b)\), where \(t=0\) has label order
\((1,2)\), \(t=1\) has label order \((2,1)\), and \(a,b\) are the colors in
the first and second positions.  The four generators act by
\[
r_1^\varepsilon(t,a,b)=(t,a+\varepsilon,b),\qquad
r_2^\varepsilon(t,a,b)=(1-t,b+\varepsilon,a+\varepsilon).
\]
Let
\[
F_{s,k,l}(t,a,b)=\mathbf 1_{t=s}\zeta^{ka+lb}.
\]
The adjacency operator therefore satisfies the exact identity
\[
A_{\rm Cay}F_{s,k,l}
=d_kF_{s,k,l}+d_{k+l}F_{1-s,l,k},
\]
where subscripts are modulo 4.  Consequently the 16 mutually orthogonal
spaces
\[
W_{k,l}=\operatorname{span}\{F_{0,k,l},F_{1,l,k}\},
\qquad (k,l)\in\mathbb Z_4^2,
\]
exhaust the 32-dimensional function space and have blocks
\[
B_{k,l}=\begin{pmatrix}d_k&d_{k+l}\\d_{k+l}&d_l\end{pmatrix}.
\]
The exact determinant table, with rows \(k=0,1,2,3\) and columns
\(l=0,1,2,3\), is
\[
\begin{array}{c|cccc}
 &0&1&2&3\\ \hline
0&x(x-4)&x(x-2)&x^2-8&x(x-2)\\
1&x(x-2)&(x-2)(x+2)&x(x+2)&(x-2)(x+2)\\
2&x^2-8&x(x+2)&x(x+4)&x(x+2)\\
3&x(x-2)&(x-2)(x+2)&x(x+2)&(x-2)(x+2)
\end{array}
\]
and multiplication gives
\[
\chi_{\rm Cay}(x)
=x^{10}(x-4)(x-2)^8(x+2)^8(x+4)(x^2-8)^2.
\]
This also proves that the generator rules specify a symmetric matrix with
constant row sum 4; the script checks those facts directly and verifies the
Fourier identities \(AU=U\bigoplus B_{k,l}\) and
\(A_{\rm Sch}V=V\bigoplus S_j\) entry by entry.

## Exact ordering and gaps

The Cayley spectrum, in decreasing order by distinct values, is
\[
4>2\sqrt2>2>0>-2>-2\sqrt2>-4,
\]
and the Schreier spectrum has the same top three distinct values.  The
ordering uses only \(1<\sqrt2<2\), obtained by squaring positive numbers.
Hence each second adjacency eigenvalue is \(2\sqrt2\), and
\[
\boxed{\psi_{4,2}=\beta_{4,2}=4-2\sqrt2}.
\]

As a nonessential cross-check, the primary source's Corollary 3.2 gives
\(\min\{\psi_{4,1},\beta_{4,2}\}\leq\psi_{4,2}\leq\beta_{4,2}\).
Here \(P(4,1)=C_4\) has \(\psi_{4,1}=2\), while
\(4-2\sqrt2<2\).  The squeeze therefore reproduces the Cayley equality from
the independently computed Schreier gap.

## Scope

This proves only the frozen fixed cell \((m,n)=(4,2)\).  It does not prove
Conjecture 5.1 for any other parameters, nor does it establish bibliographic
priority.  The copied primary source is
`evidence/external/2608.15398.pdf` (SHA-256
`49cf3770084b724debc4cf4cb29403ed23f14fb9b102a10344e7a48bc0fcdb79`).
