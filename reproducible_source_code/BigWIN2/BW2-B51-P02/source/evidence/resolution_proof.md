# Exact value of the connectivity-code number of `C_3 square C_4`

## Claim

For the graph `H=C_3 square C_4` interpreted in `problem.md`,

\[
m(H)=16.
\]

## Upper bound

Fix any vertex `v`.  Map each codeword `A` to its restriction
`A intersect delta_H(v)`.  If two distinct codewords `A,B` had the same
restriction, then `A triangle B` would contain no edge incident with `v`.
The vertex `v` would be isolated in the spanning subgraph
`(V(H),A triangle B)`, contrary to connectivity.  The restriction map is
therefore injective.  Since `H` is 4-regular, its codomain has
`2^4=16` members, so `m(H)<=16`.

## A 16-word construction

Number `(i,j)` by `4i+j`.  Number the 24 edges as follows:

- edge `4i+j` is `{(i,j),(i+1 mod 3,j)}` for `0<=i<3`, `0<=j<4`;
- edge `12+4i+j` is `{(i,j),(i,j+1 mod 4)}` for the same ranges.

Interpret a six-digit hexadecimal integer as a 24-bit edge-incidence mask,
with edge `e` represented by bit `e`.  Let

\[
g_0={\tt 470c7f},\qquad g_1={\tt 296bf4},\qquad
g_2={\tt fb304a},\qquad g_3={\tt 17e0e8}.
\]

For `a in {0,...,15}`, define `W_a` to be the bitwise XOR of those `g_b`
for which bit `b` of `a` is one.  The following table gives, for every
nonzero `a`, the mask of `W_a` and eleven edge indices contained in `W_a`.
In each row those eleven edges form a spanning tree of `H`.

| `a` | mask | spanning-tree edge indices |
|---:|:---:|:---|
| 1 | `470c7f` | 0,4,16,1,5,17,2,6,18,22,3 |
| 2 | `296bf4` | 8,4,16,19,5,7,9,21,11,13,6 |
| 3 | `6e678b` | 0,8,19,3,7,18,14,22,17,13,21 |
| 4 | `fb304a` | 12,1,13,16,17,19,6,3,21,22,20 |
| 5 | `bc3c35` | 0,12,4,19,13,20,23,18,10,5,11 |
| 6 | `d25bbe` | 8,12,4,20,23,1,7,11,22,17,14 |
| 7 | `9557c1` | 0,8,12,16,20,23,7,18,6,10,14 |
| 8 | `17e0e8` | 15,3,14,7,18,13,6,17,5,16,20 |
| 9 | `50ec97` | 0,15,4,11,14,20,7,22,2,13,1 |
| a | `3e8b1c` | 8,15,4,20,3,11,9,21,18,2,17 |
| b | `798763` | 0,8,15,16,19,20,1,21,6,10,22 |
| c | `ecd0a2` | 12,15,1,14,5,21,22,7,23,18,19 |
| d | `abdcdd` | 0,12,15,4,16,19,11,14,17,10,21 |
| e | `c5bb56` | 8,12,15,4,23,1,9,13,22,2,18 |
| f | `82b729` | 0,8,12,15,23,9,13,3,5,10,17 |

Thus every `W_a` with `a!=0` is connected and nonempty.  In particular the
16 masks `W_a` are distinct: if `W_a=W_b`, then
`W_(a XOR b)=W_a XOR W_b=0`, which is impossible for `a!=b`.  Moreover, for
distinct `a,b`,

\[
W_a\mathbin{\triangle}W_b=W_{a\mathbin{\mathrm{XOR}}b},
\]

and the right-hand side is connected by the table.  Hence the 16 masks form
a connectivity code, proving `m(H)>=16`.  Together with the upper bound this
gives `m(H)=16`.

## Exact replay

`linear_witness.json` serializes the labels and generators.
`spanning_tree_certificate.json` serializes the table.  The separate script
`verify_linear_witness.py` regenerates the graph from coordinates, reconstructs
all 16 masks, checks all 12 local label ranks, validates every listed spanning
tree, and performs a fresh graph traversal for all 120 unordered pairwise
differences.  Its recorded run is `verify_linear_witness.log`.

Known proof gaps: none.
