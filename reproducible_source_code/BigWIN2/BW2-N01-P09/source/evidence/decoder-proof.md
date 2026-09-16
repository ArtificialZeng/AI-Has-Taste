# SC229: all-arity decoding and exact counting

Proposer: `newwin-00001-p09-research-6b8b4cffaffd`.
Date: 2026-09-12. This is a proof dossier submitted for a fresh mathematical
referee, not an acceptance record or publication manuscript.

## Exact statement

Let A={0,1,2}, and define a*b by the table with rows 000, 101, 111,
in the order 0,1,2 for both arguments. Let I be any finite nonempty set of
distinct variable labels. A full linear term on I uses every x_i, i in I,
exactly once and has only the binary operation *, with arbitrary variable
order and full binary bracketing. Coordinate labels are fixed.

A decorated tree on I is a rooted tree with vertex set I, with exactly one
distinguished child at each vertex that has children; all other children are
unordered. Then full linear term functions on A^I are in bijection with these
decorated trees. Explicitly, associate to a term's leftmost decomposition

    t = (((x_i * R_1) * R_2) ... * R_m)

the tree rooted at i, whose distinguished child is the tree for R_1 and whose
other children are the trees for R_2,...,R_m, as an unordered set. A singleton
term corresponds to the one-vertex tree. Two terms induce the same function
if and only if their decorated trees coincide as labelled decorated trees.

Consequently, for the original c_n and the formal exponential generating
series T(x)=sum_{n>=1} c_n x^n/n!,

    T(x) = x(1 + T(x) exp(T(x))),
    c_n = (n-1)! [u^(n-1)] (1+u exp(u))^n
        = (n-1)! sum_{k=0}^{n-1} binom(n,k) k^(n-1-k)/(n-1-k)!.

The convention is 0^0=1, including n=1. No c_0 is required or asserted.
The proof below also gives an integer counting recurrence without requiring
coefficient inversion.

## 1. Evaluation, nonconstancy, and essential variables

For any term R define the Boolean function q_R=1[R^*=1]. If R=x_j, then
q_R(a)=1[a_j=1], whereas the term function itself is the ternary projection
a_j. If R is not a singleton, every output is in {0,1}, so q_R=R^*.
This distinction is maintained throughout the decoding.

Every nonsingleton term has a unique leftmost decomposition as above: follow
left children until reaching x_i, recording the successive right subterms
from bottom to top. Here m>=1, and {i}, supp(R_1),...,supp(R_m) partition I.

For a Boolean function q on coordinates disjoint from i put

    G_i(q)(a) = 1[a_i=2] OR (1[a_i=1] AND (1-q(a))).

The table gives x_i*R_1 = G_i(q_R1). For b in {0,1} and a in A it gives
b*a=b(1-1[a=1]), where juxtaposition is ordinary multiplication of bits.
Therefore

    q_t = G_i(q_R1) product_{j=2}^m (1-q_Rj).                 (1)

All products with no factors equal 1. Formula (1) directly shows that the
function depends only on the displayed decorated tree, inductively on |I|.
Conversely, every decorated tree is realised: recursively realise its child
trees, multiply x_i first by the distinguished child's term, and then by the
remaining child terms in any order. Thus only injectivity remains.

We prove by induction on support size the following properties of q_t:

(a) q_t(0,...,0)=0;
(b) q_t attains both 0 and 1;
(c) every variable of t is essential;
(d) if i is the leftmost label, the slice q_t|_{a_i=0} is identically zero.

For t=x_i these follow from q_t=1[a_i=1]. For a nonsingleton term, (a) and
(d) follow from the root-0 slice of G_i. To obtain output 1, set a_i=2 and
all coordinates of all children to 0, so (1) equals 1; output 0 is given by
the all-zero assignment. To witness essentiality of i, keep all children at
0 and change a_i from 0 to 2. If a variable belongs to R_1, choose two child
assignments witnessing its essentiality in q_R1, put a_i=1, and put every
other child at 0. Equation (1) becomes 1-q_R1. If a variable belongs to R_j
for j>=2, use its essentiality witness in q_Rj, put a_i=2, and every other
child at 0. Equation (1) becomes 1-q_Rj. These assignments alter only the
variable being tested. This proves all four properties for every arity.

