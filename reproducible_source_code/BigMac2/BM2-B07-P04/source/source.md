## DM07-04 Exact Kasami cyclic-additive verification at `n=14`

Use the notation of Nagy--Vajda, *On a conjecture on the Kasami APN
function: reductions, structure theorems, a proof for k mod n in
{1,2,n-2,n-1}, and exhaustive verification for n<=13*,
arXiv:2608.18584v2.

In `GF(2^14)`, separately for `k=3` and `k=5`, define

`F(t)=t^(4^k-2^k+1)` and
`Delta={F(t)+F(t+1)+1 : t in GF(2^14)}`.

Prove or disprove the following finite assertion for every
`rho in GF(2^14)\{0,1}`:

`#{(x,y,z) in Delta^3 : x+rho*y+(1+rho)*z=0} = 2^25`.

The source proves all residue classes `k=+-1,+-2 (mod n)`, verifies all
admissible pairs through `n=13`, and proves symmetry between `k` and `n-k`;
therefore `k=3,5` are the two genuinely new representatives at `n=14`.

Any result must record the irreducible polynomial/basis used for the field,
verify `|Delta|=8192`, avoid floating point, and supply a reproducible full
count or transform certificate. A counterexample must give an exact encoded
`rho` and count. A positive finite verification is not a proof for arbitrary
`n` and must be described only as the `n=14` layer.

Primary source: arXiv:2608.18584v2, Conjecture 1.1, Proposition 4.1,
Section 12, Theorem 13.1.

