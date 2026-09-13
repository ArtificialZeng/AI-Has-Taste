# A certified no-go class for substitutions

Let \(h:\{0,1,2,3\}^*\to\{0,1,2,3\}^*\) be 2-uniform and prolongable on
one letter.  After relabeling the prolongable letter as 0, its first image
starts with 0, leaving seven unrestricted image positions.  Hence exactly
\(4^7=16{,}384\) morphisms must be checked.

The complete enumeration proves that every such fixed point contains an
abelian square ending no later than position 19 (exclusive, with positions
starting at zero).  Six morphisms attain this latest first endpoint.  Since
every abelian square is an additive square under every integer weighting, no
four-state 2-uniform endomorphism fixed point can solve the source problem.

The discovery evaluator uses prefix Parikh counts.  The independent Python
verifier uses direct `Counter` comparisons of the two blocks and enumerates all
seven free image positions anew.

```sh
python3 certificates/verify_uniform2_no_go.py \
  certificates/uniform2_no_go.json
```

This statement does not cover a coding from more hidden states, nonuniform
morphisms, or uniform modulus at least 3.
