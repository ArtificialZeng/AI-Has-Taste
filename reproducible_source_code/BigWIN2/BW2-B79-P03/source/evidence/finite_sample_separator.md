# Finite-sample covariance separator

This note proves the missing random-denominator estimate for the precise
sample laws in `problem.md`.  All probabilities below are with respect to
independent samples.  Put

\[
 r=n^2,\qquad Z\sim D_{\mathbb Z,r},\qquad
 V=\mathbb E Z^2,
\]

and let every row of the random matrix of public samples be an independent
vector \(a_i\in\mathbb Z^n\) with iid coordinates distributed as \(Z\).
Write \({\bf 1}=(1,\ldots,1)^T\), \(X_i=\langle a_i,{\bf 1}\rangle\),

\[
 C={1\over N}\sum_{i=1}^N a_i a_i^T,
 \qquad D=\sum_{i=1}^N X_i^2=N{\bf 1}^TC{\bf 1}.
\]

## Lemma 1: elementary discrete-Gaussian estimates

For every real \(t\),

\[
 \mathbb E e^{tZ}\leq \exp\!\left({r^2t^2\over4\pi}\right),
 \qquad
 \Pr(|Z|>u)\leq 2\exp\!\left(-{\pi u^2\over r^2}\right).
 \tag{1}
\]

Moreover, for integer \(r\geq1\),

\[
 V\geq v_0r^2,\qquad v_0={e^{-\pi}\over8}.
 \tag{2}
\]

**Proof.** Completing the square gives

\[
 \mathbb E e^{tZ}=e^{r^2t^2/(4\pi)}
 {\rho_r(\mathbb Z-r^2t/(2\pi))\over\rho_r(\mathbb Z)}.
\]

Poisson summation writes the shifted numerator as

\[
 r\sum_{k\in\mathbb Z}e^{-\pi r^2k^2}
 e^{2\pi i k r^2t/(2\pi)}.
\]

Its (real, nonnegative) value is at most the same sum with every phase
replaced by \(1\), namely \(\rho_r(\mathbb Z)\).  This proves the moment
bound; Chernoff optimization with \(t=2\pi u/r^2\), on each tail, proves
(1).

For (2), monotonicity and integration give

\[
 \rho_r(\mathbb Z)=1+2\sum_{k\geq1}e^{-\pi k^2/r^2}
 \leq1+r\leq2r.
\]

There are at least \(r/2\) positive integers in \([r/2,r]\).  Their
positive and negative copies each have squared magnitude at least \(r^2/4\)
and weight at least \(e^{-\pi}\).  Thus the unnormalized second moment is
at least \(e^{-\pi}r^3/4\), which divided by \(2r\) proves (2). \(\square\)

## Lemma 2: an explicit empirical-covariance event

Take \(N=n^8\).  For every \(n\geq3\), except on an event of probability at
most

\[
 \mu_C(n)=2n^9e^{-\pi n^2}
 +2n^2\exp\!\left(-{e^{-2\pi}\over1{,}280{,}000}n^2\right),
 \tag{3}
\]

one has

\[
 \|C-VI_n\|_{\rm op}\leq {V\over50}.
 \tag{4}
\]

**Proof.** Set \(T=rn\).  For every pair \(p,q\), truncate

\[
 W_i^{pq}=a_{ip}a_{iq}
 {\bf 1}_{\{|a_{ip}|\leq T,\ |a_{iq}|\leq T\}}.
\]

The range of \(W_i^{pq}\) has length at most \(2T^2\).  We first bound its
truncation bias.  The tail integration identities, followed by (1), give

\[
 \mathbb E[Z^2;|Z|>T]
 \leq 2T^2e^{-\pi n^2}+4\int_T^\infty
 x e^{-\pi x^2/r^2}\,dx
 \leq3r^2n^2e^{-\pi n^2},
\]

and

\[
 \mathbb E[|Z|;|Z|>T]
 \leq r\left(2n+{1\over\pi n}\right)e^{-\pi n^2},
 \qquad \mathbb E|Z|\leq r.
\]

Coordinate independence and symmetry therefore imply, for all \(p,q\),

\[
 \left|\mathbb EW_i^{pq}-V{\bf1}_{p=q}\right|
 \leq6r^2n^2e^{-\pi n^2}.
 \tag{5}
\]

For \(n\geq3\), the last expression is at most \(V/(100n)\): by (2), it
is enough to check
\(4800n^3e^{-\pi(n^2-1)}\leq1\), which holds at \(n=3\) and decreases
thereafter.

Let \(u=V/(100n)\).  Hoeffding's inequality yields

\[
 \Pr\left(\left|N^{-1}\sum_iW_i^{pq}-\mathbb EW_i^{pq}\right|>u\right)
 \leq2\exp\left(-{Nu^2\over2T^4}\right)
 \leq2\exp\left(-{Ne^{-2\pi}\over1{,}280{,}000n^6}\right).
 \tag{6}
\]

By (1), the probability that any one of the \(Nn\) sampled coordinates
exceeds \(T\) in magnitude is at most \(2Nn e^{-\pi n^2}\).  Outside that
event the truncated and original empirical products coincide.  Union-bound
(6) over the \(n^2\) pairs and use (5).  With \(N=n^8\), every entry of
\(C-VI_n\) then has magnitude at most \(V/(50n)\), with failure probability
(3).  Its maximum absolute row sum, hence its operator norm, is at most
\(V/50\). \(\square\)

## The separator theorem

