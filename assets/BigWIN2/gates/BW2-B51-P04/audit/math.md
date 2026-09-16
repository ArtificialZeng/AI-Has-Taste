# Fresh mathematical referee report

## Scope and frozen inputs

I reviewed the exact `resolution-paper` claim in `claim.json`, bound to snapshot
digest `3b5ed735a8ac797cc4f155e461a10464ce1136d8aeab5aee3802db6f8f19f561`.
Fresh SHA-256 calculations matched every entry in `audit/snapshot.json`.  PDF
pages 2 and 22 of the frozen primary source confirm, respectively, the general
generating function and the first line of Conjecture 7.1.  Substitution of
\((r,s,k)=(4,2,4)\) gives exactly
\[
 F=f_4^8/(f_1^{16}f_2^8)=\sum_{n\geq0}a(n)q^n,
\]
so proving \(U_5(F)\equiv1\pmod 5\) is equivalent to the full original claim
for every \(n\geq1\); no scope reduction is present.

## Reconstruction of the proof

Set
\[
 A(z)=\frac{\eta(4z)^8\eta(5z)^{120}}
 {\eta(z)^{16}\eta(2z)^8}.
\]
Its exponent vector at level 20 is
\((r_1,r_2,r_4,r_5)=(-16,-8,8,120)\).  I independently recalculated
\[
 \frac12\sum r_\delta=52,\qquad
 \sum\delta r_\delta=600\equiv0\pmod {24},\qquad
 \sum(20/\delta)r_\delta=120\equiv0\pmod {24}.
\]
Also \(\prod\delta^{r_\delta}=2^8 5^{120}\) is a square, so the quadratic
character is trivial.  Applying the eta-quotient cusp-order formula at every
denominator \(d\mid20\) gives, in the order
\(d=1,2,4,5,10,20\),
\[
 (5,0,5,97,24,25).
\]
All are nonnegative.  Thus \(A\in M_{52}(\Gamma_0(20))\), and the standard
operator \(U_5\), with \(5\mid20\), preserves this space.

Consequently
\[
 C=E_4^2U_5(A)-\Delta^5
\]
is in \(M_{60}(\Gamma_0(20))\) and has integral Fourier coefficients.  The
index is
\([\mathrm{SL}_2(\mathbb Z):\Gamma_0(20)]=20(1+1/2)(1+1/5)=36\), hence the
Sturm bound is \(60\cdot36/12=180\).  Since all nonconstant coefficients of
\(E_4\) are divisible by 240, checking \(C\equiv0\pmod5\) through this bound
is exactly the same as checking
\(U_5(A)\equiv\Delta^5\pmod5\) through degree 180.

The eta shifts are also correct:
\[
 A=q^{25}f_5^{120}F=D(q^5)F(q),\qquad
 D(q)=q^5f_1^{120}=\Delta^5.
\]
Direct coefficient convolution gives
\(U_5(D(q^5)F(q))=D(q)U_5(F(q))\).  Therefore the Sturm conclusion implies
\[
 0\equiv C\equiv\Delta^5(U_5(F)-1)\pmod5.
\]
The series \(\Delta^5=q^5f_1^{120}\) is nonzero in the integral domain
\(\mathbb F_5[[q]]\), so cancellation proves \(U_5(F)\equiv1\pmod5\).

## Computational checks actually performed

I reran the frozen certificate; it checked degrees 0 through 180 and returned
an empty failure list.  I also implemented a separate in-memory coefficient
calculation.  Instead of the certificate's repeated multiplication by
\((1-q^m)^{\pm1}\), this calculation multiplied positive powers using binomial
coefficients and solved the finite recurrence obtained from
\((1-q^m)^sQ=P\) for each negative Euler factor.  It independently constructed
\(A\) through degree 900 and \(\Delta^5\) through degree 180 over
\(\mathbb F_5\).  The 181 comparisons
\([q^n]U_5(A)=[q^n]\Delta^5\), \(0\le n\le180\), again had no failures.
The truncation degree 900 is exactly \(5\cdot180\), so no required input
coefficient was omitted.

## Source comparison, gaps, and verdict

The frozen source calls this exact statement conjectural and says its listed
congruences rest on computational evidence.  The frozen literature report
records a same-day bounded search finding no separate resolution, while
explicitly disclaiming exhaustiveness and priority.  I did not treat that
search as proof of novelty.  The submitted contribution nevertheless supplies
a complete all-indices proof of the frozen original conjecture, rather than a
finite coefficient check or subsidiary result.

I found no mathematical gap, hypothesis mismatch, equality exception, or
scope failure.  **Verdict: accept.**
