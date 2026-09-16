# Locked formal statement

Status: **locked for research on 2026-08-29**. Any later change must be
recorded explicitly in this file and requires a new lock hash.

## Ambient system

Let \(\mathbb F_2=\{0,1\}\), with every displayed sum and product in the
definition below taken in \(\mathbb F_2\). A (binary) configuration is a map
\(x:\mathbb Z\to\mathbb F_2\). Put

\[
\delta_{115}(\ell,x,r)=1+x+\ell x+\ell x r.
\]

Equivalently, in Wolfram order \(111,110,101,100,011,010,001,000\), the
values of \(\delta_{115}\) are \(0,1,1,1,0,0,1,1\).

Define the global second-order rule

\[
F:(\mathbb F_2^{\mathbb Z})^2\longrightarrow
  (\mathbb F_2^{\mathbb Z})^2,
\qquad
F(m,c)=(c,c'),
\]

where, for every \(j\in\mathbb Z\),

\[
c'_j=m_j+\delta_{115}(c_{j-1},c_j,c_{j+1}).
\]

Thus the first component is the preceding time layer (the “memory”) and the
second component is the current time layer. This is precisely the RESOCA
induced by ECA rule 115 under equation (1) of Formenti--Kamilya.

Let \(u:\mathbb Z\to\mathbb F_2\) be the finite configuration with
\(u_0=1\) and \(u_j=0\) for \(j\ne0\). For every integer \(k\ge0\), define
the finite configuration \(c^{(k)}\) by

\[
c^{(k)}_j=
\begin{cases}
1,&-k\le j\le k\text{ and }j+k\equiv0\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\]

Reading from site \(-k\) to site \(k\), this is the word \(1(01)^k\).
Let

\[
P(k)=\min\{p\in\mathbb Z_{>0}:F^p(u,c^{(k)})=(u,c^{(k)})\}.
\]

Existence of this minimum follows from Theorem 1 of the source paper; it may
also be re-established rather than assumed in a self-contained proof.

## Target proposition

Prove or disprove the quantified equality

\[
\boxed{\quad
\forall i\in\mathbb Z_{\ge0},\qquad
P(2i+1)=4^{2i+3}-1=2^{4i+6}-1.
\quad}
\]

“Period” always means the least positive return time of the full two-layer
configuration, not a return modulo spatial translation, a return of only one
component, an eventual period, or merely some (possibly nonminimal) return
time. Consequently, proving only that \(P(2i+1)\) divides the displayed number
does not prove the target.

## Source-statement repair

The source paper writes the word placement as
\(c_{-k+i}=w_i\) for \(i\in[0,|w|]\). Under ordinary inclusive integer-interval
notation this has one index too many. For \(w=1(01)^k\), whose length is
\(2k+1\), the intended and table-consistent range is
\(i=0,1,\ldots,|w|-1=2k\); the definition of \(c^{(k)}\) above makes this
repair explicit. The prompt's parameter \(i\) is retained in the target,
while \(j\) is used for lattice sites to avoid overloading.

## Edge conventions

- \(\mathbb N\) in the source Conjecture 2 is interpreted as including zero,
  because the displayed family and the prompt explicitly include \(i=0\).
- No quotient by reflection or translation is taken. The centering is fixed as
  above and the memory spike is at site zero.
- Although the initial pair has finite support, later layers have the
  period-three uniform background outside a finite central interval. Equality
  in the definition of \(P(k)\) is equality at every site of \(\mathbb Z\).
- The target has no zero-word or empty-family case: its smallest member is
  \(k=1\), with current word \(101\) and claimed period \(63\).
