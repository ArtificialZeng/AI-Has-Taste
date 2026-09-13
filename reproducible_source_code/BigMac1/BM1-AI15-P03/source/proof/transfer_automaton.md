# Seam-correct finite automata and an exact positive-cone proof

This is an independent supplementary route from the literal graph definition.
The release manuscript continues to use the shorter colour-block proof in
`proof/builder_notes.md`; the present route supplies the requested finite-state
equivalence and an exact eventual-positivity certificate.  It does not use a
numerical root approximation or an enumerated large prefix.

## 1. The 12-state odd automaton

Let (K=\{0,1,2\}) and

\[
 \mathcal O=\{(x_0,x_1,x_2)\in K^3:x_0\ne x_1, x_1\ne x_2\}.
\]

Thus \(|\mathcal O|=3\cdot2\cdot2=12\).  In lexicographic order define the
zero-one matrix (O) by

\[
 O_{x,y}=1
 \quad\Longleftrightarrow\quad
 y=(x_1,x_2,z),\quad z\ne x_2,\quad z\ne x_0.                 \tag{1}
\]

The two new inequalities are respectively the offset-one and offset-three
constraints created when (z) is appended.  There are 18 transitions.

For a cyclic colour word (c), the windows

\[
 s_i=(c_i,c_{i+1},c_{i+2})
\]

form a based closed walk of length (n).  Conversely, the two-coordinate
overlap in (1) makes every based closed walk determine a unique periodic
colour word.  State membership checks the offset-one edges and (1) checks the
offset-three edges.  These two maps are inverse, with neither rotations nor
colour permutations factored out.  Hence, for odd (n\ge7),

\[
 a(n)=\operatorname{tr}(O^n).                               \tag{2}
\]

## 2. The 54-state even automaton and the necessary twist

Write (n=2m), (m\ge3), and pair opposite vertices:

\[
 q_i=(c_i,c_{i+m})\in Q:=\{(x,y)\in K^2:x\ne y\}.
\]

The six symbols in (Q) encode exactly the diameter constraint.  Put
(q\perp r) when their first coordinates differ and their second coordinates
differ.  Define the coordinate swap \(\sigma(x,y)=(y,x)\).  The original
cyclic order imposes the twisted extension

\[
 q_{i+m}=\sigma(q_i),                                      \tag{3}
\]

not ordinary period (m).

Equivalently, use the state set

\[
 \mathcal E=\{(u,v):u,v\in\mathcal O, u_j\ne v_j
                     \text{ for }j=0,1,2\}.                \tag{4}
\]

Here (u) and (v) are the two three-colour windows.  For each of the six
choices of the first paired column there are three choices for each of the
next two columns, so \(|\mathcal E|=6\cdot3\cdot3=54\).  Define (E) by
coordinatewise (O)-transitions:

\[
 E_{(u,v),(u',v')}=O_{u,u'}O_{v,v'}.                        \tag{5}
\]

It has 114 nonzero entries.  Let

\[
 \tau(u,v)=(v,u)
\]

and let (P) be the permutation matrix of \(\tau\), with
(P_{\tau(s),s}=1\).

Given a proper colouring, the paired window states beginning at positions
(0,1,\ldots,m) form a length-(m) path from (s) to \(\tau(s)\) by
(3).  Conversely, a path

\[
 s_0\longrightarrow s_1\longrightarrow\cdots
     \longrightarrow s_m=\tau(s_0)                         \tag{6}
\]

has forced overlaps and hence determines unique paired columns
(q_0,\ldots,q_{m+2}).  Its endpoint identity gives all three seam equations

\[
 q_m=\sigma q_0,qquad q_{m+1}=\sigma q_1,qquad
 q_{m+2}=\sigma q_2.                                       \tag{7}
\]

State membership enforces every diameter and offset-one constraint.  The
transition rule enforces every offset-three constraint, including the six
constraints crossing the two seams in (7).  Thus (6) reconstructs a unique
proper colouring, and the two constructions are inverse.  Therefore

\[
 \boxed{a(2m)=\sum_{s\in\mathcal E}(E^m)_{s,\tau(s)}
             =\operatorname{tr}(E^mP)}\qquad(m\ge3).        \tag{8}
\]

This also treats (n=6): there the offset-three edges coincide with the
diameters.  In (3) the corresponding constraint is
(q_i\perp\sigma(q_i)), which merely repeats the already imposed condition
that the two coordinates of (q_i) differ.

The ordinary trace is not an alternative closure.  It imposes
(q_{i+m}=q_i) instead of (3), so its accepted walks need not correspond to
the original graph.  Exact counterexamples are

