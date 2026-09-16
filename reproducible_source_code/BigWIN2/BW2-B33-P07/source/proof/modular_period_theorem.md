# A universal modular-period theorem

## Statement

For (M=2^k), let (R_M=\mathbb Z/M\mathbb Z), and let

\[
T_j(x,y)=(y,(y\mathbin{\mathrm{XOR}}j)-x)\qquad ((x,y)\in R_M^2),
\]

where XOR means XOR of the lowest (k) bits.  Put

\[
P_M=T_{M-1}\circ\cdots\circ T_1\circ T_0.
\]

Then

\[
P_M^3=\operatorname{id}_{R_M^2}. \tag{1}
\]

Consequently every solution of the recurrence, from every initial pair and
every starting phase, is periodic modulo (2^k) with period dividing
(3\cdot2^k).  In particular, the sequence in the problem satisfies

\[
a_{n+3\cdot2^k}\equiv a_n\pmod {2^k}
\quad(k\geq 0,\ n\geq0). \tag{2}
\]

This proves the former candidate C001, in the stronger all-initial-states
form.  It does **not** prove the original eight-zero assertion: a genuine
integer zero must lie in every modular zero-residue set, but (1) alone does
not classify the compatible 2-adic residue branches.

## Preliminary facts

Lowest-bit XOR is well defined on (R_M), including for negative integer
representatives, because the lowest (k) two's-complement bits depend only on
the residue modulo (2^k).  Each (T_j) is a bijection, with inverse

\[
T_j^{-1}(u,v)=((u\mathbin{\mathrm{XOR}}j)-v,u).
\]

For the induction from modulus (M) to (2M), work on (R_{2M}^2).  For
(v=(\alpha,\beta)\in\mathbb F_2^2), define the high-bit translation

\[
H_v(x,y)=(x+\alpha M,y+\beta M).
\]

Let (e=(0,1)) and let

\[
A(\alpha,\beta)=(\beta,\alpha+\beta).
\]

All entries here are in (mathbb F_2).  Direct low/high-bit separation gives,
for (0\leq j<M),

\[
T_{j+M}=H_eT_j,\qquad T_jH_v=H_{Av}T_j. \tag{3}
\]

Indeed, XOR with (j+M) toggles the (M)-bit relative to XOR with (j), so
the two results differ by (M) modulo (2M).  Translating the input pair by
((\alpha M,\beta M)) changes the two output high bits to
((\beta,\beta-\alpha)=(\beta,\alpha+\beta)).

The matrix (A) obeys

\[
A^3=I,\qquad I+A+A^2=0. \tag{4}
\]

## Induction proof

The assertion is trivial for (M=1).  Assume (P_M^3=I) on (R_M^2).  In
(R_{2M}^2), denote the lower-half word by

\[
Q=T_{M-1}\cdots T_0
\]

(composition is read from right to left), and put

\[
s=\sum_{i=0}^{M-1}A^ie,qquad B=A^M.
\]

Moving every high-bit translation in the upper-half word to the left using
(3) yields

\[
T_{2M-1}\cdots T_M=H_sQ.
\]

Therefore

\[
P_{2M}=H_sQ^2. \tag{5}
\]

The second identity in (3), applied through all (M) factors of (Q), also
gives

\[
QH_v=H_{Bv}Q. \tag{6}
\]

Cubing (5) and using (6),

\[
P_{2M}^3
=H_{s+B^2s+B^4s}Q^6. \tag{7}
\]

Since (M) is a power of two, (M\not\equiv0\pmod3).  Thus (B) is either
(A) or (A^2); (4) implies

\[
s+B^2s+B^4s=0. \tag{8}
\]

It remains to show (Q^6=I).  Reduction modulo (M) sends (Q) to (P_M),
so the induction hypothesis says that (Q^3) reduces to the identity.  Also,
by (6) and (B^3=I), (Q^3) commutes with every (H_v).  On each four-point
fiber of (R_{2M}^2\to R_M^2), a map that reduces to the identity and commutes
with every translation (H_v) is itself a translation (H_d) on that fiber.
Such a translation has square equal to the identity.  Hence

\[
Q^6=(Q^3)^2=I. \tag{9}
\]

Equations (7)--(9) prove (P_{2M}^3=I), completing the induction.

## From the word identity to the sequence

Modulo (M), the update maps satisfy (T_{j+M}=T_j).  A word of (M)
successive updates beginning at any other phase is a cyclic rotation of the
word defining (P_M).  Because all (T_j) are bijections, a cyclic rotation
is conjugate to (P_M), and its cube is therefore also the identity.  Three
complete time blocks return every consecutive state pair.  Applying this to
((a_0,a_1)=(0,1)) gives (2), including the two initial endpoints.

## Boundary and dependency audit

- (k=0) (modulus one) is included and trivial; C001 began at (k=1).
- No division, ordering, sign, finite-word overflow, or choice of integer
  representative is used.
- The proof treats arbitrary initial pairs, so it does not smuggle in a
  special property of ((0,1)).
- The only unproved statement left toward the original target is the global
  classification/escape of compatible modular zero branches.
- No external theorem and no proof assistant is used.
