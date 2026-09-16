# Mathematical referee report

**Verdict: accept the exact frozen result-note scope.**

Job: `primary-20260913-level-rook-fibres-referee-06fcc6488318`.
Snapshot digest: `9b53236858fe2abcb9e9dcfaed76cefcc619775820800eea780ad9ed287b6bd7`.
Review date: 2026-09-13, Asia/Shanghai.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

The accepted claim is the explicit fibre bijection for every 2-singleton
target and the exact algorithm for **every** nonnegative capacity vector
of variable length. Acceptance includes the stated O(t^4) integer-operation
bound, O(t log(A+t+2)) operand-bit bound, O(t^2) stored integers, and
O(t^6 log^2(A+t+2)) conservative bit bound. It does not settle the original
arbitrary-m question or full rook-equivalence-class enumeration.

This was a fresh model review of the frozen inputs, not external peer
review or a formal proof-assistant certification. No agents or other model
processes were used. I read source.md, problem.md, claim.json,
audit/snapshot.json, its listed evidence, and actual primary-source
passages. I did not consult checkpoint.md, state.json, earlier transcripts
or earlier review verdicts. Proposer assessments appearing within the
listed evidence were not treated as evidence. No frozen input was edited.

## Integrity and exact problem

All 14 file hashes in the snapshot match. Independently hashing its
sorted-key compact JSON file mapping reproduces the snapshot digest.
The source.md SHA256 remains
`0d9344b0f088a0d374302c97799c3d24e842950554cba9a17bc1af1702f2c20f`.

