# Exact finite proof dossier

All notation and normalizations are those of `problem.md`.  The verifier is
`evidence/exact_cyclic_gl.py`; it uses exact integer/rational arithmetic and
symbolic arithmetic in \(\mathbb Q(\sqrt5)\).

## Translation/Fourier reduction

For a GL-feasible squared Euclidean semimetric \(d\) on \(\mathbb Z_n\), average
all translates:
\[
 \bar d(x,y)=\frac1n\sum_z d(x+z,y+z)=f(x-y).
\]
The squared-Euclidean cone and all triangle inequalities are convex, so
\(\bar d\) is feasible.  Both the numerator and denominator are unchanged.
Thus an optimum may be sought among translation-invariant metrics.  Every such
translation-invariant squared Euclidean metric has the cyclic Fourier form
\[
 f(t)=\sum_{k=1}^{\lfloor n/2\rfloor}b_k
       \bigl(1-\cos(2\pi kt/n)\bigr),\qquad b_k\ge0.
\]
(This is the diagonalization of a conditionally negative semidefinite
circulant matrix; conjugate characters are paired.)  Conversely every such
nonnegative choice is squared Euclidean.  Its denominator is
\(D(f)=n^{-1}\sum_t f(t)=\sum_k b_k\).  The remaining conditions are the
linear inequalities
\[
 f(a)+f(b)-f(a+b)\ge0\quad(a,b\in\mathbb Z_n).
\]
Consequently each cyclic GL problem here is an exact finite linear program.

For cases not requiring negative type, put \(x_i=f(i)=f(n-i)\) for
\(1\le i\le\lfloor n/2\rfloor\).  The verifier stores a rational identity
\[
 c-Lw=\sum_{a,b}\lambda_{a,b}R_{a,b}+\sum_i\mu_i e_i,
 \qquad \lambda_{a,b},\mu_i\ge0,                         \tag{1}
\]
where \(c\cdot x=N_G(f)\), \(w\cdot x=D(f)\), and
\(R_{a,b}\cdot x=f(a)+f(b)-f(a+b)\).  Identity (1) proves
\(N_G(f)\ge L D(f)\) using only triangle inequalities and nonnegativity.
All multipliers are serialized as numerator/denominator pairs in
`RATIONAL_CERTIFICATES` and the script checks (1) with `Fraction` arithmetic.
The exhaustive cut witness proves the reverse GL inequality.

## Balanced complete multipartite cases

The only residual cases not covered by (1) below order ten are
\[
 (n,S)=(6,\{1,3,5\}),\ (8,\{1,3,5,7\}),\
 (9,\{1,2,4,5,7,8\}).
\]
They are respectively \(K_{2\times3},K_{2\times4},K_{3\times3}\), where
\(K_{p\times q}\) means \(p\) independent parts of size \(q\), with every
cross-part edge.  The order-ten presentation with all odd generators is
similarly \(K_{2\times5}\).

For vectors in the GL embedding, let \(m_i\) and \(V_i\) be the centroid and
mean squared deviation in part \(i\).  The mean squared distance conditional
on two points lying in the same part is \(2p^{-1}\sum_iV_i\).  The mean over
ordered pairs in distinct parts is this same quantity plus
\((p(p-1))^{-1}\sum_{i\ne j}\lVert m_i-m_j\rVert^2\), hence is no smaller.
The latter is the graph numerator, while the total-pair denominator is their
convex combination, so \(N_G(d)\ge D(d)\).

For a cut with part counts \(a_i\) and \(a=\sum_i a_i\), direct counting gives
\[
 p|\partial A|-(p-1)a(n-a)=p\sum_i a_i^2-a^2\ge0.
\]
After the normalization in `problem.md` this says \(\psi_G(A)\ge1\).
Taking one vertex in every part gives equality (all four cases have \(q\ge2\)).
Thus \(\psi=\operatorname{SDP}_{GL}=1\).

## Exhaustion below order ten

By the finite Abelian group classification, every noncyclic Abelian group of
order at most nine has exponent at most four.  Corollary 4.7 of the supplied
primary paper therefore proves its GL exactness, as well as all cyclic orders
at most four.  The only residue is \(\mathbb Z_n\), \(5\le n\le9\).

