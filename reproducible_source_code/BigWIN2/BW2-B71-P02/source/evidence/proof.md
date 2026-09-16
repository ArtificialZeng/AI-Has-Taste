# Proof dossier: the first stabilization kernel

Proposer job: win-00071-p02-research-588a8190eb89  
Frozen objects: exactly those in source.md and problem.md.

## Result

For the fixed complex Motakis realization \(X\) over \(S^4\), \(E=X\oplus X\),
and \(S,T\in\mathcal B(E)\) of Horváth--Kania Theorem 5.1, put

\[
u=I_E-2ST.
\]

Then

\[
\mathfrak I(\mathcal B(E))\cong \mathbb Z/2,
\qquad
\mathfrak I(M_2(\mathcal B(E)))=1,
\]

the nonidentity element of the first group is \([u]\), and consequently

\[
\ker s_{\mathcal B(E)}=\{[I_E],[u]\}\cong\mathbb Z/2,
\qquad \operatorname{ord}[u]=2.
\]

The proof rests on the following elementary component-lifting lemma. All norms
in its proof are the operator norm or the quotient norm induced from it.

## Lemma: Calkin components inject for a basis-bearing complex space

Let \(Y\) be an infinite-dimensional complex Banach space with a Schauder
basis, and let

\[
q:\mathcal B(Y)\longrightarrow \mathcal Q(Y)
       =\mathcal B(Y)/\mathcal K(Y)
\]

be the Calkin quotient. Then the induced homomorphism

\[
q_*:\mathfrak I(\mathcal B(Y))\longrightarrow
       \mathfrak I(\mathcal Q(Y))
\]

is injective.

### 1. Explicit finite-rank approximation

Let \(P_n\) be the basis partial-sum projections and
\(\beta=\sup_n\lVert P_n\rVert<\infty\). For \(K\in\mathcal K(Y)\), the set

\[
C=\overline{K(B_Y)}
\]

is compact. Given \(\varepsilon>0\), choose a finite
\(\varepsilon/(3(1+\beta))\)-net \(z_1,\ldots,z_r\) in \(C\). Pointwise
convergence \(P_nz_j\to z_j\) permits a common \(n\) such that

\[
\max_j\lVert(I-P_n)z_j\rVert<\varepsilon/3.
\]

For each \(z\in C\), choosing a corresponding \(z_j\) gives

\[
\lVert(I-P_n)z\rVert
 \le (1+\beta)\lVert z-z_j\rVert
       +\lVert(I-P_n)z_j\rVert
 <2\varepsilon/3<\varepsilon.
\]

Thus \(F=P_nK\) has finite rank and

\[
\lVert K-F\rVert<\varepsilon. \tag{1}
\]

### 2. The invertible fiber is path connected

Take \(a=I_Y+K\in\operatorname{Inv}(\mathcal B(Y))\). In (1), choose \(F\)
so that

\[
\lVert a^{-1}\rVert\,\lVert F-K\rVert<1. \tag{2}
\]

For \(0\le t\le1\),

\[
a_t=a+t(F-K)
   =a\bigl(I+t\,a^{-1}(F-K)\bigr)
\]

is invertible by (2) and the Neumann series. This joins \(I+K\) to \(I+F\).

It remains to contract the finite-rank endpoint. Set \(M=F(Y)\), choose a
closed complement \(N\), and write \(Y=M\oplus N\). Since \(F(Y)\subseteq M\),

\[
I+F=\begin{pmatrix}C&B\\0&I_N\end{pmatrix},
\qquad C\in\operatorname{Inv}(M).
\]

(Invertibility of \(C\) follows either from this triangular form or first from
injectivity and then finite dimensionality.) The path

\[
t\longmapsto
\begin{pmatrix}C&(1-t)B\\0&I_N\end{pmatrix}
\]

consists of invertibles, with inverse

\[
\begin{pmatrix}C^{-1}&-C^{-1}(1-t)B\\0&I_N\end{pmatrix}.
\]

Finally, \(GL(M)\) is path connected because \(M\) is a finite-dimensional
complex space. Explicitly, after choosing an auxiliary Hermitian inner product,
write \(C=UP\) by polar decomposition. The positive matrices
\(U((1-t)P+tI_M)\) join \(C\) to \(U\); if \(U=e^{iH}\), then
\(e^{i(1-t)H}\) joins \(U\) to \(I_M\). Extending these paths by \(I_N\)
contracts \(I+F\) to \(I_Y\). Hence

\[
\{I_Y+K:K\in\mathcal K(Y),\ I_Y+K\text{ invertible}\} \tag{3}
\]

is path connected.

### 3. Small-increment lift of a quotient path

Suppose \(v\in\operatorname{Inv}(\mathcal B(Y))\) and
\(q(v)\in\operatorname{Inv}_0(\mathcal Q(Y))\). Choose a path