\[
\begin{array}{c|cc}
n&\operatorname{tr}(E^{n/2})&\operatorname{tr}(E^{n/2}P)\\ \hline
6&0&42\\
8&114&0.
\end{array}                                                \tag{9}
\]

Thus the precise failed implication in the naive reduction is: an ordinarily
closed paired-window walk does **not** necessarily stitch into the single
(2m)-cycle; the missing hypotheses are exactly the three swap equations
(7).

## 3. Exact positive-cone certificate

The matrices above are nonnegative integer matrices constructed directly from
(1), (4), and (5).  Exact integer multiplication gives

\[
 O^{10}>0\quad\text{entrywise},\qquad E^{13}>0
 \quad\text{entrywise}.                                   \tag{10}
\]

The certificate records the following independently reconstructed invariants:

\[
\begin{array}{c|ccc}
 &\min&\max&\text{sum of all entries}\\ \hline
O^{10}&1&26&1398\\
E^{13}&20&4097&2750778.
\end{array}                                                \tag{11}
\]

It also records canonical SHA-256 digests of both transition matrices and
both positive powers.  No floating-point number occurs.

\[
\begin{array}{c|l}
\text{canonical JSON matrix}&\text{SHA-256}\\ \hline
O&\texttt{015de555faf78002f4a295aafb8db08d814956af339c6f2ef16916723baab2a9}\\
O^{10}&\texttt{60c37736e05a71a2d58e40979685e037485f9c2193cc5c3eaa9b0227362a003e}\\
E&\texttt{fbbf93271d70402aca563534f82ba99ef73c6f6dcc60f78b580e35a24d58ce7d}\\
E^{13}&\texttt{cfcbabfd011035603fd011e34e8447ab3f98085424ac9b19669ae63d95ad82b7}
\end{array}
\]

Every column of (O) and (E) is nonzero.  If a nonnegative matrix (A)
has no zero column and (A^r>0), then

\[
 (A^{r+1})_{ij}=\sum_k(A^r)_{ik}A_{kj}>0
\]

for every (i,j); induction gives (A^{r+t}>0) for all (t\ge0).  In cone
language, (A^r) maps every nonzero vector of the nonnegative cone into its
interior, and every later power retains this property.

Consequently (2) is positive for every odd (n\ge11); the remaining positive
odd base case is checked exactly as

\[
 \operatorname{tr}(O^9)=18.                               \tag{12}
\]

Likewise, for every (m\ge13), every summand
((E^m)_{s,\tau(s)}) in (8) is positive.  Hence

\[
 a(n)>0\qquad\text{for every even }n\ge26.                 \tag{13}
\]

This is an all-order consequence of the finite cone certificate (10), not an
inference from checking a long prefix.

## 4. Independent finite certificate below the threshold

For (6\le n\le25), an independent definition-level recursion fixes
(c_0=0), selects an uncoloured vertex, and branches over exactly the colours
not used by its already coloured neighbours.  Every proper colouring with
(c_0=0) reaches exactly one leaf.  Adding a constant modulo three acts
freely and transitively on the possible values of (c_0), so the resulting
leaf count multiplied by three is (a(n)).

The exact totals are

\[
\begin{array}{c|rrrrrrrrrr}
n&6&7&8&9&10&11&12&13&14&15\\ \hline
a(n)&42&0&0&18&186&66&0&234&930&750
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrr}
n&16&17&18&19&20&21&22&23&24&25\\ \hline
a(n)&0&2244&4578&6498&120&18354&22314&50922&2496&139500.
\end{array}
\]

The same values are independently produced by (2) or (8).  This bounded
recursion is the requested finite certificate; it is not extended into a
(2^n) product search.  Combining it with (12)--(13) proves again that

\[
 a(n)=0\quad\Longleftrightarrow\quad n\in\{7,8,12,16\}
 \qquad(n\ge6).                                            \tag{14}
\]

## 5. Reproduction and trust boundary

The serialized input is `certificates/transfer_automata_certificate.json`.
Run

```bash
python3 -I verification/verify_transfer_automata.py \
  certificates/transfer_automata_certificate.json
python3 -O -I verification/verify_transfer_automata.py \
  certificates/transfer_automata_certificate.json
```

The verifier rebuilds both state sets and matrices, checks (9)--(13) with
integer arithmetic, and independently reruns the direct graph recursion.  It
contains no correctness `assert`, so optimization cannot remove its checks.
The separate definition-first audit is
`audit/AUTOMATON_EQUIVALENCE_AUDIT.md`.

No proof assistant was used.