The verifier enumerates every nonempty inverse-closed generating subset and
quotients by multiplication by units.  It obtains respectively
\(2,5,3,8,6\) presentation orbits for \(n=5,6,7,8,9\).  Exhausting every cut
gives exact rational cut optima.  Twenty-one cases have certificates (1), and
the three remaining cases are the complete multipartite graphs above.  Hence
every admissible Abelian Cayley graph of order below ten is GL-exact.

## Order-ten classification

The only Abelian group of order ten is \(\mathbb Z_{10}\).  Exact orbit
enumeration gives 16 presentation orbits.  Eleven have rational certificates
(1), the all-odd set is \(K_{2\times5}\), and one further exact case
\(S=\{1,2,3,5,7,8,9\}\) has the Fourier certificate below.  Exactly three
orbits are non-exact:

| \(S\) | exact \(\psi\) | exact \(\operatorname{SDP}_{GL}\) |
|---|---:|---:|
| \(\{1,3,7,9\}\) | \(4/5\) | \(3/4\) |
| \(\{1,4,6,9\}\) | \(4/5\) | \((15+\sqrt5)/22\) |
| \(\{1,2,5,8,9\}\) | \(5/6\) | \((10+\sqrt5)/15\) |

The inequalities are strict: \(5\sqrt5<13\) and \(2\sqrt5<5\), verified by
squaring positive quantities.  The first row is also the supplied paper's
witness.

Here are the exact Fourier certificates.  Put
\(u_k(t)=1-\cos(2\pi kt/10)\),
\(T_{a,b,k}=u_k(a)+u_k(b)-u_k(a+b)\), and
\(c_k=|S|^{-1}\sum_{s\in S}u_k(s)\).  For each row the stored nonnegative
primal vector \(b^*\) sums to one, satisfies every triangle inequality, and
has objective \(L\).  The stored dual identity is
\[
 c-L\mathbf1=\sum_{a,b}\lambda_{a,b}T_{a,b}+\mu,
 \qquad \lambda_{a,b}\ge0,\quad\mu_k\ge0.              \tag{2}
\]
The verifier expands every cosine exactly and checks all primal slacks and
every coordinate of (2).

| \(S\) | \(L\) | \(b^*\) | nonzero \(\lambda\) | \(\mu\) |
|---|---|---|---|---|
| \(\{1,3,7,9\}\) | \(3/4\) | \(((5-\sqrt5)/10,0,(5+\sqrt5)/10,0,0)\) | none | \((0,1/2,0,1/2,5/4)\) |
| \(\{1,4,6,9\}\) | \((15+\sqrt5)/22\) | \((4/11-6\sqrt5/55,1/11+3\sqrt5/11,4/11-6\sqrt5/55,0,2/11-3\sqrt5/55)\) | \(\lambda_{1,1}=\lambda_{4,4}=(7-\sqrt5)/88;\ \lambda_{1,6}=(7-\sqrt5)/44\) | \((0,0,0,(15+\sqrt5)/44,0)\) |
| \(\{1,2,5,8,9\}\) | \((10+\sqrt5)/15\) | \((\sqrt5/3,(3-\sqrt5)/6,0,(3-\sqrt5)/6,0)\) | \(\lambda_{1,2}=(5-\sqrt5)/25;\ \lambda_{2,2}=(5-\sqrt5)/75\) | \((0,0,2/5,0,(8-\sqrt5)/15)\) |
| \(\{1,2,3,5,7,8,9\}\) | \(20/21\) | \((1/3,0,(3-\sqrt5)/6,(1+\sqrt5)/6,0)\) | \(\lambda_{2,2}=2/21\) | \((0,0,0,0,10/21)\) |

Finally, for each of the 16 order-ten representatives the verifier constructs
the integer adjacency matrix and computes its exact characteristic polynomial.
All 16 polynomials are distinct.  Since isomorphic graphs have the same
characteristic polynomial, no two presentation-orbit representatives give
isomorphic graphs.  Thus the three displayed non-exact presentations are also
three distinct ordinary graph-isomorphism classes, and no non-exact class has a
second inequivalent Abelian Cayley presentation at order ten.

Combining the exactness below ten with any of the three order-ten gaps gives
the minimum order \(n_*=10\), and the preceding paragraph supplies the required
order-ten classification.
