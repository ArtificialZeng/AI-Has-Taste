# Counterexample-hunter / breaker notes

## Attacks performed

1. **Equality endpoint:** checked that \(p=i=3\) survives division by \(3!\)
   exactly for \(n\bmod9\in\{0,1,2\}\).  Treating all numerator factors of 3
   as surviving would create false coverage.
2. **Strong-family deformation:** for \(n=3^m+1\), base-3 Lucas digits imply
   \(3\mid\binom nj\) for every \(2\le j\le n/2\); the prominent strong-form
   family therefore cannot yield a weak counterexample.
3. **Evaluator independence:** scanner Lucas predicates were compared with a
   verifier using Legendre valuations and with direct arbitrary-precision gcds
   through \(n=2000\).
4. **Input attacks:** missing-field, duplicate-key, and non-null-result JSON
   fixtures must all be rejected before enumeration.
5. **Boundaries:** \(n=8\), \(j=4\), odd \(n\), even \(n\), and \(j=n/2\) are
   not pruned.
6. **Frozen-release attacks:** a separate binder was run from an external cwd
   in Python normal and `-O` modes.  Changed endpoint, source hash, candidate
   count (a false-null summary), truncated strict output, duplicate certificate
   field, and duplicate binding field all exited nonzero.

## Surviving falsification route

The full conjecture can still fail for \(n>10^8\) at \(i=3\), or at any
unsettled \(i\ge4\) outside known partial ranges.  The finite computation gives
no probabilistic evidence weight to an infinite extrapolation.
