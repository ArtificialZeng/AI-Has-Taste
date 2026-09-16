# Fresh mathematical referee report

Job: `win-00056-p02-referee-720c6ebf52c4`  
Snapshot: `51c2715fbd1cb2eb3e9cf16ae1bb9da2a75eb2a8fa5d714f92324583a01fa899`

## Scope and integrity

I reviewed the exact frozen `resolution-paper` claim, not a weakened or
subsidiary version.  All seven files in `audit/snapshot.json` have their stated
SHA-256 digests, and independently canonicalizing the snapshot's `files`
mapping reproduces the stated snapshot digest.  The four explicit matrices in
`problem.md` follow entrywise from the diagonal Sylvester equation.

The determinant identities also recompute exactly as
\[
 \det X_1=\det X_4={1\over117(3+\delta)},
\]
\[
 \det X_2={5(\delta+9)(\delta+19)\over
 5928\delta(\delta+3)(\delta+6)},\qquad
 \det X_3={-5(17\delta+115)\over
 11856(\delta+3)(\delta+6)}.
\]
Their signs and denominators show that all four matrices are nonsingular for
every \(0<\delta\leq1\).  Thus the rank-deficient convention in the source is
never invoked.

## Reconstruction of the decisive mathematics

### Case 1

Apart from the scalar entry \(-1/13\), the nontrivial block is
\[
 T=\begin{pmatrix}-1/9&1/\delta\\0&1/(3+\delta)\end{pmatrix}.
\]
If \(\lambda_+\geq\lambda_-\) are the eigenvalues of \(T^T T\), then
\(\lambda_+\lambda_-=1/[81(3+\delta)^2]\).  The bounds
\[
 \delta^{-2}\leq\lambda_+\leq\delta^{-2}+10/81,
 \qquad
 \lambda_-\leq {\delta^2\over81(3+\delta)^2}
 \leq {1\over1296}<{1\over169}
\]
show that the extreme singular values of \(X_1\) both come from this
block.  Therefore
\[
 \kappa_2(X_1)=9(3+\delta)\lambda_+,
\]
and hence
\[
 1+{\delta\over3}\leq
 {\kappa_2(X_1)\over27\delta^{-2}}
 \leq(1+\delta/3)(1+10\delta^2/81).
\]
For \(0<\delta\leq1\), subtracting one from the upper bound and dividing
by \(\delta\) gives at most
\(1/3+10/81+10/243=121/243\).  This proves both the pair
\((p_1,K_1)=(2,27)\) and the claimed full-interval relative-error bound.

### Case 2

After the stated column permutation, write
\[
 M=\begin{pmatrix}t&u^T\\v&D\end{pmatrix},\qquad t=\delta^{-1}.
\]
Direct multiplication verifies the exact factorization
\[
 M=
 \begin{pmatrix}1&0\\\delta v&I\end{pmatrix}
 \operatorname{diag}(t,D-\delta vu^T)
 \begin{pmatrix}1&\delta u^T\\0&I\end{pmatrix}.
\]
Independently recomputing \(D^TD\) gives
\[
 \operatorname{tr}(D^TD)={57905\over389376},\qquad
 \det(D^TD)={25\over389376}.
\]
Its smaller eigenvalue is consequently
\[
 \mu_-={57905-5\sqrt{132562057}\over778752}>0,
\]
so \(s=\sqrt{\mu_-}=\sigma_{\min}(D)\).  With the evidence's
\(U,V,a=UV\), one has \(\|v\|\leq V\), and Weyl's inequality gives
\(s-a\delta\leq\sigma_{\min}(D-\delta vu^T)\leq s+a\delta\).

For each shear, both it and its inverse have norm bounded respectively
by \(1+\delta V\) or \(1+\delta U\).  Thus every singular value is
changed by a factor in \([f^{-1},f]\), where
\(f=(1+\delta U)(1+\delta V)\).  The auxiliary ordering is valid:
\(\|D\|_F+a<1\leq t\), while \(\delta\leq s/(2a)\) keeps the perturbed
minimum singular value positive.  Also
\(f^2\leq1+F\delta\) with the exact \(F\) in the evidence.  It follows
that
\[
 {1\over f^2}{s\over s+a\delta}
 \leq {\kappa_2(X_2)\over s^{-1}\delta^{-1}}
 \leq f^2{s\over s-a\delta}.
\]
Putting \(b=a/s\) and using \(b\delta\leq1/2\) yields precisely the
claimed bound with
\(M_2=F+2b+2Fb\) and
\(\delta_2=\min\{1,s/(2a)\}\).  Hence
\(p_2=1\) and \(K_2=s^{-1}\), with the exact radical stated in the
claim.