\[
\gamma:[0,1]\to\operatorname{Inv}(\mathcal Q(Y)),
\qquad \gamma(0)=q(v),\quad\gamma(1)=1.
\]

Let

\[
L=\max_{0\le t\le1}\lVert\gamma(t)^{-1}\rVert<\infty.
\]

Uniform continuity supplies a partition
\(0=t_0<\cdots<t_m=1\) for which

\[
\lVert\gamma(t_{i+1})-\gamma(t_i)\rVert<\frac1{2L}.
\]

Therefore, with

\[
\delta_i=\gamma(t_i)^{-1}\gamma(t_{i+1}),
\]

one has \(\lVert\delta_i-1\rVert<1/2\). By the definition of the quotient
norm, choose \(h_i\in\mathcal B(Y)\) such that

\[
q(h_i)=\delta_i-1,
\qquad \lVert h_i\rVert<1. \tag{4}
\]

Starting with \(v_0=v\), join \(v_i\) to

\[
v_{i+1}=v_i(I+h_i)
\]

by \(s\mapsto v_i(I+s h_i)\), \(0\le s\le1\). Every point is invertible by
(4) and the Neumann series. Inductively,

\[
q(v_i)=\gamma(t_i),
\]

so \(q(v_m)=1\). Hence \(v_m=I+K\) for some compact \(K\), and (3) joins
\(v_m\) to \(I\). Thus \(v\in\operatorname{Inv}_0(\mathcal B(Y))\), proving
injectivity of \(q_*\).

## Application to the frozen space and operators

The archived primary source evidence/external/2609.05362v1.pdf establishes:

1. Theorem 4.1 (printed pp. 7--9) gives the fixed complex space \(X\) a
   Schauder basis and a unital Banach-algebra isomorphism
   \(\mathcal Q(X)\cong C(S^4)\).
2. Immediately before Lemma 4.5 (printed p. 9), it identifies
   \(\mathcal Q(X^n)\cong M_n(\mathcal Q(X))\).
3. Theorem 5.1 (printed pp. 10--11) constructs the fixed \(E=X^2,S,T\), proves
   \(u=I_E-2ST\) invertible and not in the identity component, and identifies
   its Calkin image with the Klaja--Ransford function \(c\).
4. On printed p. 23 the source proves
   \(\mathfrak I(C(S^4,M_2(\mathbb C)))\cong
     \pi_4(GL_2(\mathbb C))\cong\mathbb Z/2\), and says that the Calkin image
   of \([u]\) is its nonzero element.
5. On printed p. 2 it records polar retraction and the stable-range maps
   \(\pi_j(U(m))\to\pi_j(U(m+1))\), and concludes
   \(\pi_4(GL_3(\mathbb C))=0\). Taking \(m=3,j=4\) in the same displayed
   stable-range isomorphism gives \(\pi_4(GL_4(\mathbb C))=0\).

Finite direct sums of a space with a Schauder basis again have a Schauder
basis. Apply the lemma first to \(Y=E=X^2\). Since

\[
\mathcal Q(E)\cong C(S^4,M_2(\mathbb C))
\]

has exactly two invertible components and the nonzero one has the invertible
lift \(u\), the injective map on component groups is also surjective. Therefore

\[
\mathfrak I(\mathcal B(E))\cong\mathbb Z/2,
\]

with nonzero element \([u]\).

Apply the lemma next to \(Y=E\oplus E=X^4\). The standard block-operator
isomorphism gives

\[
M_2(\mathcal B(E))\cong\mathcal B(E\oplus E),
\]

while

\[
\mathcal Q(E\oplus E)
 \cong C(S^4,M_4(\mathbb C)).
\]

By the source's map-space criterion (Lemma 2.3), pointwise normalization of a
free homotopy, and \(\pi_4(GL_4(\mathbb C))=0\), the last Calkin algebra has
trivial component group. Injectivity now forces

\[
\mathfrak I(M_2(\mathcal B(E)))=1.
\]

The first stabilization therefore has all of
\(\mathfrak I(\mathcal B(E))\) as its kernel. Since \([u]\ne 1\) and the group
has two elements, \([u]\) has order exactly two.

## Stress tests and gap list

- The quotient path itself was not assumed to lift. Only finitely many quotient
  increments were lifted, with the strict norm bound \(\lVert h_i\rVert<1\).
- The compact fiber was not contracted by the generally unsafe line
  \(I+tK\). It was first perturbed under the explicit bound (2), then reduced
  to an invertible finite-dimensional diagonal block.
- Surjectivity of the Calkin map on invertibles was not assumed. It is used for
  \(E\) only for the one nonzero component, for which Theorem 5.1 supplies the
  explicit invertible lift \(u\).
- Complex scalars are essential in the connectedness of \(GL(M)\).
- No gap is presently known in the argument. This is a proposer proof dossier,
  not a substitute for the required fresh mathematical referee.
