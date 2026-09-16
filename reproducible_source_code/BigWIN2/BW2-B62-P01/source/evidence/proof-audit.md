# Proof audit for the frozen literal claim

Research job: `win-00062-p01-research-2b0184248919`  
Audit date: 2026-09-07

This dossier uses exactly the objects and quantifiers frozen in `source.md` and
`problem.md`.  The cited primary source is preserved at
`evidence/external/2609.03372v1.pdf` with SHA-256
`b2fc6b40d51f6eb18a0aacffc8b81d9fc90a22079b40fc0571f9269d87043288`.

## Claim

For each of the product t-norm
\(T_P(a,b)=ab\) and the Lukasiewicz t-norm
\(T_L(a,b)=\max(0,a+b-1)\), the unchanged triple
\((\mathbb N_0,M,T)\) is a GV-fuzzy metric space.  With the unchanged sequence
\(x_n=n\) and \(\psi(u)=2u/(1+u)\), the sequence is strictly fuzzy
\(\psi\)-contractive and is not Cauchy.  Thus the literal claim in `source.md`
is true for both selected t-norms.

## 1. The two operations really are continuous t-norms

On \([0,1]^2\), multiplication has values in \([0,1]\), is commutative,
associative, coordinatewise nondecreasing, has neutral element 1, and is
continuous.  Its endpoint identities are \(T_P(0,b)=0\) and
\(T_P(1,b)=b\).

For \(T_L\), the range assertion follows from
\(0\leq\max(0,a+b-1)\leq1\).  The operation is commutative,
coordinatewise nondecreasing, continuous, and satisfies
\(T_L(a,1)=a\) and \(T_L(a,0)=0\).  Associativity follows without an omitted
boundary case because, for \(a,b,c\in[0,1]\), both bracketings equal
\[
 \max(0,a+b+c-2).
\]
Indeed, if \(a+b\leq1\), then
\(T_L(T_L(a,b),c)=T_L(0,c)=0\) and \(a+b+c-2\leq0\); if
\(a+b>1\), direct substitution gives the displayed expression.  The same
argument with \(b+c\) treats the other bracketing.

For every \(a,b\in[0,1]\), including all endpoints,
\[
 ab\leq a,\quad ab\leq b,
\]
and
\[
 \max(0,a+b-1)\leq a,\quad
 \max(0,a+b-1)\leq b.
\]
For the latter inequalities, the maximum is either 0 or \(a+b-1\), and in
the second case use respectively \(b\leq1\) and \(a\leq1\).  Consequently
\[
 T_P(a,b)\leq\min(a,b),\qquad
 T_L(a,b)\leq\min(a,b).                                      \tag{8}
\]

## 2. Independent audit of the minimum triangle inequality

Theorem 3.2 of the primary source proves this inequality.  Here is a direct
recheck, including its degenerate cases, so that the transfer in Section 3
does not conceal a direction error.

For any pair \(u,v\), any \(r>0\), and any real \(c\), elementary
multiplication by \(2^r-1>0\) gives
\[
 \mu_r(u,v)\leq c
 \quad\Longleftrightarrow\quad
 h(u,v)+c\leq 2^r\bigl(\ell(u,v)+c\bigr).                    \tag{9}
\]
Fix \(x,y,z\in\mathbb N_0\) and \(t,s>0\), and put
\(c=\max\{\mu_t(x,y),\mu_s(y,z)\}\).  From
\(c\geq\mu_t(x,y)\), (9) gives
\(h(x,y)+c\leq2^t(\ell(x,y)+c)\).  Also
\(\ell(x,y)+c\geq0\): if \(x\ne y\), it is at least
\(\ell(x,y)+\mu_t(x,y)=|x-y|/(2^t-1)>0\), while if \(x=y\),
it is at least \(x+\mu_t(x,x)=0\).  Hence
\(\ell(x,y)+c\leq2^t(h(x,y)+c)\).  Regardless of the order of \(x,y\),
these two inequalities say
\[
 x+c\leq2^t(y+c),\qquad y+c\leq2^t(x+c).                     \tag{10}
\]
The identical reasoning for \((y,z,s)\) gives
\[
 y+c\leq2^s(z+c),\qquad z+c\leq2^s(y+c).                     \tag{11}
\]
Composing (10)--(11) in both directions and using
\(2^t2^s=2^{t+s}\) gives
\(h(x,z)+c\leq2^{t+s}(\ell(x,z)+c)\).  A final use of (9) yields
\[
 \mu_{t+s}(x,z)\leq
 \max\{\mu_t(x,y),\mu_s(y,z)\}.                              \tag{12}
\]

If \(x,y,z\) are pairwise distinct, subtracting \(t+s\) from (12) and
using \(s,t>0\) gives
\[
 \mu_{t+s}(x,z)-(t+s)
 \leq\max\{\mu_t(x,y)-t,\mu_s(y,z)-s\}.
\]
Exponentiation therefore yields
\[
 q_{t+s}(x,z)\leq\max\{q_t(x,y),q_s(y,z)\}.                  \tag{13}
\]
All degeneracies in (13) also hold.  If \(x=z\), its left side is zero.
If \(x=y\ne z\), then \(q_t(x,y)=0\) and
\(q_{t+s}(x,z)\leq q_s(x,z)=q_s(y,z)\); here the exponent
\(|x-z|/(2^r-1)-\ell(x,z)-r\) is decreasing in \(r>0\).
The case \(y=z\ne x\) is symmetric, and \(x=y=z\) was already covered.
Since \(q\mapsto(1+q)^{-1}\) is decreasing, (13) is exactly
\[
 \min\{M(x,y,t),M(y,z,s)\}\leq M(x,z,t+s).                  \tag{14}
\]