## 2. Unique factorization on disjoint coordinate sets

A Boolean function h on A^I is AND-decomposable if I=U disjoint-union V with
U,V nonempty and h(a)=b(a_U)c(a_V) for Boolean b,c. For functions essential
in every coordinate, this entails that b and c are both nonconstant. Call
an essential nonconstant function AND-prime if no such decomposition exists.
Define OR-prime in the same way with OR in place of AND.

For completeness we prove the uniqueness property needed here. For a
nonempty relation S subset of A^I and a partition P of I, call P factorizing
if S is the Cartesian product of its projections pi_B(S), B in P. If P and
Q both factorize S, then for each B in P,

    pi_B(S) = product_{C in Q, B intersect C nonempty} pi_(B intersect C)(S).

Indeed, this is the projection onto B of the Q-product; the disjoint blocks
of Q permit independent choices, and omitted blocks can be filled because
S is nonempty. Substituting into the P-product proves that the common
refinement {B intersect C: B in P, C in Q, B intersect C nonempty} also
factorizes S. There are finitely many coordinate partitions. Their common
refinement is therefore the unique finest factorizing partition P_*.

Its factors are exactly the projections of S. A projection pi_B(S) cannot
factorize over a proper split of B, since that would refine P_*. Conversely,
any partition into prime factors equals P_*: P_* refines it, and a proper
refinement inside one block would contradict that block's primality.

Apply this to S=h^{-1}(1) for a nonzero Boolean h essential in all variables.
A Boolean AND decomposition over disjoint blocks is exactly a Cartesian
factorization of S. Each factor must have a nonempty truth set, and its truth
set equals the corresponding projection of S, since assignments in all
other nonempty factors can be filled. No factor can be constant 1, since
then all variables in its nonempty block would be inessential to h. Thus h
has unique nonconstant disjoint AND-prime factors, with uniquely determined
supports and values, up to ordering. This is an elementary general lemma;
no novelty is claimed for the Cartesian factorization argument.

## 3. The proposed factors are prime and recognizable

**Child-complement factors.** Every q_R is OR-prime. For a singleton there
is no nontrivial coordinate split. Otherwise suppose q_R=b(a_U) OR c(a_V)
for a proper split of its support. Let its leftmost label r belong to U
(interchange U,V if needed). By property (d), putting a_r=0 makes q_R zero
for all other coordinates. Because c has no r coordinate, c must be
identically zero. This would make every variable in V inessential to q_R,
contradicting (c). By the Boolean De Morgan law, 1-q_R is AND-prime, and
it is nonconstant and essential by (b),(c).

**The root factor.** Let J=supp(R_1), H=G_i(q_R1). This is essential on
{i} union J: root values 0 and 2 distinguish i, and the root-1 slice is
1-q_R1, which is essential on J. Suppose H=b(a_U)c(a_V) on a proper split
of {i} union J, and let i belong to U. The root-2 slice of H is identically
1, forcing c identically 1. This makes every variable in V inessential to
H, a contradiction. Thus H is AND-prime and nonconstant.

These factors have disjoint nonempty essential supports covering I, and q_t
is nonzero. By Section 2, the factors displayed in (1) are exactly its
unique disjoint AND-prime factors.

They also identify the root without any structural information from t:
H has an identically zero slice at value 0 in coordinate i. It has no such
slice in a child coordinate j, since a_i=2 makes H=1 even with a_j=0.
Every factor 1-q_Rj has value 1 on its all-zero assignment by property (a),
so it has no identically zero value-0 slice in any coordinate. Therefore
among all prime factors, precisely one factor has such a slice, and that
factor has precisely one coordinate with this property. These uniquely
recover H and i. The criterion uses value 0 specifically: for example
1-q_xj does have an identically zero slice at value 1, which is irrelevant.

## 4. Recursive decoding and the bijection

We establish injectivity for indicators q_t as the slightly stronger
inductive statement, keeping their coordinate support explicit. On a
one-element support {i}, the only term is x_i and the indicator is
1[a_i=1], so it decodes to the unique one-vertex tree.

