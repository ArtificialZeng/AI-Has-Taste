# Signed-moment reduction and induction route

Job: primary-20260913-chen-ulc-failure-triage-085d5b98e601.
Date: 2026-09-13 (Asia/Shanghai). Status: unreviewed triage derivation;
not an accepted mathematical candidate or a novelty claim.

This is a structural test, not an enlargement of the source's finite census.
Write n=m-1, a_j=[s^j]f_m, b_j=a_j/binom(n,j). The exact target minor is

    D_m,j=j(n-j)binom(n,j)^2 (b_j^2-b_{j-1}b_{j+1}).             (1)

All prefactors in (1) are positive for the target indices.

## Elementary validation

At s=-2 both numerators vanish, so the definitions are polynomials.
Putting x=s+1, f_(2r)=s sum_(l=0)^(r-1) x^(2l) and
f_(2r+1)=1+s x sum_(l=0)^(r-1) x^(2l). Thus all coefficients are
nonnegative; h_m=f_m+(-1)^m has the same property. Both polynomials
are monic of degree m-1 and have identical minors for j>=2.

The top three coefficients are

    a_(m-1)=1, a_(m-2)=m-2, a_(m-3)=(m^2-5m+8)/2.

Substitution gives D_(m,m-2)=-m for every m>=4, for both families.
This independently confirms the already-known non-ULC existence clause,
including m=4,5 where the higher-index target is empty. It is a
rediscovery, not a proposed contribution.

## Integral identity

The fundamental theorem of calculus gives the polynomial identity

    f_m(s)=m integral_0^1 (-1+(s+2)t)^(m-1) dt.

Taking coefficients and then setting x=2t-1 yields

    b_j=m integral_0^1 t^j(2t-1)^(m-1-j) dt
       =m/2^(j+1) integral_(-1)^1 (1+x)^j x^(m-1-j) dx.        (2)

For each target pair set p=j-1>=3 and k=m-j-2>=0. Define

    M_r(p,k)=integral_(-1)^1 x^(k+r)(1+x)^p dx  (r=0,1,2,3),
    H(p,k)=M_0 M_2-M_1^2.

Equation (2) gives

    b_(j-1)=m/2^j M_2,
    b_j=m/2^(j+1) (M_1+M_2),
    b_(j+1)=m/2^(j+2) (M_0+2M_1+M_2),

and therefore

    b_(j-1)b_(j+1)-b_j^2=m^2/2^(2j+2) H(p,k).               (3)

Thus the entire higher-index target is exactly H(p,k)>0 for all
integers p>=3,k>=0, with inverse mapping j=p+1,m=p+k+3.

## Uniform positivity route to audit in research

If k is even, x^k(1+x)^p dx is a nonnegative measure, positive on
an interval. Strict Cauchy-Schwarz for the functions 1,x gives H>0.

Let k>=1 be odd. For every p>=1, M_0,M_1,M_2 are positive.
For odd exponent k+r, pair the integral at x and -x to obtain
integral_0^1 x^(k+r)((1+x)^p-(1-x)^p) dx>0; even exponents have
nonnegative integrands. Also

    E(p,k)=M_1 M_3-M_2^2>0,

by strict Cauchy-Schwarz for the nonnegative measure
x^(k+1)(1+x)^p dx. At p=3, direct integration gives

    M_0=6/(k+2)+2/(k+4),
    M_1=2/(k+2)+6/(k+4),
    M_2=6/(k+4)+2/(k+6),
    H(3,k)=64(k+1)/((k+2)^2(k+4)^2(k+6))>0.                 (4)

Since M_r(p+1,k)=M_r(p,k)+M_(r+1)(p,k), expansion yields

    H(p+1,k)=H(p,k)+(M_0 M_3-M_1 M_2)+E(p,k)
            =(1+M_2/M_1)H(p,k)+(1+M_0/M_1)E(p,k).          (5)

The coefficients on the last line are positive. Equations (4)-(5)
therefore provide an induction from p=3 for every fixed odd k>=1.
This appears to close the full sign target together with (1)-(3).
It has not received a separate research/referee pass; this triage job
does not promote it to a resolution candidate or change workflow status.

## Exact checks and next discriminating test

`triage-verify.py` uses Python integers and Fraction to regenerate
coefficients by descending polynomial division and independently evaluate
the moments by binomial expansion. It checks (1)-(3) at every internal
index for 4<=m<=20, verifies (4) at odd 1<=k<=17, and verifies (5) for
1<=p<=8 and odd 1<=k<=17. This tests formulas, not the infinite theorem.
It also checks the sign-changing low-index case (p,k)=(2,1): H=-16/225.
This guards against mistakenly applying Cauchy-Schwarz to the signed
measure when k is odd, or dropping the necessary base restriction p>=3.

One next test: independently reconstruct (2)-(5), audit strict positivity
and the map (p,k)<->(m,j), and determine whether this induction gives a
complete proof of the frozen conjunction. If it does, freeze the smallest
claim and evidence for a fresh referee, with latest-journal novelty still
requiring inspection before any release.
