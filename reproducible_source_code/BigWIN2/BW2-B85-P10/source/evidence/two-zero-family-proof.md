# Exact proof for the length-two internal-zero family

Provenance: `win-00085-p10-research-831e68f0827d` (2026-09-11).

This proves the proper subfamily `T(p,0,0,q)`, `p,q>=1`.  It does not prove
the frozen assertion for arbitrary zero patterns or arbitrary spine length.
All polynomial coefficients below are exact integers or rationals.

## Domination polynomial

Write the four spine vertices from left to right, and put `r=p+q`.  At the
left endpoint, the contribution when its spine vertex is selected is

`U_p=x(1+x)^p`,

whereas when it is not selected all of its `p` leaves are forced, giving
`V_p=x^p`.  Define `U_q,V_q` analogously at the right endpoint.  If both
endpoint spine vertices are selected, the two middle vertices may be chosen
arbitrarily, with polynomial `(1+x)^2`.  In each of the other three endpoint
states, at least one of the two middle vertices must be chosen, with polynomial

`(1+x)^2-1=x(2+x)`.

Consequently

`D_{T(p,0,0,q)}(x)=x^2 H_{p,q}(x)`,                         (1)

where

`H_{p,q}(x)=(1+x)^(r+2)`
`             +x^p(2+x)(1+x)^q+x^q(2+x)(1+x)^p`
`             +x^(r-1)(2+x)`.                              (2)

This case split proves (1)--(2); it does not depend on finite testing.

Multiplication by `x^2` merely introduces two initial zero coefficients, so
it suffices to prove that `H_{p,q}` is log-concave.  Its degree is `r+2`.
Reversing its coefficient sequence preserves every log-concavity inequality.
The reversed polynomial is

`H*=(1+x)^(r+2)+(x+2x^2)((1+x)^p+(1+x)^q)+x^2+2x^3`.       (3)

By symmetry assume `p<=q` and put `u=q-p>=0`.  Define

`K_p=(1+x)^(p+2)+x+2x^2`,

`R_{p,u}=(1+x)^u K_p+x+2x^2`.

Then (3) has the nested exact form

`H*=(1+x)^p R_{p,u}+x^2+2x^3`.                             (4)

## Log-concavity certificate

We use the elementary convolution lemma: the product of two polynomials whose
coefficient sequences are nonnegative, log-concave, and have no internal zero
again has such a coefficient sequence.  For completeness, associate to a
sequence `c` its Toeplitz matrix.  Log-concavity plus absence of internal zeros
is equivalent to nonnegativity of all its order-two minors (adjacent minors
give the displayed inequalities, and monotonicity of consecutive ratios gives
the remaining minors).  Polynomial convolution is Toeplitz matrix
multiplication, whose order-two minors are nonnegative by the order-two
Cauchy--Binet formula.  This proves the lemma.

It remains only to audit the coefficients altered by the three sparse
additions in (4).  For fixed `h>=0`, set

`C(z,h)=z(z-1)...(z-h+1)/h!`, with `C(z,h)=0` for `h<0`,

and define

`k_h=C(p+2,h)+1_(h=1)+2*1_(h=2)`,

`r_h=sum_(i=0)^h C(u,i) k_(h-i)+1_(h=1)+2*1_(h=2)`,

`s_h=sum_(i=0)^h C(p,i) r_(h-i)+1_(h=2)+2*1_(h=3)`.        (5)

These are precisely the coefficients of `K_p`, `R_{p,u}`, and `H*`.  Starting
from the log-concave binomial row, adding `x+2x^2` can change only the minors
centered at `h=1,2,3`; adding `x^2+2x^3` can change only those centered at
`h=1,2,3,4`.  Thus it is enough to check

`k_h^2-k_(h-1)k_(h+1)` for `1<=h<=3`,

`r_h^2-r_(h-1)r_(h+1)` for `1<=h<=3`, and

`s_h^2-s_(h-1)s_(h+1)` for `1<=h<=4`.                      (6)

Substitute `p=a+1`, so `a,u>=0`.  Direct expansion of (5)--(6) gives a
polynomial in `a,u` with nonnegative rational coefficients, and at least one
positive coefficient, in every one of the ten cases.  For example, the three
`K_p` minors are respectively

`(a^2+11a+22)/2`,

`(a^4+10a^3+65a^2+200a+252)/12`,

`(a+1)(a+2)(a+3)(a^3+9a^2+14a+24)/144`.                   (7)

The exact reconstruction in `verify_two_zero_family.py` checks all ten
expansions coefficient by coefficient.  Their positive-monomial counts are

| stage | changed centers | monomial counts after `p=a+1` |
|---|---|---|
| `K_p` | `1,2,3` | `3,5,7` |
| `R_{p,u}` | `1,2,3` | `6,15,28` |
| `H*` | `1,2,3,4` | `6,15,28,45` |

As an explicit check on the largest expansion, if `Delta_4=s_4^2-s_3s_5`,
then `2880 Delta_4`, after `p=a+1`, is

`256a^8 + 64(16u+51)a^7`
`+16(112u^2+714u+1179)a^6`
`+16(112u^3+1089u^2+3537u+3825)a^5`
`+8(140u^4+1875u^3+9120u^2+19125u+14988)a^4`
`+16(28u^5+490u^4+3225u^3+10025u^2+14988u+8901)a^3`
`+8(14u^6+309u^5+2625u^4+10950u^3+23967u^2+26703u+12682)a^2`
`+8(2u^7+54u^6+579u^5+3115u^4+8979u^3+14393u^2+12682u+4560)a`
`+(u+1)(u^7+31u^6+395u^5+2565u^4+8484u^3`
`         +13484u^2+15360u+2880)`,                          (8)

which is strictly positive for `a,u>=0`.  The other nine expansions are
constructed by the same displayed formulas (5) and are shorter; the verifier
uses exact SymPy rationals and asserts coefficientwise nonnegativity.

It follows successively from (6), the convolution lemma, and (4) that `K_p`,
`R_{p,u}`, and `H*` are log-concave.  Reversal and (1) then show that
`D_{T(p,0,0,q)}` is log-concave for every `p,q>=1`.

## Independent and finite checks

The companion verifier compares (1)--(2) with the general tree DP for all 400
ordered pairs `1<=p,q<=20`, and with direct subset enumeration for all 36 such
pairs having total order at most 13.  It also checks every minor for
`1<=p<=q<=150` (11,325 pairs and 1,744,050 minors).  These finite checks guard
the transcription and implementation; the universal conclusion comes from
the case split and symbolic certificate above.
