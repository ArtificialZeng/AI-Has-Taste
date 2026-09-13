# Exact resolution of the family \((1,4,5,6,7,m)\)

This note proves the full formula and equality classification requested in
`source.md`.  All times below are elements of \(\mathbb R/\mathbb Z\), and
\(D=\mathbb Z_{>0}\setminus\{1,4,5,6,7\}\).

## Theorem

For every \(m\in D\), the following mutually exclusive cases hold.

1. If \(11\nmid m\), then
   \[
     L(m)=\frac2{11}.
   \]
   Writing \(r\equiv m\pmod {11}\), the complete maximizer set is
   \[
   A(m)=
   \begin{cases}
   \{4/11,7/11\},&r\in\{2,9\},\\
   \{5/11,6/11\},&r\in\{3,8\},\\
   \{4/11,5/11,6/11,7/11\},
       &r\in\{1,4,5,6,7,10\}.
   \end{cases}
   \]
2. If \(m=11\), then
   \[
      L(m)=\frac2{13},\qquad A(m)=\{4/13,9/13\}.
   \]
3. If \(m=22\), then
   \[
      L(m)=\frac2{13},\qquad
      A(m)=\{4/13,6/13,7/13,9/13\}.
   \]
4. If \(m=11n\) with \(n\ge3\), put \(Q=11n+4\).  Then
   \[
      L(m)=\frac{2n}{Q},\qquad
      A(m)=\left\{\frac{5n+2}{Q},\frac{6n+2}{Q}\right\}.
   \]
   (The two displayed times sum to one.)

Consequently, with the strict definition in `source.md`, the near-tight
parameters are exactly
\[
   \{m\in D:1/7<L(m)<1/6\}=\{11,22,33\}.
\]

## Proof

Set
\[
 g(t)=\min_{v\in\{1,4,5,6,7\}}\|vt\|.
\]
We first record the small piece of the graph of \(g\) which controls the
whole problem.  By the symmetry \(g(1-t)=g(t)\), restrict to
\(0\le t\le1/2\).  The condition \(\|vt\|\ge2/13\) says that the fractional
part of \(vt\) belongs to \([2/13,11/13]\).  For \(v=1,4,5,6,7\), respectively,
the allowed sets in \([0,1/2]\) are
\[
\begin{array}{c|l}
v&\{t:\|vt\|\ge2/13\}\cap[0,1/2]\\ \hline
1 &[2/13,1/2]\\
4 &[1/26,11/52]\cup[15/52,6/13]\\
5 &[2/65,11/65]\cup[3/13,24/65]\cup[28/65,1/2]\\
6 &[1/39,11/78]\cup[5/26,4/13]\cup[14/39,37/78]\\
7 &[2/91,11/91]\cup[15/91,24/91]\cup[4/13,37/91]
       \cup[41/91,1/2].
\end{array}
\]
Their intersection is exactly
\[
 \{4/13\}\ \cup\ I_4\ \cup\ I_5,
 \qquad
 I_4=[14/39,24/65],\quad I_5=[41/91,6/13].                 \tag{1}
\]
Direct substitution on these two intervals gives
\[
 g(t)=
 \begin{cases}
   \min(6t-2,\,2-5t),&t\in I_4,\\
   \min(7t-3,\,2-4t),&t\in I_5,
 \end{cases}                                                \tag{2}
\]
while \(g(4/13)=2/13\).  The two triangular functions in (2)
peak at \(4/11\) and \(5/11\), respectively, both with value \(2/11\).
Thus
\[
 \max g=2/11,\qquad
 \operatorname*{argmax}g=\{4/11,5/11,6/11,7/11\}.           \tag{3}
\]

