# Frozen source — win-00040-p04

## Source

Nikola Zlatanov, *Beyond Minimum Distance: The Optimal Leading Coefficient in the High-SNR Error-Probability Expansion for AWGN Spherical Codes*, arXiv:2608.25805v1 (2026), equations (27), (30), (35), Proposition 5, Conjecture 1.
Primary text: https://arxiv.org/html/2608.25805v1

## Immutable problem statement

For a seven-point unit spherical code `C` in `R^4`, let `rho_e(C)` be the ordered-pair correlation and use the orthoplex optimum `rho*_(7,4)=0`. Define

`G_gamma(C)=sum_e exp(gamma*(rho_e(C)-rho*_(7,4)))`,

`V_gamma(7,4)=min_C G_gamma(C)`, and `K*_(7,4)=lim_{gamma->infinity} V_gamma(7,4)` as in the cited paper.

Prove or disprove `K*_(7,4)=24`. This is Conjecture 1 at the smallest nonempty intermediate parameter `(n,k)=(4,3)`. A proof needs a global liminf lower bound 24; a disproof needs a rigorously feasible SNR-indexed code family with limsup soft-packing energy strictly below 24. Numerical optimization alone is not a resolution.

