# Triage analysis: a different recovery test

Job: newwin-00001-p10-triage-c547cde10837. These are inspectable mathematical derivations and calibration results, not referee acceptance or a manuscript.

## 1. The old prefix target is known

For decreasing positive entries a1,...,an,

s22 = m22 + m211 + 2 m1111,

and the number of entries of S22 is n^2(n^2-1)/12, strictly increasing for n>=2. Its maximum is (a1*a2)^2. For 2<=r<n, subtract the complete prefix multiset with all multiplicities. Every surviving indexed monomial has a variable of value at most t=a_(r+1). Type (2,2) is at most a1^2*t^2; type (2,1,1) is at most a1^2*a2*t; type (1,1,1,1) is at most a1*a2*a3*t. All are at most a1^2*a2*t, attained by a1^2*a2*t on distinct indices 1,2,r+1. Equal numerical values do not invalidate multiset subtraction: the residual counts exactly the monomials involving an outside index.

This is precisely the shape-(2,2) specialization of Thomas–Tung Theorem 5.7's proof. It is not a new result. Given a1, the maximum determines a2, then the prefix formula determines the rest. Choosing a1 remains essential. For example, (4,1,1) and (2,2,2) share N, length, and largest monomial, but their complete multisets differ.

## 2. Logarithmic moments: proposed research scope

The scope here temporarily extends to arbitrary positive real lists of a fixed length n. Put yi=log(ai), p_j=sum_i yi^j, p_0=n, and let Q_j be the sum of jth powers of the logarithms of every S22 entry, with multiplicity. These Q_j are determined by the FULL observed multiset. They are not inferred from the single scalar s22(a).

Let P(t)=sum_i exp(t*yi). From the degree-four identity

s22(x) = (p1(x)^4 + 3*p2(x)^2 - 4*p1(x)*p3(x))/12,

one obtains the exact generating-function identity

sum_(v in S22(a)) exp(t*log(v))
  = (P(t)^4 + 3*P(2t)^2 - 4*P(t)*P(3t))/12.

For 1<=j<=n, expansion in the input power sums yields

Q_j = c_j(n)*p_j + R_(j,n)(p_1,...,p_(j-1)),
c_j(n) = n/3 * (n^2 - 1 + 3*2^(j-1) - 3^j).

Indeed a term containing p_j at total t-degree j can contain no other positive-degree term. Its coefficient is [4*n^3+6*n*2^j-4*n*(1+3^j)]/12. All remaining terms use lower moments only. If every c_j(n) for 1<=j<=n is nonzero, induction recovers p_1,...,p_n. Newton identities then recover the monic polynomial with roots y_i, including repeated roots. Exponentiation recovers the original positive multiset. This argument suggests an all-N injectivity result for every length satisfying this explicit condition, even without fixing N.

Natural infinite scope: every odd n>=3 satisfies the condition. For j=1, c_1(n)=n(n^2-1)/3. For j>=2, the number 1+3^j-3*2^(j-1) is even, whereas n^2 is odd. Also all n divisible by 4 with n>=8 satisfy it: j=2,3 give only n=2,4; for even j>=4 the right side is 2 mod 8, and for odd j>=5 it is 4 mod 8, neither divisible by 16. These are elementary deductions from the displayed criterion, awaiting the next research pass's complete scope and novelty check.

Exact bounded coefficient screening found zeros only at (j,n)=(1,1),(2,2),(3,4),(5,14) for j<=256. Separately all 2<=n<=256 and 1<=j<=n were checked. **This does not prove that there are no later square-equation solutions.** A zero coefficient is a failure of this particular triangular induction, not a collision or disproof. In particular n=14 remains a named exceptional case.

## 3. Easy boundary reduction; not the proposed new contribution

Let E_k(a) be the k-fold products on distinct indices, and H2(B) the products b_i*b_j for i<=j in a list B. Directly grouping overlapping and disjoint index pairs gives

H2(E2(a)) = S22(a) disjoint-union E4(a).

For n<4 the correction is empty. For n=4, it is the singleton product A=prod_i a_i. This A is determined by S22 because the product of its 20 entries is A^20 (symmetry and total degree give exponent 20 on each variable). H2 is injective on positive lists: its largest entry gives the largest b, then subtracting H2 of a known prefix exposes largest residual b1*b_next. Thus S22 determines E2 for n<=4. At fixed sum Li's pair-product theorem finishes reconstruction. This is an elementary corollary of known tools, not presently a standalone novelty claim. For n>4, E4 is no longer determined just by total product; this reduction alone is incomplete.

## 4. Reproducibility and decision

Run `python3 evidence/check-triage-log-moments.py`. It imports the existing baseline definitions without running or overwriting their main outputs. All 7313 partitions N=2..24 were rechecked with two exact multiset implementations; 3196 also with tableaux; no same-N collisions. It checked 40496 prefix residual maxima and 1267 length-at-most-four reductions. Logarithmic calibration used 76 deterministic integer-coordinate lists (four at each length 2..20): all generating-function identities passed, and 64 lists at nonexceptional lengths had all input moments recovered. Integer coordinates can be regarded as logarithms base 2 of positive rational parts; no numerical logarithms were evaluated. These finite tests support implementation only.

Admit a bounded research pass for the nonvanishing-coefficient criterion and its infinite length classes. Nearest prior results: Thomas–Tung's largest-part-conditional recovery, Li's pair-product theorem, and the classical triangular-moment method. Proposed delta: explicit shape-(2,2) recovery criterion and a natural infinite range, with the original all-length claim left unresolved. Verification route: formal generating-function derivation, exact Newton reconstruction, coefficient arithmetic, then a literature comparison against general Schur representation invariants. No candidate kind is assigned at triage.

One next test: independently rederive the coefficient from indexed tableaux weights and complete the nonvanishing/Newton proof for all odd lengths, while checking whether a prior general Schur-weight reconstruction theorem already implies that same statement. This can either justify a useful subsidiary theorem or reject it as a rediscovery. Do not resume the already-known prefix proof as the research target.
