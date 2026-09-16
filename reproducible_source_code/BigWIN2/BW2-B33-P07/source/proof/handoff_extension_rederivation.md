# Independent rederivation of handoff sections E and F

The sections headed E and F in `handoff/independent-structural-hints.md` are
unreviewed external leads.  This file derives the adopted statements from the
frozen recurrence and the already proved modular-period theorem.  The
separate exact producer and checker are
`experiments/analyze_handoff_extensions.py` and
`experiments/verify_handoff_extensions.py`.

Throughout, XOR is infinite-width two's-complement XOR.  Put

\[
 T_q(X,Y)=(Y,(Y\mathbin{\mathrm{XOR}}q)-X),\qquad A_q=T_q^2,
 \qquad \tau(X,Y)=(X,Y-1).
\]

## H5: second stripping and the unavoidable borrow

Let \(g_n=\lfloor a_n/4\rfloor\) and
\(R_m=(g_{2m},g_{2m+1})\).  The modular-period theorem at modulus four
shows that \(a_n\bmod4\) has period dividing 12.  Direct evaluation of one
period therefore proves

\[
 (\lfloor a_n/2\rfloor\bmod2)_{n=0}^{11}
 =(0,0,1,1,0,1,0,0,0,1,0,0).
\]

Write the exact first-strip pair as
\((h_{2m},h_{2m+1})=2R_m+\beta_m\).  The six possible low-bit pairs are