Suppose first that \(11\nmid m\), and put \(r=m\bmod 11\).
The extra coordinate at the four times in (3) is determined by
\(\|4r/11\|\) for the pair \(\{4/11,7/11\}\) and by
\(\|5r/11\|\) for the pair \(\{5/11,6/11\}\).  Reducing the ten nonzero
residues gives
\[
\begin{array}{c|c|c|c}
r&11\|4r/11\|&11\|5r/11\|&\text{pairs whose value is at least }2/11\\ \hline
1&4&5&\text{both}\\
2&3&1&\{4/11,7/11\}\\
3&1&4&\{5/11,6/11\}\\
4&5&2&\text{both}\\
5&2&3&\text{both}\\
6&2&3&\text{both}\\
7&5&2&\text{both}\\
8&1&4&\{5/11,6/11\}\\
9&3&1&\{4/11,7/11\}\\
10&4&5&\text{both}.
\end{array}
\]
At least one base maximizer therefore remains a maximizer after adjoining
\(m\), proving the lower bound \(2/11\); (3) proves the matching upper
bound and also proves that the table lists every equality time.  This proves
case 1.

It remains to take \(m=11n\).  First let \(n\ge3\), and define
\[
 Q=11n+4,\qquad q=\frac{2n}{Q},\qquad
 \Delta=\frac2{11}-q=\frac8{11Q}.                            \tag{4}
\]
Here \(2/13<q<2/11\).  Equations (1)--(2) show that, in the half-circle,
\(g(t)\ge q\) precisely on
\[
 J_4=\left[\frac4{11}-\frac{\Delta}{6},
            \frac4{11}+\frac{\Delta}{5}\right],\qquad
 J_5=\left[\frac5{11}-\frac{\Delta}{7},
            \frac5{11}+\frac{\Delta}{4}\right].             \tag{5}
\]
For \(t=4/11+x\in J_4\),
\[
 |11nx|\le \frac{11n\Delta}{5}=\frac{8n}{5Q}<q<\frac12,
\]
and hence \(\|11nt\|=|11nx|<q\).  For
\(t=5/11+x\in J_5\), the negative endpoint has
\(11n|x|=8n/(7Q)<q\), while the positive endpoint has
\[
 11nx=\frac{11n\Delta}{4}=q.
\]
Throughout \(J_5\), therefore, \(\|11nt\|\le q\), with equality only at
the positive endpoint.  That endpoint is
\[
 \frac5{11}+\frac{\Delta}{4}
   =\frac{5n+2}{11n+4},                                      \tag{6}
\]
and (2) gives \(g(t)=q\) there.  Outside (5), \(g(t)<q\).
Thus (6) is the unique maximizing time in \([0,1/2]\), and reflection gives
its complement \((6n+2)/(11n+4)\).  This proves case 4, including the full
equality set.

Finally take \(n=1,2\) and put \(q_0=2/13\),
\(\Delta_0=2/11-q_0=4/143\).  On \(I_4\), writing
\(t=4/11+x\),
\[
 |11nx|\le \frac{11n\Delta_0}{5}=\frac{44n}{715}<q_0
 \quad(n\le2).                                                \tag{7}
\]
On \(I_5\), writing \(t=5/11+x\), the negative endpoint gives
\(11n|x|=44n/1001<q_0\), and the positive endpoint gives
\[
 11nx=\frac{11n\Delta_0}{4}=\frac n{13}\le q_0,              \tag{8}
\]
with equality exactly when \(n=2\); its time is then \(6/13\).
All quantities in (7)--(8) are below \(1/2\), so they equal the corresponding
circle norms.  The isolated point \(4/13\) in (1) has
\[
 \|11(4/13)\|=5/13,qquad \|22(4/13)\|=3/13,
\]
so it works for both \(n=1\) and \(n=2\).  Equation (1), together with
(7)--(8), proves that these are all equality times in the half-circle and
that no value above \(q_0\) is possible.  Reflection proves cases 2 and 3.

For the last assertion, \(2/11>1/6\), while \(2/13\) lies strictly between
\(1/7\) and \(1/6\).  For \(n\ge3\),
\[
 \frac{2n}{11n+4}<\frac16\quad\Longleftrightarrow\quad n<4.
\]
Hence only \(n=1,2,3\), namely \(m=11,22,33\), satisfy both strict
near-tight inequalities.  This completes the proof.
