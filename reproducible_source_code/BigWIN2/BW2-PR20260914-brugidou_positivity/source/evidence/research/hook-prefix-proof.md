# Initial coefficients and an enlarged positive region for hooks

Proposer job: primary-20260914-brugidou-positivity-research-cd617853de0e.
Research candidate for a fresh referee; no acceptance is asserted.
The original all-partition positivity conjecture remains unresolved.

## Exact scope

Use the specialization and normalization in `source.md` and `problem.md`.
For integers a>=2 and b>=0, put

    K_(a,b)(q) = J_(a,1^b)(q)/b!,
    d_(a,b) = binom(a-1,2)+(a-1)b,
    D_a = binom(a-2,2),
    F(a) = max(0, ceil((D_a-4)/2)).

The proposed theorem is:

1. K_(a,b) belongs to Z[q].
2. For every 0<=k<=min(d_(a,b),2b+3), [q^k]K_(a,b)>0.
3. If b>=F(a), all coefficients of K_(a,b), from degree zero through
   degree d_(a,b), are strictly positive.

Consequently item 3, together with the established one-row cases b=0,
verifies Brugidou's positivity conjecture for every hook with 2<=a<=6 and
for the indicated region at larger a. It has no implication here
for non-hooks or for general short-leg hooks outside that region. F is a
sufficient bound, not a claimed optimal bound. Coefficient log-concavity is
not part of this submission.

## Established dependencies

The primary text is Brugidou, arXiv:2306.15300v7, preserved in
`evidence/external/2306.15300v7.html` and the full text extraction
`evidence/external/2306.15300v7.txt`.

We use Corollary 3.5 for polynomiality and degree; equation (3.22) for the
a=2 base; and the established polynomials J_n^(r) in the introduction and
the unnumbered positive recurrence displayed in the proof of Corollary 3.4
(cited there as [8, Equation (6.5)]). In particular, J_n=J_n^(1) has positive integer
coefficients, degree binom(n-1,2), and constant (n-1)!, while
J_n^(r)(0)=(n-r)!. Setting r=1 in that recurrence gives, for m>=2,

    J_m = sum_(j=1)^(m-1) binom(m-1,j) q^binom(j,2) J_(m-1)^(j).       (1)

These are established results, not proposed new results. The coefficient
inequality extracted from (1) below also has the elementary interpretation
of adding a largest labeled leaf to a tree rooted at its smallest label.

## Hook recurrence and integrality

For a>=3, multiplication of symmetric functions gives

    p_(a-1)e_(b+1) = m_(a,1^b) + m_(a-1,1^(b+1)).                    (2)

The distinguished variable of exponent a-1 either occurs among the b+1
elementary variables or does not. Each resulting monomial occurs once;
a-1>=2 is essential for this multiplicity statement.

The defining normalization specializes to

    phi_q(m_(a,1^b))
      = (1-q)^(a-1) q^binom(b+1,2) K_(a,b)/(a+b-1)!.

Apply phi_q to (2), cancel in Q(q), and then use polynomiality to obtain

    (1-q)K_(a,b)
      = binom(a+b-1,a-2) J_(a-1) - q^(b+1)K_(a-1,b+1).              (3)

The base is K_(2,b)=1+q+...+q^b. Induction on a proves integrality:
the numerator on the right of (3) is integral, and division by 1-q takes
integer coefficient prefixes. Its final prefix is zero because the quotient
is already known to be a polynomial. Thus no divisibility by b! was assumed.
The degree d_(a,b) follows by substituting the hook in Corollary 3.5.

For a=3, (3) directly gives the complete coefficient list

    K_(3,b): (b+2 repeated b+1 times), b+1,b,...,1.                    (4)

Its degree is 2b+1. The a=2 and a=3 cases of all three assertions follow.

## A row inequality with its first nonzero excess

For m>=3 define

    R_m = J_m - (m-1)J_(m-1).

By (1), R_m has nonnegative coefficients. Only the j=2 summand can
contribute to degree one, so

    [q]R_m = binom(m-1,2)(m-3)! = (m-1)!/2 > 0.                    (5)

Both nonnegativity and this precise coefficient are needed. No conjectural
positivity of an individual non-row J_lambda is used in (5).

## Positive initial coefficients, without an inductive positivity assumption

Fix a>=4, b>=0, and set

    s=b+1, N=a+b-1,
    A=binom(N,a-2)J_(a-1),
    B=K_(a-1,b+1),
    P=binom(N,a-3)J_(a-2),
    C=K_(a-2,b+2).

