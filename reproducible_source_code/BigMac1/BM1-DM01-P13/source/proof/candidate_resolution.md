# Candidate proof of FS1 — awaiting independent audit

Status: **candidate only**.  The argument below has not passed the resolution
gate.  It replaces the two empirical kernels HC1 and LC1 by a direct
Legendre--Lucas lift.  Throughout, (p\geq5) is prime,

\[
h=\frac{p-1}{2},\qquad N=\frac{p^2-1}{2}=hp+h,
\qquad z^2=-63.
\]

All congruences involving (z) are in

\[
R_e=(\mathbb Z/p^e\mathbb Z)[z]/(z^2+63).
\]

For the target classes (p\bmod7\in\{3,5,6\}), one has (p\ne3,7) in
the present part of the proof and

\[
\left(\frac{-63}{p}\right)=\left(\frac{-7}{p}\right)
=\left(\frac p7\right)=-1.
\]

Thus (R_1\) is a field, while (z,u=(z+1)/2), and (v=(z-1)/2) are
units; indeed (uv=(z^2-1)/4=-16).

## Lemma C1: Clausen bridge from the original sum

For every eligible (p\ge5),

\[
A(p^2)-8\equiv P_N(z)^2\pmod {p^3}. \tag{C1}
\]

### Proof

Clausen's terminating identity gives, exactly over the rationals,

\[
P_N(z)^2={}_3F_2\!\left(
\begin{matrix}-N,N+1,\tfrac12\\1,1\end{matrix};1-z^2\right).
\]

At (z^2=-63), its (k)-th term is

\[
t_kR_k,\qquad t_k=\binom{2k}{k}^3,
\qquad
R_k=\prod_{j=0}^{k-1}
\left(1-\frac{p^4}{(2j+1)^2}\right). \tag{C2}
\]

No odd number (2j+1<p^2) is divisible by (p^2).  Hence every factor
in (C2) is (p)-integral, including those for which (p\mid2j+1).
Kummer's theorem shows that (t_k\equiv0\pmod {p^3}) unless, on writing
(k=ap+b), both digits satisfy (0\le a,b\le h).  The largest such
index is (hp+h=N).  Therefore all terms outside this rectangle may be
discarded modulo (p^3), both in (A(p^2-1)) and in (C2).

For a surviving (k=ap+b), the multiples of (p) among
(1,3,\ldots,2k-1) are precisely (p(2r+1)), (0\le r<a).  Consequently

\[
R_{ap+b}\equiv1-p^2E_a\pmod {p^3},
\qquad E_a=\sum_{r=0}^{a-1}\frac1{(2r+1)^2}\in\mathbb F_p.
\]

Lucas' theorem, with no carry in either digit, gives
(t_{ap+b}\equiv t_at_b\pmod p).  It follows that the total correction
to (A(p^2-1)) is

\[
-p^2\left(\sum_{a=0}^h t_aE_a\right)
       \left(\sum_{b=0}^h t_b\right)\pmod {p^3}.
\]

Zhi-Hong Sun's Theorem 3.2 gives
(\sum_{b=0}^h t_b\equiv0\pmod {p^2}) in the target residue classes, so
this correction is zero.  Finally, the already proved special Jacobsthal
congruence gives (t_{p^2}\equiv8\pmod {p^3}).  This proves (C1).

## Lemma C2: the Legendre--Lucas lift at a trace-zero root

Suppose (p\ge5), ((-63/p)=-1), and
(P_h(z)\equiv0\pmod p).  Then

\[
P_N(z)\equiv(-1)^h p\pmod {p^2}. \tag{C3}
\]

### A binomial identity used in the lift

For (0\le a,b\le h), expansion of the three unit factorial tails and
the special Jacobsthal congruence give

\[
\binom{ph+h}{pa+b}
\equiv \binom ha\binom hb(1+pE_{a,b})\pmod {p^2}, \tag{C4}
\]

where

\[
E_{a,b}=hH_h-aH_b-(h-a)H_{h-b}
=h(H_h-H_{h-b})+a(H_{h-b}-H_b). \tag{C5}
\]

Indeed, for (0\le s\le r<p),

\[
\binom{pA+r}{pB+s}
=\binom{pA}{pB}
\frac{\prod_{i=1}^r(pA+i)}
{\prod_{i=1}^s(pB+i)\prod_{i=1}^{r-s}(p(A-B)+i)},
\]

