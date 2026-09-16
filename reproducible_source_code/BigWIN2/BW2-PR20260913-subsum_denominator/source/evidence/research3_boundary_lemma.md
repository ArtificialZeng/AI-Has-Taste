# The first excluded degree: an infinite method obstruction

Job: `primary-20260913-subsum-denominator-research-077128f18f2f`.
This extends the pass-2 isolated boundary witness to every actual stage.
It is an auxiliary proved lemma, not a disproof of K_sharp_v1, H, or the
original denominator conjecture. No fresh referee has yet assessed it.

For n>=9 and t>=0 with s=n/2^t a positive integer, put

\[
A(x)=a_{s,t}(x)=D_{n-1}(x)
 \prod_{\ell=1}^{v_2(s)}(1+x^{s/2^\ell}),\qquad j=2n-1.
\]

The full ascending dyadic stage is encoded by the product above; its order
does not affect A. Define, with coefficients zero outside their support,

\[
T_j(a)=a_j^2-a_{j-1}a_{j+1},\qquad
F_{s,j}(v)=2T_j(a_{s,v}(1+x^s))-T_j(a_{s,v})-T_{j-s}(a_{s,v}).
\]

**Lemma.** There is a polynomial P(u) of degree at most 4n-2 such that
F_(s,j)(t+u)=P(u) for every integer u>=1, and

\[
F_{s,j}(t)-P(0)=-a_{2n-2}-2a_{2n-s-2}<0.
\tag{1}
\]

Consequently, for every integer h>4n-2,

\[
\Delta^h F_{s,j}(t)=(-1)^{h+1}(a_{2n-2}+2a_{2n-s-2}).
\tag{2}
\]

In particular every even h>=4n gives a negative forward difference.

**Proof.** The exponent of (1+x^i) in D_(n-1) is
e_i(n)=#{q>=0:2^q i<n}. Splitting off q=0 proves the exact identity

\[
e_i(2n)-e_i(n)=\mathbf1_{i<2n}.
\]

At the doubled start, all exponents through m=j+1=2n are affine at
subsequent doublings. To extrapolate back one step, each of these exponents
is decreased by one. This reproduces A's exponents for i<m, but gives -1
instead of 0 at i=m. No earlier-stage factor has degree m because s<=n.
Thus the extrapolated old series at u=0 is

\[
\widehat A(x)=\frac{A(x)}{1+x^{2n}}
          \equiv A(x)-x^{2n}\pmod{x^{2n+1}}.
\]

At all u>=1 the old series is, to this precision,
A(x) P_m(x)^u/(1+x^m), where P_m=product_(i=1)^m(1+x^i).
Each coefficient of degree r is a polynomial in u of degree at most r,
also with the shifted exponent u-1 at i=m. Substitution into the quadratic
definition of F gives P with degree at most 2j=4n-2.

The only changed old coefficient needed for F at u=0 is a_(j+1), which
increases by one when passing from the extrapolation to the actual A.
Expand the margin as

\[
F=T_j(a)+T_{j-s}(a)+4a_j a_{j-s}
       -2a_{j-1}a_{j-s+1}-2a_{j+1}a_{j-s-1}.
\]

Its coefficient of a_(j+1) is -a_(j-1)-2a_(j-s-1), proving (1).
The factor product_(i=1)^(n-1)(1+x^i) divides D_(n-1); its coefficients
are positive throughout degrees 0 through n(n-1)/2, since the integers
1,...,n-1 have every subset sum in that interval. For n>=9,
2n-2<=n(n-1)/2, so a_(2n-2)>0. This proves strict negativity.

The actual sequence differs from the polynomial sequence only at u=0,
by the discrepancy in (1). Every forward difference of P of order greater
than 4n-2 vanishes. The h-th difference of the sequence supported at u=0
is (-1)^h times its value there. This proves (2).

## Meaning and exact checks

The lemma proves that the polynomial degree bound and nonnegativity of
*all* forward differences cannot extend unchanged to 2n=j+1. It does not
claim that a Newton coefficient of order at most 2j is negative at this
excluded start. It makes no assertion about the sign of the actual margin
F_(s,j)(t). The starting-point hypothesis of K_sharp_v1 is 2n>j+1, so the
lemma supplies no counterexample to that hypothesis.

`research3_boundary_verify.py/.json` computes every actual stage for
9<=n<=32 at j=2n-1. It reconstructs the coefficients by logarithmic
derivatives, extrapolates the polynomial tail, and directly takes the
signed binomial sum of all 4n+1 actual margins at order 4n. These finite
checks supplement the proof and do not replace its universal argument.
