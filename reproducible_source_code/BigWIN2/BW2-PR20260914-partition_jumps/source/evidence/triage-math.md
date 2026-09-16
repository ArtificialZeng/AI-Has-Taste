# Mathematical evidence and proposed research target

Status: triage deductions and proof leads, not an independently audited
resolution or a manuscript. Use the notation of problem.md.

## Exact finite observation

`python3 evidence/triage_check.py` enumerates all partitions and all legal
row moves for every n from 2 through 20. It deduplicates outputs, checks
that adjacency is symmetric and stays in P(n), counts degrees directly,
and searches all cliques in each induced neighborhood by exact recursion.
The recursion only prunes when the number of remaining candidates cannot
beat the largest clique already found. Integer/set operations are used.

Coverage: 2,712 vertices and 12,929 undirected edges across these graphs.
Both cited formulas agree everywhere in this finite range. The output
contains maxima and witness edges for each n. Reproducibility artifact:
`evidence/triage_check.json`. This is finite evidence, not a proof for all n.

Observed D_delta(n): zero at n=2,3; one at n=4,...,10 and n=12,13;
two at n=11 and n=14,...,20. D_d(10), D_d(15), D_d(20) are 8,12,13.

## Immediate consequences of existing formulas

The local formula gives r-1 <= delta <= r+1. Combining it with support
change at most two gives D_delta(n) <= 4. Thus coarse boundedness already
follows from the cited results and should not be advertised as a substantial
new theorem by itself.

Let s=floor((sqrt(8n+1)-1)/2), the greatest possible support size. A transfer
changes multiplicities at at most four positive sizes. Consequently
|Delta B| <= 4. Inserting or deleting one support size changes A by at
most one: one gap is split or two are merged, with the top endpoint handled
separately. Since at most four support memberships change, |Delta A| <= 4.
The cited degree formula therefore gives

    |Delta d - Delta(r(r-1))| <= 8.

For n >= 10 (s >= 4), write n=T_s+q, 0<=q<=s. The adjacent pair

    mu = (s+q,s-1,s-2,...,3,2,1),
    lambda = (s+q,s-1,s-2,...,4,3,3)

is obtained by moving the unit row to the row of size 2. The range ending
at 4 in lambda is empty when s=4. Their supports are s and s-2; their
degrees differ by 4s-8 according to the degree formula. Together the
preceding arguments suggest the explicit bounds

    4s-8 <= D_d(n) <= 4s+2  (n >= 10),

and hence D_d(n)=4sqrt(2n)+O(1). These short deductions need a research
proof check, including the support-gap insertion/deletion endpoints.
They are not statements located in a prior paper by this screen.

## Sharp dimension target

The dimension formula simplifies to three cases:

* delta=r-1 for the staircase partition (r,r-1,...,1);
* delta=r+1 if some repeated size s_i has s_i-s_{i+1}>1;
* delta=r in all other cases.

Proposed sharp statement, unaccepted: D_delta(n) <= 2 for every n>=2,
with equality exactly at n=11 and n>=14. The exceptional values in
2<=n<=13 are covered by the exact computation.

Potential all-n witnesses are obtained by sorting the two multisets

    (k,4,4,3) and (k,4,4,2,1),  k=n-11 >= 4.

The transfer splits the 3 into 2 and 1. For k=4 the formula predicts
dimensions 2 and 4; for k>=5 it predicts 3 and 5. At n=14 the pair
(5,5,4) and (5,5,3,1) has predicted dimensions 2 and 4. At n=11 use
(4,4,3) and (4,4,2,1), predicted dimensions 2 and 4.

Critical next step: orient an arbitrary edge so support does not decrease
and analyze support differences 0,1,2 using the three dimension cases.
In particular, check whether support increase two forces a repeated donor
size with a missing predecessor, and handle equal donor/recipient sizes,
q=0, vanishing rows, and coincidences among affected sizes. This can prove
or refute the universal bound independently of enlarging the finite table.

## Admission rationale

Nearest prior X: exact vertex formulas and the support-jump bound.
Proposed delta Y: explicit leading coefficient for D_d and exact D_delta,
in one coherent result, beyond merely showing O(sqrt(n)) and O(1).
Verifier Z: a short local case analysis plus direct graph certificates for
the finite exceptions and symbolic checks of witnesses for every large n.
The qualitative localization question and a full exact formula for D_d
remain outside this proposed first contribution. No manuscript is authorized
by this triage decision.
