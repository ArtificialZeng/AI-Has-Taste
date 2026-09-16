# Mathematical referee report

**Verdict: accept the exact frozen result-note scope.**

Referee job: newwin-00001-p10-referee-4a51a5b060c8.
Snapshot digest: e01d88ae352c8527e95f46dea33aabb64ff973109a9e88f15f45b6adef55cccc.
Candidate kind: result-note. Original status: unresolved.

Theorems A--C in `evidence/research-moment-proof.md` are correct as stated.
The contribution passes as a modest reconstruction application with an
explicit infinite family of lengths. This accepts neither an all-length
solution nor a new general moment or Chern-shadow formalism.

## Scope and integrity

The original question requires positive integer partitions of the same
integer N, with at least two parts, and equality of every numerical output
multiplicity. I retained these hypotheses. The accepted positive-real
theorem has the stronger domain stated in the candidate, but requires
nonzero coefficients through order n. Its explicit sufficient length
classes exclude residues 14, 26, 34 and 46 modulo 60, with fixed-sum
arguments separately supplying lengths 2 and 4.

All ten files in the snapshot, including claim.json, source.md and
problem.md, matched their hashes. I independently recomputed the snapshot
digest from the sorted compact JSON mapping. The unchanged source hash is
08e71a9e52f039251c1c05f8a22310eb23c909494da046a0a0ca716d20f1de10.
Only the frozen project inputs and newly created referee artifacts were
used locally. No checkpoint.md, state.json, earlier review, job transcript
or owner progress summary was read. Proposer assertions of completeness
were not evidence for the decision. No frozen input was edited.

## Reconstruction of the decisive argument

For a two-by-two tableau the two columns are strictly increasing and the
two rows are weakly increasing in the variable indices. The content types
are (2,2), (2,1,1), and (1,1,1,1), with coefficients 1, 1, and 2. They
give

    s22 = m22 + m211 + 2 m1111,
    D(n) = C(n,2) + 3 C(n,3) + 2 C(n,4) = n^2(n^2-1)/12.

The first summand is strictly increasing for integer n>=2 and the others
are nondecreasing. Thus output cardinality determines n. Index labels
remain distinct when their assigned positive values coincide; numerical
collisions add multiplicities. The argument consequently covers repeated
parts and does not accidentally replace a multiset by its support.

Writing u_r=sum_i x_i^r, direct monomial expansion gives

    s22(x) = (u_1^4 + 3 u_2^2 - 4 u_1 u_3)/12.

In particular the coefficients of m4 and m31 cancel, and those of m22,
m211 and m1111 become 1, 1 and 2. This supplies the needed identity
without a representation-theoretic hypothesis.

For positive a_i, put y_i=log(a_i), p_0=n, p_j=sum_i y_i^j and
P(t)=sum_i exp(t y_i). If Q_j denotes the jth logarithmic power sum of
the output, then the finite exponential identity is

    sum_(v in S22(a)) exp(t log(v))
      = [P(t)^4 + 3 P(2t)^2 - 4 P(t)P(3t)]/12.

Taking the jth derivative at zero, the coefficient of p_j is

    [4 n^3 + 6 n 2^j - 4 n(1+3^j)]/12
      = n(n^2-1+3*2^(j-1)-3^j)/3 = c_j(n).

Every remaining term is a polynomial in p_1,...,p_(j-1): a factor of
degree j leaves only degree-zero factors elsewhere. There is no hidden
p_j product at that total degree. Thus

    Q_j = c_j(n) p_j + R_(j,n)(p_1,...,p_(j-1)).

The first n nonzero coefficients give successive recovery of p_1,...,p_n.
Newton identities then determine the monic degree-n polynomial with
root multiset {y_i}; equality of this polynomial determines its roots
with multiplicities. Exponentiation is injective on real numbers. This
proves Theorem A, including the assertion that only the output cardinality
and first n logarithmic moments suffice. Existence is automatic because
the data are assumed to arise from an input. There is no claim about
arbitrary inconsistent moment data or numerical stability.

The redundant distinct-index derivation is also consistent: partition
lattice inclusion-exclusion has block factor (-1)^(|B|-1)(|B|-1)!, and
the three ordered-content sums require divisors 2, 2 and 12. These match
the tableau multiplicities. The main proof does not depend on this
redundant derivation.

The zero-coefficient equation is

    n^2 = A_j = 1 + 3^j - 3*2^(j-1).

The first three orders give n=1,2,4. For even j>=4, A_j is 2 modulo 8,
so cannot be a square. For odd j>=5, A_j is 4 modulo 8 and 1 modulo
both 3 and 5. Therefore a positive n solving the equation must satisfy
n=2 modulo 4, n not divisible by 3, and n=1 or -1 modulo 5. Checking
these simultaneous congruences yields exactly 14,26,34,46 modulo 60.
These are necessary conditions for a zero, not sufficient conditions.
This proves Theorem B for all orders, stronger than the orders needed
by A. No finite search is used to establish this infinite assertion.

For the boundary proof let E_k(a) contain products on k-element index
subsets, and let H_2(B) contain b_i b_j for i<=j. Two pairs that coincide,
intersect in one index, or are disjoint give, respectively, content
coefficients 1, 1 and 3. Hence

    H_2(E_2(a)) = S22(a) disjoint-union E_4(a).

