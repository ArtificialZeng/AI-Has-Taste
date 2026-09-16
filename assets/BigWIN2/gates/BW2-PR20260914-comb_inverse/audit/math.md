# Fresh mathematical referee report

**Verdict: accept the exact frozen claim.** The argument proves the complete
support-refined compositional inverse in Q(t)[[x]], at every degree.

Job: `primary-20260914-comb-inverse-referee-6f40fd4698e5`.
Review date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).
Snapshot: `fac6a5d3e0cc11fe8e7a02ae312a3c4409afeaca9b3251dfc764c6d793a56ea2`.
Frozen workflow fields: `kind=resolution-paper`, `original_status=proved`.

## Scope and input integrity

The accepted statement is precisely the statement in `claim.json` and
`source.md`: the recursively defined minimum-rooted comb, all lower-ideal
inequalities, the raw lattice-point support statistic, the factor t^(-n),
and both formal compositions. There is no finite-range restriction, replacement
by t=1, or change from support enumeration to an Ehrhart h-star polynomial.

The eleven snapshot files were rehashed and all match. The snapshot digest was
also recomputed from the sorted-key, compact JSON file-to-hash mapping and
matches. Its file set is exactly `claim.json` together with the claimed
evidence list. The original source remains byte-for-byte unchanged, with hash
`43669ff2a9b8b7c472001ccd2e726fe69f54a96d58bb34957d636160c09bcfce`.

Local review inputs were limited to the four prescribed files and the
snapshot-listed evidence. Relevant primary sources were additionally inspected
live. No earlier audit, checkpoint, state, job transcript, or progress summary
was read. Proposer conclusions embedded in required inputs were disregarded.
This is a fresh referee context under the supplied job ID; it is not a claim
of statistically independent evidence or external human peer review.

## Reconstructed argument

Write q=1+t and K=Q(t). Use r_1,...,r_n for the spine, starting at the minimum,
and s_i for the leaf immediately above r_i. Induction from the original
recursion gives exactly the covering relations used in the proof dossier.

Every nonempty ideal has the form

    {r_1,...,r_k} union {s_i : i in S},  S subseteq {1,...,k}.

No leaf can occur without its parent and all preceding spine vertices; these
are all its predecessors. Conversely each displayed set is an ideal. With
a_i=x_(r_i), b_i=x_(s_i), its inequality is

    sum_(i<=k) a_i + sum_(i in S)(b_i-1) <= k.

The maximum over S is the sum of the positive parts. Therefore the entire
inequality system is equivalent, in both directions, to

    sum_(i<=k) c_i <= k,   c_i=a_i+max(b_i-1,0),   1<=k<=n.

This is stronger than checking only principal ideals and retains every
inequality of the frozen problem. The empty ideal is vacuous.

For c=0, the local coordinate pairs are (0,0) and (0,1), giving w_0=q.
For c>=1, (c,0) and (0,c+1) have support one; the remaining c pairs have
support two. Thus w_c=2t+ct^2. Fixing costs separates the choices of the
coordinate pairs, and the support statistic adds. Consequently h_n is the
sum of products of these weights over all allowed cost sequences, and

    W(t,u) = sum_(c>=0) w_c u^c
           = (1+(t-1)u)(q-u)/(1-u)^2.

The decisive combinatorial step also holds in both directions. Prepend zero
to a cost sequence and process its degrees from left to right. At degree c_i,
the number of available completed trees is i-sum_(j<i)c_j. Replacing its
last c_i entries by a parent with those ordered children is legal exactly
when sum_(j<=i)c_j<=i. Degree zero appends a leaf. After each operation the
stack is nonempty, and its concatenated postorder word is the processed word.

Conversely, processing an actual ordered forest in postorder leaves a
completed subtree precisely when that subtree's root is processed. At each
parent, its children are the last completed trees in their given order.
Induction over subtrees and then components reconstructs the original forest
uniquely. The first postorder vertex is always a leaf. This proves the
bijection with all nonempty ordered forests on n+1 vertices, without a
labelling multiplicity or an assumption that the final forest is connected.

Give a degree-c vertex weight z w_c, and let T enumerate trees. Root
decomposition yields T=zW(t,T), with T=qz+O(z^2). The generating series of
nonempty forests is T/(1-T). Under the bijection the first postorder vertex
is one specified extra leaf. Its two possible cost-zero decorations give
exactly qz; no leaf is chosen or marked arbitrarily. Therefore, with
H(z)=sum_(n>=0)h_n(t)z^n,

    qz H(z) = T(z)/(1-T(z)).

