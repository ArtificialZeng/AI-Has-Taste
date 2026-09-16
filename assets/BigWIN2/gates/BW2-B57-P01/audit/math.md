# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot
`262a7afcbfcd4342ded297d9f65e0c8d13db48329a503c1f554b3d10ef6aeb51`.
I independently recomputed the SHA-256 digest of every frozen file and the
canonical digest of the snapshot file map; all values agree with
`audit/snapshot.json`.  The claim concerns only the displayed
three-parameter family and does not identify its supremum with the global
constant \(f(\alpha)\).

## Reconstruction of the Lorentzian criterion

Let \(U=\langle e_6-e_7\rangle\), let \(V\) be spanned by
\(u=e_6+e_7\) and \(v=e_1+\cdots+e_5\), and let \(W\) consist of vectors
supported on the first five coordinates with coordinate sum zero.  Direct
matrix multiplication verifies that this is a direct sum orthogonal for the
bilinear form represented by \(P\).  The restriction to \(U\) is zero.  In
the basis \((u,v)\), the restriction to \(V\) is

\[
  \begin{pmatrix}4&10t\\10t&5+10r+10q\end{pmatrix}.
\]

It has a positive direction because its first diagonal entry is positive.
Consequently it has at most one positive eigenvalue exactly when its
determinant is nonpositive, which is

\[
  4(5+10r+10q)-100t^2\leq0
  \quad\Longleftrightarrow\quad
  t^2\geq\frac{1+2r+2q}{5}.
\]

On \(W\), the two eigenvalues, each of multiplicity two, are

\[
  1-\frac{r+q}{2}\mathbin{\pm}\frac{\sqrt5}{2}(r-q).
\]

Thus this restriction is negative semidefinite exactly when
\(r+q-2\geq\sqrt5\lvert r-q\rvert\).  Since \(V\) always supplies a
positive direction, these two conditions are together necessary and
sufficient for the full matrix to have exactly one positive eigenvalue.
This also checks the equality cases: the forced kernel on \(U\), and any
additional zero eigenvalues at boundary points, are allowed by the stated
definition of Lorentzian.  As an independent algebraic check, I factored the
symbolic characteristic polynomial of the full \(7\times7\) matrix; its
linear/quadratic factors reproduce these four \(W\)-eigenvalues, the zero
eigenvalue on \(U\), and the two-dimensional \(V\) restriction.

## Reconstruction of the optimization

Substitution in the exponent gives

\[
  P(r,q,t)^\alpha=(q^5/t^{10})^{1/4}=(q/t^2)^{5/4}.
\]

For fixed feasible \((r,q)\), this is strictly decreasing in \(t^2\), so its
maximum over allowed \(t\) occurs at
\(t^2=(1+2r+2q)/5\).  It remains to maximize

\[
  B(r,q)=\frac{5q}{1+2r+2q}.
\]

Put \(s=\sqrt5\).  If \(r\leq q\), feasibility is equivalent to

\[
  r\geq a(q)=\frac{(s-1)q+2}{s+1}
             =\frac{(3-s)q+(s-1)}2.
\]

The interval \([a(q),q]\) is nonempty exactly when \(q\geq1\).  Since
\(B\) decreases in \(r\),

\[
  B(r,q)\leq B(a(q),q)
   =\frac{5q}{s+(5-s)q}
   <\frac5{5-s}
\]

for every finite feasible \(q\).  If \(r\geq q\), the other branch of the
same feasibility condition is

\[
  (s-1)r\leq(s+1)q-2,
\]

which is compatible with \(r\geq q\) exactly when \(q\geq1\).  Here

\[
  B(r,q)\leq\frac{5q}{1+4q}<\frac5{5-s}.
\]

The cases exhaust all positive \((r,q)\), the displayed denominators are
positive, and both inequalities are strict for every finite feasible triple.
Therefore

\[
  P(r,q,t)^\alpha
  <\left(\frac5{5-s}\right)^{5/4}
  =\left(\frac{5+s}{4}\right)^{5/4},
\]

which proves the upper bound and nonattainment, provided the bound is
approached.

For integer \(n\geq1\), set

\[
 q_n=n,\qquad
 r_n=\frac{(s-1)+(3-s)n}{2},\qquad
 t_n^2=\frac{s+(5-s)n}{5}.
\]

All three parameters are positive and \(r_n\leq q_n\).  Exact simplification
gives

\[
 r_n+q_n-2=s(q_n-r_n),\qquad
 t_n^2=\frac{1+2r_n+2q_n}{5}.
\]

Thus every triple is feasible, including \(n=1\), and

\[
  P(r_n,q_n,t_n)^\alpha
   =\left(\frac{5n}{s+(5-s)n}\right)^{5/4}
   \longrightarrow
   \left(\frac5{5-s}\right)^{5/4}.
\]

This supplies the matching lower bound and verifies all three requested
parts of the frozen problem.

## Source comparison and contribution

I inspected the frozen primary PDF.  Its equation (1) gives the clique-web
vector, equation (2) gives \((q^5/t^{10})^{1/4}\), and Lemma 3.2 gives and
proves precisely the two feasibility inequalities used here.  It then checks
the single point \((284,701,20)\) and obtains approximately \(2.01638>2\).
The inspected source does not state the exact supremum of this family, its
nonattainment, or the extremal sequence above.  The submitted delta is
therefore correctly distinguished from the cited result.  The audit supports
only that source comparison and the stated family result; it makes no claim
of exhaustive literature priority or of a global value for \(f(\alpha)\).

## Attacks and gaps

I checked the branch boundary \(r=q\), the forced condition \(q\geq1\), all
equality cases in the Lorentzian characterization, positivity of the exact
sequence, the strict inequalities needed for nonattainment, and the limiting
calculation.  No quantifier gap, degenerate-domain issue, division by zero,
or unsupported limiting exchange remains.  The proof settles the original
claim in its full frozen scope.

## Verdict

**Accept.**  Scope, mathematical correctness, exact extremal evidence, and
the claimed contribution relative to the frozen primary source all pass.
