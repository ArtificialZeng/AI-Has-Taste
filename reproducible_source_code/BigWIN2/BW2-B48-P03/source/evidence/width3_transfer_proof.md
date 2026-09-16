# Width-three transfer proof certificate

## Statement

For every integer `m >= 2`,

\[
  \psi(P_3\mathbin\square P_m)\equiv2\pmod4.
\]

Consequently, for every `k >= 1`, this holds at `m=2k+1`, resolving the
frozen claim in `source.md` affirmatively.

## Exact two-state transfer

First take an integer `q >= 3` and count proper `q`-colorings.  A proper
coloring of the last three-vertex column has one of exactly two equality
types:

* `A`: top and bottom have the same color, so the pattern is `(a,b,a)`;
* `B`: all three colors are distinct, so the pattern is `(a,b,c)`.

Let `A_m(q)` and `B_m(q)` count colorings of the first `m` columns according
to the last-column type, and use the row vector `v_m=(A_m,B_m)`.  The first
column gives

\[
 v_1=\bigl(q(q-1),\ q(q-1)(q-2)\bigr).
\]

For any fixed coloring of the old column, direct counting of the new column,
subject to its two vertical inequalities and its three horizontal
inequalities with the old column, gives the following table.  Rows are old
types and columns are new types:

\[
M(q)=\begin{pmatrix}
q^2-3q+3 &(q-2)(q^2-4q+5)\\
q^2-4q+5&q^3-6q^2+14q-13
\end{pmatrix}.
\]

For completeness, fix old representatives `(0,1,0)` and `(0,1,2)`.  The
`A -> A` entry is
`(q-1)+(q-2)^2=q^2-3q+3`: choose the repeated new endpoint color; if it is
`1` there are `q-1` middle choices, and for each of its other `q-2` values
there are `q-2` middle choices.  Similarly, the `B -> A` entry is
`(q-1)+(q-3)(q-2)=q^2-4q+5`, according as the repeated endpoint color is or
is not `1`.

For `A -> B`, split on the new middle color.  If it is `0`, the ordered
distinct endpoint colors have `(q-1)(q-2)` choices.  If it is neither `0`
nor `1`, they have `(q-2)(q-3)` choices for each of `q-2` middle colors.
The total is
`(q-1)(q-2)+(q-2)^2(q-3)=(q-2)(q^2-4q+5)`.  Finally, for `B -> B`, apply
inclusion--exclusion to the `q(q-1)(q-2)` ordered distinct triples, excluding
respectively a top `0`, middle `1`, and bottom `2`.  This gives

\[
q(q-1)(q-2)-3(q-1)(q-2)+3(q-2)-1
=q^3-6q^2+14q-13.
\]

Thus

\[
 v_{m+1}=v_mM(q),\qquad \chi_{P_3\square P_m}(q)=A_m(q)+B_m(q).
\]

These identities hold for every integer `q >= 3`, hence as polynomial
identities in `q`.  It is therefore valid to specialize them at `q=-1`.

## Modulo-four invariant

At `q=-1`,

\[
M(-1)=\begin{pmatrix}7&-30\\10&-34\end{pmatrix}
 \equiv\begin{pmatrix}3&2\\2&2\end{pmatrix}\pmod4,
\qquad v_1(-1)=(2,-6)\equiv(2,2)\pmod4.
\]

One multiplication gives

\[
v_2(-1)\equiv(2,0)\pmod4,
\]

and this state is fixed, since

\[
(2,0)M(-1)\equiv(2,0)\pmod4.
\]

Therefore `v_m(-1)=(A_m(-1),B_m(-1))` is congruent to `(2,0)` for every
`m >= 2`, and

\[
 \chi_{P_3\square P_m}(-1)=A_m(-1)+B_m(-1)\equiv2\pmod4.
\]

Stanley's evaluation gives
`psi(G)=(-1)^{|V(G)|} chi_G(-1)`.  As `2` and `-2` have the same residue
modulo four, the asserted acyclic-orientation congruence follows for every
`m >= 2`, in particular for every odd `m=2k+1 >= 3`.

## Reproducibility and independent finite cross-checks

`width3_transfer_certificate.py` checks the four transition polynomials by
direct color enumeration at `q=3,...,12`, checks the resulting full chromatic
polynomial against the independent FK connectivity transfer for every
`m=1,...,9`, and verifies the modulo-four fixed orbit.  The symbolic proof
above, rather than those finite checks, establishes the infinite statement.

For the requested first unreported case `m=9`,

\[
 \chi_{P_3\square P_9}(-1)=-514302841174,
 \qquad \psi(P_3\square P_9)=514302841174\equiv2\pmod4.
\]

The exact value is independently reproduced by
`ao_deletion_contraction.py`, whose core recurrence is
`a(G)=a(G-e)+a(G/e)`, and by `chromatic_fk_transfer.py`, which produces the
full degree-27 chromatic polynomial using the Fortuin--Kasteleyn subset sum.