For n=0 this is the single-vertex forest of weight qz and yields h_0=1.
At each size there are finitely many shapes and decorations. Hence the
tree equation and every infinite sum above are coefficientwise finite.

Now set U=T(x/t). Since F=xH(x/t),

    F=tU/[q(1-U)],       U=qF/(t+qF),       U=(x/t)W(t,U).

Direct substitution into the displayed factorization of W gives
W(t,U)=q(1+F)(1+qF), and hence

    x=F/[(1+F)(1+qF)(1+qF/t)].

Finally, sum the original coefficients of R rather than assuming its rational
form. The initial 1 contributes y/(1+y). In the remaining sum put m=k+2,
a=j and b=k-j; summation over the finite diagonals a+b=k gives

    R(t,y)=y/(1+y)-q^2 y^2/[(1+qy)(t+qy)]
          =y/[(1+y)(1+qy)(1+qy/t)].

For the last simplification the cleared numerator identity is
(1+qy)(t+qy)-q^2 y(1+y)=t. This proves R(t,F)=x. Both series have zero
constant coefficient and linear coefficient one. Recursive coefficient
inversion therefore gives F(t,R)=x as well. These steps are an all-degree
proof, independent of the numerical checks.

## Attacks on hypotheses and boundary cases

All substitutions use series of zero constant coefficient. Division by t
and q is legitimate in K, and all series denominators have nonzero constant
coefficients. Division by z removes an explicitly present factor. No analytic
limit, convergence, compactness, or finite-step path theorem is used.

The argument includes zero costs, all-zero words, costs exhausting the
available prefix budget, and words with final total strictly smaller than n.
The last case produces several tree components and is why all forests occur.
Ordered children and ordered components account for uniqueness without any
extra factorial. Local decorations preserve the full support parameter.

The m=1 inner sum is empty as required. Specializing F at t=0 or the forest
quotient at t=-1 is not used. The polynomial consequence

    H=(1+tzH)(1+tqzH)(1+qzH)

is valid in Z[t][[z]], since its residual polynomials vanish in Q(t). Its
specializations give H=1/(1-z) at t=0 and H=1/(1+z) at t=-1. These observations
do not extend the original Laurent series to an undefined scalar value.

## Fresh exact verification actually performed

`python3 audit/referee-check.py` completed successfully and wrote
`audit/referee-check.json`. It uses Python's standard library and exact integer
arithmetic. It imports and executes neither proposer program and modifies no
frozen input. Its SHA-256 is
`3e7cf2e1039fe76ed179f4c1df08c526b109d488e0ad7b5f501f2bff4aebbf76`.

The fresh implementations enumerate vectors by stars and bars, generate the
ideal family directly from the original minimum-adjunction recursion, and
encode forests by balanced-parenthesis strings. These differ from the
proposer's vector recursion and recursive tuple-of-trees enumeration.

| Check | Actual coverage | Result |
| --- | --- | --- |
| Local coordinate-pair weights | c=0,...,25 | All match w_c |
| Original all-ideal membership versus prefix membership | n=0,...,5; 198,627 ambient vectors | No discrepancy |
| Direct support coefficients | n=0,...,5 | Match inverse coefficients |
| Parenthesis-encoded forests versus all admissible cost words | 1,...,9 vertices; 6,917 forests; 17,577 ambient words | Exact sets match; no duplicate degree words |
| First-leaf normalization and support weights | n=0,...,8 | Full forest weight equals q times h_n |
| Separate coefficient extraction versus both frozen coefficient lists | n=0,...,12 | Exact agreement |
| Original R(F), F(R), and R times its proposed denominator | Through x^13 over Z[t,t^(-1)] | Each is exactly x in this truncation |
| Polynomial evaluations | n=0,...,12 at t=0 and t=-1 | h_n(0)=1 and h_n(-1)=(-1)^n |

For the separate coefficient extraction, the verifier expands

    (1/(n+1)) [u^n] ((1+tu)(1+tq u)(1+q u))^(n+1)

by binomial sums. This is a finite check oracle from formal Lagrange inversion
of the claimed rational inverse, not an additional theorem claimed by this
review. Direct lattice enumeration checks the polytope connection through
n=5; independent forest enumeration checks it through n=8; comparison with
the supplied prefix recurrence reaches n=12. The proof, not extrapolation
from these ranges, establishes the general connection. The larger proposer
forest run was inspected as code and data, but was not independently rerun
and is not reported as fresh coverage.

