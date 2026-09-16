# Uniform boundary compensation and a precise induction obstruction

Job: `primary-20260913-binary-subsum-shape-research-f5d9991a30d8`.
This is a research dossier, not a manuscript or an independently accepted result.
The original all-coefficient conjecture remains unresolved. No priority claim
is made for the boundary consequences below.

## Scope

Use the exact N_n, A_n, B_n and T_j of `problem.md`. For every even n>=6,

    T_j(N_n) > T_j(A_n) > 0

at j=1,2,d(n)-2,d(n)-1. The j=2 and j=d(n)-2 assertion already holds for even
n>=4. This proves only four boundary inequalities, not the original conjecture.
Odd N_n inherit the corresponding original inequalities from N_(2m+1)=N_(2m).
The claims about A_n refer only to its defined even-index scope.

The proof uses the prior binary recurrence (BBFM Theorem 4.7), its first
coefficient identity (Corollary 4.2), and elementary polynomial algebra.
The formulas for coefficients 0,1,2 below are prior facts (Corollary 4.5 and
Remark 8). They are rederived here to show their dependencies. The cubic
formula and the compensation calculations are derived in this dossier.
See `literature/research-pass1-source-check.md` for source access and limits.

## Coefficient identities

Let w_k be the number of binary partitions of k, including w_0=1. Adding a
part 1 is injective, so w_0<=w_1<=... . Write n=2m, w=w_m, and

    S_r = sum_(k=0)^m k^r w_k  (r=0,1,2,3),
    R_r = sum_(k=0)^(m-1) k^r w_k.

For r=0, take k^0=1 also at k=0. Define c_j=[x^j]N_(2m), with coefficients
outside the degree range set equal to zero for the identities in this proof.
The first four coefficients are

    c_0 = S_0,
    c_1 = 2 S_1,
    c_2 = 2 S_2,
    c_3 = sum_(k=0)^m H_m(k) w_k,
    H_m(k) = (4k^3+2k)/3 - (m-k)(m-k+1).                (1)

Here is a derivation of (1). The prior identity at an arbitrary integer k is

    [x]N_k = k w_k - sum_(h=0)^(k-1) w_h.              (2)

It also follows directly by summing k-m_lambda(1) over partitions: summing
m_lambda(1) counts partitions obtained after removing one or more ones.
The recurrence for N_(2k) has carry factor 1+x^2+O(x^4). Thus its constant,
linear, and quadratic coefficient increments, relative to N_(2k-2), are
w_k, 2k w_k, and

    binom(2k,2) w_k + [x]N_k + [x^0]N_(2k-2) = 2k^2 w_k.

These telescope to the first three formulas. The cubic increment is

    binom(2k,3) w_k + 2k [x]N_k + [x]N_(2k-2)
    = (4k^3+2k)w_k/3 - 2 sum_(h=0)^(k-1) (k-h)w_h.

Summing over k=1,...,m gives the cubic formula in (1).

For A_(2m)=(1+x)^(2m)N_m(x^2), (2) gives

    a_0=w,  a_1=2mw,  a_2=2m^2w-R_0,
    a_3=(4m^3+2m)w/3-2mR_0.

Consequently

    T_1(A_(2m)) = 2m^2w^2+wR_0,
    T_2(A_(2m)) = 4m^2(m^2-1)w^2/3+R_0^2.           (3)

Both are strictly positive for the stated internal-index ranges.

## First boundary position

Expansion of (1) and (3) yields

    T_1(N_(2m))-T_1(A_(2m))
      = w sum_(k=0)^(m-1) g_m(k)w_k + 4R_1^2-2R_0R_2,
    g_m(k)=8mk-2k^2-2m^2-1.                           (4)

The increasing weights w_k imply 2R_1>=(m-1)R_0; this is the elementary
Chebyshev sum inequality applied to k and w_k. Since R_2<=(m-1)R_1,
the last two terms in (4) have nonnegative sum. Also g_m(k) increases over
0<=k<m, and its average is

    (1/m) sum_(k=0)^(m-1) g_m(k) = (4m^2-9m-4)/3.

