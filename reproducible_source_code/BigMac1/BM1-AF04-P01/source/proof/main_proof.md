# Proof: the A278992 recurrence follows from the EGF

Write (D=d/dt), (q=1-2t), and choose (s=q^{1/2}) with (s(0)=1).
Set

\[
E=e^{-1-t+s},\qquad U=E,\qquad V=E/s,\qquad G=(2-t)e^{-t}.
\]

Then (F=U+V-G).  Since (s'=-1/s), exact differentiation gives

\[
\begin{pmatrix}U\\V\\G\end{pmatrix}'=
A\begin{pmatrix}U\\V\\G\end{pmatrix},\qquad
A=\begin{pmatrix}
-1&-1&0\\
-1/q&1/q-1&0\\
0&0&(t-3)/(2-t)
\end{pmatrix}.
\tag{1}
\]

In particular, for (H=U+V), elimination in the first two rows yields

\[
(4t^2-1)H''+(8t^2+2t+3)H'+(4t^2+4t+7)H=0,
\tag{2}
\]

whereas

\[
(2-t)G'+(3-t)G=0.
\tag{3}
\]

Thus the two pieces of the given EGF are individually D-finite.

## Combined annihilator and exact symbolic identity

Let (X=(U,V,G)^T), (r_0=(1,1,-1)), and recursively define

\[
r_{k+1}=r_k'+r_kA.
\]

Then (F^{(k)}=r_kX).  Direct rational-function arithmetic gives the
componentwise identity

\[
p_3r_3+p_2r_2+p_1r_1+p_0r_0=(0,0,0),
\tag{4}
\]

where

\[
\begin{aligned}
p_3&=(t+1)(2t-1)^2=4t^3-3t+1,\\
p_2&=(2t-1)(6t^2+4t+1)=12t^3+2t^2-2t-1,\\
p_1&=3(4t^3+2t^2+2t-5),\\
p_0&=4t^3+4t^2+3t-18.
\end{aligned}
\]

For completeness, the four rows used in (4) are

\[
\begin{aligned}
r_0={}&\left(1,1,-1\right),\\
r_1={}&\left(
\frac{-2(t-1)}{2t-1},
\frac{-(4t-1)}{2t-1},
\frac{t-3}{t-2}\right),\\
r_2={}&\left(
\frac{4t^2-10t+1}{(2t-1)^2},
\frac{4(3t^2-2t+1)}{(2t-1)^2},
\frac{-(t-4)}{t-2}\right),\\
r_3={}&\left(
\frac{-(8t^3-36t^2+8t-11)}{(2t-1)^3},
\frac{-(32t^3-40t^2+28t+7)}{(2t-1)^3},
\frac{t-5}{t-2}\right).
\end{aligned}
\]

It follows from (4) that

\[
\mathcal L_3F:=p_3F'''+p_2F''+p_1F'+p_0F=0.
\tag{5}
\]

This is already a polynomial-coefficient ODE proving D-finiteness.

## A polynomial left multiple adapted to the OEIS recurrence

Differential-operator multiplication is composition, so derivatives act on
coefficients to their right.  Define

\[
\mathcal M=
\frac{t}{(t+1)(2t-1)}D^2
+\frac{t-2}{(t+1)^2(2t-1)^2}D
-\frac{1}{(t+1)^2(2t-1)^2}.
\]

An exact use of (D^i f=\sum_{r=0}^i\binom{i}{r}f^{(r)}D^{i-r})
gives the Ore-algebra identity

\[
\boxed{\mathcal M\circ\mathcal L_3=\mathcal L_5},
\tag{6}
\]

where

\[
\boxed{\begin{aligned}
\mathcal L_5={}&t(2t-1)D^5+(6t^2+10t-2)D^4\\
&+(6t^2+36t+7)D^3+(2t^2+37t+35)D^2\\
&+(12t+39)D+12.
\end{aligned}}
\tag{7}
\]

The denominators in (mathcal M) have nonzero constant terms.  Hence (6) is
valid over (mathbb Q[[t]]); applying it to (5) proves
(mathcal L_5F=0).

## Exact coefficient extraction

For (m,j,k\ge0), the EGF convention gives

\[
\left[\frac{t^m}{m!}\right]t^jF^{(k)}
=(m)_j a_{m-j+k},
\qquad (m)_j=m(m-1)\cdots(m-j+1).
\tag{8}
\]

Fix (n\ge4) and put (m=n-4).  Applying (8) to (7) and collecting like
coefficients gives the following complete table.

| coefficient | contribution before (m=n-4) | result |
|---|---:|---:|
| (a_n) | (-m-2) | (2-n) |
| (a_{n-1}) | (2m(m-1)+10m+7) | (2n^2-8n+7) |
| (a_{n-2}) | (6m(m-1)+36m+35) | (6n^2-18n+11) |
| (a_{n-3}) | (6m(m-1)+37m+39) | ((n-1)(6n-11)) |
| (a_{n-4}) | (2m(m-1)+12m+12) | (2(n-1)(n-2)) |

The coefficient of (t^{n-4}/(n-4)!) in (mathcal L_5F=0) is therefore
exactly

\[
\begin{aligned}
0={}&(2-n)a_n+(2n^2-8n+7)a_{n-1}
+(6n^2-18n+11)a_{n-2}\\
&+(n-1)(6n-11)a_{n-3}
+2(n-1)(n-2)a_{n-4}.
\end{aligned}
\]

This proves the recurrence for every (n\ge4).

## Initial values and OEIS offset

Exact formal expansion gives

\[
F(t)=\frac{t^2}{2!}+\frac{t^3}{3!}
+21\frac{t^4}{4!}+168\frac{t^5}{5!}
+1968\frac{t^6}{6!}+\cdots.
\]

Thus ((a_0,a_1,a_2,a_3)=(0,0,1,1)), which is the initial block needed
for the recurrence at (n\ge4).  Since OEIS has offset (1), an equivalent
OEIS-native statement begins the recurrence at (n=5) and uses
((a_1,a_2,a_3,a_4)=(0,1,1,21)).  The (n=4) identity is valid after the
canonical EGF extension (a_0=0).
