# Certified A114216 recurrence frontier through 100 million

Let `p_n` be the `n`th prime, let `a_0=0`, and for every `n>=1` define

\[
a_n=\operatorname{oddpart}(a_{n-1}+p_n),
\]

where `oddpart(m)` is the largest odd divisor of the positive integer `m`.

Either find an integer `n` with

\[
78,493,252<n\leq100,000,000\quad\text{and}\quad a_n=1,
\]

or prove by a reproducible exhaustive exact computation that no such index
exists.  A negative result is only a finite exclusion, not evidence that the
sequence has a last occurrence.  The certificate must reconstruct prime
indices and recurrence checkpoints independently; a single opaque run is not
sufficient.

Sources: OEIS A114216 for the definition and former frontier; user bibliography
row 32 for the certified occurrence at `n=78,493,252`.