H_2 is injective on nonempty positive multisets. Its maximum is b_1^2
when b_1 is the largest input. After deleting all pairs within a recovered
prefix, the maximum residual is b_1 b_(r+1): every residual pair contains
an outside index, and all factors are bounded above by b_1. Subtraction
uses multiplicities, so repeated maxima cause no problem. The empty
auxiliary case is separately determined by cardinality zero and never
arises in the boundary application.

At length four, put A=prod_i a_i. There are 20 output entries. Symmetry
and total degree four make their product A^20, so positivity determines
A uniquely. Adding one copy of A recovers H_2(E_2(a)), then E_2(a) and
e_2(a). The scalar identity s22=e_2^2-e_1 e_3 and the prescribed positive
e_1=N determine e_3. Together with e_4=A these determine the quartic
with roots a_i. At length two, the sole output is (a_1 a_2)^2, and
the positive product together with the given sum determines the quadratic.
These facts complete Corollary C without changing its fixed-sum scope.

## Attacks and exact checks performed

The domains exclude zero and negative a_i, so logarithms, positive roots,
and the divisions used above are valid. Logs may be zero or negative;
the polynomial argument does not assume otherwise. No exchange of an
infinite limit with an uncontrolled operation is required: the displayed
series identities are formal, or identities of finite sums of entire
functions. No genericity, distinct-root, compactness, or uniformity
assumption is used. Independent low-order checks give
c_1=n(n^2-1)/3, c_2=n(n^2-4)/3, c_3=n(n^2-16)/3 and
c_5=n(n^2-196)/3, explaining the stated exceptional controls.

I wrote and ran `audit/referee-verify.py`, without importing or executing
the proposer program. It enumerates tableaux as pairs of comparable
strict columns and evaluates ordinary Taylor series with exact rational
arithmetic. Results are saved in `audit/referee-checks.json`:

- 1,281 nondecreasing log lists over {-3,-1,0,2,5}, lengths 2--8. Every
  direct output moment through order n agrees with the formal expression.
  Full moment/Newton recovery succeeds in 1,196 cases; the remaining
  85 have exactly the predicted length-2 or length-4 zero.
- Six serialized structured proposer inputs, selected at lengths
  9,14,14,26,46,61, were independently re-evaluated. The two length-14
  inputs stop at order 5; the other four recover. Rational-log inputs
  were checked using their integral numerators, which is equivalent by
  homogeneity and their recorded common denominator.
- 85 positive rational boundary inputs, from {1/7,1/2,1,3/2,5} at
  lengths 2 and 4, recover their exact characteristic polynomials. The
  product A in the four-part tests is obtained from the output, rather
  than supplied from the original input.
- All 26 rows of the serialized coefficient certificate were checked
  independently, together with 4,093 finite modular checks. The bound
  A_26>10^12 and the exact positive difference
  A_(j+1)-A_j=2*3^j-3*2^(j-1) justify the certificate's stopping rule.
- Both unequal-sum boundary witnesses were rechecked with complete exact
  multiplicities. They demonstrate why those unrestricted boundary
  extensions would be false; neither is a same-N counterexample.

All assertions passed, and frozen-file integrity was rechecked afterward.
I did not independently repeat every proposer sample or its 2,079 Mobius
checks. The infinite theorem is certified here by the reconstructed
symbolic proof, with these computations as corroboration. The finite
coefficient certificate supports the ancillary bounded-length statement;
it is not an unbounded Diophantine classification.

## Source comparison and mathematical value

The detailed fresh comparison is in `audit/referee-sources.md`.
[Thomas--Tung, Theorem 5.7 and Conjecture 6.3](https://arxiv.org/html/2606.19796v1)
provide the nearest reconstruction benchmark: known-prefix recovery and
the broader two-row fixed-sum question.
[Fomin](https://arxiv.org/pdf/1903.04062) supplies the established triangular
moment method, while
[D'Andrea--Fatighenti--Onorati](https://arxiv.org/html/2508.03568v2)
already supply the Chern-shadow coefficient formalism, including the
shape-(2,2) derivative. These attributions in the frozen candidate are
substantively accurate. No equivalent reconstruction theorem was located
in the inspected primary material on 2026-09-12; this is bounded screening,
not a worldwide priority guarantee.

The abstract inversion principle alone would be a routine observation.
The combined A--C application additionally identifies the actual tableau
coefficient, proves an all-order arithmetic nonvanishing family, and
removes the previously needed largest-part information for a substantial
natural range of the stated problem. The domain covers arbitrary positive
real multisets in the admitted lengths, including repetitions, and all
but four residue classes in the fixed-sum partition consequence. This is
a useful partial theorem rather than an arbitrary small restriction.
Its concrete uses are reconstruction from finitely many logarithmic
moments and exclusion of those lengths from the search for a same-sum
collision. I judge this delta sufficient for one short result-note.
Neither the boundary reductions nor the general formalism warrants a
separate novelty claim.

## Remaining gaps and disposition

No mathematical gap remains in the exact frozen A--C scope. The original
all-length problem, notably length 14 here, remains unresolved. A zero
coefficient does not establish noninjectivity, and a residue exclusion
does not classify actual failures. Claims of a full resolution, sharp
classification of coefficient zeros, global priority, or stable numerical
inversion would exceed this acceptance.

The manuscript should preserve these limits and the existing attributions.
No substantive claim revision is requested. The next workflow step is the
runner's `check-math` integrity/provenance gate, followed by writing only
the accepted scope. This report is a fresh computational and mathematical
review pass, not formal proof-assistant certification or journal peer review.
