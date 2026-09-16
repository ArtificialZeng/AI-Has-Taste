# Independent rederivation of the structural handoff

The input `handoff/independent-structural-hints.md` is external, unreviewed
handoff material.  Nothing below is accepted merely because it appears there.
This file rederives the universal identities from the frozen recurrence and
records the separately checked finite claims.  XOR always means infinite-width
two's-complement XOR.

## H1: the one-bit dyadic shift signature

Fix (k\geq0), put (M=2^k) and (L=3M), and use the already proved
congruence (a_{n+L}\equiv a_n\pmod M).  Define

\[
 \varepsilon_k(n)=\frac{a_{n+L}-a_n}{M}\pmod2.
\]

If (x'\equiv x\pmod M), compare the lowest (k+1) bits.  Replacing (x)
by (x') changes bit (k) by

\[
 \delta_M(x',x)=\frac{x'-x}{M}\pmod2,
\]

whereas replacing (n) by (n+L\equiv n+M\pmod {2M}) toggles bit (k)
of the second XOR operand.  The lower (k) bits do not change.  Consequently

\[
 \delta_M(x'\mathbin{\mathrm{XOR}}(n+L),
          x\mathbin{\mathrm{XOR}}n)
 =\delta_M(x',x)+1\quad\hbox{in }\mathbb F_2. \tag{H1.1}
\]

This residue-bit argument includes negative (x), because the lowest
(k+1) sign-extended bits depend only on the residue modulo (2M).
Subtracting the shifted and unshifted recurrences and applying (H1.1) gives,
for (n\geq2),

\[
 \varepsilon_k(n)=\varepsilon_k(n-1)+\varepsilon_k(n-2)+1. \tag{H1.2}
\]

Applying (H1.2) twice shows
(\varepsilon_k(n+3)=\varepsilon_k(n)).  Hence its three-bit signature is
one of (001,010,100,111).

For (r\in Z_k), let
(h_k(r)=a_r/M\pmod2), and put
(E_{k,c}=\varepsilon_k(c)).  The lower child (r) lies in (Z_{k+1})
exactly when (h_k(r)=0).  Since

\[
 \frac{a_{r+L}}M\equiv h_k(r)+E_{k,r\bmod3}\pmod2,
\]

the upper child (r+L) lies in (Z_{k+1}) exactly when
(h_k(r)=E_{k,r\bmod3}).  This proves the four-row child table in the
handoff and, for an actually selected child (d\in\{0,1\}), the equivalent
condition (h_k(r)=E_{k,r\bmod3}d).

Two independent exact implementations reproduce all signatures through
(k=22) and every child decision through (k=18).  In particular,

\[
 E_2=(0,1,0),\quad
 Z_2=\{0,4,6,10,11\},\quad
 Z_3=\{0,4,6,11,12,18,22,23\}.
\]

The claimed obstruction to retaining only two state high bits is also exact.
Modulo (8), the word (T_{11}\cdots T_0) sends
((0,0)\mapsto(4,0)) and ((1,0)\mapsto(5,4)).  The inputs have the same
quotient bits modulo (4), but the output quotient bits differ, so a quotient
that discards the lower residues is not closed.  Separately,
(a_{49139}=a_{49151}=2^{25}); thus the reported 11-edge lower run is real
and refutes every proposed uniform lower-run bound at most 10.

## H2: three-step reduction to unit values

For (n\geq1), binary carry at the last one of (n-1) gives

\[
 M_n=(n-1)\mathbin{\mathrm{XOR}}n=2^{\nu_2(n)+1}-1. \tag{H2.1}
\]

More generally, let (P=2^j), (M=P-1), and write the Euclidean division
(x=Pq+r), (0\leq r<P).  XOR by (M) flips exactly the lowest (j)
bits and leaves the sign-extended quotient bits unchanged, so even for
negative (x),

\[
 x\mathbin{\mathrm{XOR}}M=Pq+(M-r),\qquad
 (x\mathbin{\mathrm{XOR}}M)-x=M-2r. \tag{H2.2}
\]

If (n\geq3), eliminate (a_{n-2}) from the recurrences at (n-1,n).
XOR is an involution, and (H2.1) yields the bidirectional equivalence

\[
 a_n=0\iff
 a_{n-3}=(a_{n-1}\mathbin{\mathrm{XOR}}M_n)-a_{n-1}. \tag{H2.3}
\]

The same elimination three steps forward gives, for (n\geq0),

\[
 a_n=0\iff
 a_{n+3}=(a_{n+1}\mathbin{\mathrm{XOR}}((n+2)\mathbin{\mathrm{XOR}}(n+3)))
 -a_{n+1}. \tag{H2.4}
\]

Equation (H2.2) proves the necessary bound
(|a_{n-3}|\leq2^{\nu_2(n)+1}-1).

The parity word (011100) makes the advertised unit reduction exact, rather
than merely heuristic.  A zero at (n=6q) is equivalent via (H2.4) to
(a_{6q+3}=-1), because the relevant mask is 1 and (a_{6q+1}) is odd.
A zero at (n=6q+4) is equivalent to (a_{6(q+1)+1}=1), because
(a_{6q+5}) is even.  A zero at (n=6q+5) is equivalent via (H2.3) to
(a_{6q+2}=1), because the mask is 1 and (a_{6q+4}) is even.  Therefore
the original target is equivalent to the conjunction

\[
 \{q\geq0:a_{6q+3}=-1\}=\{0,1,6,7,8,9\},
\]
\[
 \{q\geq0:a_{6q+1}=1\}=\{0\},\qquad
 \{q\geq0:a_{6q+2}=1\}=\{1,3\}. \tag{H2.5}
\]

The (a_1=1) occurrence corresponds under the reverse coordinate change to
the inadmissible index (-2).  Thus (H2.5) introduces no spurious original
zero.  It is a coordinate equivalence, not a solved smaller theorem.

## H3: exact bit stripping

Let (p_n=(0,1,1,1,0,0)^\infty) and
(h_n=(a_n-p_n)/2=\lfloor a_n/2\rfloor).  Write
(n=2\lfloor n/2\rfloor+(n\bmod2)).  The identity

\[
 (2x+b)\mathbin{\mathrm{XOR}}(2m+e)
 =2(x\mathbin{\mathrm{XOR}}m)+(b\mathbin{\mathrm{XOR}}e)
\]

and the six possible parity residues show that the carry correction is zero
except at (n\equiv3\pmod6), where it is (-1).  Hence

\[
 h_n=(h_{n-1}\mathbin{\mathrm{XOR}}\lfloor n/2\rfloor)-h_{n-2}
 -\mathbf1_{n\equiv3\pmod6}. \tag{H3.1}
\]

Putting (x=h_{2m-2}), (y=h_{2m-1}), (H3.1) at (2m,2m+1) becomes

\[
 z=(y\mathbin{\mathrm{XOR}}m)-x,\qquad
 w=(z\mathbin{\mathrm{XOR}}m)-y-\mathbf1_{m\equiv1\pmod3}, \tag{H3.2}
\]

with ((h_{2m},h_{2m+1})=(z,w)).  Direct-XOR and independent AND-formula
evaluators verify (H2.3), (H2.4), (H3.1), and (H3.2) throughout their saved
million-index frontier, including negative sequence values.

## H4: an exact obstruction to small linear 2-kernel closure

Modulo 4 the proved period theorem makes the following integer-valued:

\[
 U_q=\frac{a_{6q+1}-1}{4},\quad
 V_q=\frac{a_{12q+8}-1}{4},\quad
 W_q=\frac{a_{6q+3}+1}{4}.
\]

For a sequence (s), enumerate its standard 2-kernel rows as
(s_{e,r}(q)=s(2^e q+r)), first by (e), then by (r), where
(0\leq r<2^e).  For each (s\in\{U,V,W\}), take the first 2047 rows
((0\leq e<11)) and evaluate them at (q=0,\ldots,2046).  The determinants
of the resulting integer matrices are nonzero modulo 1,000,003:

| sequence | mod 1,000,003 |
|---|---:|
| (U) | 329819 |
| (V) | 646456 |
| (W) | 520101 |

A nonzero modular determinant makes the integer determinant nonzero.  Thus
the corresponding 2047 finite row vectors, and hence the 2047 kernel
subsequences, are linearly independent over (\mathbb Q).  Each rational
2-kernel span therefore has dimension at least 2047.  This independently
reproduces and strengthens the handoff's reported lower bound 63.

This is a proved finite-rank obstruction only.  It neither proves infinite
2-kernel rank nor excludes nonlinear finite carry automata.  The producer and
checker use distinct recurrence formulas and differently normalised modular
eliminations. Full definitions and every (2^d-1) determinant for
(3\leq d\leq10), checked modulo both 1,000,003 and 1,000,033, are serialized
in `experiments/kernel-rank-evidence.json`. The independently replayed
(d=11) test is in `experiments/kernel-rank-d11-evidence.json`.

## Provenance and exact checks

- External lead: `handoff/independent-structural-hints.md`, read before route
  selection and treated as unreviewed.
- Owner rederivation: this file, from the frozen recurrence and the already
  proved modular-period theorem.
- Direct producer: `experiments/analyze_structural_hints.py`.
- Independent formula checker: `experiments/verify_structural_hints.py`.
- Kernel-rank producer: `experiments/analyze_kernel_rank.py`.
- Independent kernel-rank checker: `experiments/verify_kernel_rank.py`.
- Exact data: `experiments/structural-hints-evidence.json`,
  `experiments/kernel-rank-evidence.json`, and the next-level adversarial test
  `experiments/kernel-rank-d11-evidence.json`.

No claim in this file closes the fatal infinite-tail gap.
