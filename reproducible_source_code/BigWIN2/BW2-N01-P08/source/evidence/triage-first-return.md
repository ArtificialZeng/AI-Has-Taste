# First-return reduction found at triage

Job: newwin-00001-p08-triage-3c7429bdb0aa. Date: 2026-09-12.
This is a mathematical lead with a derivation, not an independently accepted
resolution or a novelty claim.

Fix m>=2. Write height h=y-mx, so N adds 1 and E subtracts m. Let
F(z,u,t)=1+sum_(n>=1,k,j) a_(n,k,j) z^n u^k t^j, where a counts the
literal paths of source.md by east steps, NE factors, and NNE factors.

Every nonempty excursion has a unique decomposition

    N P1 N P2 ... N Pm E P_(m+1),

with all Pi excursions for the same steps. The distinguished E is the first
return to height zero. Before that E, take the last upward departure from each
height 0,...,m-1. These are the displayed N steps in order; their intervening
subwords stay above their respective starting levels and return to them.
The remaining suffix is P_(m+1). This also gives the inverse construction.

Every nonempty Pi starts with at least m north steps and ends in E. As m>=2,
prepending an N to Pi introduces no additional NNE factor at its beginning.
The only factors not contained within the components end at the distinguished E:

| Condition | Extra peaks | Extra NNE | Component weight |
|---|---:|---:|---|
| Pm nonempty | 0 | 0 | F^m(F-1) |
| Pm empty, P_(m-1) nonempty | 1 | 0 | u F^(m-1)(F-1) |
| Pm and P_(m-1) empty | 1 | 1 | ut F^(m-1) |

Thus the proposed identity is

    F = 1 + z F^(m-1) [F(F-1) + u(F-1) + ut].                 (GF)

Checks: u=t=1 gives F=1+zF^(m+1); t=1 gives
F=1+zF^m(F-1+u). The argument explicitly uses m>=2 and does not
give the ordinary m=1 equation by substitution.

Put Y=F-1. Then

    Y = z (1+Y)^(m-1) [Y(1+Y)+u(Y+t)].

Formal Lagrange inversion over Q[u,t] gives, for n>=1 and 1<=k<=n,

    W^(m)_(n,k)(t)
      = (1/n) C(n,k) [v^(k-1)] (1+v)^(mn-k) (v+t)^k
      = (1/n) C(n,k) sum_(j=1)^k C(k,j) C(mn-k,j-1) t^j.   (CF)

The extraction comes from choosing k factors u(v+t) out of n factors
v(1+v)+u(v+t). The residual factor v^(n-k) lowers the coefficient
index from n-1 to k-1. Here mn-k>=k, so all displayed coefficients
are positive, the degree is k, and zero is a simple root if this formula holds.

Let V_(r,k) denote the *ordinary* Dyck polynomial from Wang--Zhang,
arXiv:2309.05903v1, Theorems 1.1 and 1.2 (recalling Bóna et al.).
Their coefficient formula, applied at r=mn+1, yields

    W^(m)_(n,k)(t)
      = C(n-1,k-1) / C(mn+1,k-1) * V_(mn+1,k)(t).         (R)

The scalar is strictly positive; r>=2k+1 lies within their nonexceptional
range. Their real-rootedness theorem would therefore settle the frozen
claim once the counting derivation has been fully checked. The potentially
new step is (GF)/(CF), not the known real-rootedness of V.

Next decisive test: attack the uniqueness and cross-boundary factor claims
in the decomposition, check the formal extraction for all parameter boundaries,
and verify the exact scope and prior occurrence of (CF)/(R). If those checks
succeed, a research worker can freeze a complete resolution claim for fresh
mathematical review. Finite coefficient agreement is only corroboration.
