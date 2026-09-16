# Breakpoint-free proof of the universal identity

All extrema and distributions below are understood up to null sets. This is
harmless because changing the endpoint values of the indicators does not
change the cost measure or \(K_v\).

## A ladder lemma

Let \(\eta\) be a probability measure of finite support on the integers, and
suppose its support lies in \([L,H]\cap\mathbb Z\), where \(H-L\leq 3\). Form
the locally finite, infinite measure

\[
  \mu=\sum_{r\geq0}T_{2r}\eta,
\]

where \(T_a\) translates a measure upward by \(a\). Let
\(F(x)=\mu((-∞,x])\), let

\[
  \lambda(s)=\inf\{x:F(x)\geq s\}\qquad(s>0),
\]

and put \(K(s)=\int_0^s\lambda(t)\,dt\). Then

\[
  \lambda(s+1)=\lambda(s)+2\quad(s>1)                                      \tag{1}
\]

and, writing \(m=\int x\,d\eta(x)\),

\[
  K(s+1)-K(s)=2s+m\quad(s\geq1).                                           \tag{2}
\]

To prove (1), first observe that, for every real \(x\geq H-2\), each
progression \(h,h+2,h+4,\ldots\) contributes exactly one point to
\((x,x+2]\). Hence

\[
  F(x+2)=F(x)+1.                                                            \tag{3}
\]

Also \(F(H-2)\leq1\): since \(L\geq H-3\), a rung with \(r\geq1\) has value
at least \(L+2\geq H-1\), so only base rungs can lie at or below \(H-2\).
Thus, if \(s>1\), the quantile \(q=\lambda(s)\) satisfies \(q>H-2\). Both
the closed and open versions of (3) apply at \(q\):

\[
  F(q+2)=F(q)+1,
  \qquad \mu((-∞,q+2))=\mu((-∞,q))+1.
\]

The defining inequalities
\(\mu((-∞,q))<s\leq F(q)\) therefore become the defining inequalities
for \(q+2\) at mass \(s+1\). This proves (1), including masses that end at
an atom.

It remains to identify the integral over one quantile block. Let \(A\) and
\(B\) be the pushforwards under \(\lambda\) of Lebesgue measure on
\((0,1]\) and \((1,2]\), respectively. The standard generalized-inverse
identity

\[
  \bigl|\{s>0:\lambda(s)\leq x\}\bigr|=F(x)
\]

shows that \(\mu\) is the pushforward of Lebesgue measure under \(\lambda\).
By (1), its unit blocks decompose as

\[
  \mu=A+\sum_{j\geq0}T_{2j}B.                                              \tag{4}
\]

On the other hand, the ladder definition gives
\(\mu=\eta+T_2\mu\). Subtracting the translate of (4) from (4) (on every
bounded set only finitely many terms occur) gives

\[
  \eta=A+B-T_2A.                                                            \tag{5}
\]

Both \(A\) and \(B\) have mass one. Taking first moments in (5) yields

\[
  m=\int x\,dB(x)-2,
  \qquad\text{so}\qquad
  K(2)-K(1)=m+2.                                                            \tag{6}
\]

For \(D(s)=K(s+1)-K(s)\), equation (1) gives, first on
\(1\leq s\leq2\) by splitting off equal-length end pieces, and then by
integer translation,

\[
  D(s)-D(1)=2(s-1).
\]

Together with (6), this is (2).

## Application to the frozen \(h_v\)

Fix \(v\in[0,1)\), put \(a=\alpha(v)\), \(b=\beta(v)\), and let \(\eta_v\)
be the distribution of \(h_v(y)\) for uniform \(y\in[0,1)\). It is a
finitely supported probability measure on the integers.

The two sets \([0,a)\) and \([0,v)\) are nested. Consequently

\[
  p(z)=2\mathbf 1_{z<a}-\mathbf 1_{z<v}
\]

has oscillation at most two: its values lie in \(\{0,1,2\}\) if
\(a\geq v\), and in \(\{-1,0,1\}\) if \(a<v\). Adding the single
indicator \(\mathbf 1_{y>b}\) increases oscillation by at most one, while
the floor term in \(h_v\) is constant in \(y\). Therefore

\[
  \operatorname{osc}(h_v)\leq3                                             \tag{7}
\]

for every \(v\), including every floor and endpoint breakpoint. The ladder
lemma applies.

The map \(y\mapsto z(y)\) preserves Lebesgue measure. Write
\(q=\lfloor20v\rfloor\), \(a=20v-q\),
\(r=\lfloor41v\rfloor\), and \(b=41v-r\). Direct integration gives

\[
\begin{aligned}
 m_v:=\int_0^1h_v(y)\,dy
 &=2q-r+2a-v+(1-b)\\
 &=40v-r-v+1-b\\
 &=1-2v.                                                                   \tag{8}
\end{aligned}
\]

Apply (2) with \(s=j+v\geq1\). Equations (2) and (8) give, for every
integer \(j\geq1\),

\[
  K_v(j+1+v)-K_v(j+v)=2(j+v)+(1-2v)=2j+1.                                  \tag{9}
\]

For \(n=1\) the desired identity is tautological. For \(n\geq2\), summing
(9) over \(j=1,\ldots,n-1\) yields

\[
\begin{aligned}
 K_v(n+v)-K_v(1+v)
   &=\sum_{j=1}^{n-1}(2j+1)\\
   &=n^2-1.
\end{aligned}
\]

Hence, for every real \(v\in[0,1)\) and every integer \(n\geq1\),

\[
  \boxed{K_v(n+v)=n^2+K_v(1+v)-1}.
\]

This proof does not sample parameter cells: (7) and (8) hold identically,
so all breakpoint values are included. Its only source-specific inputs are
the definitions frozen in `source.md`; the ladder lemma itself applies to
any integer-valued base distribution of oscillation at most three.
