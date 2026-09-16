# Gale-dual reduction and an exact frozen-extension obstruction

This note records a structural result from research pass 2. It does **not**
resolve the unbounded problem. All vector spaces below have characteristic
zero, and \(xy\) denotes the symmetric product \(x\odot y\).

## 1. Exact dual formulation

Put \(d=n-1-a\), work over a characteristic-zero field \(K\), and let
\(p\colon[n]\to K^d\) affinely span. If
\(Z\) is an \(n\times a\) Gale matrix for \(p\), with rows
\(z_1,\ldots,z_n\), then the stress matrices of the complete framework are
precisely

\[
                 Z\Psi Z^{\mathsf T},\qquad \Psi\in\operatorname{Sym}_a.
\]

For an edge \(ij\), restriction of this stress to that coordinate is, up to
the harmless stress-sign convention, \(z_i^{\mathsf T}\Psi z_j\). Linear
algebra therefore gives the following criterion:

> If \(D\subseteq E(K_n)\), then deleting \(D\) from \(K_n\) preserves
> full generic \(d\)-rigidity exactly when the tensors
> \(\{z_i z_j:ij\in D\}\) are generically linearly independent in
> \(\operatorname{Sym}^2(K^a)\).

Indeed, the remaining rigidity rows span the complete-graph rigidity row
space iff projection of the complete-graph stress kernel onto the coordinates
in \(D\) is onto. Under the displayed parametrisation, the transpose of that
projection has columns \(z_i z_j\). This is also the standard duality between
the contracted generic rigidity matroid and the symmetric-power matroid.

For the frozen problem, \(D=sC_3\sqcup tC_4\), \(|D|=n\), and the Maxwell
condition is exactly

\[
n\leq\dim\operatorname{Sym}^2(\mathbb Q^a)=a(a+1)/2.
\]

Thus the remaining universal kernel is

\[
 \{z_i z_j:ij\in sC_3\sqcup tC_4\}\text{ is generically independent
 whenever }3s+4t\leq a(a+1)/2.
\]

## 2. A frozen certificate need not extend

Let \(U=\langle e_1,e_2,e_3\rangle\subset V=\mathbb Q^4\). Place the first
two triangle components at

\[
(e_1,e_2,e_3),\qquad
(e_1+e_2,e_2+e_3,e_3+e_1).
\]

The first triangle gives \(e_1e_2,e_2e_3,e_1e_3\). Modulo their span, the
three products from the second triangle give respectively
\(e_2^2,e_3^2,e_1^2\). Hence these six tensors form a basis of
\(W=\operatorname{Sym}^2 U\).

No placement of one further four-cycle can extend these frozen six tensors to
a basis of \(\operatorname{Sym}^2V\). To see this, for four proposed cycle
vectors \(x_1,x_2,x_3,x_4\in V\), put

\[
A=\langle x_1,x_3\rangle,\qquad B=\langle x_2,x_4\rangle.
\]

If either space has dimension less than two, the four cycle products are
already dependent. Otherwise, since \(U\) is a hyperplane, choose nonzero
\(\alpha\in A\cap U\) and \(\beta\in B\cap U\). The nonzero tensor
\(\alpha\beta\) is both a linear combination of

\[
x_1x_2,\ x_2x_3,\ x_3x_4,\ x_4x_1
\]

and an element of \(\operatorname{Sym}^2U=W\). Thus the new
four-dimensional cycle span (if it is four-dimensional) intersects the
frozen old span, and the ten tensors cannot be independent.

This is an exact obstruction to the strong *placement-preserving* extension
lemma. It is not a counterexample to the graph claim: the obstruction is to
this certificate, not to every placement.

## 3. Exact basis exchange in the first obstructed case

For vertex order \(C_3(0,1,2),C_3(3,4,5),C_4(6,7,8,9)\), the following rows
of \(\mathbb Z^4\) give a replacement placement:

```text
( 2,-1, 1,-2)  (-1, 2, 2, 0)  ( 1, 0, 2, 2)
( 0,-1, 1, 1)  ( 0, 1, 0,-2)  (-2,-1,-1, 1)
( 1, 2,-2,-1)  (-1,-1, 2,-2)  ( 0, 1, 1, 1)  (0,2,1,2)
```

Using columns \(e_i^2\) and \(e_ie_j\) in lexicographic upper-triangular
order, the \(10\times10\) matrix of the ten cycle-edge symmetric products
has integer determinant

\[
                            -3,616,140\ne0.
\]

Therefore \(2C_3\sqcup C_4\) is independent in the symmetric-power matroid
at \(a=4\), but reaching it from the displayed two-triangle certificate
requires changing the old placement. The accompanying verifier recomputes
both exact determinants.

## Consequence for the next proof attempt

A uniform induction cannot demand that an arbitrary previously certified Gale
placement remain fixed. The next viable lemma must permit a simultaneous
generic perturbation/basis exchange of old components and prove that the
relevant determinant polynomial is not identically zero. The smallest sharp
test is the fixed-\(a=4\) transition
\(2C_3\leadsto2C_3\sqcup C_4\), followed by the analogous transition from a
full \(\operatorname{Sym}^2(\mathbb Q^{a-1})\) certificate across each
triangular threshold.
