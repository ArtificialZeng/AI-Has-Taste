# Proof dossier: strict higher-index ULC failure

Proposer job: `primary-20260913-chen-ulc-failure-research-14052831c026`.
Date: 2026-09-13 Asia/Shanghai. This is a research argument for a fresh
referee, not an acceptance report or a publication manuscript.

## Exact theorem submitted

For each integer m >= 4 define

    f_m(s) = ((s+1)^m - (-1)^m)/(s+2),
    h_m(s) = ((s+1)^m + (-1)^m(s+1))/(s+2).

For either polynomial P write a_j = [s^j]P and d=m-1. Then P has
nonnegative integer coefficients, is monic of degree d, and

    D_m,j(P) := j(m-1-j)a_j^2
                - (j+1)(m-j)a_(j-1)a_(j+1) < 0

for every integer 4 <= j <= m-2. Moreover D_m,m-2(P)=-m for every
m >= 4. Consequently both polynomials fail ordinary ULC of order m-1
for every m >= 4, including m=4,5 where the higher-index range is empty.
This settles both clauses of the immutable source if the proof passes
review. The endpoint identity is included for completeness; non-ULC
existence is already established by Chen's Proposition 3.8.

## 1. Elementary polynomial facts and the endpoint

Set z=s+1. For r >= 1, geometric summation gives

    f_(2r)(s)   = s sum_(ell=0)^(r-1) (s+1)^(2ell),
    f_(2r+1)(s) = 1+s(s+1) sum_(ell=0)^(r-1) (s+1)^(2ell).

Also h_m=f_m+(-1)^m, by direct subtraction of the defining numerators.
These identities prove polynomiality, integrality, nonnegativity and
degree m-1 with leading coefficient 1, for both families in the theorem.
They also show that the two families have the same a_j for j>=1, hence
the same D_m,j for j>=2. It therefore suffices to treat f_m in the
higher-index range and at j=m-2.

Equating the top coefficients of (s+2)f_m=(s+1)^m-(-1)^m gives

    a_(m-1)=1,
    a_(m-2)=m-2,
    a_(m-3)=binom(m,2)-2(m-2)=(m^2-5m+8)/2.

All three indices are positive when m>=4. Thus the same formulas hold
for h_m, and direct substitution gives

    D_m,m-2 = (m-2)^3-(m-1)(m^2-5m+8) = -m < 0.       (1)

The index m-2 is an internal index for all m>=4. This proves the
existence clause without assuming that the higher-index range is nonempty.

## 2. Exact normalization and integral reduction

For f_m put b_j=a_j/binom(m-1,j), 0<=j<=m-1. At each internal index,
the binomial coefficient ratios give the identity

    D_m,j = j(m-1-j)binom(m-1,j)^2
                      (b_j^2-b_(j-1)b_(j+1)).        (2)

The prefactor is strictly positive. This uses degree m-1 throughout.

The fundamental theorem of calculus, applied to t ->
(-1+(s+2)t)^m, gives

    f_m(s)=m integral_0^1 (-1+(s+2)t)^(m-1) dt.         (3)

For s != -2 this follows by division by s+2. Both sides are
polynomials in s, so it also holds at s=-2. Expanding
(-1+(s+2)t)^(m-1)=(st+(2t-1))^(m-1) and extracting coefficients
is valid term by term in a finite sum. Therefore

    b_j=m integral_0^1 t^j(2t-1)^(m-1-j) dt
       =m/2^(j+1) integral_(-1)^1 (1+x)^j x^(m-1-j) dx. (4)

For a target pair (m,j), put p=j-1 and k=m-j-2, and define

    M_r(p,k)=integral_(-1)^1 x^(k+r)(1+x)^p dx,
    H(p,k)=M_0(p,k)M_2(p,k)-M_1(p,k)^2.

Here r is a nonnegative integer; only r=0,1,2,3 is needed. At the
target indices p>=3 and k>=0. Conversely any pair of integers p>=3,
k>=0 gives j=p+1, m=p+k+3, hence m>=6 and 4<=j<=m-2.
This is a bijection with the entire nonempty higher-index target domain.

Using the same moments M_r=M_r(p,k) in all three lines, (4) yields

    b_(j-1)=m/2^j M_2,
    b_j    =m/2^(j+1)(M_1+M_2),
    b_(j+1)=m/2^(j+2)(M_0+2M_1+M_2).

On multiplying and cancelling the common terms we obtain

    b_(j-1)b_(j+1)-b_j^2 = m^2/2^(2j+2) H(p,k).       (5)

It remains to prove H(p,k)>0 for all integers p>=3,k>=0.