and first-order expansion of the products proves (C4) directly.

We also use the finite companion identity

\[
\sum_{b=0}^h\binom hb^2u^bv^{h-b}(H_{h-b}-H_b)=-W_h(z), \tag{C6}
\]

where

\[
W_h(z)=\sum_{j=1}^h\frac1jP_{j-1}(z)P_{h-j}(z).
\]

Identity (C6) is an identity over (\mathbb Q[z]).  One direct proof is
to denote its left side by (D_h), use Pascal's identity and
(H_{m+1}=H_m+1/(m+1)), and verify

\[
(h+1)D_{h+1}=(2h+1)zD_h-hD_{h-1},
\qquad D_0=0,\quad D_1=-1.
\]

The generating function

\[
\sum_{h\ge0}W_h(z)t^h
=(1-2zt+t^2)^{-1/2}
  \int_0^t(1-2zs+s^2)^{-1/2}\,ds
\]

gives the same recurrence with (W_0=0,W_1=1), proving (C6).

### Proof of the lift

The Bernstein form of the Legendre polynomial is

\[
P_N(z)=\sum_{k=0}^N\binom Nk^2u^kv^{N-k}. \tag{C7}
\]

Lucas' theorem shows that a summand of (C7) can survive modulo (p^2)
only when (k=pa+b) with (0\le a,b\le h); otherwise
(p\mid\binom Nk), and the square vanishes modulo (p^2).

Because (z^p=-z) in (R_1),

\[
u^p\equiv-v\pmod p,\qquad v^p\equiv-u\pmod p.
\]

Since (u,v) are units, there are (alpha,\beta\in R_1) such that, for
arbitrary lifts to (R_2),

\[
u^p=-v(1+p\alpha),\qquad v^p=-u(1+p\beta). \tag{C8}
\]

Insert (C4) and (C8) into (C7).  Put

\[
 A_a=\binom ha^2u^{h-a}v^a,
 \qquad B_b=\binom hb^2u^bv^{h-b}.
\]

Both (\sum_aA_a) and (\sum_bB_b) equal (P_h(z)).  The constant
term, every Frobenius correction from (alpha,beta), and the first
term in (C5) therefore contain a factor (P_h(z)); after the outside
factor (p), they vanish modulo (p^2).  The sole remaining coupled
term is

\[
P_N(z)\equiv(-1)^h,2p
\left(\sum_{a=0}^h aA_a\right)
\left(\sum_{b=0}^hB_b(H_{h-b}-H_b)\right)\pmod {p^2}. \tag{C9}
\]

Let (C_1=\sum_b bB_b).  Replacing (a) by (h-a) and using
(P_h(z)=0) in (R_1) gives

\[
\sum_a aA_a=-C_1.
\]

Differentiating the Bernstein form for (P_h), then using
(u'=v'=1/2), (v-u=-1), (uv=-16), and (P_h(z)=0), yields

\[
P_h'(z)=C_1\left(\frac1{2u}-\frac1{2v}\right)=\frac{C_1}{32}.
\]

Thus the first factor in (C9) is (-32P_h'(z)), while (C6) says that
the second is (-W_h(z)).  The polynomial Bezout--Wronskian identity

\[
(1-z^2)(P_h'W_h-P_hW_h')=1-P_h^2
\]

therefore gives, at the root,

\[
P_h'(z)W_h(z)=\frac1{1-z^2}=\frac1{64}.
\]

The product in (C9) is consequently
(2(-32P_h')(-W_h)=1), proving (C3).

## Candidate conclusion

Sun's Theorem 2.5 supplies (P_h(z)=0) in (R_1) for every eligible
(p\ge5).  Lemma C2 then implies

\[
P_N(z)^2\equiv p^2\pmod {p^3}.
\]

Lemma C1 gives (A(p^2)\equiv8+p^2\pmod {p^3}).  The excluded small
prime (p=3) was independently computed exactly:

\[
A(9)=117106008311825\equiv17=8+3^2\pmod {27}.
\]

Subject to a fresh audit of C1--C9 and the two cited Sun endpoints, this
proves FS1 for every prime (p\equiv3,5,6\pmod7).

## Audit warnings

- This file is not an accepted proof and does not authorize a paper or PDF.
- The earlier HC1 and LC1 remain unproved; the candidate proof bypasses them.
- No proof assistant was used.
- The current owner context cannot set `independent_audit_passed=true`.
