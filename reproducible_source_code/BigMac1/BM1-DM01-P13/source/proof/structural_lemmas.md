# Exact structural reduction (not a proof of FS1)

Throughout this file (p\ge5) is prime, (h=(p-1)/2), (B_k=\binom{2k}{k}), and (t_k=B_k^3). All harmonic numbers occurring below have indices at most (p-1), so their denominators are (p)-adic units.

## Lemma L1: the special Jacobsthal congruence

For integers (M\ge N\ge0),

\[
\binom{pM}{pN}\equiv\binom MN\pmod {p^3}.
\]

Proof. For (q\ge0), let (R(q)) be the product of the integers in ({1,\ldots,pq}) not divisible by (p). Splitting into blocks gives

\[
R(q)=\prod_{r=0}^{q-1}\prod_{j=1}^{p-1}(rp+j).
\]

Modulo (p^3), each inner product is ((p-1)!), because

\[
\prod_{j=1}^{p-1}\left(1+\frac{rp}{j}\right)
\equiv 1+rpH_{p-1}+\frac{r^2p^2}{2}
\left(H_{p-1}^2-H_{p-1}^{(2)}\right)\equiv1\pmod{p^3}.
\]

Here (H_{p-1}\equiv0\pmod{p^2}) follows by pairing (j) with (p-j) and using (sum_{j=1}^{p-1}j^{-2}\equiv0\pmod p); the latter is the usual nonzero finite-field power sum. Thus (R(q)\equiv((p-1)!)^q\pmod{p^3}). Removing the multiples of (p) from the three factorials gives

\[
\binom{pM}{pN}=\binom MN\frac{R(M)}{R(N)R(M-N)}\equiv\binom MN\pmod{p^3}.
\]

In particular, (B_{ap}\equiv B_a\pmod{p^3}), and applying L1 twice gives

\[
B_{p^2}=\binom{2p^2}{p^2}\equiv\binom{2p}{p}\equiv2\pmod{p^3},
\qquad t_{p^2}\equiv8\pmod{p^3}.
\]

## Lemma L2: exact no-carry support

For (0\le k<p^2), write (k=ap+b) with (0\le a,b<p). Kummer's carry formula gives

\[
v_p(B_k)=\text{the number of carries when (k+k) is added in base (p)}.
\]

Therefore (t_k\not\equiv0\pmod{p^3}) is possible exactly when (0\le a,b\le h). Consequently

\[
A(p^2)\equiv t_{p^2}+\sum_{a=0}^h\sum_{b=0}^h t_{ap+b}\pmod{p^3}.
\]

This is a proved representation obstruction: every carry stratum is identically zero at the required modulus and cannot contain a counterexample contribution.

## Lemma L3: block expansion

Define

\[
L_b=2(H_{2b}-H_b),\qquad
M_b=H_b^{(2)}-2H_{2b}^{(2)}.
\]

For (0\le a,b\le h), L1 and the factorial quotient give

\[
\begin{aligned}
B_{ap+b}
&=B_{ap}B_b
\frac{\prod_{j=1}^{2b}(1+2ap/j)}
{\prod_{j=1}^{b}(1+ap/j)^2}\\
&\equiv B_aB_b\left(1+paL_b+p^2a^2
\left(M_b+\frac12L_b^2\right)\right)\pmod{p^3}.
\end{aligned}
\]

Cubing and summing yields the exact reduction

\[
\sum_{a,b=0}^h t_{ap+b}
\equiv S^2+3pXU+3p^2YV\pmod{p^3}, \tag{R}
\]

where

\[
\begin{aligned}
S&=\sum_{k=0}^h t_k,&
X&=\sum_{k=0}^h kt_k,&
Y&=\sum_{k=0}^h k^2t_k,\\
U&=\sum_{k=0}^h t_kL_k,&
V&=\sum_{k=0}^h t_k\left(M_k+\frac32L_k^2\right).
\end{aligned}
\]

The expansion uses only finite products of (p)-adic units; no formal logarithm outside its valid truncated power-series use is required.

## Lemma L4: known half-sum and the squared Legendre polynomial

Zhi-Hong Sun's Theorem 3.2 proves

\[
S\equiv0\pmod{p^2}
\]

when (p\equiv3,5,6\pmod7). An exact polynomial identity used in the same paper gives, modulo (p),

\[
F(x):=\sum_{k=0}^h t_kx^k
\equiv P_h\!\left(\sqrt{1-64x}\right)^2. \tag{P}
\]

For the eligible residue classes, Sun's Theorem 2.5 gives (P_h(z)=0) in the quadratic (mathbb F_p)-algebra with (z^2=-63). Applying (D=x\,d/dx) to (P) at (x=1) proves

\[
X\equiv0\pmod p,
\qquad
Y\equiv-\frac{2048}{63}P_h'(z)^2\pmod p. \tag{Y}
\]

The second formula uses (D^2F(1)=F''(1)), since (F'(1)=0), and (dz/dx=-32/z).

## Lemma L5: proved Legendre-companion Wronskian

Set

\[
W_h(z):=\sum_{j=1}^{h}\frac1jP_{j-1}(z)P_{h-j}(z).
\]

The standard second Legendre solution can be written

\[
Q_h(z)=\frac12P_h(z)\log\frac{1+z}{1-z}-W_h(z).
\]

Substitution in the Legendre recurrence verifies this finite companion formula, while the second-order differential equation gives

\[
P_hQ_h'-P_h'Q_h=\frac1{1-z^2}.
\]

At a root (P_h(z)=0) with (z^2=-63), these two identities give

\[
P_h'(z)W_h(z)=\frac1{64}. \tag{W}
\]

All denominators (1,\ldots,h) and (64) are units modulo eligible (p\ge5); (W) also proves that the root is simple.

## The unresolved kernel

The computation has isolated two unproved finite congruences:

\[
U\equiv0\pmod p, \tag{HC1}
\]

and, for (z^2=-63) in (mathbb F_p[z]/(z^2+63)),

\[
V\equiv-42W_h(z)^2\pmod p. \tag{LC1}
\]

They are not asserted as theorems. If HC1 and LC1 hold, (Y) and (W) imply

\[
3YV=3\left(-\frac{2048}{63}P_h'(z)^2\right)
\left(-42W_h(z)^2\right)\equiv1\pmod p.
\]

Since (S\equiv0\pmod{p^2}), (X\equiv0\pmod p), and HC1 gives (U\equiv0\pmod p), reduction (R) becomes

\[
\sum_{a,b=0}^h t_{ap+b}\equiv p^2\pmod{p^3}.
\]

Together with (t_{p^2}\equiv8\pmod{p^3}), this proves FS1 for every eligible (p\ge5). The remaining prime (p=3) is independently exact-checked. Thus HC1+LC1 are a strictly finite, lower-modulus kernel that implies the original claim, but neither missing congruence has been proved in this research block.