## Primary-source comparison and contribution

The archived source's Sections 1, 5, and 9.6 were inspected using their actual
mathematical text and compared with the live primary page. They define the
same all-ideal polytope and support statistic and propose the same refined
comb inverse. It is an unnumbered proposal, distinct from Conjecture 5.4.
The live submission history displayed only v1. This is a version observation,
not a certificate of worldwide open status.
[Athanasiadis--Chapoton, Section 9.6](https://arxiv.org/html/2605.26916v1#S9.SS6),
[submission history](https://arxiv.org/abs/2605.26916).

The nearest prior general enumeration machinery inspected is Chapoton's
support-and-height recursion, Propositions 2.8 and 2.9. Its displayed
statements give recursive arbor coefficients; they do not state the explicit
comb inverse reviewed here. The proof under review does not invoke them.
[On posets and polytopes attached to arbors](https://arxiv.org/html/2503.04247v2).

Weighted-tree inversion is classical. Banderier--Flajolet, Example 3,
printed page 52, equation (24), displays the tree equation and Lagrange
coefficient formula in a finite-degree setting. That source uses a preorder
tree traversal; the present forest coding is supplied and proved directly.
The unbounded-degree formal equation here is justified coefficientwise, so
none of that paper's finite-step analytic hypotheses is silently imported.
[Basic analytic combinatorics of directed lattice paths](https://lipn.fr/~banderier/Papers/tcs_banderier_flajolet_2002.pdf).

Wang et al., Theorem 1.3 and its following paragraph, explicitly establish
support-enumerator duality and identify the preorder application as a proof
of Conjecture 5.4. Thus the research screen's correction of the earlier
duality-status description is warranted. The theorem is acknowledged prior
work, not a dependency or contribution of this candidate. A live text search
found no occurrence of "comb" in that paper.
[Counting Lattice Points in Minkowski Sums of Cross Polytopes](https://arxiv.org/html/2608.16037v1).

Two nearby source families checked are stars: the root with singleton leaves
in Athanasiadis--Xiao--Yan, and the extension allowing doubleton leaves in the
octopus paper. Their inspected statements concern those families, rather
than arbitrary-length combs.
[Lattice point enumeration of some arbor polytopes](https://arxiv.org/html/2603.11654v1),
[Gamma-positivity for octopuses: a bijective proof](https://arxiv.org/html/2608.13247v1).

A new search lead, Yan's colored multiset Eulerian paper, was checked at its
abstract and Section 5.3, including Corollary 5.4. That application enumerates
the Ehrhart h-star polynomial of the associated reflexive polytope; it does
not state the present raw-support comb inverse in the inspected passages.
[Variations of colored multiset Eulerian polynomials and applications](https://arxiv.org/html/2608.15682v1#S5.SS3).

Independent live searches included the exact source identifier with comb and
inverse, the source title with comb, "comb" "support" "compositional inverse"
proof, "A034015" "polytopes", and "comb" "Chapoton" "inverse". No equivalent
resolution was found in the primary passages inspected on the review date.
Searches were noisy and do not exclude unindexed work or older equivalent
enumerations. Absolute priority is not certified, consistent with the frozen
candidate's qualification. No external theorem requires an unaudited
hypothesis to complete this proof.

The precise contribution is the full resolution of the specified source
proposal: reducing all comb ideal inequalities to local support-weighted
prefix costs, identifying the forest boundary factor, and deriving the
explicit inverse. The credible use is exact support enumeration for every
comb size from a single algebraic equation. Neither a new general tree
inversion principle nor a new support-duality theorem is claimed. This scope
passes the contribution test and is not an arbitrary restriction of the
original problem.

## Final decision and remaining work

Scope, correctness, and contribution pass. **Accept**, with no identified
mathematical gap and no required revision to the frozen statement or proof.
No stronger assertion of global priority, formal proof-assistant certification,
or journal acceptance is made.

The runner should perform `check-math` against this snapshot and the existing
job provenance before dispatching manuscript work. That structural gate was
left to the runner; no job metadata was read or invented in this review.
The manuscript should retain the original support statistic, the full
indeterminate-t scope, the canonical-first-leaf explanation, and the bounded
prior-work language. No manuscript, publication file, checkpoint, or state
file was created or changed by this referee.
