# Exact counting of two-level transpose fibres with binary heights

Research job: primary-20260913-level-rook-fibres-research-4655afa47dc0.
Status: proposed theorem and complete argument, not independently refereed.
This is a result for m=2; the original arbitrary-m problem is unresolved.

## Statement

For every t>=1 and a=(a_1,...,a_t) in Z_{≥0}^t, define

    P(a) = {d in Z_{≥0}^t : d_i+d_(i+1)<=a_i (i<t), d_t<=a_t}.

Let A=max_i a_i. The algorithm in m2-compressed.py computes #P(a) using
O(t^4) integer arithmetic operations, each on integers of
O(t log(A+t+2)) bits, and O(t^2) stored integers of that size.
In particular its bit cost is O(t^6 log^2(A+t+2)) with elementary integer
arithmetic. The empty vector has count 1 and constant cost.

Consequently F_2(C), for every positive weakly increasing 2-singleton
shape C=(c_1,...,c_t), can be evaluated in time polynomial in
L=log(t+1)+sum_i log(c_i+1), with leading zero columns identified as in
problem.md. No statement here evaluates F_m for arbitrary m>=3.

The quantitative purpose is to replace a capacity-sized transfer table by
at most i polynomial intervals at layer i. It is not an assertion that
polynomial interpolation, prefix sums, or path transfer matrices are new.

## Row-pair bijection (full argument)

Put s_i=c_(t+1-i), s_(t+1)=0, and

    a_i=floor(s_i/2)-ceil(s_(i+1)/2).

For consecutive singleton columns u<=v, ceil(u/2)<=floor(v/2): failure
would require u=v odd, forbidden by the singleton condition. Thus a>=0.

For a preimage B, let r_j be the number of columns of height at least j,
including zero rows up to j=2t. The r_j decrease weakly, are nonnegative,
and obey r_(2i-1)+r_(2i)=s_i. Define
d_i=floor(s_i/2)-r_(2i). Within-pair order is precisely d_i>=0, and
between-pair order is precisely d_i+d_(i+1)<=a_i. The last row is
nonnegative precisely when d_t<=a_t.

Conversely, given d in P(a), set

    r_(2i-1)=ceil(s_i/2)+d_i,
    r_(2i)=floor(s_i/2)-d_i.

These rows decrease within each pair by d_i>=0 and between pairs by the
adjacent-sum inequalities. The last row is nonnegative; alternatively
d_i<=a_i<=floor(s_i/2) for i<t. Thus all rows are nonnegative. Since
s_t>0, the reconstructed shape has exactly t nonempty levels. Conjugation
of the row lengths gives a unique finite sequence of positive column
heights; leading zero columns are never introduced as distinct objects.
The two maps are inverse, and the level totals are s_i. Hence F_2(C)=#P(a).
The empty shape separately has one preimage.

The capacity generality is real: every nonnegative vector a of positive
length is obtained from a singleton C. Set s_t=2a_t+1 and recursively
s_i=2(a_i+ceil(s_(i+1)/2)) for i<t, then reverse s to form C. All entries
are positive; entries other than s_t are even and decrease weakly in s.
The odd entry s_t occurs only once, so C is singleton, and its capacities
are exactly a. The verifier also checks this construction throughout its
exhaustive capacity range.

## The numerical recurrence and its compressed representation

Set U_1=a_1 and U_i=min(a_(i-1),a_i) for 2<=i<=t. These upper bounds are
redundant consequences of P(a), including its terminal condition. Define
f_i(x) as the number of prefixes (d_1,...,d_i) with d_i=x, satisfying all
edges within the prefix and all the individual bounds 0<=d_j<=U_j.
The prefix bound for d_i also anticipates its edge to the next vertex.
Since all such bounds are redundant in the full system, imposing them
does not change the desired final count. Explicitly,

    f_1(x)=1 (0<=x<=U_1),
    H_i(z)=sum_(x=0)^z f_i(x) (0<=z<=U_i),
    f_(i+1)(y)=H_i(min(U_i,a_i-y)) (0<=y<=U_(i+1)),
    #P(a)=H_t(U_t).

Here U_(i+1)<=a_i ensures a_i-y>=0, so no negative-prefix convention is
needed by this implementation. These formulas follow by fixing the final
coordinate and enumerating the preceding coordinate.

Partition [0,U_i] into disjoint consecutive nonempty integer intervals.
On each [l,r], store an integer coefficient vector c=(c_0,...,c_d) with

    f_i(x)=sum_(k=0)^d c_k binom(x-l,k),  l<=x<=r.

We maintain both d<=i-1 and d<=r-l. Values only on the integer interval
matter; a short interval may be represented by its lower-degree interpolant.
The initial layer has the single interval [0,U_1], c=(1).

For a piece with prefix total T from all preceding pieces, the identity

    sum_(q=0)^n binom(q,k)=binom(n+1,k+1)

and Pascal's identity give the inclusive-prefix polynomial on that piece.
Its binomial coefficients relative to l are

    h_0=T+c_0,
    h_k=c_(k-1)+c_k (1<=k<=d),
    h_(d+1)=c_d.

Evaluation at r updates T. Thus prefix summation keeps the same intervals
and raises the degree by at most one.

To form the next layer, reflect each prefix interval [l,r] to
[a_i-r,a_i-l] and intersect with [0,U_(i+1)]. These intersections are
disjoint. On them the reflected polynomial has degree at most i.
There can additionally be one saturated constant interval

    [0,min(U_(i+1),a_i-U_i-1)],