The source's subquestion is genuine: BLRS, Section 6.2, printed p.21,
asks for the number of arbitrary Ferrers boards mapping to a singleton
under the level transpose. Definition 4 and the subsequent paragraph give
the transpose by reversed level totals and its singleton image. I checked
these in the snapshot-listed PDF and the
[primary text](https://arxiv.org/html/1508.05944v1).
The positive-column normalization is supported by the paragraph introducing
Ferrers boards in Section 3 of
[Barrese's paper](https://arxiv.org/html/1812.00533v2), checked in the
snapshot-listed HTML: adding zero-height columns leaves the shape unchanged.
Thus there is no uncounted infinite family of padded representations.

For m=2 the singleton condition is exactly that odd column heights cannot
repeat. The empty target is handled separately and has one preimage.
For a nonempty target, reversing its columns gives positive level totals
s_1,...,s_t and s_(t+1)=0. Since consecutive target heights u<=v satisfy
ceil(u/2)<=floor(v/2) unless u=v is odd, every stated capacity is nonnegative.

## Reconstruction of the proof

**Bijection.** Let r_j count columns of the preimage of height at least j,
padding rows to length 2t. They are nonnegative and weakly decreasing.
The fixed level totals give r_(2i-1)+r_(2i)=s_i. The integral parameter
d_i=floor(s_i/2)-r_(2i) is nonnegative precisely when the two rows have
the required order. Solving for the rows yields

    r_(2i-1)=ceil(s_i/2)+d_i,
    r_(2i)=floor(s_i/2)-d_i.

The intervening order r_(2i)>=r_(2i+1) is precisely
d_i+d_(i+1)<=a_i. Nonnegativity of the last row is d_t<=a_t.
Conversely, these inequalities imply all the reconstructed rows are
ordered and nonnegative. Since s_t>0, exactly t levels are nonempty.
Row conjugation gives one positive-column shape and is inverse to the
forward construction. Preimage width varies freely through r_1.

Every nonnegative capacity vector really occurs: set s_t=2a_t+1 and
s_i=2(a_i+ceil(s_(i+1)/2)) recursively. The reversed sequence is positive
and increasing, its only odd entry occurs once, and its computed capacities
are exactly a. This is not an extra restriction on the general algorithm.

**Recurrence.** For t>=1 define U_1=a_1 and
U_i=min(a_(i-1),a_i) for i>=2. These individual upper bounds follow from
the original edges and terminal bound. At prefix length i let f_i(x)
count prefixes with last coordinate x and all these individual bounds.
Fixing the next coordinate gives

    f_1(x)=1,                         0<=x<=U_1,
    H_i(z)=sum_(x=0)^z f_i(x),        0<=z<=U_i,
    f_(i+1)(y)=H_i(min(U_i,a_i-y)),   0<=y<=U_(i+1).

The final answer is H_t(U_t). The argument of H_i is never negative:
U_(i+1)<=a_i. Anticipating the next edge with a redundant individual
bound does not discard any full solution. The formula also covers t=1,
when the answer is a_1+1.

**Interval and degree induction.** Suppose a layer-i piece on [l,r]
is sum_k c_k binom(x-l,k), with degree d<=min(i-1,r-l).
Summing binomial coefficients gives the submitted inclusive-prefix
coefficients h_0=T+c_0, h_k=c_(k-1)+c_k, and h_(d+1)=c_d.
Here T is exactly the total over preceding intervals; the last term and
inclusive endpoint are necessary and both are implemented correctly.

Reflection maps each old prefix interval to [a_i-r,a_i-l], intersected
with the new domain. Each old interval supplies at most one interval.
The only additional interval is the constant saturated part ending at
min(U_(i+1),a_i-U_i-1). Its strict endpoint excludes a_i-y=U_i,
which belongs to the reflected polynomial piece. These pieces cover the
new integer domain without overlap or gaps.

On a short surviving interval the algorithm samples every point and uses
the lower-degree interpolant. On a longer interval it takes enough samples
for the actual polynomial degree, so Newton interpolation is an identity.
No extrapolation outside an old interval occurs in evaluation. Induction
therefore gives at most i pieces of degree at most i-1 at layer i,
including one-point intervals, zero capacities and coincident breakpoints.

**Bit and operation bounds.** Each stored coefficient is a forward
difference using only actual values in its interval. Fixing the last
coordinate leaves at most (A+1)^(i-1) prefixes. Thus

    |c_k| <= 2^k (A+1)^(i-1),
    0<=T<=(A+1)^i.

These estimates control both stored count coefficients and the prefix
coefficients. For an evaluation offset n between 0 and A, each nonzero
binom(n,k) is at most (A+t+2)^t. Consequently its products with the
coefficients, signed partial sums (including cancellation), and temporary
products before exact division all have O(t log(A+t+2)) bits. The binomial
recurrence remains exact when k exceeds n: the binomial factor has become
zero. Intermediate difference-table rows satisfy the same type of bound.
Endpoint arithmetic and degree counters fit within this operand bound.

At transition i there are O(i) pieces. Each needs O(i) evaluations of
cost O(i), plus an O(i^2) difference table; thus O(i^3) integer operations
suffice. Summing gives O(t^4). Old, prefix and new layers and one temporary
table together occupy O(t^2) integers. Standard quadratic multiplication
and division yield the stated conservative bit complexity. The count has
at most O(t log(A+2)) bits. Since t=O(L) and A<=c_t/2 for the binary
target input, this proves the claimed polynomial dependence on L.

I found no gap in these steps and no extra hypothesis is needed. The code
implements them faithfully. The unused generalized-binomial helper is not
needed for the proof. Optional trace collection does not change the claimed
asymptotic bounds.

## Independent computational checks actually performed

The new verifier is `audit/referee-independent.py`; its exact results are
in `audit/referee-independent.json`. It imports only the frozen counter,
not the proposer’s checker or numeric baseline. Run from the project root:

    python3 -B audit/referee-independent.py > audit/referee-independent.json

All checks passed:

- Direct recursive enumeration from the original inequalities and a reverse
  suffix DP agree with the counter on all 5,461 vectors in {0,1,2,3}^t,
  0<=t<=6.
- A multiplicity-based partition generator independently enumerates all
  7,338 Ferrers shapes of area 0..24, in 1,866 fibres. Counts and complete
  inverse sets agree. The held-out area range 21..24 contributes 4,624
  shapes and 1,069 fibres beyond the submitted census.
- On 400 deterministic heterogeneous vectors, with seed 61408327,
  lengths 1..25 and capacities 0..40, every integer value of every count
  interval agrees with a raw prefix DP: 74,587 values. Inclusive-prefix
  values, interval coverage, degree and coefficient bounds also pass.
- Sixteen heterogeneous vectors of lengths 2..18, scaled by integers
  near 10^75, agree with an independent rational Lagrange oracle. Exact
  input bases, scales and answer digests are serialized in the JSON.
  The largest checked answer has 4,504 bits.

The last oracle has a mathematical justification separate from the
compression algorithm. Signing alternate columns of the edge matrix
turns it into the transpose of a directed incidence matrix; the terminal
and nonnegativity rows are unit rows. The matrix is totally unimodular,
so the bounded polytope P(b) is integral for every integral b>=0.
P(kb)=kP(b), hence its lattice count is an Ehrhart polynomial of degree
at most len(b), also when zero capacities lower the dimension. Counts at
0,...,len(b), obtained by reverse DP, determine it. One additional small
scale checks each interpolant before evaluation at the large scale.

I also inspected the submitted checker and its recorded ranges. I did
not rerun its whole suite or treat its success flag as a proof. In
particular its four 80-coordinate stress cases remain stress tests in
that dossier; my heterogeneous large tests are different inputs with
their own oracles. All finite checks here support implementation reliability;
the unlimited theorem is established by the argument above.

## Primary-source comparison and contribution

The nearest theorem within rook theory is BLRS, *m-Level rook placements*,
Theorem 5.2, printed p.15, checked in the snapshot-listed PDF and identified
by its [primary record](https://arxiv.org/abs/1308.4081). It enumerates
singleton boards in an equivalence class. Our fibre contains arbitrary
boards with one fixed transpose. That theorem does not supply this count.

The following adjacent statements were independently inspected online:

- [Bona, Ju and Yoshida, *On the Enumeration of Certain Weighted Graphs*](https://arxiv.org/html/math/0606163),
  equation (1), Section 2.1 and Theorems 2.1–2.2, use a common capacity
  and a matrix of order n+1. This covers uniform-capacity path enumeration.
- [Jiang, Wen and Zhong, *Alternating adjacent-sum polytopes*](https://arxiv.org/html/2607.14887v1),
  Section 2.1 and Proposition 2.1, use alternating capacities s,s+1
  and matrices of order s+2. They give useful special-pattern formulas.
- [Cigler and Krattenthaler, *Bounded Dyck paths, bounded alternating sequences, orthogonal polynomials, and reciprocity*](https://arxiv.org/pdf/2012.03878),
  Section 3 and Theorem 4, count alternating sequences in a common
  interval with specified first and last entries. The introduction also
  describes weighted and tableau extensions. This does not state a
  binary-input bound for arbitrary individual markings.
- [Jochemko and Sanyal, *Arithmetic of marked order polytopes*](https://arxiv.org/pdf/1206.4066),
  Theorem 2.6 and its proof, establish piecewise polynomiality by products
  of simplices indexed by chains of ideals and inversion. The submitted
  alternating-affine coordinate change to a marked fence is correct.
  The theorem does not bound computation polynomially in the variable
  poset size. The present result's linear univariate piece count is an
  additional quantitative assertion.
- [Assaf and Bergeron, *Flagged (P,rho)-partitions*](https://arxiv.org/pdf/1904.06630),
  Corollary 3.15 and Remark 3.16, give a linear-extension expansion.
  This is not itself a polynomial-size enumeration of extensions.
- [Zeng and Van den Broeck, *Efficient Search-Based Weighted Model Integration*](https://proceedings.mlr.press/v115/zeng20a/zeng20a.pdf),
  Theorem 4.4 and Corollary 4.5, and the related
  [*Hybrid Probabilistic Inference with Logical Constraints*](https://starai.cs.ucla.edu/papers/ZengKR2ML19.pdf),
  Sections 3–4 and the message-size discussion, establish continuous
  piecewise-polynomial inference methods. Their general tree/path bounds
  allow growth in the number of pieces. They are clear methodological
  predecessors; neither inspected statement gives this discrete
  arbitrary-capacity bound.

Additional referee searches considered binary-input path counting,
bounded order maps, flagged ribbons, weighted paths and level-transpose
preimages. I followed three further primary leads:
[Ekhad and Zeilberger's umbral P-partition paper](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/rotastanley.pdf),
its grafting construction and common-bound paragraph;
[Fischer's directed-graph-polytope paper](https://www.mat.univie.ac.at/~ifischer/papers/directedgraphpolytope_revision.pdf),
Theorem 1 and Corollary 2 on chamber polynomiality; and
[*Skew shapes, Ehrhart positivity and beyond*](https://arxiv.org/html/2503.16403),
Section 1.3's Kreweras determinant and Section 1.4 on fences.
The inspected statements supply general symbolic tools or common-bound
enumerations, not an equivalent arbitrary-capacity binary-input theorem.
This comparison does not rule out every consequence of these methods.

The credible use is exact evaluation of the entire m=2 slice of an
explicitly posed fibre-counting question when heights are binary encoded
and a capacity-sized table is impractical. The combined reduction and
bounded interval computation give a concrete improvement over enumerating
partitions or tabulating every coordinate value. This qualifies as a
nontrivial, coherent result-note under the stated contribution threshold.
It is not being accepted as an invention of transfer matrices, finite
differences, interpolation or symbolic message passing, nor as a new
general polynomiality theorem for marked polytopes. No equivalent was
identified in the primary statements inspected on this review date;
worldwide priority and journal acceptance are not certified.

## Gaps, limitations and disposition

No unresolved mathematical or contribution gap requiring a change to the
frozen candidate was found. No claim revision or silent downgrade has
been used to reach this decision. The source's m>=3 question remains
unresolved here. Literature coverage is bounded, especially for all
possible specializations of the long tableau and symbolic-enumeration
papers; the manuscript must retain the present qualified novelty language.

The next authorized workflow step is the runner's integrity/provenance
gate, followed by writing this exact accepted scope and fresh citation,
build and visual checks. This review creates no manuscript or release.
