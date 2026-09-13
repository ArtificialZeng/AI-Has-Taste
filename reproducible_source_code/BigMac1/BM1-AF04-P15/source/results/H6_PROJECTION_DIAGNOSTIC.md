# Exact bounded diagnostic for scalar projections of the h6 construction

Using the six Rao--Rosenfeld \(\mathbb Z^2\) weights, every adjacent pair of
equal-length blocks in the generated prefix has a nonzero difference vector.
A primitive integer direction \((p,q)\) makes the scalar sums equal exactly
when it is the normalized perpendicular direction of this vector.

The local exact screen checked the first 30,000 symbols and all 225,000,000
adjacent block pairs.  All 12,176 primitive normalized directions satisfying
\(0\le p\le100\), \(|q|\le100\), and \(p>0\) or \(p=0,q>0\), are killed in
that prefix.  There are no survivors in this finite scope.

```sh
clang++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  src/h6_projection_screen.cpp -o experiments/h6_projection_screen
./experiments/h6_projection_screen --prefix 30000 --height 100
```

This is a diagnostic, not an impossibility theorem for all scalar projections:
directions above height 100 remain outside the run, and a finite survivor would
not by itself prove infinite avoidance.