Applying the same inequality to g_m(k) and w_k gives the quantitative bound

    T_1(N_(2m))-T_1(A_(2m))
      >= wR_0 (4m^2-9m-4)/3 > 0,                    (5)

for m>=3. The Chebyshev inequality used here follows by expanding the sum
of (f_i-f_j)(w_i-w_j)>=0 over pairs of increasing sequences; it does not
require f_i to be nonnegative. This completes the first-position proof.

## Second boundary position: a nonnegative quadratic kernel

For 0<=l<=m set

    U_l = sum_(k=l)^m k,
    V_l = sum_(k=l)^m k^2,
    W_l = sum_(k=l)^m H_m(k),
    alpha = 4m^2(m^2-1)/3,
    K_m(l,t) = 4V_l V_t-U_l W_t-U_t W_l-alpha-(m-l)(m-t).   (6)

All these are explicit polynomials, since H_m is given in (1). Let
e_0=w_0 and e_l=w_l-w_(l-1) for l>=1. Then e_l>=0 and expansion gives

    T_2(N_(2m))-T_2(A_(2m))
      = sum_(l=0)^m sum_(t=0)^m e_l e_t K_m(l,t).      (7)

For completeness, the polynomial certificate for K_m(l,t)>=0 follows below.
Symmetry allows l<=t. The four substitutions cover every pair of integers
0<=l<=t<=m:

1. l=u+1, t=u+1+b, m=u+1+b+c, with u,b,c>=0;
2. l=0, t=b+2, m=b+2+c, with b,c>=0;
3. l=t=0, m=c>=0;
4. l=0, t=1, m=c+1, with c>=0.

In each case write 36K=sum_(r=0)^6 P_r c^r. Every displayed coefficient
below is nonnegative. These identities are polynomial expansions of (6),
not numerical approximations. Full expanded monomials are also serialized
in `evidence/research_boundary.json` and reproduced by
`python3 evidence/research_boundary.py`.

In case 1:

    P6 = 4
    P5 = 24(b+u+2)
    P4 = 2(33b^2+66bu+114b+36u^2+108u+74)
    P3 = 4(22b^3+66b^2u+114b^2+72bu^2+216bu+131b
           +24u^3+108u^2+114u+42)
    P2 = 2(27b^4+108b^3u+207b^3+180b^2u^2+594b^2u+363b^2
           +120bu^3+612bu^2+642bu+192b
           +24u^4+192u^3+300u^2+132u+14)
    P1 = 2(6b^5+30b^4u+75b^4+72b^3u^2+294b^3u+193b^3
           +72b^2u^3+468b^2u^2+522b^2u+156b^2
           +24bu^4+288bu^3+516bu^2+228bu+14b
           +48u^4+144u^3+96u^2)
    P0 = 12b(b+u+1)(b^3+4b^2u+3b^2+8bu^2+8bu+2b+4u^3+8u^2).

In case 2:

    P6 = 4
    P5 = 24(b+3)
    P4 = 2(33b^2+180b+230)
    P3 = 4(22b^3+180b^2+443b+354)
    P2 = 2(27b^4+315b^3+1191b^2+1890b+1118)
    P1 = 2(b+2)(6b^4+93b^3+385b^2+646b+438)
    P0 = 12(b+2)^2(b+3)(b^2+2b+4).

In case 3 the polynomial is

    36K = 4c^6+24c^5+4c^4+48c^3+28c^2.

In case 4 the polynomial is

    36K = 4c^6+48c^5+166c^4+276c^3+262c^2+180c+72.

Thus K is nonnegative everywhere on the required integer domain.
Moreover, K_m(0,0)>0 for m>=1 and e_0=w_0=1. Equation (7) is therefore
strictly positive. Equations (3), (5), and (7) prove the stated inequalities.
Palindromicity of A_n and N_n gives the reflected positions.

## Exact obstruction to an abstract induction cone

