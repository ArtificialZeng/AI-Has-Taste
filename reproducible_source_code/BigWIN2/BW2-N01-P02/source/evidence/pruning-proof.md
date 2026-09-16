# Proof candidate: the ordered associative spectrum of SC258

Proposer job: newwin-00001-p02-research-0e4a4dc1b1e3.
Date: 2026-09-12. Status: complete proposed proof, pending fresh referee.
This is a mathematical evidence dossier, not an accepted manuscript.

## Exact statement

Let A={0,1,2} and define the binary operation by

    * | 0 1 2
    --+------
    0 | 0 0 0
    1 | 1 1 0
    2 | 1 0 1.

Let B_n be all binary bracketings with leaves x_1,...,x_n in this fixed
order, each used once, and let a_n count the distinct induced functions
A^n -> A. Then a_1=a_2=1, a_3=2 and, for every n>=4,

    a_n = 3 a_(n-1) - 2 a_(n-2) + a_(n-3).

Equivalently, as a formal power series,

    sum_(n>=1) a_n z^n = z(1-z)^2/(1-3z+2z^2-z^3).

The operation table and the definition above are exactly those in source.md
and problem.md. No permutation of variables or identification of inessential
coordinates is made when comparing n-ary functions.

## 1. Pruning preserves the function

A tree is composite if it is not a single leaf. Every composite term takes
values in {0,1}, and b*c=b for b,c in {0,1}. Therefore u*v and u induce the
same function, with the variables of v ignored, whenever both u and v are
composite.

Define P on labeled trees recursively:

* P(x_i)=x_i.
* If t=(u*v) has two composite children, P(t)=P(u).
* Otherwise P(t)=(P(u)*P(v)).

Labels are retained exactly, including any gaps. Structural induction proves
t^A=P(t)^A on the full original set of variables. The same induction proves
that P(t) has at least two leaves when t is composite, retains t's first
leaf, and has a leaf child at every internal node. Call a tree with the last
property a comb. In particular, pruning never turns a composite subtree into
a leaf.

## 2. A comb is uniquely determined by its function

Here allow any increasing sequence of distinct leaf labels, not necessarily
consecutive or obtainable by pruning. A variable is essential for a function
if changing only that coordinate can change its value.

**Lemma 1 (essential variables).** The essential variables of a labeled comb
are exactly its leaves.

Proof. The assertion is immediate for one leaf. For two leaves x_i*x_j,
vary x_i between 0 and 1 with x_j=0, and vary x_j between 0 and 2 with
x_i=1. Both leaves are essential. For a larger comb exactly one root child
is a leaf. If g denotes the function of the composite child, the table gives

    (x_i*g)|_(x_i=0) = 0,
    (x_i*g)|_(x_i=1) = 1,
    (x_i*g)|_(x_i=2) = 1-g;

    (g*x_j)|_(x_j=0) = g,
    (g*x_j)|_(x_j=1) = g,
    (g*x_j)|_(x_j=2) = 0.

Thus every essential variable of g remains essential: use x_i=2 in the first
case and x_j=0 in the second. The new left leaf is essential by its constant
0 and 1 sections. The new right leaf is essential because g takes value 1
when all its leaves equal 1 (1*1=1), and its 0 and 2 sections then differ.
No absent variable can affect the value. Induction proves the lemma.

**Lemma 2 (separation).** Two combs whose labels increase from left to right
induce the same function on a common ambient set of variables if and only
if they are the same labeled tree.

Proof. Equality implies equality of the essential leaf sets by Lemma 1.
Induct on their common cardinality k. For k=1 or 2 there is only one ordered
tree on that leaf set. Suppose k>=3, and write i and j for its least and
greatest labels. There are exactly two possible root types:

    L: x_i*u, where u is composite;
    R: u*x_j, where u is composite.

For type L the section at x_i=1 is identically 1. For type R that section
is not constant: set all leaves of u to 1, so u=1 and x_i=1, and vary x_j
from 0 to 2. The outputs are respectively 1 and 0. Consequently equal
functions must have the same root type.

For type L, the child function is recovered as 1-f|_(x_i=2). For type R,
it is recovered as f|_(x_j=0). Equal parent functions therefore have equal
child functions on the remaining labels. The induction hypothesis gives
equal child trees and hence equal parent trees. The converse is immediate.

It follows that for s,t in B_n,

    s^A=t^A  if and only if  P(s)=P(t).

This proves the separation claim left open by the triage pilot. It also
shows why gaps in the surviving labels cannot be silently renumbered:
the surviving label set is precisely the essential support of the function.

## 3. Removing an ignored terminal interval