Given \(N=n^8\) samples, use the convention

* output **constructed** iff \(D>0\) and
  
  \[
  \widehat\theta={\sum_iX_i b_i\over D}>{3\over2};
  \]
* output **legal** when \(D=0\) or the strict inequality fails.

This test uses \(O(Nn)\) arithmetic operations and does not depend on the
secret, on its noise scale, or on \(M\).

On the event (4),

\[
 D\geq {49\over50}NVn>0. \tag{7}
\]

For a legal secret put \(t=s/M\in[0,1)^n\).  Its noiseless empirical slope
is

\[
 R_Q={{\bf1}^TCt\over{\bf1}^TC{\bf1}}.
\]

Writing \(C=VI+E\), using \(\|E\|_{\rm op}\leq V/50\),
\(\|t\|_2\leq\sqrt n\), and \({\bf1}^Tt\leq n\), gives

\[
 R_Q\leq{(51/50)Vn\over(49/50)Vn}={51\over49},
 \qquad {3\over2}-R_Q\geq{45\over98}>{1\over4}. \tag{8}
\]

For the constructed law, the noiseless empirical slope is

\[
 R_P=2+{1\over4M}
 {{\bf1}^TCe_1\over{\bf1}^TC{\bf1}}.
\]

Again from (4),

\[
 \left|{{\bf1}^TCe_1\over{\bf1}^TC{\bf1}}\right|
 \leq{50+\sqrt n\over49n}.
\]

Since \(M\geq1\) and \(50+\sqrt n\leq49n\) for \(n\geq2\),

\[
 R_P\geq {7\over4},
 \qquad R_P-{3\over2}\geq {1\over4}. \tag{9}
\]

It remains to control the response noise without dividing expectations.  If
the independent errors have law
\(\nu_\gamma=N(0,\gamma^2/(2\pi))\), then, conditional on all public
vectors and on \(D>0\),

\[
 {\sum_iX_i e_i\over D}
 \sim N\left(0,{\gamma^2\over2\pi D}\right). \tag{10}
\]

Here \(\gamma=1/2\) for the constructed law and
\(0<\gamma=\beta\leq1/2\) for every legal law.  Equations (8)--(10) and a
Gaussian tail bound show that either kind of classification error,
conditional on (4), has probability at most

\[
 2e^{-\pi D/4}
 \leq2\exp\!\left(-{49\pi e^{-\pi}\over1600}n^{13}\right), \tag{11}
\]

where (2), (7), \(r=n^2\), and \(N=n^8\) were used in the last step.
Consequently, for every admissible \(M\), and uniformly over every fixed
legal \(s\in[0,M)^n\cap\mathbb Z^n\) and \(0<\beta\leq1/2\), each error
probability is bounded by

\[
 \boxed{\mu(n)=2n^9e^{-\pi n^2}
 +2n^2e^{-e^{-2\pi}n^2/1{,}280{,}000}
 +2e^{-49\pi e^{-\pi}n^{13}/1600}.} \tag{12}
\]

Every summand is negligible.  The event \(D=0\) is included in the covariance
failure event under the constructed law by (7), while the stipulated
zero-denominator convention can only favor the legal law.  Thus (12) proves
the required uniform overwhelming-probability separation, including the
random denominator and its zero event.

## Promise audit for the frozen family

The remaining assertions are deterministic.  For \(L=A=I_n\), one has
\(L^*=\mathbb Z^n\), \(\lambda_1(L)=1\), and the smallest eigenvalue of
\(A^TA\) is \(\sigma=1\).  Dean--Goldsmith Claim 2 gives
\(\eta_{2^{-n}}(\mathbb Z^n)\leq\sqrt n\), hence
\(r=n^2>\sqrt2\eta_{2^{-n}}(L)\) for \(n\geq2\).  Also

\[
 {m\alpha\over k^2}={3n^5(1/2)\over n^4}={3n\over2}>\sqrt n,
 \qquad {k\alpha\over r}={1\over2}=\alpha.
\]

The imposed inequality on \(M\) is exactly the Lemma 7 constellation-size
inequality (and in particular gives \(M\geq2\) eventually).  Also
\(\|\delta\|_2=1/4<r=n^2\), as invoked in the construction.  Put
\(F(n)=2^{n\log\log n/\log n}\).  Since
\(\log F(n)/\log n\to\infty\), \(F\) dominates every fixed power of \(n\).
The Lemma 7 distance ceiling specializes to

\[
 {M\sigma\alpha\over k^2r\sqrt2}={M\over2\sqrt2\,n^6}
 >{3\over2\sqrt2}{F(n)\over n}\longrightarrow\infty.
\]

Thus, eventually, \(d_0=3/8\) is strictly below this ceiling.  Finally,
\(y=c+e_1/4\), with \(c=2M{\bf1}\in\mathbb Z^n\), has distance \(1/4<d_0\)
from the lattice; \(c\) is its unique closest lattice point, and
\(d_0<\lambda_1(L)/2=1/2\).  Hence the BDD distance and uniqueness promises,
the smoothing promise, the effective-noise promise, and the stated
constellation/parameter promises all hold for every sufficiently large \(n\).

Substitution in Dean--Goldsmith Eq. (19) is exact:

\[
 a=v\sim D_{\mathbb Z^n,n^2},\qquad
 b=2\sum_ja_j+{a_1\over4M}+e,
 \quad e\sim\nu_{1/2}.
\]

Combining this audit with (12) proves the frozen assertion in `source.md`.
