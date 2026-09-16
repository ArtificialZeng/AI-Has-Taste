# Frozen source — win-00040-p03

## Source

Shiri Artstein-Avidan and Yaron Sadovsky, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v1 (2026), equations (1) and (2), contributions (iii)--(v).
Primary text: https://arxiv.org/html/2608.14909v1

## Immutable problem statement

Index sixteen nonnegative real variables by the vertices `v` of `{0,1}^4`. For every five-vertex set `S`, let `Vol(S)` be the normalized four-dimensional volume of its convex hull, and let `F` run over the eight facets of the four-cube. Prove or disprove, for every `x_v>=0`,

`(sum_{S subset {0,1}^4, |S|=5} Vol(S) prod_{v in S} x_v) * (sum_v x_v)^3 <= prod_F (sum_{v in F} x_v)`.

An exact nonnegative rational vector with strict reverse inequality is a complete counterexample. A proof must certify global nonnegativity of the resulting homogeneous polynomial. The source proves the preceding `n=4`/`d=3` layer; this is the next dimension.

