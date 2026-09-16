# Formal statement

## Corrected definition

There is a unique sequence \(a:\mathbb N\to\mathbb Z_{>0}\) with
\(a_0=4,a_1=16\) and, for every \(n\ge0\),
\[
a_{n+2}=\begin{cases}
\left\lceil a_{n+1}^2/a_n\right\rceil-1,&n\text{ even},\\
\left\lfloor a_{n+1}^2/a_n\right\rfloor+1,&n\text{ odd}.
\end{cases}
\]
The positivity needed to keep this definition meaningful is part of the
statement to be proved (and follows immediately once the displayed formula is
shown to produce positive terms).

Equivalently, provided \(a_n,a_{n+1}>0\), for even \(n\), \(a_{n+2}\) is the
greatest integer \(m\) satisfying
\(m/a_{n+1}<a_{n+1}/a_n\); for odd \(n\), it is the least integer \(m\)
satisfying the reverse strict inequality.  The ceiling-minus-one convention
is essential when \(a_n\mid a_{n+1}^2\).

## Conjectured endpoint

Prove or disprove that, for every integer \(n\ge4\),
\[
a_n=4a_{n-1}-a_{n-3}+a_{n-4}.
\]

Equivalently, let \(L_0=4,L_1=16,L_2=63,L_3=249\) and
\(L_n=4L_{n-1}-L_{n-3}+L_{n-4}\) for \(n\ge4\).  It is enough to prove
\(L_n>0\) and, with
\(d_n=L_{n+1}^2-L_nL_{n+2}\),
\[
1\le d_n\le L_n\quad(n\text{ even}),\qquad
-L_n\le d_n\le-1\quad(n\text{ odd}).
\]

## Quantifiers and conventions

All indices are natural numbers starting at zero; all divisions in the
extremal formulation are divisions of positive real numbers; `greatest' and
`least' range over all integers.  Strict inequalities are literal.  No claim
is made here about the obsolete nonalternating definition recorded in the
comments of OEIS A022030.
