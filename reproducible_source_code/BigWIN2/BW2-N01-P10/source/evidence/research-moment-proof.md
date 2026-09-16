# Schur (2,2) reconstruction: proof dossier

Proposer job: newwin-00001-p10-research-b1ee08dba39b.
Research statement v1, 2026-09-12. This is a proof dossier for a subsidiary
result, not a referee acceptance or manuscript. The frozen original claim
remains unresolved. Positivity is essential for the logarithmic argument.

## Exact subsidiary statement

For n>=2 define

    c_j(n) = n/3 * (n^2 - 1 + 3*2^(j-1) - 3^j),  j>=1.

**Theorem A (coefficient criterion).** If c_j(n) is nonzero for every
1<=j<=n, then the complete Schur-(2,2) monomial-value multiset determines
every n-element multiset of positive real numbers, including repetitions.
In fact, its cardinality and its first n logarithmic power sums suffice.
No prescribed sum of the positive entries is needed in this assertion.

**Theorem B (explicit length classes).** If n>=3, n!=4, and

    n mod 60 is not in {14,26,34,46},

then the hypothesis of Theorem A holds. In particular it holds for every
odd n>=3 and every multiple of four n>=8.

**Corollary C (the frozen problem on these lengths).** For every integer
N>=2, if lambda and mu are positive integer partitions of N, have length
at least two, and have equal S22 multisets, then they are equal whenever
their common length is outside {14,26,34,46} modulo 60. Lengths 2 and 4
are included in this fixed-sum corollary by an elementary separate proof.
The length is automatically determined by S22.

These are sufficient conditions. No converse and no collision at an
excluded length is asserted. In particular length 14 is unresolved here.
Theorem A can certify individual lengths excluded by Theorem B.

## 1. Contents of indexed tableaux

Write a tableau as rows (a,b), (c,d), with a<=b, c<=d, a<c and b<d.
No variable can occur three times. For content (2,2) there is one tableau;
for each content with one doubled label and two other labels there is one;
for four distinct labels there are two. For three labels i<j<k the three
tableaux are (i,i;j,k), (i,j;j,k), and (i,j;k,k). For four distinct labels
i<j<k<l they are (i,j;k,l) and (i,k;j,l). Thus

    s22 = m22 + m211 + 2*m1111.

Here the indices remain distinct even if their input values coincide.
Consequently the number of entries, counted with multiplicity, is

    D(n) = C(n,2) + 3*C(n,3) + 2*C(n,4) = n^2*(n^2-1)/12.

It is strictly increasing for integer n>=2. For example its displayed
count is strictly increasing already in the first term. Hence equality
of output multisets forces equality of input lengths.

Let u_k=sum_i x_i^k. Expansion by the same index-content types proves

    s22(x) = (u_1^4 + 3*u_2^2 - 4*u_1*u_3)/12.                 (1)

For completeness, in u_1^4 the coefficients of m4,m31,m22,m211,m1111
are 1,4,6,12,24. In u_2^2 they are 1,0,2,0,0, and in u_1*u_3 they are
1,1,0,0,0. Substitution gives 0,0,1,1,2, as required.

## 2. Triangular logarithmic moments

For positive a_1,...,a_n set y_i=log(a_i), p_0=n, and
p_j=sum_i y_i^j for j>=1. Let Q_j be the jth power sum of the logarithms
of ALL entries of S22(a), with multiplicity, and put

    P(t)=sum_i exp(t*y_i)=sum_(j>=0) p_j*t^j/j!.

Equation (1), evaluated at x_i=exp(t*y_i), yields the formal identity

    sum_(v in S22(a)) exp(t*log(v))
      = (P(t)^4 + 3*P(2t)^2 - 4*P(t)*P(3t))/12.              (2)

It is also an equality of entire functions; no convergence assumption or
floating-point approximation is being used. At total t-degree j, a term
involving p_j can have no other positive-degree factor. Its coefficient
in the jth derivative at zero is

    [4*n^3 + 6*n*2^j - 4*n*(1+3^j)]/12 = c_j(n).

Every other term uses only p_1,...,p_(j-1). Thus, for every j>=1,

    Q_j = c_j(n)*p_j + R_(j,n)(p_1,...,p_(j-1)),             (3)

where R is explicitly specified by setting p_j=0 in the degree-j
expansion of (2). This formal expression suffices even when j>n;
uniqueness as an expression in independent p_i is used only for j<=n.

If the coefficients in Theorem A are nonzero, (3) recovers p_1,...,p_n
successively. To make the last reconstruction step explicit, set e_0=1
and use Newton's recurrence

    k*e_k = sum_(j=1..k) (-1)^(j-1)*e_(k-j)*p_j, 1<=k<=n.

Then the polynomial z^n-e_1*z^(n-1)+...+(-1)^n*e_n has root multiset
{y_1,...,y_n}. Equality of its coefficients gives equality of the root
multisets even with repeated roots. Exponentiation, an injective map on
the real line, recovers the original positive multiset. This proves A.

## 3. A separate coefficient derivation from distinct-index sums

This verifies the coefficient without presupposing (1). For a list of
positive weights b=(b_1,...,b_k), sum (b_1*y_(i_1)+...+b_k*y_(i_k))^j
over ordered distinct indices i_1,...,i_k. Inclusion-exclusion on set
partitions pi of {1,...,k} gives its coefficient at p_j as

    sum_pi [prod_(B in pi) (-1)^(|B|-1)*(|B|-1)!]
           * n^(|pi|-1) * sum_(B in pi) (sum_(r in B) b_r)^j. (4)

