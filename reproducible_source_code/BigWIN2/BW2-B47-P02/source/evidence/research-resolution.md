# Research-pass resolution and exact certificates

Provenance: `win-00047-p02-research-4c4d58865add`  
Scope: exactly the six deleted-one graphs defined in `problem.md`.

## Theorem

The six graphs $G_a$, $a\in\mathbb F_7^*$, form exactly one
graph-isomorphism class.  The lexicographically ordered graph $G_1$ in
`evidence/adjacency/G_1.adj` is the designated reproducible representative.
For every ordered pair $a,b\in\mathbb F_7^*$, an isomorphism is

\[
 \phi_{a,b}(\alpha,r,x)
   =\bigl(u\alpha,u^{-1}r,x\bigr),\qquad
 u=ba^{-1}\in\mathbb F_7^*.
\]

## Proof

Multiplication by $u$ bijects
$S_a=\mathbb F_7^*\setminus\{a\}$ with
$S_b=\mathbb F_7^*\setminus\{b\}$.  Multiplication by $u^{-1}$ bijects
the row labels, while the Hadamard coordinate $x$ is fixed.  Hence
$\phi_{a,b}:\Omega_a\to\Omega_b$ is a bijection.

For two vertices in one retained square, equality of slopes and inequality of
row labels are both preserved, so the $A_4$ adjacency relation is preserved.
For distinct slopes, the common-symbol formula in `problem.md` gives

\[
\begin{aligned}
K_{u\alpha,u\beta}(u^{-1}r,u^{-1}s)
 &=\frac{(u\alpha)(u\beta)(u^{-1}r-u^{-1}s)}
          {u\beta-u\alpha}\\
 &=\frac{\alpha\beta(r-s)}{\beta-\alpha}
  =K_{\alpha,\beta}(r,s).
\end{aligned}
\]

Thus the same Hadamard outer-product matrix $B_K$ is used before and after
the map.  Since $x,y$ are unchanged,
$(B_K)_{xy}=+1$ is also unchanged, so the $A_2$ relation is preserved.
The bijection therefore preserves adjacency in both directions and is a graph
isomorphism.  Taking arbitrary $a,b$ proves that all six graphs lie in one
class.  There is at least one graph, so the class count is exactly one.  No
unproved mathematical step remains in this scoped argument.

## Independent exact reconstruction

`evidence/verify_slope_scaling.py` is a dependency-free Python verifier using
only exact integer arithmetic modulo $7$.  It fixes the normalized order-8
Paley matrix explicitly and checks its Gram matrix.  For each deletion it
constructs the full graph twice:

1. by scanning all seven columns to find the unique equality
   $L_\alpha(r,c)=L_\beta(s,c)$, without using the closed formula for $K$;
2. by the closed formula for $K$.

It requires both edge sets to be equal, verifies simplicity and symmetric
adjacency, and finds 280 vertices, constant degree 160, and 22,400 edges in
each graph.  It then serializes all 36 ordered vertex permutations as lists of
280 target IDs and checks each map against every neighbor set.  Running

```text
python3 evidence/verify_slope_scaling.py --verify-existing
```

recomputes all objects in memory and requires every saved artifact to agree
byte-for-byte.  The successful deterministic summary is
`evidence/verification-summary.json`; the explicit permutations are in
`evidence/slope_scaling_certificates.json`.

The adjacency-list SHA-256 values are:

| graph | SHA-256 |
|---|---|
| $G_1$ | `a32c0282a6ea831e4805eb62cfb22e99e7fb0bec2b345da604d4ed6b28846cce` |
| $G_2$ | `7a1dfa786ef8b17d01a1fa4cabf150fe7276034c28397eb701bfec3ea5f9454e` |
| $G_3$ | `d3ed52a1e40015a2f6ac184be587eea4c995cc34a4f4858ca66265b55f6e5e4b` |
| $G_4$ | `87acd7617733888ca0739819f5674c0040505678d2e3eaa7ea37f927eaa8f795` |
| $G_5$ | `2cbc17369b87e113b74d5d3c6f4c31ca0aa347ab46e43f98d29ea7e65b3195f5` |
| $G_6$ | `a56f01040df43bd6f8957c2f3e53f5efe816e46c33067f430a4f73c6bedcc2a1` |

This research pass proposes a resolution candidate only.  Fresh mathematical
referee acceptance is still required by the workflow.
