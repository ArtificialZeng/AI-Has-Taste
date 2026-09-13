# Explicit MSO realizations for all nonnegative and nonpositive cases

Provenance: `bigMac-00011-p02-research-999996ce998a` (research pass 1,
2026-09-07).  This note proves a partial classification under the precise
reading in `problem.md`.  It makes no assertion about mixed-sign weights.

## A one-copy MSO transduction for plateau reversal

Work in the usual input-word structure, with position order `<` and unary
letter predicates `U` and `D`.  For `A` equal to either letter, abbreviate

\[
 I_A(x,y)\;:\Longleftrightarrow\;
 \exists z\,(x\le z<y\mathbin\wedge A(z))\qquad(x<y).
\]

Define the following strict order on input positions:

\[
x\prec_A y\;:\Longleftrightarrow\;
 \bigl(x<y\mathbin\wedge I_A(x,y)\bigr)
 \ \vee\ 
 \bigl(y<x\mathbin\wedge \neg I_A(y,x)\bigr).                 \tag{1}
\]

This is an explicit first-order, hence MSO, formula.  In the notation of
Definition 3.7 of the primary source, take `phi_dom := true`, one copy name
`C={1}`, selection formula `phi_1(x) := true`, label formulas
`psi_{1,U}(x) := U(x)` and `psi_{1,D}(x) := D(x)`, and ordering formula
`chi_{1,1}(x,y) := (x prec_A y)`.  These data are a finite one-copy MSO
string-transduction presentation; call it `M_A`.

To verify the presentation, partition the input into maximal intervals on
which the number of occurrences of `A` strictly before a position is
constant.  For two positions in different intervals, (1) orders their
intervals from left to right; within one interval, it orders positions from
right to left.  Thus `\prec_A` is a strict total order and `M_A` reverses each
such interval, in increasing interval order.

## Application to the level sorts

If `u,d>0`, every step strictly increases the starting level.  Hence the
positions already occur in strictly increasing level order and

\[
 \Phi_{u,d}^{L}=\Phi_{u,d}^{R}=\operatorname{id}
 \quad\text{on every input word}.                              \tag{2}
\]

For `(u,d)=(1,0)`, the starting level at a position is the number of earlier
`U` positions.  Its equal-level classes are exactly the intervals used in the
verification of `M_U`.  For `(u,d)=(0,1)`, the analogous marker is `D`.
Consequently, again on every input word,

\[
\begin{array}{c|cc}
(u,d)&L&R\\ \hline
(1,0)&\operatorname{id}&M_U\\
(0,1)&\operatorname{id}&M_D.
\end{array}                                                     \tag{3}
\]

Identity and one-copy MSO transductions are regular, hence polyregular.
Equations (2)--(3) therefore give explicit realizations on all Dyck inputs.

Finally use only the identity already proved in `problem.md`,

\[
 \Phi_{-u,-d}^{t}=\operatorname{rev}\circ
                   \Phi_{u,d}^{\bar t}.                        \tag{4}
\]

Output reversal is a regular transduction, and polyregular functions are
closed under composition.  Equations (2)--(4) settle the following exact
labeled triples as polyregular:

* identity: `(1,1,L/R)`, `(1,2,L/R)`, `(2,1,L/R)`, `(1,0,L)`,
  `(0,1,L)`;
* plateau MSO: `(1,0,R)` via `M_U`, `(0,1,R)` via `M_D`;
* reversal: `(-1,-1,L/R)`, `(-1,-2,L/R)`, `(-2,-1,L/R)`,
  `(-1,0,R)`, `(0,-1,R)`;
* reversal after plateau MSO: `(-1,0,L)` via `rev o M_U` and
  `(0,-1,L)` via `rev o M_D`.

These are 20 of the 32 labeled triples.  The twelve triples with mixed-sign
weights are not settled by this note.
