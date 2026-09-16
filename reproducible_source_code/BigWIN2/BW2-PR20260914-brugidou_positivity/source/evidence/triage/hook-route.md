# Hook reduction and a partial positivity argument

Job: primary-20260914-brugidou-positivity-triage-820b8c1104a3.
Status: local mathematical derivation for triage; no fresh referee or novelty
acceptance. The original all-partition conjecture is unresolved.

Set K_(a,b)=J_(a,1^b)/b! for integers a>=2,b>=0. The source implies that this
is a rational polynomial; integrality after division by b! follows below.
For a>=3, multiplication of p_(a-1) by e_(b+1) gives

p_(a-1)e_(b+1)=m_(a,1^b)+m_(a-1,1^(b+1)).                 (H0)

Indeed, the variable carrying exponent a-1 either occurs among the b+1
distinct elementary variables or does not. Each resulting monomial occurs
once. The condition a-1>=2 prevents collisions with the elementary exponents.
Under phi, use phi(p_(a-1))=(1-q)^(a-2)J_(a-1)/(a-2)! and
nu(a,1^b)=binom(b+1,2). Since both hooks in (H0) have size a+b, cancellation
in Q(q), followed by polynomial equality, gives

(1-q)K_(a,b) = binom(a+b-1,a-2) J_(a-1)
              - q^(b+1)K_(a-1,b+1).                    (H1)

Here J_(a-1) denotes the one-row tree polynomial, not a hook with b>0.
The base case is K_(2,b)=[b+1]_q from source (3.22). Induction on a in (H1)
shows K_(a,b) in Z[q] for every b>=0: the numerator is integral and division
by 1-q, known to have zero remainder, gives integral coefficient prefixes.
Its degree is d_(a,b)=binom(a-1,2)+(a-1)b. In particular

K_(3,b) = (b+2) sum_(k=0)^b q^k
          + sum_(j=1)^(b+1) (b+2-j)q^(b+j).             (H2)

This includes K_(3,0)=2+q. It follows either from (H1) or from
m_(3,1^b)=p_2 e_(b+1)-p_1 e_(b+2)+(b+3)e_(b+3).

**Local partial theorem.** For every a>=3 and
b>=max(0,binom(a-2,2)-1), all coefficients of K_(a,b), and hence J_(a,1^b),
from degree zero through d_(a,b) are strictly positive.

Proof: induct on a, with the known a=2 family as base. Put
A=binom(a+b-1,a-2)J_(a-1), B=K_(a-1,b+1), s=b+1, and
D=deg A=binom(a-2,2). The assumed threshold gives s>=D. The smaller hook
satisfies the inductive threshold because b+1>=max(0,binom(a-3,2)-1)
(for a=3 use the base directly). Thus A and B have positive coefficients
through their degrees. Polynomiality in (H1) gives A(1)=B(1).
Write a_i=[q^i]A and b_i=[q^i]B, extended by zero outside their degrees.
Then

[q^k]K_(a,b)=sum_(i=0)^k a_i - sum_(j=0)^(k-s) b_j.      (H3)

If k<s, the second sum is empty and the first contains a_0>0. If k>=s,
then k>=D, so the first sum equals A(1)=B(1). The coefficient is therefore
sum_(j>k-s)b_j, which is strictly positive for
k<=s+deg B-1=d_(a,b). This proves every required coefficient is positive.
The boundary s=D is covered without requiring disjoint supports at degree D.

This argument does not cover every short-leg hook: when s<D, the window
s<=k<D contains overlapping prefix sums. Failure of support separation is
not a negative coefficient, nor an obstruction to other methods. The region
outside this window is positive whenever the smaller hook is positive.

Exact validation in `hook_check.py`/`.json`: 45 direct defining-specialization
checks for hooks of size <=10; 66 comparisons to prior calibration through
size 12; (H2) for 0<=b<=30; and 28 cutoff/adjacent cases with 3<=a<=12.
All final checks pass. These are validation ranges, not a universal proof.
The first test run omitted a factor b! when comparing augmented monomials
with K and failed at (a,b)=(2,2). Correcting that normalization produced the
reported pass; this implementation error was not a mathematical counterexample.

Next bounded test: use (H3) to analyze the overlapping window
b+1<=k<binom(a-2,2) below the cutoff. Derive the a=5 family symbolically from
(H1), where b=1 is the first non-row case outside the theorem, and determine
whether a usable coefficient bound extends to arbitrary a. Stop after this
one comparison if it supplies no uniform bound; retain the partial theorem
for a separate novelty and mathematical audit rather than extending finite rows.
