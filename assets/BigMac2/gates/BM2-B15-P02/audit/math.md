# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, not a
weakened substitute.  The snapshot digest is
`3cd1d027218b5c503da5bcf5a88808e84a9d69d2d4668141e37fe863084fdff8`.
I recomputed the SHA-256 hashes of `claim.json`, `source.md`, `problem.md`, and
all three other listed evidence files; every value agrees with
`audit/snapshot.json`.  In particular, the immutable `source.md` still has
SHA-256 `3e003968a6991322c7ad79fac1cf58c3f36107f2bb5344109cf871bbfce585be`.

The claim has full original scope.  It asserts existence of the minimum for
every parameter in the domain and proves the one-sided limit over all real
parameters, while its two-lattice-step estimate is asserted only for
sufficiently small positive `a`, exactly as the proof requires.

## Independent reconstruction of the decisive argument

For

\[
 a=\operatorname{arcosh}(e^\Delta/2)>0
\]

one has

\[
 q=\frac{2}{e^\Delta+2}=\frac1{1+\cosh a}.
\]

Writing `f(w)=log cosh(w)` as its analytic germ near the relevant real
arguments, the elementary factorization

\[
 1-q+q\cosh z
 =\frac{\cosh((z+a)/2)\cosh((z-a)/2)}{\cosh^2(a/2)}
\]

gives, for every integer \(m\geq1\),

\[
 \kappa_{2m}=2^{1-2m}f^{(2m)}(a/2).
\]

Differentiating the Euler product for `cosh` at least twice is legitimate
locally: after pairing the zeros \(\pm i\pi(2k+1)/2\), the differentiated
series is locally normally and absolutely convergent.  Thus

\[
 f^{(2m)}(x)=-(2m-1)!\sum_{k\geq0}
 \left((x-i y_k)^{-2m}+(x+i y_k)^{-2m}\right),
 \qquad y_k=\frac{\pi(2k+1)}2.
\]

At \(x=a/2\), set

\[
 \beta_k=\arctan\!\frac{a}{\pi(2k+1)},\qquad \beta=\beta_0.
\]

Tracking both the argument
\(\arg(a+i\pi(2k+1))=\pi/2-\beta_k\) and all powers of two gives
the exact identity

\[
 (-1)^{m+1}\kappa_{2m}
 =4(2m-1)!\sum_{k\geq0}
 \frac{\cos(2m\beta_k)}
 {(a^2+\pi^2(2k+1)^2)^m}. \tag{A}
\]

This independently confirms the normalization and sign in the submitted
formula.

Formula (A) also establishes existence of a failing order for every fixed
\(a>0\).  Relative to the `k=0` term, the tail tends to zero geometrically.
If \(\beta/\pi\) is irrational, density of its integer multiples supplies
infinitely many `m` with \(\cos(2m\beta)\leq-1/2\).  If
\(\beta/\pi=p/r\) is rational in lowest terms, then \(0<p<r/2\), hence
\(r\geq3\); multiplication by `p` permutes residues modulo `r`, including
a residue in \([r/3,2r/3]\), and the same inequality recurs periodically.
The negative leading term therefore eventually dominates.  This covers the
rational as well as irrational cases and makes the defining set for
\(m_*\) nonempty.

Now let

\[
 t=\frac{\pi}{4\beta}.
\]

For every integer \(m\leq t\), one has
\(0<2m\beta_k\leq\pi/2\).  Every summand in (A) is nonnegative.  Even if
`m=t` and the `k=0` summand vanishes, all `k>=1` summands are strictly
positive because \(\beta_k<\beta\).  Consequently

\[
 (-1)^{m+1}\kappa_{2m}>0\quad(m\leq t),
\]

so every strict failure satisfies \(m_*>t\); the strict-zero convention in
the original problem is handled correctly.

For \(n=\lceil t+1\rceil\),

\[
 \frac\pi2+2\beta\leq2n\beta<\frac\pi2+4\beta.
\]

When `a` is small enough this interval lies in \((\pi/2,\pi)\), and hence
the normalized `k=0` contribution is at most \(-\sin(2\beta)\).  For
\(a\leq\pi\), the absolute normalized tail obeys

\[
 R_m\leq\left(\frac29\right)^{m-1}
 \left(\frac{\pi^2}{4}-2\right). \tag{B}
\]

Indeed, each weight ratio is at most `2/9`, and one remaining power is at
most \(2/(2k+1)^2\).  Since
\(n\geq\pi/(4\beta)+1\), the right side of (B) is
`o(beta)`, whereas \(\sin(2\beta)\sim2\beta\).  Therefore the complete
sum in (A) is strictly negative at `n` for all sufficiently small `a`.
Together these estimates give precisely

\[
 t<m_*\leq\lceil t+1\rceil<t+2.
\]

It follows that \(\beta m_*\to\pi/4\).  Since
\(\beta=\arctan(a/\pi)\sim a/\pi\), this yields
\(a m_*\to\pi^2/4\).  Finally, when
\(\Delta=\log2+\varepsilon\), one has
\(\cosh a=e^\varepsilon\) and therefore
\(a/\sqrt\varepsilon\to\sqrt2\).  This proves the frozen limit

\[
 \sqrt\varepsilon\,m_*(\log2+\varepsilon)
 \longrightarrow \frac{\pi^2}{4\sqrt2}.
\]

No limiting interchange, unproved monotonicity, or subsequence-only sign
claim is used.

## Computational and source checks actually performed

I ran the frozen exact recurrence for `N=1,2,20,100,1000`; it reproduced
first failures `3,3,8,18,56`.  I then independently formed the truncated
formal series

\[
 \log\left(1+q\sum_{r\geq1}\frac{x^r}{(2r)!}\right)
 =\sum_{j\geq1}\frac{(-1)^{j+1}}j
 \left(q\sum_{r\geq1}\frac{x^r}{(2r)!}\right)^j
\]

using exact rational arithmetic, rather than the submitted
moment--cumulant recurrence.  It gave the same five first failures, including
all preceding signs.  As a supplementary normalization check, direct
summation of (A) through 200,000 zero pairs for `N=20` and `m=2,...,8`
agreed with the exact rational cumulants to ordinary floating-point error
and changed sign first at `m=8`.  The tabulated values for
`N=20,100,1000,2000,10000,100000` also all satisfy the claimed interval
`t < m_* <= ceil(t+1)`.

I inspected the primary source Sheng Chun Yu, *A note on Ursell functions
for the Blume--Capel model*, arXiv:2609.04610v1 (submitted 4 September
2026), including its complete seven-page text.  Proposition 4 states only
fixed-parameter existence of a failing order.  Its equations (8)--(9) use
the nearest four zeros with a fixed-parameter error term; the paper does not
state the first-failure critical limit or the submitted two-lattice-step
localization.  A bounded arXiv search on 8 September 2026 using the title,
model, Ursell/cumulant terminology, first-failure wording, and the proposed
constant returned that paper but no equivalent result.  This supports the
submitted conservative comparison but is not a priority guarantee.

## Gaps, contribution, and verdict

I found no unresolved mathematical gap in the frozen claim.  The exact
zero-sum identity controls every earlier integer order, which is the central
quantifier absent from a fixed-parameter eventual-failure argument.  The
two-lattice-step localization is a nontrivial strengthening with a direct
critical interpretation, not a toy restriction or a silently downgraded
claim.

**Verdict: accept.**  The argument proves the immutable original assertion
in full scope, establishes existence required by the definition, and
supports the stated contribution with appropriately bounded literature
language.