For |I|>=2, the truth table of q_t determines its unique finest AND
factorization by Section 2. Section 3 determines H and i. The distinguished
child's support is J=supp(H) minus {i}, and its indicator is

    q_R1 = 1 - H|_{a_i=1}.                                  (2)

For each other prime factor h with support K, the corresponding ordinary
child indicator is 1-h on K. Each of J and all such K is nonempty and has
size strictly smaller than |I|. The existence of t and formula (1) guarantee
that all recovered functions are indicators of terms on these supports.
Thus induction uniquely recovers each child tree, with (2) identifying
which one is distinguished. Their unordered collection and the root label
recover the entire decorated tree.

This is a decoder defined from the function and its fixed labelled support;
it does not presume the unknown syntactic term when choosing any factor or
coordinate. Essentiality guarantees the supports do not hide unused labels.
On a singleton recovered support the indicator is decoded as a leaf, never
misidentified with a Boolean-valued nonsingleton term on the same support.

Hence q_s=q_t implies equality of the decorated trees for any terms s,t
on I. For |I|>=2 these indicators are exactly the term functions. For
|I|=1 there is only the projection. Combined with realization and the
function formula in Section 1, this proves the stated bijection for all n.

A concrete representative can be selected recursively by ordering the
ordinary child subtrees by their least vertex label. Their supports are
disjoint and nonempty, so those least labels are distinct. Use the
distinguished child first and the sorted children afterward in the leftmost
product. The resulting full linear terms are exhaustive and have no
duplicate functions.

## 5. Counting without function deduplication

A decorated tree consists of a root and either no children, or one
distinguished decorated child tree together with a set of other decorated
child trees on disjoint labels. The usual labelled product and set counting
give T=x(1+T exp T). More explicitly, define B_r to count sets of decorated
trees whose vertex sets partition a fixed r-element label set, with B_0=1.
The block containing a specified label gives, for r>=1,

    B_r = sum_{j=1}^r binom(r-1,j-1) c_j B_(r-j).             (3)

Choose the root of an n-vertex nonleaf tree, then its k distinguished-child
labels, its distinguished child tree, and the remaining set of child trees:

    c_1 = 1,
    c_n = n sum_{k=1}^{n-1} binom(n-1,k) c_k B_(n-1-k)       (4)

for n>=2. These equations are an effective integer recurrence: after c_1,
compute B_1, then c_2, B_2, then c_3, B_3, and so on. Formula (4) only
uses c_k with k<n and B_r with r<=n-2. Consequently (3),(4) by themselves
meet the original counting requirement.

For the displayed explicit formula, the standard formal Lagrange inversion
identity for T=x phi(T), phi(0)=1, gives
[x^n]T=(1/n)[u^(n-1)]phi(u)^n. Apply this with phi(u)=1+u exp(u).
Expanding (1+u exp(u))^n as sum_{k=0}^n binom(n,k) u^k exp(ku) gives the
stated finite sum. This use of Lagrange inversion is not a new result, and
the independently derived recurrence does not depend on it.

## Dependencies, comparison, and remaining gaps

The argument uses only the given table, finite set partitions, Boolean
complementation, elementary labelled counting, and (for the optional
closed expression) formal Lagrange inversion. It has no asymptotic,
numerical, source-access, or unproved external theorem dependency.

The original primary question is Huang--Lehtonen (2024), Section 7, p.17;
it supplies the table and c_1,...,c_5=1,2,12,108,1340. Its Definition 1.1
matches the present full linear terms. Huang--Lehtonen (2023), Definitions
6.1.2--6.1.3, already give leftmost decomposition and a rooted ordered tree
encoding. Their Proposition 6.1.4 assumes (x*y)*z=(x*z)*y, which is false
here: at (x,y,z)=(2,0,1) the two sides are 0 and 1. The new proposed
contribution is the exact SC229 function classification retaining one
distinguished child, and its resulting all-n count. Neither the existence
of leftmost trees nor Lagrange inversion is claimed as new.

Known mathematical gaps in the submitted proof: none identified by the
proposer. A fresh referee must still check the all-arity factorization and
decoding argument, counting, and full-scope relation to source.md. No fresh
referee was run by this research job. Computational tests are corroboration,
not the proof of the universal quantifier. Current literature comparisons
are bounded and do not certify priority; see the research literature screen.
