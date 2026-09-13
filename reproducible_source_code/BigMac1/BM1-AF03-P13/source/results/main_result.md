# Main exact result

Under the actual-length repair forced by the source definition and functional
equation, the Ehrhart root-disk conjecture is false.

For the length-10 regular word
`epsilon LRLRLRLRLR`, the order polytope has dimension 24, disk center `-7`,
and radius `6`.  Exact reconstruction gives

```text
h* = [1,21,181,833,2241,3653,3653,2241,833,181,21,1]
```

and

```text
24! L(x-7) = 36 prod_{k=0}^6 (x^2-k^2) Q(x^2),
Q(y) = 385y^5+25789y^4+923223y^3+10769815y^2
       +70801492y+23924096.
```

A rational Rouché disk isolates one root of `Q` and lies strictly outside
`|y|=36`.  Independently, an order-ideal/multichain reconstruction and exact
Cayley--Routh count proves that `Q` has a nonreal conjugate pair outside that
circle.  Hence `L` has roots satisfying `|t+7|>6`.

The separately audited regular length-9 word `epsilon LRLRLRLRL` also violates
the corresponding disk.  This corrects the authors' unsupported reported
baseline under the same repaired convention; length 10 remains the main
theorem requested by the project.

No Lean, Coq, Isabelle, or other proof assistant was used.  The endpoints are
covered by exact standard-library Python verifiers, integer/rational
arithmetic, Rouché's theorem, and the Routh theorem.
