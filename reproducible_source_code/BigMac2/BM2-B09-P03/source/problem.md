# Precise problem reading

Provenance: `bigMac-00009-p03-triage-d78df83dfcbc`  
Canonical statement: `source.md` (immutable; SHA-256
`4f9bfba8efa3d546f6395bd3dbf1f3b5375bfecc6cd2f0f03ab0163c28247545`).

## Objects and definitions

Fix the single ordering $1,2,3,4$ throughout. Let

\[
\mathcal S_4=\{P=(p_{ij})\in\mathbb R_{\ge0}^{4\times4}:
\sum_{j=1}^4p_{ij}=1\text{ for every }i\}
\]

be the row-stochastic matrices. The support of a nonnegative matrix is
\(\operatorname{supp}(P)=\{(i,j):p_{ij}>0\}\). A (possibly rectangular)
nonnegative matrix is **row-allowable** when every one of its rows has a
positive entry; this condition is vacuous when it has no rows.

For a row-allowable square nonnegative matrix $A$ of order $s$, put
\([s]=\{1,\ldots,s\}\) and, for $I\subseteq[s]$,

\[
F_A(I)=\{j\in[s]:a_{ij}>0\text{ for some }i\in I\}.
\]

The matrix $A$ is **GE** if, for every pair of disjoint nonempty
$I,J\subseteq[s]$, either $F_A(I)\cap F_A(J)\ne\varnothing$, or

\[
|F_A(I)\cup F_A(J)|\ge |I\cup J|.
\]

It is **GR** if the last inequality is strict whenever the two consequent
sets are disjoint.

For $P\in\mathcal S_4$, let $P^{[s]}=(p_{ij})_{1\le i,j\le s}$ be its
leading principal block; it may be substochastic. For $r\in[4]$, let
$P_{21}^{[r]}=(p_{ij})_{r<i\le4,\ 1\le j\le r}$. Define

\[
\begin{aligned}
\mathcal T_{\mathrm{NE},4}(r)
 &=\{P\in\mathcal S_4:P^{[r]}\text{ is GR and }
 P^{[s]}\text{ is GE for every }r<s\le4\},\\
\mathcal T_{\mathrm{AS},4}(r)
 &=\{P\in\mathcal T_{\mathrm{NE},4}(r):
 P_{21}^{[r]}\text{ is row-allowable}\},\\
\mathcal A_4&=\bigcup_{r=1}^4\mathcal T_{\mathrm{AS},4}(r).
\end{aligned}
\]

Thus a matrix is admitted if at least one level $r$ works; its least such
level need not be prescribed in advance.

The notation in the source, `T_AS(4)`, is read as the **full almost-Sarymsakov
class in dimension four**, namely \(\mathcal A_4\). It is not the paper's
level-$4$ component \(\mathcal T_{\mathrm{AS},4}(4)=\mathcal T_0\).
This disambiguation is forced by “all order-four” and by the cited bound
\((4-1)(4-1)!=18\), which applies to the union over levels. Every factor uses
the same ordering above; conjugating different factors by different
permutations is outside the problem.

A matrix $Q\in\mathcal S_4$ is **scrambling** when

\[
\forall i,j\in[4]\ \exists k\in[4]\quad q_{ik}>0\ \text{and}\ q_{jk}>0.
\]

For \(\mathcal C\subseteq\mathcal S_4\) and $h\ge1$, define

\[
\mathcal C^h=\{P_hP_{h-1}\cdots P_1:P_1,\ldots,P_h\in\mathcal C\}.
\]

(Reversing the written multiplication convention does not change the
universally quantified set of words.)

## Frozen question and quantifiers

Determine the integer

\[
H=h_{\mathrm{scr}}(\mathcal A_4)
=\min\{h\ge1:\forall P_1,\ldots,P_h\in\mathcal A_4,
\ P_h\cdots P_1\text{ is scrambling}\}.
\]

Both halves of exactness are required:

1. exhibit $H-1$ admitted supports whose Boolean product is not
   scrambling, with positive stochastic realizations; and
2. certify exhaustively that every word of $H$ admitted supports has a
   scrambling Boolean product.

All entries declared positive by a support may have arbitrary positive
values subject only to row sums equal to one. For nonnegative products,

\[
\operatorname{supp}(P_h\cdots P_1)
=\operatorname{supp}(P_h)\odot\cdots\odot\operatorname{supp}(P_1),
\]

where \(\odot\) is Boolean matrix multiplication. Hence the exact-support
scrambling property is independent of the positive weights, and an exhaustive
support proof covers the full weighted class. Sampling weights does not.

## Known boundary and proposed contribution

Hsu, arXiv:2609.05050v1, Definition 3 and Theorem 5, proves $H\le18$ but
states sharpness only for order three. Since
\(\mathcal T_{\mathrm{AS},4}(4)=\mathcal T_0\subseteq\mathcal A_4\) and the
order-four Sarymsakov horizon is $3$, the inspected paper also gives
$3\le H\le18$. It does not determine $H$.

Nearest prior result: the interval above. Proposed delta: the exact $H$, a
longest nonscrambling legal support word, and a complete upper-bound
certificate. Verification route: enumerate all $15^4=50{,}625$ row-nonempty
binary $4\times4$ supports, retain exactly those satisfying the displayed
level conditions, and perform exact reachability under Boolean products in
the at-most $2^{16}$-element relation semigroup. A separate checker should
rebuild the legal alphabet and verify both the witness and the exhaustive
frontier/certificate.

Literature status is **status-uncertain**, not “verified open.” On 2026-09-07,
exact-phrase and equivalent-term searches located the cited new preprint but
no independent primary source resolving the order-four value. This limited
search is not a priority or novelty claim; the older term “almost scrambling”
denotes a different class.