when its right endpoint is nonnegative; it corresponds to a_i-y>U_i.
The point a_i-y=U_i stays in the polynomial interval, so no boundary is
double counted. Reversing the original interval order gives all reflected
pieces in increasing order, with no sorting needed.

For each surviving interval [b,e], set D=min(i,degree of its reflected
prefix polynomial,e-b). Compute the D+1 actual values at b,...,b+D, and
store their successive forward differences. If the interval contains more
than D+1 points, the reflected polynomial has degree <=D and Newton
interpolation is an identity. Otherwise every point of the interval has
been sampled. In both cases the representation is exact and its degree
does not exceed i or e-b.

Each old piece contributes at most one new piece; saturation contributes
at most one. Induction therefore gives at most i pieces at layer i and
degree at most i-1. This proves correctness and the linear piece bound
for all nonnegative capacities, including zero and repeated capacities.

## Integer and bit-size control

All stored coefficients are integers: the prefix transformation is integral
and each interpolation coefficient is an integer forward difference.
More strongly, if a layer-i piece has degree d, its coefficient is

    c_k=Delta^k f_i(l)=sum_(j=0)^k (-1)^(k-j) binom(k,j) f_i(l+j).

All sampled points lie in the actual interval because d<=r-l. Fixing
d_i leaves at most (A+1)^(i-1) prefixes. Hence

    |c_k| <= 2^k (A+1)^(i-1) <= 2^(i-1)(A+1)^(i-1).

This is why normalizing on short intervals is useful: no extrapolation
bound for an artificial polynomial is required. In addition,
0<=T<=#prefixes<=(A+1)^i. The h-coefficients above obey the same
O(i log(A+2)) bit bound up to an absolute constant.

Every evaluation is at a nonnegative integer offset <=A. It uses the
recurrence binom(n,k+1)=binom(n,k)*(n-k)/(k+1); the division is exact.
The binomial factors have at most O(t log(A+t+2)) bits, as do products,
partial sums, and the temporary integers preceding exact division.
The subtraction table forming forward differences obeys the bound just
proved, with the same bound also valid at its intermediate rows.
Endpoints and clipping operations use O(log(A+2)) bits.

At transition i there are O(i) pieces, each with O(i) coefficients.
An evaluation costs O(i) integer operations. At most i+1 evaluations and
O(i^2) finite-difference operations per reflected piece suffice. Thus a
transition costs O(i^3), and summing over i costs O(t^4). Prefix summation
and the last total cost less. Two adjacent layers occupy O(t^2) integers.
Using quadratic-time multiplication/division on b-bit integers gives the
stated conservative O(t^4 b^2)=O(t^6 log^2(A+t+2)) bit bound.

The count itself is <=(A+1)^t, so the binary output length is polynomial
as well. Since A<=c_t/2, t<=O(L), and log(A+2)<=O(L), the fibre algorithm
is polynomial in the binary column input size. The displayed exponent
is an upper bound, not an optimality claim.

## Verification design and limitations

m2-compressed-check.py compares with the earlier numeric path counter on
every a in {0,...,4}^t for 0<=t<=6 and {0,...,3}^7; lengths 0 through 5
also use direct Cartesian-product enumeration. It separately groups every
Ferrers shape of area 0..20 by actual level totals and compares all fibres.
Large t=2 cases use the exact formula

    #P(a,b)=(q+1)(a+1)-q(q+1)/2, q=min(a,b).

Uniform capacities have an independent large-value check by rational
Lagrange interpolation, using no binomial-evaluation or finite-difference
code from the compressed implementation. Justification: the incidence
matrix of a bipartite graph
is totally unimodular after signing one bipartition (it becomes the
transpose of a directed incidence matrix); adjoining unit rows preserves
total unimodularity. Thus P(1,...,1) is an integral bounded polytope of
dimension t, and its dilation count is a polynomial in the common capacity
of degree t. Values at 0,...,t determine it. This established Ehrhart fact
is used only as a test oracle, not in the counting theorem's proof.

Long heterogeneous inputs with moderate capacities use the independent
numeric DP; 80-coordinate, 100-digit inputs exercise storage and integer
growth, but are explicitly marked as stress runs without a separate oracle.
The JSON records actual results and exact ranges. No prefix of tests is
asserted to prove the unlimited theorem or to establish novelty.

An initial test run reached the large-answer serialization stage and hit
Python's decimal-string length limit. The output digest was changed to a
digest of unsigned big-endian answer bytes. This was a serialization
failure, with no mathematical consequence.

Reproduction from the project root:

    python3 evidence/m2-compressed-check.py > evidence/m2-compressed-check.json
    python3 evidence/m2-compressed.py '[1,1]'

The second command reports count_binary="0b11", that is, three. The
library entry point fibre_count(C) accepts the target column sequence;
compressed_count(a) accepts capacities. Both return exact Python integers.
The CLI uses binary output to avoid decimal-string conversion limits.

## Gap and scope list

No mathematical gap is currently identified in the argument above.
This declaration is the proposer's assessment; fresh mathematical review
is still required. The original m>=3 fibre question is outside the theorem.
The current primary-literature comparison and its limits belong in
literature/research-comparison.md; absence of an equivalent there is not
proof of worldwide priority.
