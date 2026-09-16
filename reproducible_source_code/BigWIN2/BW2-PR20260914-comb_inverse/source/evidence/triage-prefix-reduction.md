# Comb prefix reduction and uniform proof route

Job: primary-20260914-comb-inverse-triage-109258fe42b6.
Date: 2026-09-14 Asia/Shanghai. This is a triage derivation, without a fresh
mathematical review or candidate acceptance.

## Exact ideal reduction

Index the spine r_1<...<r_n from its minimum, with s_i the leaf above r_i.
Every nonempty lower ideal has the form

    {r_1,...,r_k} union {s_i : i in S},  1<=k<=n, S subset of {1,...,k}.

Indeed, its spine part must be an initial segment; a leaf can be included only
if its spine parent is included. Conversely every displayed set is an ideal.
For a_i=x_(r_i), b_i=x_(s_i), its inequality is

    sum_(i<=k) a_i + sum_(i in S) (b_i-1) <= k.

Maximizing independently over S proves equivalence to the n constraints

    sum_(i<=k) c_i <= k,  c_i=a_i+max(b_i-1,0),  1<=k<=n.       (1)

This reduction works for real nonnegative coordinates; enumeration below uses
nonnegative integer coordinates. It retains all ideals, including those with
several incomparable leaves.

## Local support weights and exact recurrence

For a nonnegative integer c, let w_c(t) be the support enumerator of pairs
(a,b) with a+max(b-1,0)=c. Directly,

    w_0=1+t,                 w_c=2t+c t^2  (c>=1),
    W(t,u)=sum_(c>=0) w_c(t)u^c
          =(1+(t-1)u)(1+t-u)/(1-u)^2.                         (2)

For c=0 the pairs are (0,0),(0,1). For c>=1 the support-one pairs are
(c,0),(0,c+1); there are exactly c support-two pairs. Thus h_n is the sum of
product_i w_(c_i) over the integer sequences in (1), preserving the full
support statistic rather than only cardinality.

Equivalently, with D_0(0)=1 and all other states zero, use heights
s=k-sum_(i<=k)c_i. From height s append any 0<=c<=s+1 with weight w_c,
and move to s+1-c. Summing states at length n gives h_n. This is the recurrence
implemented in `triage-prefix-check.py`.

## Weighted forest step to verify in the research pass

Put H(z)=sum_(n>=0) h_n(t)z^n. Let T(z) be the series of nonempty ordered
rooted trees with a vertex of outdegree c weighted z w_c(t). Root decomposition
gives T=z W(t,T), T(0)=0. Nonempty ordered forests then have series T/(1-T).

The proposed precise correspondence is to send a sequence c_1,...,c_n in (1)
to the postorder degree sequence (0,c_1,...,c_n) of a nonempty ordered forest.
To reconstruct it, keep a stack of completed trees. Each degree d consumes the
last d trees (in their existing order), makes them the children of a new root,
and pushes the resulting tree. Before processing c_i the stack has
i-sum_(j<i)c_j trees, so (1) is exactly the condition that enough trees exist.
The initial degree zero supplies the first leaf. The final stack is the forest.
Conversely, postorder traversal of a nonempty forest starts with a leaf and
has precisely these inequalities. Formalize this inverse correspondence and
check that no marking multiplicity is introduced: it is the first leaf, not an
arbitrarily selected leaf.

The initial leaf has weight z w_0=z(1+t), whereas the original sequence has
only the n subsequent weighted entries. Thus the correspondence would give

    H(z)=T(z)/[z(1+t)(1-T(z))].                               (3)

This includes n=0: a one-vertex forest contributes exactly one after division.
Division by z is valid because T is divisible by z; 1+t is invertible in Q(t).
Unbounded degrees cause no formal summability issue: each fixed total size
uses only finitely many degrees. The classical tree equation is prior art;
the comb interpretation and boundary factor need the project-specific proof.

## Algebraic consequence of (3)

Set c=1+t, z=x/t and U=T(x/t). If (3) holds, then

    F(t,x)=t U/[c(1-U)],    U=c F/[t+c F].

Substituting the latter into (2) gives

    W(t,U)=c(1+c F)(1+F),
    x=F/[(1+F)(1+c F)(1+c F/t)].                              (4)

The source's proposed inverse sums, over Q(t), to

    R(t,y)=y/(1+y) - c^2 y^2/[(1+c y)(t+c y)]
          =y/[(1+y)(1+c y)(1+c y/t)].                         (5)

One way to check the first equality is to replace the inner finite geometric
sum by (1-t^(m-1))/(1-t), sum the two geometric series for m>=2, and cancel
1-t. Equation (5) is an identity of rational functions over Q(t); no evaluation
at a singular intermediate expression is required. Together (3)--(5) give a
specific route to the full original identity, rather than a new conjecture
inferred from coefficient agreement.

## Reproducible finite evidence and limits

Run `python3 evidence/triage-prefix-check.py` from the project root. The output
`triage-prefix-check.json` records all checks. For every n=0,...,5 it enumerates
all nonnegative vectors with sum at most 2n and constructs every lower ideal
from predecessor masks; direct membership agrees with (1) for all 198627
vectors. This domain is exhaustive because the full-set ideal bounds the sum.
The independent-from-intake implementation reproduces every h_n through n=5.
The prefix recurrence computes n=0,...,12 with integer arithmetic, and the
Laurent-series composition R(F) is x through degree 13. Multiplication also
checks the three-factor expression (5) through degree 13.

These checks test the reduction and algebra but do not replace the all-n
forest proof or an independent referee. No counterexample was found in the
stated finite ranges. The next decisive task is the all-n verification of (3),
with both directions, support weights, and empty-case normalization explicit.