## 3. GV1--GV5, separately under both labels

The common four t-norm-free axioms follow directly from the frozen formula.

- **GV1:** \(q_t(x,y)\geq0\), so \(M(x,y,t)=1/(1+q_t(x,y))>0\).
- **GV2:** on the diagonal \(q_t(x,x)=0\), hence \(M(x,x,t)=1\).  Off the
  diagonal, \(q_t(x,y)=2^{\mu_t(x,y)-t}>0\), hence \(M(x,y,t)<1\).
- **GV3:** both \(|x-y|\) and \(\min(x,y)\) are symmetric, so \(M\) is
  symmetric.
- **GV5:** on the diagonal the map in \(t\) is constantly 1.  Off the
  diagonal it is a composition of continuous functions on \(t>0\); crucially
  \(2^t-1>0\) there.  The values lie in \((0,1]\) by GV1--GV2.

For GV4 under \(T_P\), the inputs \(M(x,y,t),M(y,z,s)\) lie in \((0,1]\),
so (8) followed by (14) gives, for all quantified variables,
\[
 M(x,y,t)M(y,z,s)
 \leq\min\{M(x,y,t),M(y,z,s)\}
 \leq M(x,z,t+s).
\]
For GV4 under \(T_L\), the same two cited inequalities give
\[
 \max\{0,M(x,y,t)+M(y,z,s)-1\}
 \leq\min\{M(x,y,t),M(y,z,s)\}
 \leq M(x,z,t+s).
\]
Thus every GV axiom holds under each selected t-norm.  Notice that the
inequality needed here is \(T\leq\min\), not its reverse, because GV4 places
the t-norm expression on the left-hand side.

## 4. Strict fuzzy contractivity is unchanged

For \(0<u\leq1\), \(\psi(u)=2u/(1+u)\) lies in \((0,1]\), is continuous and
strictly increasing, and
\[
 \psi(u)-u=\frac{u(1-u)}{1+u}>0\quad(0<u<1).
\]
Hence \(\psi\in\Psi\).

For all \(x,y\in\mathbb N_0\), shifting both arguments preserves their
distance and increases their minimum by one.  If \(x\ne y\), this gives
\(\mu_t(x+1,y+1)=\mu_t(x,y)-1\), hence
\(q_t(x+1,y+1)=q_t(x,y)/2\).  If \(x=y\), both q-values are zero, so the
same identity still holds.  Therefore, for every \(m,n\in\mathbb N\) and
\(t>0\),
\[
\begin{aligned}
 M(x_{m+1},x_{n+1},t)
 &=\frac{1}{1+q_t(x_m,x_n)/2}\\
 &=\frac{2}{2+q_t(x_m,x_n)}\\
 &=\psi\!\left(\frac{1}{1+q_t(x_m,x_n)}\right)\\
 &=\psi(M(x_m,x_n,t)).
\end{aligned}
\]
This is the source definition's required inequality with equality.  Neither
the definition of \(\Psi\) nor this identity evaluates the selected t-norm,
so it holds unchanged in both GV-fuzzy metric spaces.

## 5. Exact non-Cauchy witness is unchanged

Fix any proposed Cauchy index \(N\in\mathbb N\), and choose the two sequence
indices \(n=N\), \(m=2N+1\), both at least \(N\).  At \(t=1\),
\[
 \ell(x_N,x_{2N+1})=N,\qquad |x_N-x_{2N+1}|=N+1,
\]
so
\[
 \mu_1(x_N,x_{2N+1})=\frac{N+1}{2^1-1}-N=1,
 \quad q_1(x_N,x_{2N+1})=2^{1-1}=1,
\]
and therefore
\[
 M(x_N,x_{2N+1},1)=\frac12.
\]
Taking \(\varepsilon=1/2\), the Cauchy definition demands the strict
inequality \(M>1-\varepsilon=1/2\), which this pair violates for every
candidate \(N\).  The Cauchy definition contains no t-norm evaluation, so the
failure is unchanged under both labels.

## Audit conclusion and gap list

The frozen literal claim is proved.  The argument checks the domains and
endpoints, both selected operations, all five GV axioms, the diagonal case in
the shift identity, and the strict threshold in the non-Cauchy witness.  No
mathematical gap is known in this exact scope.  This research-stage conclusion
still requires a fresh referee under the release workflow; it is not a novelty
or publication-priority assertion.

Limited literature screen on 2026-09-07: the current arXiv record for
2609.03372 remained v1 and still stated Problem 3.  Exact-phrase and targeted
arXiv searches for the same-construction observation found that primary record
and no separate primary answer.  This records search coverage only and does not
prove novelty or priority.
