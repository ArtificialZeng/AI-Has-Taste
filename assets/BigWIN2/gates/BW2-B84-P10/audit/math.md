# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` claim.  The original
all-length top-row classification remains unresolved, as the candidate states.

## Frozen scope and integrity

I reviewed the statement in `claim.json` against snapshot digest
`3834d08af55e3093bb5d14d217a85162f2e55a6bf6324fd79bef15afbb1ca85f`.
All seven file hashes in `audit/snapshot.json` matched the current files.  In
particular, `source.md` retained SHA-256
`4b1056ed0d2c409f9cc07de953b852ea0dea8b612228770e77593f7baa1ebd69`,
and the local arXiv PDF retained the frozen v2 digest.

The candidate asserts a subsidiary theorem, not a solution of the source
question:

\[
 K_S\ne C_S\quad\Longrightarrow\quad |K_S|\ge 10
 \qquad(S\in\mathcal G_n,\ n\ge3),
\]

with sharpness at \((2,3,5,9,15)\), followed by the exact consequence
\(|K_S|\le9\iff K_S=C_S\) and \(A(S)\le7\), and a four-type reduction for the
ordered anti-diagonal.  It expressly does not claim the missing classification
of all top rows realizing those types.  I assessed that complete frozen scope.

## Reconstruction of the proof

First, every top-row entry \(s_j\) with \(j\ge2\) is odd.  For the prefix of
length \(j\), reducing its bottom difference modulo two gives

\[
 1\equiv\sum_{a=1}^j {j-1\choose a-1}s_a\pmod2.
\]

Induction from \(s_2=3\), together with
\(\sum_{a=2}^{j-1}{j-1\choose a-1}=2^{j-1}-2\), forces \(s_j\) odd.  Thus row
one has left entry 1 and all later entries even; the same property propagates
down every nontrivial row.  Consequently

\[
 e_1,\ldots,e_{n-2}\text{ are even},\qquad e_{n-1}=1. \tag{1}
\]

The realizability lemma used by the candidate is also valid.  Fix
\(i\le n-2\).  If \(e_{i+1}=\cdots=e_{n-2}=0\), view row \(i\) as
\((x_1,\ldots,x_L)\).  Successively reading the zero rightmost differences
forces \(x_2=\cdots=x_L=e_i\).  Since \(x_1=1\) and the first entry of the
next row is also 1, \(|e_i-1|=1\), hence

\[
 e_i\in\{0,2\}. \tag{2}
\]

Now assume \(K_S\ne C_S\).  Theorem 20 of the cited source supplies a failing
index; take the largest one and put
\(q=\sum_{j>i}e_j\).  The inequalities strictly to its right hold.  By (1),
\(q\) is odd.  If \(q=1\), all intervening even entries vanish, and (2) gives
\(e_i\le2=1+q\), contradicting failure.  Therefore \(q\ge3\).

Starting from \(T_{n-1}=\{1\}\), Proposition 18 and the holding tail
inequalities give, step by step,

\[
 T_i=\{0,2,\ldots,q+1\}.
\]

Indeed, after the initial \(P_1(\{1\})=\{0,2\}\), if the current set is
\(\{0,2,\ldots,R\}\) and the next even entry \(e\le R\), the lower and upper
branches of \(P_e\) have union \(\{0,2,\ldots,R+e\}\).  At the failing index,
\(e_i>q+1\).  Hence all lower branches are allowed, the reflected lower and
translated upper copies intersect only at \(e_i\), and

\[
 |T_{i-1}|=2|T_i|-1=q+2\ge5,\qquad 0\notin T_{i-1}. \tag{3}
\]

Every remaining outer preimage step is cardinality-nondecreasing because it
contains the injective translate \(e+T\).  If the final distance set
\(D_S=T_0\) omits zero, reflection gives \(|K_S|=2|D_S|\ge10\).  If it contains
zero, consider the first outer step at which zero appears.  The input then has
at least five nonzero elements; zero requires \(e\in T\), while the positive
translate \(e+T\) contributes \(|T|\) distinct elements in addition to zero.
Thus that step has at least six outputs, later cardinalities cannot decrease,
and \(|K_S|=2|D_S|-1\ge11\).  This proves the claimed gap without using the
bounded census.

