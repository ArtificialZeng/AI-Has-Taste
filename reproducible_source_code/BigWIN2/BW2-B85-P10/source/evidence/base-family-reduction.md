# Exact reduction for the first internal-zero family

Let `p,q >= 1` and put

`F_m(x) = x^m + x(1+x)^m`.

For the three-spine core `T(p,0,q)`, a split according to whether the middle
spine vertex is selected gives the exact identity

`D_{T(p,0,q)}(x) = (1+x) F_p(x) F_q(x) - x^{p+q}`.                 (1)

Indeed, selecting the middle vertex contributes `x F_p F_q`.  If it is not
selected, the two positive-leg endpoint blocks contribute `F_p F_q`, except
that the configuration in which neither endpoint spine vertex is selected
leaves the middle vertex undominated; all endpoint leaves are then forced,
and this unique excluded choice has weight `x^{p+q}`.  This proves (1).

As a transcription check, (1) was compared with the independently
brute-force-validated three-state DP in `caterpillar_small_search.py` for all
400 ordered pairs `1 <= p,q <= 20`; all full coefficient lists agreed.  The
case split above, rather than this finite check, is the justification of (1).

## Decisive symbolic test

Set `Q=(1+x)F_pF_q` and let `r=p+q`.  The factors of `Q` are log-concave, so
`Q` is log-concave.  Equation (1) changes only its coefficient of `x^r`, and
the inequalities centered at `r-1` and `r+1` only become easier.  Consequently
log-concavity of `D_{T(p,0,q)}` reduces to the single inequality

`(q_r-1)^2 >= q_{r-1} q_{r+1}`,                                      (2)

where `q_i=[x^i]Q`.

For a direct binomial attack, let `N=p+q+3`, and write `q_{N-t}=ell_t`.  If

`h_t = binom(p+q,t) + binom(p,t-1) + binom(q,t-1) + 1_{t=2}`

(with out-of-range binomial coefficients zero), then
`ell_t=h_{t-1}+h_t`.  Thus (2) is the explicit two-parameter inequality

`(ell_3-1)^2 >= ell_4 ell_2`.

The inequality is proved strictly for all `p,q>=1` in
`base-family-inequality-proof.md`; its exact symbolic audit is
`verify_base_family_inequality.py`.  This resolves only this subfamily.
