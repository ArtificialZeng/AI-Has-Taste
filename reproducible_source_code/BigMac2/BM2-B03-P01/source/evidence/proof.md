# Proof of the fixed-periodic bound and equality classification

Let \(G=\mathbb Z/q\mathbb Z\), let \(r=|R|>0\), and put
\[
T=T_q(R)=\#\{(u,v)\in G^2:u,u+v,u+3v\in R\}.
\]
All constants implicit below may depend on the fixed modulus \(q\), but not on
\(N\).

## 1. Residue-class asymptotics in the two signed triangles

First,
\[
|A_N|=\sum_{a\in R}\#\{1\le n\le N:n\equiv a\pmod q\}
=\frac rqN+O_q(1).
\]

Fix \(u,v\in G\). For positive dilations define
\[
C^+_{u,v}(N)=\#\{(x,d)\in\mathbb Z^2:d\ge1,\ 1\le x,\ x+3d\le N,\ x\equiv u,\ d\equiv v\pmod q\}.
\]
The condition \(1\le x+d\le N\) is automatic in this region. Set
\(m=\lfloor(N-1)/3\rfloor\). For every admissible \(d\), the number of
\(x\equiv u\pmod q\) in \([1,N-3d]\) is
\[
\frac{N-3d}{q}+O(1).
\]
In any fixed residue class modulo \(q\), among \(1\le d\le m\) there are
\(m/q+O_q(1)\) terms and their sum is \(m^2/(2q)+O_q(m)\). Hence
\[
\begin{aligned}
C^+_{u,v}(N)
&=\frac1q\sum_{\substack{1\le d\le m\\d\equiv v\ (q)}}(N-3d)+O_q(N)\\
&=\frac1q\left(\frac{Nm}{q}-\frac{3m^2}{2q}+O_q(N)\right)+O_q(N)\\
&=\frac{N^2}{6q^2}+O_q(N),
\end{aligned}
\]
because \(m=N/3+O(1)\). This is the boundary estimate for the
positive-dilation triangle.

For negative dilations write \(e=-d\ge1\). The three interval conditions are
equivalent to
\[
1+3e\le x\le N;
\]
then \(x-e\) automatically lies in the interval. With \(x\equiv u\) and
\(d\equiv v\pmod q\), one has \(e\equiv-v\pmod q\). For each such \(e\le m\),
the interval \([1+3e,N]\) contains
\[
\frac{N-3e}{q}+O(1)
\]
integers congruent to \(u\). The identical arithmetic-progression estimate,
now in residue class \(-v\), gives
\[
C^-_{u,v}(N)=\frac{N^2}{6q^2}+O_q(N).
\]
This is the boundary estimate for the negative-dilation triangle.

The case \(v=0\) in both formulas consists of \(d=q,2q,\ldots\) in the
positive triangle and \(d=-q,-2q,\ldots\) in the negative triangle. Thus it
is part of the main term. The forbidden integer dilation \(d=0\) occurs in
neither triangle; it must not be confused with the residue condition
\(v=0\). Equivalently, adding and then deleting the line \(d=0\) would alter
the count by only \(|A_N|=O_q(N)\).

Membership of the three residues in \(R\) is exactly the condition defining
\(T\). Summing the last two estimates over those \(T\) residue pairs yields
\[
M(A_N)=\frac{T}{3q^2}N^2+O_q(N).
\]
Together with the estimate for \(|A_N|\), this proves existence of the limit
and the exact reduction
\[
L(q,R)=\lim_{N\to\infty}\frac{M(A_N)}{|A_N|^2}
=\frac{T_q(R)}{3r^2}.
\]

## 2. Finite inequality and equality case

The bijective change of variables
\[
(u,v)\longmapsto(a,b)=(u,u+v)
\]
rewrites the modular count as
\[
T_q(R)=\#\{(a,b)\in R^2:3b-2a\in R\}.
\]
Consequently \(T_q(R)\le r^2\), and equality holds exactly when
\[
3b-2a\in R\qquad(a,b\in R). \tag{*}
\]

Assume equality and choose \(c\in R\). For \(S=R-c\), condition (*) becomes
\[
3y-2x\in S\qquad(x,y\in S),
\]
and \(0\in S\). Taking \(x=0\) gives \(3S\subseteq S\); taking \(y=0\)
gives \(-2S\subseteq S\). Since multiplication by \(3\) and by \(-2\) is
injective on \(G\) under \(\gcd(q,6)=1\), finiteness gives
\[
3S=S=-2S.
\]
For arbitrary \(s,t\in S\), choose \(y,x\in S\) with \(3y=s\) and
\(-2x=t\). The displayed closure then gives \(s+t=3y-2x\in S\). Thus \(S\)
contains zero and is closed under addition. A finite additive submonoid of a
group is a subgroup: if \(z\in S\) has order \(k\), then
\(-z=(k-1)z\in S\). Hence \(S\le G\), and \(R=c+S\) is an additive-subgroup
coset.

Conversely, if \(R=c+H\) with \(H\le G\), then for
\(a=c+h_1,b=c+h_2\) one has
\[
3b-2a=c+(3h_2-2h_1)\in c+H.
\]
Therefore (*) holds, \(T_q(R)=r^2\), and \(L(q,R)=1/3\). In all other cases
\(T_q(R)<r^2\), so \(L(q,R)<1/3\). This proves both assertions in the frozen
problem.