For \(S=(2,3,5,9,15)\), the triangle is Gilbreath and its ordered
anti-diagonal is \((6,2,0,1)\).  Direct reverse calculation gives

\[
 \{1\}\to\{0,2\}\to\{0,2\}\to\{0,2,4\}
 \to\{2,4,6,8,10\},
\]

so
\(K_S=\{5,7,9,11,13,17,19,21,23,25\}\), of size 10, whereas
\(C_S\) also contains 15.  Sharpness is therefore exact.

Finally, when \(K_S=C_S\), parity makes \(|C_S|=A(S)+2\).  The gap theorem
therefore yields

\[
 |K_S|\le9\iff K_S=C_S\text{ and }A(S)\le7.
\]

Writing \(e_i=2a_i\) for \(i<n-1\), strict increase gives \(a_1\ge1\), and
the last condition gives \(\sum a_i\le3\).  Theorem 20 becomes
\(a_i\le1+\sum_{j>i}a_j\).  Exhausting totals one, two, and three leaves
exactly: \(e_1=2\); \(e_1=2\) plus one later 2; \(e_1=2\) plus two later 2s;
or \(e_1=4\) plus one later 2.  Each listed type satisfies the inequalities.
Thus the claimed four-type anti-diagonal reduction is both necessary and
sufficient at that level, while realization by top rows is correctly left
open.

## Checks performed

- I inspected Proposition 18, Theorem 20, the length-five example, and open
  question 16(5) in the frozen primary-source PDF.  Their statements and
  hypotheses agree with the candidate's use: the reverse step is ordered and
  its lower branch is allowed only for \(e\ge t\).
- I separately implemented direct difference-triangle generation and direct
  testing of every extension in the exhaustive radius through \(n=8\), without
  importing the submitted program.  The sequence/defective counts were
  \((1,0),(2,0),(6,1),(27,5),(180,60),(1786,760)\) for \(n=3,\ldots,8\), and
  the minimum defective width was 10 whenever defective sequences existed.
  The zero-tail lemma held for every generated anti-diagonal.  These values
  agree with the frozen census.  This computation is corroborative only.
- Code inspection confirmed that `enumerate_threshold.py` generates increasing
  children by direct triangle tests as well as by the reverse tree, compares
  the two frontiers exactly, and directly reconstructs \(K_S\) for every
  minimum-width hit.  Its finite range is exhaustive because for
  \(d>A(S)\) the folds have no sign change and end at \(d-A(S)\), so only
  \(d=A(S)+1\) can be valid outside \([0,A(S)]\).

## Source comparison and contribution

The frozen arXiv v2 source proves the ordered reverse recurrence (Proposition
18), interval-completeness criterion (Theorem 20), and unique width-five
minimum (Theorem 25).  It identifies \((2,3,5,9,15)\) as the first hole and
asks in question 16(5) for the width-at-most-nine stability classification.
It does not state the all-length defective-width gap or the resulting four-type
reduction.  A fresh, limited exact-term and equivalent-term search of arXiv on
2026-09-09 found that preprint but no separate primary source claiming the
gap.  This is evidence only for the candidate's appropriately bounded novelty
language, not proof of priority.

The theorem is a nontrivial all-length obstruction using a realizability fact
that is unavailable for arbitrary folding tuples, and it makes a direct,
useful reduction of the stated open problem.  It is therefore substantial
enough for the frozen `result-note` category rather than a toy restriction or
mere finite observation.

## Gaps and verdict

I found no mathematical gap in the frozen subsidiary theorem, sharpness
claim, equivalence, or anti-diagonal enumeration.  The unresolved gap is
exactly the one disclosed by the candidate: classify the normalized top rows
realizing the four ordered anti-diagonal types.  That missing step prevents a
resolution of `source.md` but does not weaken the proved result-note scope.

**Verdict: accept.**
