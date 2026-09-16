# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the `resolution-paper` claim that, for every integer \(n\geq 1\),
the monomial-cleared Q-polynomial of Shoji's rational link
\(\mathcal C(1^{2n+1})\) has only simple real zeros, all in \([-3,1]\).
This is the full universal assertion frozen in `source.md` and made precise in
`problem.md`, not a restricted subfamily.

Every file hash in `audit/snapshot.json` agrees with the file reviewed.  I also
recomputed the canonical SHA-256 digest of its sorted compact `files` mapping;
it is
`eb73600bdefeeca266c30849fc372ec8b0a4bc7be535e33f4e0f22d48ecaf0a6`,
the recorded snapshot digest.

## Reconstruction of the decisive argument

Let \(q_j=Q_{\mathcal C(1^j)}\).  In the four-ended relative Q-skein, with
vertical, cup--cap, and crossing diagrams denoted by \(1,e,g\), respectively,
the skein relation and Reidemeister-I invariance give
\[
g+g^{-1}=x(1+e),\qquad ge=eg=e,\qquad
e^2=(2x^{-1}-1)e.
\]
Thus \(g^2=-1+xe+xg\).  Reciprocal rotation swaps \(1,e\), fixes \(g\), and
the all-one rational-tangle step is addition of a crossing after reciprocal
rotation.  It sends a coefficient column in the basis \((1,e,g)\) by
\[
A=\begin{pmatrix}0&0&-1\\1&0&x\\0&1&x\end{pmatrix}.
\]
The numerator closure has values \((2x^{-1}-1,1,1)\), so
\(q_j=N(A^{j-1}g)\).  This gives
\[
q_1=1,\quad q_2=2x+1-2x^{-1},\quad q_3=2x^2+2x-3.
\]
The first two nontrivial closures are the Hopf link and trefoil.  Moreover the
same transfer gives
\(q_4=2x^3+4x^2-2x-3\), exactly the value obtained from Shoji's even-family
recurrence and initial data.  These comparisons fix the closure and continued-
fraction convention rather than merely checking an abstract recurrence.

Direct calculation gives
\[
\det(\lambda I-A)=(\lambda+1)
  (\lambda^2-(x+1)\lambda+1),
\]
and hence \(q_{j+3}=xq_{j+2}+xq_{j+1}-q_j\).  Matching its three initial
values after setting \(x=2\cos\theta-1\) yields, as a cross-multiplied
polynomial identity,
\[
q_j(2\cos\theta-1)=
\frac{(-1)^j(\cos2\theta-\cos\theta)+2\cos((j+1)\theta)}
     {(2\cos\theta-1)(\cos\theta+1)}.
\]
The cross-multiplied formulation is important: no value at a vanishing
denominator is inferred by division.

For the odd family put \(m=2n+2\), \(c=(x+1)/2\), and
\[
H_n(x)=2\{c-T_2(c)+2T_m(c)\}.
\]
Then \(x(x+3)q_{2n+1}=H_n\), and \(H_n\) has degree exactly \(m\).  At
\(\theta_k=k\pi/m\), the corresponding trigonometric numerator is
\[
h_n(\theta_k)=2(-1)^k+\phi(\cos\theta_k),
\qquad \phi(c)=-2c^2+c+1.
\]
On \([-1,1]\), \(-2\leq\phi\leq9/8\), with the lower equality only at
\(c=-1\).  Therefore the grid values are strictly positive for even \(k<m\)
and strictly negative for odd \(k\), while \(h_n(\pi)=0\).  There is one root
in each of the \(m-1\) open intervals for \(0\leq k\leq m-2\), plus the
endpoint root \(c=-1\).  These are \(m\) distinct roots of a degree-\(m\)
polynomial.  Consequently all roots of \(H_n\) are simple and lie in
\([-3,1]\).

Finally, \(H_n(-3)=0\), and
\[
H_n(0)=2\left(1+2\cos\frac{m\pi}{3}\right)
=0\quad\Longleftrightarrow\quad n\not\equiv2\pmod3.
\]
All these roots are already known to be simple.  If
\(n\not\equiv2\pmod3\), division by the two distinct factors \(x(x+3)\)
leaves the ordinary canonical polynomial with \(m-2=2n\) simple real roots.
If \(n\equiv2\pmod3\), the only Laurent factor is \(x^{-1}\), and the
canonical polynomial is \(xq_{2n+1}=H_n/(x+3)\), with \(m-1=2n+1\)
simple, nonzero real roots.  This covers both knots and two-component links
and every \(n\geq1\).

## Attacks and computational checks

- The smallest allowed case is \(n=1\), so \(m\) is always even and at least
  four; no empty interval count or excluded one-entry case enters the proof.
- The possible poles at \(x=0\) and \(x=-3\) were handled through the
  polynomial identity and explicit simple-factor cancellation.  No zero is
  created by monomial clearing.
- As topological normalization checks, the transfer gives \(Q(1)=1\); at
  \(x=-2\) it gives \(1\) in the knot congruence classes and \(-2\) in the
  two-component class, agreeing with the source's special-value formula.
- I ran `evidence/verify_odd_family.py` afresh.  It completed over exact
  rational arithmetic, reproduced the two characteristic polynomials and
  initial values, matched transfer and Chebyshev forms, and returned
  degree-many distinct real roots by exact Sturm sequences for every
  \(1\leq n\leq20\).  I separately recomputed the characteristic polynomial,
  \(q_3,q_4\), and the source special values through \(j=15\).  The finite
  calculations are consistency checks; the all-\(n\) conclusion rests on the
  degree and sign-interlacing argument above.

## Source comparison and verdict

The archived primary source defines the same Q-polynomial and real stability,
proves the separate \(2n\)-entry family in Proposition 4.3, and explicitly
identifies the \(2n+1\)-entry analogue as lacking a complete proof in Remark
4.5.  The candidate derives the odd subsequence with its distinct initial
data and proves the universal analogue, so it is not a silent relabeling or a
finite computational observation.  The frozen literature reports make only
a bounded negative-search statement and the claim makes no exhaustive
priority assertion; nothing stronger is needed for the mathematical claim
reviewed here.

**Verdict: accept.**  The argument proves the frozen original assertion in
full scope and also justifies the stated simplicity and interval refinement.
I found no unresolved mathematical gap requiring a claim revision.
