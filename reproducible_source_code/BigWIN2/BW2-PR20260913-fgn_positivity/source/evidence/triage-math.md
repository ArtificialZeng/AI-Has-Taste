# Bounded triage mathematics

Job: primary-20260913-fgn-positivity-triage-00acd6d3f130.
Date: 2026-09-13 (Asia/Shanghai). These are inspectable arguments from triage,
without independent referee acceptance or a novelty claim.

## Exact global certificate for the already-stated n=4 inequality

Put t=2H, a=2^t, b=3^t, and
q=rho_2+rho_2^2-rho_1^2-rho_1*rho_3. Direct Cramer's-rule expansion gives

Gamma_4^3=(1-rho_2)q/det(T_3),

where T_3=(rho_|i-j|) for 1<=i,j<=3. The denominator is positive definite's
determinant, and 1-rho_2>0. Substituting the covariance gives

F(t)=4q=9^t-8^t-2*6^t+4*4^t-2*2^t-1.

The ordered coefficients, at bases 1,2,4,6,8,9, are -1,-2,4,-2,-1,1,
with three sign changes. Thus F has at most three real zeros, counted
with multiplicity, by the exponential version of Descartes' rule.

For completeness, that standard rule has this short proof. If the coefficient
sequence of E(t)=sum c_i exp(lambda_i*t), lambda_i strictly increasing, has
no sign changes, E never vanishes. Otherwise choose lambda strictly between
two consecutive exponents at a coefficient sign change. The derivative of
exp(-lambda*t)E(t) has coefficients c_i*(lambda_i-lambda), with exactly one
fewer sign change. Induction and Rolle's theorem, counting multiplicities,
bound the number of zeros of E by its sign variations. If one posits more
zeros, apply Rolle on a finite interval containing them; no assumption about
zeros at infinity is needed. This is a standard lemma, not a new theorem.

Exact evaluations give

- F(1)=F(2)=0 and F(3)=24;
- F'(1)=2*log(27/16)>0;
- F'(2)=18*log(243/256)<0.

Consequently there is a third zero in (2,3), since F is negative just to
the right of 2. The three-zero bound leaves no zeros in (1,2). Since F
is positive just to the right of 1, F(t)>0 throughout (1,2). Thus q>0.
Together with 2022 Proposition 2.11 (Gamma_4^2>Gamma_4^3 and Gamma_4^4>0),
this proves positivity of the whole n=4 row. The inequality q>0 was already
stated as 2025 Proposition 1; this argument supplies a global certificate
where that paper uses a graph. It does not resolve the original all-n claim.

## A structural reduction at n=5

Let N_5k be the determinant formed from T_4 by replacing column k-1 with
(rho_1,rho_2,rho_3,rho_4)^T. Exact symbolic expansion gives

N_53=q*K,  K=(1-rho_2)(1-rho_4)-(rho_1-rho_3)^2.

For U=Delta_1-Delta_5 and V=Delta_2-Delta_4, their covariance matrix is
2*[[1-rho_4,rho_1-rho_3],[rho_1-rho_3,1-rho_2]]. It is strictly positive
definite: the underlying five-increment covariance is strictly positive
definite and the two coefficient vectors are linearly independent.
Its determinant is 4K>0. Hence Gamma_5^3=q*K/det(T_4)>0.

The first coefficient Gamma_5^2 is positive by the conditional argument
below, now that the entire n=4 row is positive. The last coefficient
Gamma_5^5 follows from 2025 Proposition 2, whose explicit assumption of
positivity of the preceding row is now satisfied. Therefore the complete
n=5 case reduces to the one inequality N_54>0 for all 1<t<2.

The script records the exact 30-term exponential sum P(t)=16*N_54(t).
Its raw coefficient sequence has 18 sign variations; the three-zero argument
for n=4 does not by itself certify this new inequality. Exactly,
P(1)=P(2)=P'(2)=P''(2)=0 and
P'(1)=80*log(2)-48*log(3)=16*log(32/27)>0.
The exact cubic expression for P'''(2) is recorded in the JSON. Its sign
has not been certified here. The next test should deflate these endpoint
zeros and bound the resulting analytic function on the closed interval.

## A dependency correction to the handoff

The 2022 paper states unrestricted first-coefficient positivity in
Proposition 2.17, pp.13–14 (journal Proposition 6). Its final step writes
the residual covariance as

sum_{k=2}^n Gamma_n^k*(rho_{k-2}-rho_k)>0

and invokes only decrease of rho. Positive differences do not establish
positivity of a weighted sum with coefficients of unestablished sign.
This passage is rigorous under positivity of the previous row. Its
unconditional conclusion needs an additional argument, or an independently
verified source. This identifies a proof dependency, not a counterexample
or a claim that the published conclusion is false. For n=5 the dependency
is supplied by the n=4 certificate above.

## Reproduction and scope

Run `python3 evidence/triage_algebra.py`. The script checks the determinant
identities, exact exponential coefficients, endpoint values and derivative
identities using SymPy. The zero-count and positive-definiteness arguments
above require mathematical inspection; a successful script is not their
formal verification. No numerical sweep, interval certificate for N_54,
full-n proof, independent audit, or publishability decision is claimed.