| \(m\bmod6\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|---:|
| \(\beta_m\) | 00 | 11 | 01 | 00 | 01 | 00 |

Substitute this table into the proved first-strip map H3.2 and use

\[
 (2Y+\eta)\mathbin{\mathrm{XOR}}(2q+s)
 =2(Y\mathbin{\mathrm{XOR}}q)+(\eta\mathbin{\mathrm{XOR}}s).
\]

The six cases give, for every \(m\ge1\),

\[
 R_m=A_{\lfloor m/2\rfloor}(R_{m-1})-(0,\delta_m),
 \qquad
 \delta_m=\mathbf 1_{m\bmod6\in\{1,2,4\}}. \tag{H5.1}
\]

Grouping the steps \(m=2q,2q+1\) consequently gives

\[
 R_{2q+1}=B_q(R_{2q-1}),\qquad
 B_q=\begin{cases}
 \tau A_q^2,&q\equiv0\pmod3,\\
 A_q\tau A_q,&q\not\equiv0\pmod3.
 \end{cases} \tag{H5.2}
\]

The internal translation in the second case cannot be replaced, on all
integer states, by a correction depending on a fixed low-bit window and the
phase alone.  Indeed, if \(A_q(X,Y)=(u,v)\), the deviation of the first
coordinate from \(A_q^2(X,Y)\) is

\[
 \Delta_q(v)=((v-1)\mathbin{\mathrm{XOR}}q)
              -(v\mathbin{\mathrm{XOR}}q). \tag{H5.3}
\]

For \(v\ne0\), put \(t=\nu_2(v)\).  The lowest \(t\) bits change from zero
in \(v\) to one in \(v-1\), bit \(t\) changes from one to zero, and all
higher bits agree.  This argument is valid for negative integers because it
uses their sign-extended low bits.  It gives

\[
 \Delta_q(v)=2^{t+1}\operatorname{bit}_t(q)
             -2(q\bmod2^t)-1. \tag{H5.4}
\]

For \(v=0\), the identity \((-1)\mathbin{\mathrm{XOR}}q=-q-1\) gives

\[
 \Delta_q(0)=-2q-1. \tag{H5.5}
\]

Fix any window width \(W\).  Choose \(q=4^s\) with \(2^W\mid q\), and
put \(P_0=(0,q)\), \(P_1=(q,0)\).  These states have identical lowest
\(W\) bits and \(q\equiv1\pmod3\), but direct use of (H5.2) gives

\[
 B_q(P_0)-A_q^2(P_0)=(-2q-1,0),\qquad
 B_q(P_1)-A_q^2(P_1)=(2q-1,0). \tag{H5.6}
\]

Thus no function of only
\((q\bmod3,X\bmod2^W,Y\bmod2^W)\) can supply this correction for every
integer state.  This is a representation obstruction, not a theorem about
the distinguished orbit and not an obstruction to a bit-serial or unbounded
carry state.

The local repair really is a borrow bit.  If \(z=2Z+\zeta\), with
\(\zeta\in\{0,1\}\), and \(b\in\{0,1\}\), then the two cases
\(b=0,1\) prove

\[
 z-b=2(Z-b')+(\zeta\mathbin{\mathrm{XOR}}b),
 \qquad b'=b(1-\zeta). \tag{H5.7}
\]

Finite exact checks reproduce the handoff's examples:

\[
 B_4(0,4)=(-5,0),\quad B_4(4,0)=(7,0),\quad
 A_4^2(0,4)=(4,0),\quad A_4^2(4,0)=(0,0),
\]

and on the distinguished orbit

\[
 R_{24571}=(-2^{23},-2666497),\qquad
 A_{12286}R_{24571}=(5726209,2^{23}).
\]

The orbit example shows that a 23-bit borrow occurs, but one finite occurrence
does not prove unbounded carry growth.

## H6: an all-depth 2-adic determinant divisor

For \(E\ge2\), put \(N=2^{E+1}-1\).  For
\(S\in\{U,V,W\}\), define the integer matrix

\[
 H_E(S)_{(e,r),j}=S(2^e j+r),
 \quad 0\le e\le E,\quad0\le r<2^e,\quad0\le j<N,
\]

and write \(D_E(S)=\det H_E(S)\).  This is the matrix called
\(K_{E+1}^S\) in C002.

For every nonzero column, write \(j=2^\ell+s\), where
\(0\le s<2^\ell\).  In descending order of \(j\), perform the
determinant-preserving operation

\[
 C_j\leftarrow C_j-C_s. \tag{H6.1}
\]

Descending order makes the new entry literally the difference of the two
original sequence values.  In a row of depth \(e\), the two underlying
indices of \(a\) differ by

\[
 3\cdot2^{e+\ell+1}\quad(S=U,W),\qquad
 3\cdot2^{e+\ell+2}\quad(S=V).
\]

The modular-period theorem therefore shows that the transformed entry is
divisible by

\[
 2^{e+\ell-1}\quad(S=U,W, e+\ell\ge1),\qquad
 2^{e+\ell}\quad(S=V). \tag{H6.2}
\]

After division by the displayed power, its parity is the shift-signature bit
\(\varepsilon_{e+\ell+1}(1)\) for \(U\),
\(\varepsilon_{e+\ell+1}(0)\) for \(W\), and
\(\varepsilon_{e+\ell+2}(2)\) for \(V\).  Hence this normalized bit depends
only on the row depth \(e\) and column scale \(\ell\), never on the row
residue \(r\) or column offset \(s\).  This proves the structural layer
claim for every depth.

We use the elementary fact that if an \(m\)-square integer matrix has rank at
most \(\rho\) modulo two, its determinant is divisible by \(2^{m-\rho}\).
Gaussian row operations modulo two leave at least \(m-\rho\) zero rows;
performing the same integer row operations makes those rows even, from which
the divisor follows.

For \(V\), expand the transformed determinant along column zero.  If the
removed row has depth \(d\), factor \(2^e\) from every remaining row of
depth \(e\), and \(2^\ell\) from every nonzero column of scale \(\ell\).
The normalized minor has rank at most \(E+1\) modulo two by the block property
above.  The required sums are

\[
 \sum_{e=0}^E e2^e=(E-1)2^{E+1}+2,
\]

and, because the final scale has \(2^E-1\) rather than \(2^E\) columns,

\[
 \sum_{j=1}^{N-1}\lfloor\log_2j\rfloor
 =(E-1)2^{E+1}-E+2.
\]

Using \(d\le E\) and the rank divisor for the \((N-1)\)-square minor gives

\[
 2^{(4E-2)2^E-3E+1}\mid D_E(V). \tag{H6.3}
\]

For \(U,W\), expand along both column zero and column one.  If their selected
rows have depths \(d_i,d_h\), respectively, the column-one entry has
2-adic valuation at least \(\max(d_h-1,0)\).  In the remaining minor all
column scales satisfy \(\ell\ge1\), so factor \(2^e\) from each remaining
row and \(2^{\ell-1}\) from each remaining column.  The normalized parity
matrix has rank at most \(E\), because it has only the \(E\) column-scale
classes \(1,\ldots,E\).  Here

\[
 \sum_{j=2}^{N-1}(\lfloor\log_2j\rfloor-1)
 =(E-2)2^{E+1}-E+5.
\]

Finally,
\(-d_i-d_h+\max(d_h-1,0)\ge-E-1\).  Applying the rank divisor to the
\((N-2)\)-square minor proves the stronger bound

\[
 2^{(4E-4)2^E-3E+3}\mid D_E(U),D_E(W). \tag{H6.4}
\]

For \(E\ge2\), (H6.4) implies the handoff's weaker exponent
\((4E-4)2^E-4E+3\).  Neither (H6.3) nor (H6.4) proves that a determinant is
nonzero; a zero determinant is divisible by every power of two.  Thus these
facts diagnose the carry structure but do not prove C002.

Exact determinants through \(E=4\) pass a direct-XOR producer and a separate
AND-formula/SymPy checker.  They also reproduce

\[
 103\mid D_2(U),\ D_3(U)\equiv47\pmod {103},
\]
\[
 5\mid D_2(V),\ D_3(V)\equiv3\pmod5,
 \qquad
 11\mid D_2(W),\ D_3(W)\equiv7\pmod {11}.
\]

These examples refute a naive integral block recursion that would retain the
previous determinant as a factor of the next.  They do not refute every block
decomposition or the nonsingularity conjecture.

## Scope and provenance

- External lead: handoff sections E and F, treated as unreviewed.
- Owner derivation: H5.1--H5.7 and H6.1--H6.4 above.
- Producer: `experiments/analyze_handoff_extensions.py`, using direct signed
  XOR and fraction-free Bareiss determinants.
- Independent checker: `experiments/verify_handoff_extensions.py`, using the
  AND identity and SymPy's exact domain determinant.
- Exact record: `experiments/handoff-extensions-evidence.json`.

No assertion here classifies an infinite zero-residue branch or excludes a
zero after 54.