## 3. Positivity lemma, including the signed case

If k is even, the measure

    dmu(x)=x^k(1+x)^p dx on [-1,1]

is nonnegative. Its density is strictly positive on (0,1), so the
functions 1 and x are not proportional mu-almost everywhere. The strict
Cauchy--Schwarz inequality gives M_1^2<M_0 M_2. Thus H(p,k)>0.

Now fix an odd integer k>=1. For every integer p>=1, all M_r(p,k)
are strictly positive. Indeed, for even k+r the integrand is
nonnegative and positive on (0,1). For odd k+r, pairing x and -x gives

    M_r(p,k) = integral_0^1 x^(k+r)
                         ((1+x)^p-(1-x)^p) dx > 0.   (6)

The integrand in (6) is strictly positive throughout (0,1).

Define E(p,k)=M_1 M_3-M_2^2. Since k+1 is even, the measure

    dnu(x)=x^(k+1)(1+x)^p dx

is nonnegative and has positive density on (0,1). Its moments of
orders 0,1,2 are M_1,M_2,M_3. Applying strict Cauchy--Schwarz to
1,x in this measure proves

    E(p,k)>0.                                         (7)

Crucially, Cauchy--Schwarz has not been applied to x^k(1+x)^p dx
when k is odd; that measure is signed.

For the induction base p=3, expand (1+x)^3 and integrate the even
monomials. Odd k gives

    M_0=6/(k+2)+2/(k+4),
    M_1=2/(k+2)+6/(k+4),
    M_2=6/(k+4)+2/(k+6).

Subtracting the resulting rational expressions gives exactly

    H(3,k)=64(k+1)/((k+2)^2(k+4)^2(k+6))>0.             (8)

For clarity, on writing t=k+2 the numerator before the factor 16
is t(2t+3)(2t+7)-(t+4)(2t+1)^2=4(t-1), which verifies (8).

For the induction step, multiplying the integrand by 1+x shows

    M_r(p+1,k)=M_r(p,k)+M_(r+1)(p,k).

Abbreviate A=M_0(p,k), B=M_1(p,k), C=M_2(p,k), D=M_3(p,k),
H=AC-B^2, and E=BD-C^2. Here B>0 by (6). Direct algebra gives

    H(p+1,k)=(A+B)(C+D)-(B+C)^2
             =H+(AD-BC)+E
             =(1+C/B)H+(1+A/B)E.                      (9)

The last equality follows from B(AD-BC)=CH+AE and involves no
unproved moment inequality. The two coefficients in the last line
are positive by (6), and E>0 by (7). Thus H(p,k)>0 implies
H(p+1,k)>0. Starting from (8), induction proves H(p,k)>0 for
every integer p>=3 at this fixed odd k. Since k was arbitrary, the
lemma covers every odd k>=1 and, with the even case, all k>=0.

Equations (2) and (5), with strictly positive prefactors, now give
D_m,j<0 at every target index. Section 1 transfers the result to h_m
and supplies (1) at every m>=4. This proves the stated theorem.

## 4. Dependencies, adversarial checks, and scope

The proof depends only on finite polynomial algebra, the binomial
theorem, elementary integration, strict Cauchy--Schwarz (with its equality
criterion), and induction. It has no computational cutoff or asymptotic
remainder. The source is used to identify the conjecture and prior work,
not to supply a missing mathematical step.

The researcher reconstructed the coefficient extraction, the bijection,
the determinant cancellation, the p=3 rational numerator, and the
denominator-free recurrence identity. This research reconstruction of
triage's route is not a fresh independent referee report.

The regression program `research-verify.py` compares a forward polynomial
recursion and exact division with moment evaluation, symbolically checks
the identities in (1), (8), and (9), and exercises boundary and asymmetric
parameter choices. Its exact finite output is `research-verify.json`.
These computations check formulas; the infinite proof is Sections 1--3.

The negative control H(2,1)=-16/225, corresponding to m=6,j=3,
shows that lowering the uniform cutoff from j=4 to j=3 would be false.
This is outside the frozen target and is not a counterexample to it.
Here f_6 has coefficients [0,3,6,7,4,1] and D_6,3=6. The first
regression run stopped at a mistyped expected value 16 for this control;
direct substitution gave 6, and the assertion was corrected before
generating the evidence JSON. No theorem statement or proof step changed.

Known mathematical gap list: empty. Fresh referee review: pending.
Novelty boundary: the uniform higher-index clause is conjectural in the
inspected arXiv v2. The full later journal body has not been obtained;
no absolute priority or present global open-status claim is made. See
`../literature/research-screen.md` for the bounded live source check.
