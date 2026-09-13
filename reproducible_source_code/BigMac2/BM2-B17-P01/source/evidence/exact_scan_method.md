# Exact finite scan method

This file documents the mathematics encoded by `exact_scan.py`.  It proves only
the finite statement for \(2001\le n\le100000\), not the frozen infinite claim.

Put \(t=n-2a+1\).  Lemma 7.3's adjacent ratio \(q_n(a)=R_n(a-1)/R_n(a)\)
satisfies, after clearing its positive denominator,
\[
\begin{aligned}
&a(a-1)(n-2a+3)-(n-a+1)^2(n-2a+1)\\
&\qquad=\tfrac12\{n^2-n(2t^2+3t)-t-1\}.
\end{aligned}
\]
Consequently the sign of \(q_n(a)-1\) is the sign of
\(H_n(t)=n^2-n(2t^2+3t)-t-1\).  As \(a\) increases, \(t\) decreases by two
and \(H_n(t)\) strictly increases.  Thus the first \(a_0\ge2\) with
\(H_n(n-2a_0+1)\ge0\) is the first nonincreasing step in the row, and
\(a_0-1\) is a row maximizer (with a second tied maximizer \(a_0\) only if the
threshold is zero).  Binary search therefore localizes a genuine row maximum.

For propagation between consecutive localized maxima, direct cancellation in
the defining binomial formula gives
\[
\frac{R_{n+1}(a)}{R_n(a)}=
\frac{(n+1)^2(n-1)(n-2a+2)}
 {2(2n-1)(n-a+1)^2(n-2a+1)}
\]
and
\[
\frac{R_{n+1}(a+1)}{R_n(a)}=
\frac{(n+1)^2(n-1)(n-2a)}
 {2(2n-1)a(a+1)(n-2a+1)}.
\]
The scan starts from the defining binomial formula at \(n=2001\), applies the
appropriate rational factor, and independently recomputes the defining formula
at six dispersed rows.  Each of the 98,000 localized maxima is held as a
reduced exact fraction and checked by integer cross-multiplication.  The output
in `exact_scan_results.json` records zero ties and zero violations.  Its largest
scanned value occurs at \((n,a)=(2001,985)\), where the recorded positive value
of `denominator_minus_numerator` certifies strict inequality exactly.
