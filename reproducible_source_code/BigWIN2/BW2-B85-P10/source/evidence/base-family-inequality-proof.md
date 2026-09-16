# Exact proof for the first internal-zero family

Provenance: `win-00085-p10-triage-a175262e65a9` (2026-09-11).

This independently checks the algebraic lead in
`literature/supervisor-algebra-handoff-20260911.md`.  It proves only the
two-ended, one-internal-zero family `T(p,0,q)`, not the frozen universal
claim.

Let `p,q >= 1`, `r=p+q`, and `s=pq`.  Put

`F_m(x)=x^m+x(1+x)^m` and `Q(x)=(1+x)F_p(x)F_q(x)`.

The direct middle-vertex split in `base-family-reduction.md` gives

`D_{T(p,0,q)}(x)=Q(x)-x^r`.                                      (1)

Each of `1+x`, `F_p`, and `F_q` has a nonnegative log-concave coefficient
sequence with no internal zero, so their product `Q` is log-concave.  In (1)
only the coefficient in degree `r` decreases, by one.  The inequalities
centered in degrees `r-1` and `r+1` therefore get weaker, and all other
inequalities except the one centered in degree `r` are unchanged.  It remains
to prove

`(q_r-1)^2 >= q_{r-1}q_{r+1}`, where `q_i=[x^i]Q`.                (2)

Write `N=r+3`, `q_{N-t}=ell_t`, and first take the high-degree coefficients
`h_t` of `F_pF_q`.  Expanding its four summands gives

`h_t=C(r,t)+C(p,t-1)+C(q,t-1)+1_{t=2}`,

and multiplication by `1+x` gives `ell_t=h_{t-1}+h_t`.  Direct use of
Pascal's identity and

`C(p,2)+C(q,2)=C(r,2)-s`,

`C(p,3)+C(q,3)=C(r,3)-s(r-2)/2`

yields

`ell_2=(r^2+3r+6)/2`,

`ell_3-1=C(r+2,3)-s`,

`ell_4=C(r+2,4)-rs/2`.                                           (3)

Consequently the difference between the two sides of (2) is the monic
quadratic

`Delta_r(s)=(C(r+2,3)-s)^2`
`           -((r^2+3r+6)/2)(C(r+2,4)-rs/2)`.

Its discriminant with respect to `s` is exactly

`disc_s Delta_r = -r(r^2+3r+6)(r^3+7r^2+2r+8)/48`.              (4)

For `r>=2`, every factor after the minus sign in (4) is positive.  Hence the
discriminant is negative.  Since `Delta_r` is monic, it follows that
`Delta_r(s)>0` for every real `s`, in particular for `s=pq`.  Thus (2) is
strict and the domination polynomial of `T(p,0,q)` is log-concave for every
`p,q>=1`.

The companion exact symbolic verifier is
`verify_base_family_inequality.py`.