To justify (4), first enforce that indices are equal inside each block
of pi, with no restriction between blocks. In the jth power expansion,
the p_j term assigns all j units of degree to one block; the other
blocks contribute p_0=n. The partition-lattice Mobius factor shown in
(4) changes these unrestricted sums to the distinct-index sum. This is
ordinary finite inclusion-exclusion and also follows inductively by
separating the actual equality partition of each index tuple.

Apply (4) with weights (2,2), (2,1,1), and (1,1,1,1), dividing by 2, 2,
and 12 respectively; these are precisely m22, m211, and 2*m1111.
Their three contributions are

    n*2^j - 4^j/2,

    n^2*(2^j+2)/2 - n*(3^j+1+2^j) + 4^j,

    n^3/3 - n^2*(2^(j-1)+1)
      + n*(2^(j-1) + 2*(3^j+1)/3) - 4^j/2.

Their sum is c_j(n). This supplies the requested direct check against
indexed tableau contents, in addition to (2).

## 4. Arithmetic nonvanishing for the explicit classes

The condition c_j(n)=0 is

    n^2 = A_j := 1 + 3^j - 3*2^(j-1).                       (5)

For j=1,2,3 this gives n=1,2,4 respectively. If j>=4 is even, then
A_j is 2 modulo 8, which is not a square. If j>=5 is odd, then
A_j is 4 modulo 8. A square with this residue has n=2 modulo 4.
Also A_j=1 modulo 3, so 3 does not divide n. Finally, for odd j,
A_j=1 modulo 5: for j=1 modulo 4 use 3^j=3 and 2^(j-1)=1 modulo 5;
for j=3 modulo 4 use 3^j=2 and 2^(j-1)=4 modulo 5.
Therefore n=1 or -1 modulo 5. The simultaneous necessary conditions

    n=2 mod 4, n=1 or -1 mod 3, n=1 or -1 mod 5

give exactly n=14,26,34,46 modulo 60, by the Chinese remainder theorem
(or checking the fifteen residues equal to 2 modulo 4).
For n>=3 with n!=4 outside those four classes, equation (5) has no
solution j>=1. This proves the stronger all-order nonvanishing statement,
and hence Theorem B. These residue classes have density 4/60=1/15;
this is a bound on potentially excluded lengths, not on actual failures.

## 5. Fixed-sum boundary lengths: a self-contained known-tool corollary

For a positive multiset a, let E_k(a) consist of products on distinct
k-element index subsets. For a positive multiset B, let H_2(B) consist
of b_i*b_j with i<=j. Classifying two pairs by whether they coincide,
intersect in one index, or are disjoint proves the multiset identity

    H_2(E_2(a)) = S22(a) disjoint-union E_4(a).               (6)

The disjoint case has three pairings per four indices; S22 has two.
All equal numerical values are still counted with their multiplicities.

H_2 is injective on positive multisets. Its cardinality gives |B| and
its largest entry gives b_1=sqrt(max H_2(B)). After recovering a prefix
b_1>=...>=b_r, subtract its complete H_2 multiset. The largest residual
is b_1*b_(r+1), since every surviving pair has an outside index. This
recovers the next value, including repetitions, until the list is complete.

For n=4, write A=prod_i a_i. There are D(4)=20 output entries. Symmetry
in the indices and total degree four show that the product of these
entries is A^20: the total exponent 80 is distributed equally among
four variables. Thus A is uniquely determined as a positive real number,
and E_4(a)={A}. Equation (6) and injectivity of H_2 recover E_2(a), hence
the scalar e_2(a). The identity

    s22(a) = e_2(a)^2 - e_1(a)*e_3(a)

follows by classifying the same monomial contents (or the two-column
Jacobi-Trudi formula). The left side is the sum of the output entries.
With e_1(a)=N prescribed and positive, it determines e_3(a). Together
with e_4(a)=A these determine the monic quartic with roots a_i. This
proves fixed-sum reconstruction for n=4, for positive reals as well.
For n=2 the sole output is (a_1*a_2)^2; the prescribed sum and positive
product determine the quadratic with roots a_1,a_2. This proves C using
A and B for all other admitted lengths. No new-priority claim is attached
to the boundary argument; it also follows from the known pair-product
reconstruction theorem of Li and (6).

## 6. Scope, dependence, and limitations

The proof is self-contained apart from standard polynomial root
uniqueness, Newton identities, and finite inclusion-exclusion (only the
second, redundant coefficient derivation uses the latter). The direct
tableau proof supplies all required Schur identities. No theorem about
an unbounded exponential Diophantine equation is invoked.

The power-sum method is established prior art, including Fomin's Moser
polynomial treatment. The coefficient c_j(n) is exactly the (j-1)st
Chern shadow of S_(2,2) in D'Andrea--Fatighenti--Onorati's terminology.
The proposed contribution is the positive-real reconstruction criterion
and its explicit infinite-length application to the Thomas--Tung fixed-sum
question, not the invention of either general formalism. The bounded
literature comparison is in literature/research-20260912.md.

Mathematical gap list for A--C: none identified by the proposer. Fresh
referee review, including novelty/value assessment, has not occurred.
The all-length original problem and the existence of any additional
solutions of (5) remain unresolved here. A zero coefficient only blocks
this particular triangular induction; it does not refute injectivity.
Finite computations validate implementation, not the infinite proof.