For n>=2 let S_n={P(t):t in B_n}. Let C_n consist of the elements of S_n
whose largest leaf label is n, and put c_n=|C_n|. By Lemma 2, a_n=|S_n|.
The sets C_m for different m are disjoint as sets of labeled trees.

**Lemma 3 (terminal interval).** If p in S_n has largest label m, then m>=2,
p belongs to C_m, and either m=n or m<=n-2. Conversely, if p belongs to
C_m and n>=m+2, then p belongs to S_n.

Proof. The first assertion follows from retention of the first leaf and of
at least two leaves. Prove the rest of the forward assertion by induction on
n, also allowing a uniform shift of the interval of labels. If m=n it is
immediate. Suppose m<n and choose t with P(t)=p.

A root with right child x_n is impossible, since that leaf would survive.
If the root has left child x_1 and composite right child v on labels 2,...,n,
apply the induction hypothesis to v. The last retained label is still m,
so n-m>=2, and there is a bracketing v' on labels 2,...,m with
P(v')=P(v). Then x_1*v' is a bracketing on 1,...,m that prunes to p.
If both root children are composite, write them as u on 1,...,k and v on
k+1,...,n, where k<=n-2. Now p=P(u). The induction hypothesis applied to
u (or u itself if m=k) gives a bracketing on 1,...,m that prunes to p.
Also m<=k<=n-2. These exhaust the possibilities. They prove p in S_m,
and its largest label is m, so p in C_m.

For the converse choose t in B_m with P(t)=p, and choose any bracketing v
on the n-m>=2 following labels. Both t and v are composite. Therefore
P(t*v)=P(t)=p, proving p in S_n.

In particular, exactly one ignored terminal variable is impossible. Combining
the two directions of this lemma gives the disjoint decomposition, for n>=2,

    S_n = C_n disjoint-union (disjoint-union_(m=2)^(n-2) C_m),
    a_n = c_n + sum_(m=2)^(n-2) c_m.                         (1)

An empty sum is zero.

## 4. Counting the forms retaining the last variable

Clearly C_2={x_1*x_2}, so c_2=1. For n>=3 consider any raw bracketing
whose pruning belongs to C_n. Its root cannot have two composite children:
pruning at such a root deletes the entire right child, including x_n.

If its left child is x_1, the pruned right subtree retains x_n. The resulting
forms are in bijection with C_(n-1), after shifting all labels by 1 and
adjoining the left leaf x_1. If its right child is x_n, its pruned left
subtree can be any member of S_(n-1), giving a bijection with that set.
Every form in either construction is attained by the corresponding raw
bracketing. The two constructions are disjoint because the composite child
lies on opposite sides; pruning preserves its being composite. Hence

    c_n = c_(n-1) + a_(n-1),       n>=3.                    (2)

These are bijections of labeled trees, so there is no implicit count of
multiple raw bracketings realizing the same form.

Let C(z)=sum_(n>=2)c_n z^n and F(z)=sum_(n>=2)a_n z^n. Equations (1) and
(2), respectively, give identities of formal power series

    F(z) = (1 + z^2/(1-z)) C(z),
    C(z) = z^2 + z C(z) + z F(z).

Solving these equations (all denominators have constant term 1) gives

    C(z) = z^2(1-z)/(1-3z+2z^2-z^3),
    F(z) = z^2(1-z+z^2)/(1-3z+2z^2-z^3).

Since a_1=1, adding z to F(z) yields the asserted generating function.
Coefficient extraction gives a_1=a_2=1, a_3=2 and the stated recurrence
for every n>=4. As a boundary check, c_3=2, c_4=4 and a_4=c_4+c_2=5.

## Dependencies, contribution, and limits

The proof uses only the displayed operation table, structural induction,
essential-variable restrictions, disjoint set decompositions, and formal
power-series algebra. It does not depend on extrapolating finite data or on
any external theorem. The primary paper is needed for the provenance of
the problem and the comparison with prior work, not for a lemma of this proof.

Nearest inspected prior statement: Huang and Lehtonen (2024), Definition 1.1
and Section 7, lists the first nine values for this operation and notes their
agreement with a Padovan trisection, without a general formula. The proposed
contribution is the all-arity classification by pruned labeled trees and the
complete recurrence for the exact operation in source.md. Bounded current
literature searches are documented separately; no exhaustive priority claim
is made. Other groupoids and the spectrum allowing variable permutations
are outside this claim.

Known mathematical gap list: empty after the proposer's checks. Fresh
mathematical review is still required. The accompanying exact computations
are reproducible finite crosschecks, not the justification for the all-n
result and not an independent referee review.