Applying (3) twice gives

    (1-q)K_(a,b)=A-q^s B,
    (1-q)B=P-q^(s+1)C.                                             (6)

Write p_i=[q^i]P, extended by zero off the support, and put

    Delta=A-(s+1)P=binom(N,a-2)R_(a-1).

The binomial-factor equality follows from
binom(N,a-2)(a-2)=(b+2)binom(N,a-3). Therefore Delta has nonnegative
coefficients and, by (5),

    Delta_1 = (s+1)p_0/2,     p_0>0.                               (7)

Let c_k=[q^k]K_(a,b). For 0<=k<s, (6) yields c_k=sum_(i=0)^k A_i>0.
For k=s+t and 0<=t<=s, the C term in (6) has not yet contributed to the
prefix of B. Taking the two coefficient prefixes yields the exact identity

    c_k = sum_(i=0)^k Delta_i
          + sum_(i=0)^t (s-t+i)p_i
          + (s+1)sum_(i=t+1)^k p_i.                               (8)

Every summand is nonnegative. If t<s, the term (s-t)p_0 is positive.
If t=s, k=2s>=2 and the first sum contains Delta_1>0. Thus c_k>0
through k=2s, insofar as these indices are within the degree.

At the next index k=2s+1, t=s+1, the C term contributes exactly its
constant coefficient C_0 to the double prefix. Hence

    c_(2s+1) = sum_(i=0)^(2s+1) Delta_i
                + sum_(i=0)^(s+1) (i-1)p_i
                + (s+1)sum_(i=s+2)^(2s+1) p_i + C_0
             >= Delta_1 - p_0 + C_0
              = (s-1)p_0/2 + C_0 > 0.                            (9)

Here C_0>0 follows from the constant coefficient of (3), or from the
a=2 base when a=4. This uses only constants, not the positivity of other
coefficients of C. Explicitly, K_(u,v)(0)=(u+v-1)!/(v+1)! for u>=2.
For a>=4, d_(a,b)>=3s>=2s+1, so the last coefficient used is in range.
Equations (4), (8), and (9) prove item 2 for every hook.

## Completion of the enlarged region by tail induction

Induct on a; the a=2 and a=3 bases were proved above. Suppose b>=F(a).
The function F is nondecreasing, so b+1>=F(a-1). The induction hypothesis
therefore gives strictly positive coefficients throughout B=K_(a-1,b+1).

Let D=deg A=D_a and L=deg B. Polynomiality in (6) implies A(1)=B(1).
For any k>=D, the coefficient-prefix identity in (6) becomes

    c_k = A(1) - sum_(j=0)^(k-s) B_j
        = sum_(j>k-s) B_j,                                       (10)

with the usual empty-prefix convention. This is positive whenever
0<=k<=s+L-1. A direct degree calculation gives

    s+L-1 = d_(a,b).

Thus all coefficients from D through the degree are positive. The assumed
bound b>=ceil((D-4)/2) is exactly D-1<=2b+3. Item 2 already covers
every coefficient below D, so there is no gap. This proves item 3.
The small values where the ceiling is negative are covered by b>=0.

## The assigned overlap test and the change from triage

For a=5, b=1, A=10(6+6q+3q^2+q^3) and B=K_(4,2), with B_0=20.
The sole overlap below deg A=3 is k=2, giving 10(6+6+3)-20=130.
The complete exact polynomial is

    K_(5,1)=60+120q+130q^2+110q^3+80q^4+55q^5
             +35q^6+20q^7+10q^8+4q^9+q^10.

Uniformly in b, two applications of (3) give

    (1-q)^2 K_(5,b)
      = binom(b+4,3)(1-q)J_4
        - q^(b+1)binom(b+4,2)J_3 + q^(2b+3)K_(3,b+2),             (11)

where (4) supplies the last term explicitly. The a=5 overlap suggested
using the row excess in (5); the proof is the uniform identities (8)-(10),
not the finite a=5 check.

The saved triage bound was b>=max(0,D_a-1), based on separated supports.
The present bound max(0,ceil((D_a-4)/2)) includes new overlapping regimes:
for a=6,7,8,9,10 the new minima are 1,3,6,9,12, respectively,
whereas the old minima were 5,9,14,20,27. It also gives positive initial
coefficients for every hook outside the fully settled region.

No missing mathematical step is known in this submitted argument.
A fresh referee must still check correctness, source overlap, and whether
the contribution is sufficient. Exact computations in `hook_prefix_check.py`
validate formulas and boundary cases; they do not prove infinite scope.
