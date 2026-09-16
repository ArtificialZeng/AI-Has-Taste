# Two-level fibre reduction and a discriminating algorithmic lead

Job: primary-20260913-level-rook-fibres-triage-4e5c62cdde68.
These are triage derivations and finite tests, not an accepted contribution.
The original target still quantifies over every m>=1.

## Exact reduction derived in this pass

Fix m=2 and a nonempty singleton C=(c_1,...,c_t). Put
s_i=c_(t+1-i), s_(t+1)=0, and

    a_i = floor(s_i/2) - ceil(s_(i+1)/2),  1<=i<=t.

All a_i are nonnegative: for consecutive singleton columns u<=v,
ceil(u/2)<=floor(v/2); the only possible failure is repeated odd heights,
which violate the singleton condition.

Let r_j be the number of columns of B of height at least j, padding with
zero rows through row 2t. Then B belongs to the fibre if and only if
r_1>=...>=r_(2t)>=0 and r_(2i-1)+r_(2i)=s_i for all i. Set

    d_i = floor(s_i/2) - r_(2i).

The within-pair order says d_i>=0. The order between pairs becomes
d_i+d_(i+1)<=a_i. Nonnegativity of the last row says d_t<=a_t.
Conversely, these inequalities give the ordered nonnegative row sequence

    r_(2i-1)=ceil(s_i/2)+d_i,
    r_(2i)=floor(s_i/2)-d_i.

For i<t, d_i<=a_i<=floor(s_i/2), and the terminal bound deals with i=t.
Thus all reconstructed rows are nonnegative. Positive s_t guarantees
exactly t nonempty levels. Conjugating the rows reconstructs a unique
positive column-height sequence. This gives the claimed bijection to

    d_i>=0; d_i+d_(i+1)<=a_i (i<t); d_t<=a_t,

over integer d. The empty case has one preimage and is separate.

## Baseline computation and benefit that still needs strengthening

Define U_1=a_1 and U_i=min(a_(i-1),a_i) for 2<=i<=t. Let f_i(x)
count admissible prefixes d_1,...,d_i with d_i=x. Then

    f_1(x)=1                     (0<=x<=U_1),
    f_(i+1)(y)=sum f_i(x)        (0<=x<=min(U_i,a_i-y)),
    F_2(C)=sum_(x=0)^U_t f_t(x).

An empty sum is zero. Prefix sums implement each transition in
O(U_i+U_(i+1)+1) integer additions. Since

    sum_i a_i = floor(s_1/2) - sum_(i=2)^t (s_i mod 2),

the full cost is O(t+c_t) arithmetic operations, with two layers in memory.
This is pseudopolynomial for binary heights, not a polynomial bit-complexity
result. Generic path transfer is known prior technology; the recurrence
alone is not being promoted as a paper.

The promising stronger test is compression: f_i is piecewise polynomial on
integer intervals. Discrete prefix summation raises degree by at most one;
reflection z=a_i-y and clipping to [0,U_(i+1)] should add only constantly
many interval boundaries. Starting from one constant interval suggests
O(i) pieces of degree at most i-1. A binomial-coefficient basis may make
summation exact without iterating through U_i. Endpoint conventions,
coefficient bit growth, and an actual polynomial bit bound remain to be
checked. This is the proposed all-m=2 contribution, not a proved algorithm.

For context, the same inequalities imply a simple stabilization: if t>=2,
adding 2K to every c_i leaves a_1,...,a_(t-1) unchanged and replaces a_t
by a_t+K. Once a_t+K>=a_(t-1), the terminal inequality is redundant.
Hence the fibre counts are then constant as K increases. This observation
does not by itself meet the contribution gate.

## Exact finite verification

Run `python3 evidence/m2-path-check.py > evidence/m2-path-check.json`.
It independently enumerates positive column partitions, computes actual
level totals, and compares the path recurrence and inverse reconstruction.
Every one of 2,714 boards, grouped into 797 fibres over area 0..20, passes.
There is no randomness or floating point. This includes all odd/even and
zero-capacity cases occurring in that range, not all possible inputs.
For C=(2,4), a=(1,1) gives three points and exactly the boards
(1,1,4), (2,4), (3,3); the independent-level product would give six.
Uniform capacity one gives Fibonacci counts for lengths 1..12, which is a
known path phenomenon and a calibration, not a novelty claim.

## Prior-work obstacle and next test

Jiang–Wen–Zhong, arXiv:2607.14887v1, studies uniform/period-two adjacent-sum
models and uses transfer matrices whose size grows with the capacity.
Its Section 1, equation (1), and Section 2.1 were inspected; the paper's
HTML contains no occurrence of `rook`. This does not rule out a prior
equivalent algorithm in the wider polytope literature. See the literature
record for earlier weighted-graph leads.

Next test: implement and prove the compressed recurrence for arbitrary
binary-encoded 2-singleton C, checking linear growth in interval pieces and
polynomial coefficient bit size against the saved exact census and large
capacities; compare that specific claim with the weighted-path literature.
If only the pseudopolynomial transfer survives or the stronger algorithm is
already standard without a substantive new benefit, park this target.
