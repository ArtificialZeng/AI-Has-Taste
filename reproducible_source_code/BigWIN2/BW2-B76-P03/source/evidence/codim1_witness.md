# Exact codimension-one witness

All calculations below use the bracket convention
\(\operatorname{ad}_B(X)=[B,X]\) from `source.md` and `problem.md`.

## General codimension-one elimination

Let \(\mathfrak h=V\oplus\mathbb Rz\), and suppose the displayed
complement \(\mathbb Rz\) satisfies
\(\kappa_{\mathbb Rz}|_V=0\). The latter condition says exactly that
\([z,V]\subseteq V\). Hence there are maps
\[
 [z,X]=DX,\qquad [X,Y]=C(X,Y)+a(X,Y)z
 \quad(X,Y\in V),
\]
where \(C:\Lambda^2V\to V\) and \(a\in\Lambda^2V^*\).

Every complement of \(V\) is uniquely
\(\mathfrak q_p=\mathbb Rw\), where \(w=z-p\) and \(p\in V\). Directly
rewriting brackets in the splitting \(V\oplus\mathbb Rw\) gives
\[
 \kappa_{\mathfrak q_p}(B)=-a(B,p)\quad(B\in V)
\]
and
\[
 \kappa_V^{\mathfrak q_p}(w)
 =\operatorname{tr}D-\operatorname{tr}(C_p),
 \qquad C_p(X)=C(p,X).
\]
Indeed, the remaining term in the projected map on \(V\) is
\(-a(p,\mathord\cdot)p\), whose trace is \(-a(p,p)=0\). Thus this is
an exact elimination of the all-complements quantifier.

## The Lie algebra and polarization

Take the real vector space with ordered basis
\((e_1,e_2,r,z)\), and define the only nonzero brackets, apart from
skew-symmetry, by
\[
 [e_1,e_2]=e_1+z,\qquad [e_1,r]=-r,\qquad [z,r]=r. \tag{1}
\]
The Jacobi sums for the four triples of distinct basis vectors are:
\[
\begin{array}{c|c}
(e_1,e_2,r)&[r,e_1+z]=r-r=0,\\
(e_1,e_2,z)&[z,e_1+z]=0,\\
(e_1,r,z)&[e_1,-r]+[z,-r]=r-r=0,\\
(e_2,r,z)&0.
\end{array}
\]
Alternation then covers every triple, so (1) defines a Lie algebra
\(\mathfrak h\).

Set \(V=\operatorname{span}(e_1,e_2,r)\). It Lie-generates
\(\mathfrak h\), since
\(z=[e_1,e_2]-e_1\). For the complement \(\mathfrak q=\mathbb Rz\),
all brackets \([B,z]\), \(B\in V\), lie in \(V\), so
\(\kappa_{\mathfrak q}|_V=0\).

## Exact obstruction for every complement

For this splitting,
\[
 a(e_1,e_2)=1,
 \quad D(e_1)=D(e_2)=0,
 \quad D(r)=r,
\]
and
\[
 C(e_1,e_2)=e_1,
 \qquad C(e_1,r)=-r,
 \qquad C(e_2,r)=0.
\]
Write an arbitrary graph parameter as
\(p=xe_1+ye_2+tr\). The vertical trace character on the basis of
\(V\) is
\[
 \bigl(\kappa_{\mathfrak q_p}(e_1),
       \kappa_{\mathfrak q_p}(e_2),
       \kappa_{\mathfrak q_p}(r)\bigr)=(-y,x,0). \tag{2}
\]
Also \(\operatorname{tr}D=1\) and
\(\operatorname{tr}C_p=-x-y\), so
\[
 \kappa_V^{\mathfrak q_p}(z-p)=1+x+y. \tag{3}
\]
A modularly balanced complement would make (2) vanish, forcing
\(x=y=0\), but then (3) equals \(1\). Hence no complement of this
same \(V\) is modularly balanced.

The exact verifier `evidence/verify_witness.py` independently constructs
the bracket tensor, checks all Jacobi sums, checks the generating rank,
and derives (2)--(3) by symbolic projection matrices.
