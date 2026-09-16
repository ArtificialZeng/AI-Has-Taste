# Coset proof and full automorphism-group derivation

Research job: `win-00086-p02-research-ebf264565005`  
Date: 2026-09-10  
Status: elementary proof, independently rederived without using the finite
enumeration in `triage_exact_check.py`.

## Theorem

Let

\[
F_1=\{s\in S_4:s\text{ has exactly one fixed point}\},\qquad
V_4=\{1,(12)(34),(13)(24),(14)(23)\}.
\]

With the left-Cayley convention in `problem.md`,

\[
\operatorname{Cay}(S_4,F_1)\cong A(4,4,3)\cong 2K_{4,4,4},
\]

and

\[
\operatorname{Aut}(A(4,4,3))
 \cong (S_4\wr S_3)\wr S_2,
\]

where the wreath products use their natural imprimitive actions. Its order is
13,759,414,272. Consequently Conjecture 3.1 of Pan's arXiv v1 is false at
`(n,t)=(4,1)`.

## Proof

### 1. The connection set

A permutation of four letters with exactly one fixed point acts without a
fixed point on the other three letters. The only fixed-point-free
permutations of a three-element set are its two 3-cycles. Conversely, a
3-cycle in `S_4` fixes the remaining letter. Hence

\[
F_1=\{(123),(132),(124),(142),(134),(143),(234),(243)\}.
\]

These are precisely the eight 3-cycles. The even permutations in `S_4` are
the identity, the three double transpositions, and the eight 3-cycles, so

\[
F_1=A_4\setminus V_4. \tag{1}
\]

The displayed set `V_4` is a subgroup: each nonidentity element is an
involution and the product of two distinct nonidentity elements is the third.
It is normal in `S_4`, since conjugation preserves the cycle type of the three
double transpositions. (Normality is useful context, although the left-coset
argument below only needs the subgroup property.)

### 2. Cayley adjacency is exactly coset adjacency

For `g,h in S_4`, the Cayley convention gives

\[
g\sim h \quad\Longleftrightarrow\quad hg^{-1}\in F_1. \tag{2}
\]

For completeness, identify `g` with `[g(1),g(2),g(3),g(4)]`. The fixed
points of `hg^{-1}` correspond bijectively to the indices `i` for which
`h(i)=g(i)`: use the bijection `i \mapsto g(i)`. Thus (2) is also exactly the
rule that the two tuples differ in three coordinates, proving the stated
Cayley/arrangement-graph identification.

Let `epsilon(g)` be the parity of `g`. By (1) and (2),

\[
\begin{aligned}
g\sim h
&\Longleftrightarrow hg^{-1}\in A_4\setminus V_4\\
&\Longleftrightarrow
  \epsilon(g)=\epsilon(h)\ \text{ and }\ hg^{-1}\notin V_4\\
&\Longleftrightarrow
  \epsilon(g)=\epsilon(h)\ \text{ and }\ V_4g\ne V_4h. \tag{3}
\end{aligned}
\]

The last equivalence follows from
`hg^{-1} in V_4` if and only if `h in V_4 g`, which is equivalent to equality
of the left cosets containing `h` and `g`.

Every left `V_4`-coset has four elements of one parity. The twelve even and
twelve odd permutations therefore each split into exactly three such cosets.
Equation (3) says that within either parity class there are no edges inside a
coset and all possible edges between distinct cosets. Hence each parity class
induces `K_{4,4,4}`. Each such graph is connected, while (3) gives no edge
between the two parity classes. These are therefore exactly the two connected
components, proving

\[
A(4,4,3)\cong 2K_{4,4,4}. \tag{4}
\]

### 3. All graph automorphisms

Put `Y=K_{4,4,4}` and denote its three parts by `P_1,P_2,P_3`. Every
independent set of `Y` is contained in one part, because vertices in distinct
parts are adjacent. It follows that the maximal independent sets are exactly
`P_1,P_2,P_3`. Every graph automorphism must therefore permute these three
parts. The kernel of this action consists of arbitrary and independent
permutations within the parts, and so is `(S_4)^3`. Conversely, every
permutation of the parts and every choice of bijections within the parts
preserves adjacency. Thus the action on the parts is the full `S_3`, splits,
and

\[
\operatorname{Aut}(Y)\cong(S_4)^3\rtimes S_3=S_4\wr S_3,
\qquad
|\operatorname{Aut}(Y)|=(4!)^3 3!=82{,}944. \tag{5}
\]

By (4), every automorphism of the full graph permutes its two connected
components. The kernel of that action is
`Aut(Y) times Aut(Y)`, while interchanging the two isomorphic components
realizes the nontrivial element of `S_2`. This action also splits, with `S_2`
exchanging the two factors. Therefore

\[
\operatorname{Aut}(A(4,4,3))
\cong\operatorname{Aut}(Y)^2\rtimes S_2
\cong(S_4\wr S_3)\wr S_2, \tag{6}
\]

of order

\[
\big((4!)^3 3!\big)^2 2!=13{,}759{,}414{,}272. \tag{7}
\]

### 4. Comparison with the conjectured group

The center of `S_4` is trivial, so `Inn(S_4)` is isomorphic to `S_4` and has
order 24. The group prescribed by Conjecture 3.1 at this parameter consequently
has order

\[
|R(S_4)|\,|\operatorname{Inn}(S_4)|\,2=24\cdot24\cdot2=1{,}152. \tag{8}
\]

The orders in (7) and (8) differ, so the asserted isomorphism/equality cannot
hold. This disproves that universally quantified conjecture at `(n,t)=(4,1)`.
QED.

## Dependency and gap audit

- Dependencies: the definitions frozen in `source.md` and interpreted in
  `problem.md`; elementary permutation parity, left cosets, connected
  components, and maximal independent sets.
- The graph classification and full-group derivation above have no known
  mathematical gap.
- This proof concerns the precisely frozen Conjecture 3.1 in arXiv
  `2407.19745v1`. It makes no claim that the conjecture is retained in the
  inaccessible 2027 journal full text, and no novelty or priority claim.
- The exhaustive program and output in `evidence/triage_exact_check.py` and
  `evidence/triage_exact_check.txt` provide a separate exact finite
  cross-check, but no step of this proof depends on their enumeration.