### Case 3

At \(\delta=0\), exact expansion of \(X_{3,0}^T X_{3,0}\) gives
\[
 \det(zI-X_{3,0}^TX_{3,0})={P(z)\over45542974464},
\]
where
\[
 P(z)=45542974464z^3-13786630308z^2+429202697z-330625.
\]
I independently evaluated the exact Sturm chain.  Its signs at the
left and right endpoints of the three claimed intervals, followed by
the corresponding variation counts, are

| interval | left signs | right signs | variations |
| --- | --- | --- | --- |
| \((1/1300,1/1200)\) | \((- ,+,-,+)\) | \((+,+,-,+)\) | \(3\to2\) |
| \((1/30,1/29)\) | \((+,-,+,+)\) | \((-,-,+,+)\) | \(2\to1\) |
| \((1/4,1/3)\) | \((-,+,+,+)\) | \((+,+,+,+)\) | \(1\to0\) |

Thus each interval contains exactly one root.  These three disjoint
positive intervals account for all roots of the cubic, so their ordering
defines \(0<\rho_1<\rho_2<\rho_3\) without numerical assumptions.  The
limiting condition number is therefore
\(K_3=\sqrt{\rho_3/\rho_1}\).

Only entries \((2,2)\) and \((3,2)\) change with \(\delta\), and their
exact differences imply
\[
 \|X_3(\delta)-X_{3,0}\|_2
 \leq\|X_3(\delta)-X_{3,0}\|_F
 \leq {\sqrt{17}\over36}\delta=e\delta.
\]
Weyl's singular-value inequality gives the four extreme-value bounds
used in the evidence.  Since \(\rho_1>1/1300\),
\((e/\sqrt{\rho_1})\delta<1/2\) on \(0<\delta\leq1/10\).
Expanding the resulting quotient bounds proves the stated relative error
with \(\alpha=e/\sqrt{\rho_3}\),
\(\beta=e/\sqrt{\rho_1}\), and
\(M_3=\alpha+2\beta+2\alpha\beta\).  Thus
\((p_3,K_3)=(0,\sqrt{\rho_3/\rho_1})\).

### Case 4

For \(0<\delta\leq1\), the largest diagonal magnitude is
\(1/(3+\delta)\) and the smallest is \(1/13\).  Hence
\[
 \kappa_2(X_4)={13\over3+\delta},\qquad
 (p_4,K_4)=(0,13/3),
\]
and its relative error from \(13/3\) is
\(\delta/(3+\delta)\leq\delta/3\), as claimed.

## Checks performed and source comparison

I reran the supplied exact symbolic verifier successfully and separately
recomputed the determinant formulas, the \(D^TD\) trace and determinant,
the radical simplification, the Sturm variation counts, and the numerical
sizes needed in the ordering arguments.  As a non-probative sanity check,
80-digit singular-value calculations at the held-out rational values
\(\delta=1/10,1/100,1/10000\) gave normalized ratios tending to one for
cases 1--3; these calculations were not used as proof.

The hash-matched primary PDF defines \(\kappa_2\) using the smallest
nonzero singular value in its equation (2), gives the diagonal Hadamard
representation in Proposition 1, and in Example 6 uses the same four
matrices and 30 logarithmically spaced values in \([10^{-6},1]\).  The
paper reports only the empirical orders \(\delta^{-2},\delta^{-1}\), and
bounded behavior for the final two cases.  It does not give the exact
constants or the proved error bounds established here.  The PDF confirms
that the authors are Massimiliano Fasi and Behnam Hashemi; the different
author list in immutable `source.md` is a bibliographic error already
correctly identified in `problem.md`, not an ambiguity in the mathematical
scope.

The contribution is a complete exact resolution of all four frozen cases,
not a routine restatement of the paper's plotted observations.  The limited
literature screen is represented as such and makes no unsupported priority
claim.  No mathematical gap remains in the frozen candidate.  There are two
stray control characters before `eta` and `ho_1` in the case-3 prose of
`evidence/exact_asymptotics.md`; the intended \(\beta\) and \(\rho_1\) are
unambiguous from the surrounding displayed formulas and should be cleaned
up when typesetting, but this is editorial and does not alter the claim or
proof.

## Verdict

**Accept.**  The frozen scope, mathematical correctness and error control,
and the stated contribution all pass review.