When n=2m with m odd, the prior equality N_m=N_(m-1) makes the carry-one
step exactly

    A_new=(1+x)^2 A_old,
    B_new=(1+x^2) N_old,
    N_new=A_new+B_new.                                (8)

Consider the abstract hypothesis class: A,B,N=A+B have positive palindromic
coefficients and equal degree, and T_j(N)>T_j(A)>0 at every internal index.
This class is **not** preserved by (8), even for degree 8 inputs.
An exact witness is

    A=[10,11,12,13,14,13,12,11,10],  B=2A,  N=3A.

All internal T_j(A) are positive: they are 1 except for the middle value 27.
Thus T_j(N)=9T_j(A)>T_j(A)>0. The output triples at j=1 are

    A_new: (10,31,44), B_new: (30,33,66), N_new: (40,64,110).

Hence T_1(A_new)=521 but T_1(N_new)=64^2-40*110=-304, and the
compensation is -825. Every input condition and output integer is checked
in `research_boundary.py` and retained in its JSON.

This is a proved obstruction to an induction using only the specified abstract
shape assumptions. The input polynomials are not claimed to be actual binary
numerators. It is not a counterexample to the original or to the invariant
restricted to the actual recurrence sequence. Additional relations specific
to binary partition counts are still available and may support an induction.

## Verification limits

The script checks the complete symbolic kernel expansions above, compares them
with 454 literal finite-sum evaluations, and checks coefficient identities
against actual N_n for even 2<=n<=128. The separate assigned test covers every
coefficient through n=512. Neither finite range supplies the universal step:
the boundary proof comes from (1)–(7) and the nonnegative polynomial identities.
There has been no fresh-context referee or independent novelty audit. The
remaining internal positions and a preserved all-index invariant are unknown.

## One next test: the third-position kernel

Coefficient extraction gives a concrete next target without extending the
finite N_n range. With R_0(k)=sum_(h=0)^(k-1)w_h, put

    L_k = k w_k-R_0(k),
    Q_k = 2 sum_(h=0)^floor(k/2) h^2 w_h.

The next coefficient is the linear functional

    c_4(2m) = sum_(k=1)^m [binom(2k,4)w_k+binom(2k,2)L_k+Q_k
                           +2 sum_(h=0)^(k-1)h^2w_h
                           +1_(k even)R_0(k)],
    a_4(2m) = binom(2m,4)w_m+binom(2m,2)L_m+Q_m.     (9)

Indeed the x^4 coefficient of the carry factor for N_(2k) is 1 for even k
and 0 for odd k. Its x^2 coefficient is always 1, and its odd coefficients
are zero. Extracting x^4 in the recurrence proves (9).

Treat (1), (3)'s underlying a_j formulas, and (9) as linear functions of
formal weights w_0,...,w_m. For the tail vector w_k=1_(k>=l), denote the
resulting coefficients by p_j(l), a_j(l). Define the symmetric kernel

    2K3_m(l,t) = 2p_3(l)p_3(t)-p_2(l)p_4(t)-p_2(t)p_4(l)
                -2a_3(l)a_3(t)+a_2(l)a_4(t)+a_2(t)a_4(l).       (10)

Then compensation at j=3 equals sum_(l,t)e_l e_t K3_m(l,t).
`research_boundary.py` calibrates (9) against the actual recurrence through
even n=128 and checks (10) exactly for all 6510 pairs with
5<=m<=32 and 0<=l<=t<=m. No negative kernel entry occurs; the minimum is zero.
This is finite evidence for a subsidiary monotone-weight statement, not an
all-m proof or an additional original-conjecture resolution.

**Next test:** decide K3_m(l,t)>=0 for every integer m>=5 and 0<=l<=t<=m
by an exact piecewise polynomial certificate, separating the parity and
halfway boundaries introduced by (9). A negative kernel entry must be
reported as failure of this proposed monotone-weight certificate, not as an
actual binary-numerator counterexample. A certificate would extend the
uniform compensation proof to the third and reflected positions and test
whether the method has a useful general pattern. Do not merely extend the
already completed all-coefficient n<=512 computation.
