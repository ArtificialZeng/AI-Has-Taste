# Sextic Jacobi bound and finite certificate

This note proves the frozen assertion in source.md, under the precise reading
in problem.md. It makes no priority claim.

## The analytic count

Let $p\equiv1\pmod {12}$, choose a primitive root $g$, and let
$\chi(g)=\zeta_6$. Put $C_i=g^i\langle g^6\rangle$ and

$$
S_p=(1,5)_6+(5,1)_6,\qquad
(i,j)_6=\#\{x\in C_i:1+x\in C_j\}.
$$

Because $-1=g^{(p-1)/2}\in C_0$, replacing $x$ by $-a$ shows that
$S_p$ is exactly the number of parameters witnessed by this fixed sextic
character. In particular, $N_p\ge S_p$.

Extend every multiplicative character, including the principal character
$\varepsilon$, by zero at zero. For $t\in\mathbb F_p$,

$$
1_{C_i}(t)=\frac16\sum_{r=0}^5\zeta_6^{-ir}\chi^r(t).
$$

Writing $J(\alpha,\beta)=\sum_t\alpha(t)\beta(1-t)$, expansion of the two
cyclotomic numbers gives

$$
36S_p=\sum_{r,s=0}^5 c_{r-s}J(\chi^r,\chi^s),\qquad
c_d=\zeta_6^d+\zeta_6^{-d}=(2,1,-1,-2,-1,1)_d.
$$

Here the substitution $t=-x$ introduces no factor because $\chi(-1)=1$.
The elementary Jacobi identities needed below are

$$
J(\varepsilon,\varepsilon)=p-2,\quad
J(\varepsilon,\alpha)=J(\alpha,\varepsilon)=-1,\quad
J(\alpha,\alpha^{-1})=-\alpha(-1)=-1
$$

for nonprincipal $\alpha$. If $\alpha,\beta,\alpha\beta$ are all
nonprincipal, then $|J(\alpha,\beta)|=\sqrt p$. For completeness, the last
fact follows by choosing a nontrivial additive character, using
$|G(\gamma)|^2=p$ for nonprincipal $\gamma$, and expanding
$G(\alpha)G(\beta)=J(\alpha,\beta)G(\alpha\beta)$. Both identities follow
directly by grouping the defining sums by the ratio of their nonzero
variables and by their sum, respectively.

The $(0,0)$ term is $2(p-2)$. On either principal axis,
$\sum_{r=1}^5c_r=-2$, so the two axes contribute $4$. For the five pairs
$r,s\ne0$ with $r+s\equiv0\pmod6$, their coefficient sum is

$$
c_2+c_4+c_0+c_2+c_4=-2,
$$

and hence their contribution is $2$. The remaining 20 pairs have
$r,s,r+s\ne0$, and the sum of the absolute values of their coefficients is
exactly $28$. Consequently

$$
36S_p=2p+2+E_p,\qquad |E_p|\le28\sqrt p,
$$

and therefore

$$
\boxed{S_p\ge \frac{p+1-14\sqrt p}{18}}.
$$

For every integer $p\ge194$, the numerator is positive: after squaring the
positive sides this is $(p+1)^2>196p$, true at $p=194$, and the difference
$p^2-194p+1$ is strictly increasing thereafter. Thus $N_p>0$ for every
eligible prime in this range.

## Exact finite remainder

The integer-only program evidence/jacobi_bound_check.py enumerates all primes
$p<194$, verifies primitive roots from the prime divisors of $p-1$, builds
complete discrete-log tables, and checks the residue classes of $a$ and
$1-a$ modulo 6. For every eligible $p\ge37$, one replayable certificate
$(p,g,a,\log_g(a)\bmod6,\log_g(1-a)\bmod6)$ is:

| $p$ | $g$ | $a$ | two residues |
|---:|---:|---:|:---:|
| 37 | 2 | 18 | 5, 1 |
| 61 | 2 | 18 | 1, 5 |
| 73 | 5 | 15 | 1, 5 |
| 97 | 5 | 14 | 5, 1 |
| 109 | 6 | 11 | 5, 1 |
| 157 | 5 | 61 | 1, 5 |
| 181 | 2 | 18 | 5, 1 |
| 193 | 5 | 45 | 1, 5 |

This list is complete because these are exactly the primes congruent to 1
modulo 12 in $[37,194)$, as the same program verifies by exact trial
division.

Finally, $N_{13}=0$ has a short complete discrete-log certificate. With
primitive root $2$, the nontrivial characters satisfying $\chi(-1)=1$ have exponents
$k=2,4,6,8,10$ in $\chi(2)=e^{2\pi i k/12}$. Exponents $4,6,8$ cannot
take the values $\zeta_6^{\pm1}$. For $k=2,10$, the two needed logarithm
classes modulo 6 are $1$ and $5$, whose elements are respectively
$\{2,11\}$ and $\{6,7\}$. Direct subtraction gives
$1-\{2,11\}=\{12,3\}$ and $1-\{6,7\}=\{8,7\}$, so no element in one class
has its complement in the other. The program independently enumerates all
five allowed nontrivial characters and returns the empty set.

Combining the analytic range, the complete finite remainder, and the
fixed-parameter equivalence recorded in problem.md proves the original
quandle-ring assertion and the stated uniqueness of $p=13$.
