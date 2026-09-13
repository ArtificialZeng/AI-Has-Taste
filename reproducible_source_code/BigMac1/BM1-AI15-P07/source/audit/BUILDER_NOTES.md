# Builder notes

The strongest locally complete endpoint is a finite theorem, not a resolution
of the conjecture: all valid triples with \(i=3\) and \(n\le10^8\) satisfy the
weak form.  Its proof consists of the exact Lucas reduction and exhaustive
enumeration in `proof/i3_finite_theorem.md`.

Separate exact structural lemmas L1--L6 prove \(i=1,2\), the transport
divisibility \(V_i(n)\mid\binom ji\) in a counterexample, a fixed-pair bound,
the prime-gap obstruction, and terminal-interval smoothness.  These lemmas do
not close the unbounded \(i=3\) stratum or any general \(i\ge4\) stratum.

No numerical observation is used to prove an infinite claim.
