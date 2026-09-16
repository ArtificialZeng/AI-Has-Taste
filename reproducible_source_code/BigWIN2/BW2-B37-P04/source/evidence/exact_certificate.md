# Exact dual-replay certificate through 100,000,000

## Certified statement

For the sequence fixed in `source.md` and interpreted in `problem.md`, exact
exhaustive computation gives

\[
  a_n\ne 1\qquad(78{,}493{,}252<n\le 100{,}000{,}000).
\]

This is only the requested finite exclusion. It makes no assertion for larger
indices or about whether the sequence has a last occurrence.

## Two independent paths

`path_a_numpy.py` builds its base primes with a dense full-integer
Eratosthenes sieve. It then processes odd-only segments represented by NumPy
Boolean arrays, marks an arithmetic progression for each odd base prime, and
extracts the surviving primes. Its recurrence uses `total & (-total)` to
obtain the exact power of two dividing each sum.

`path_b_numba.py` builds its base primes by trial division. It processes
irregular-width full-integer segments, including even candidates, and marks
multiples in scalar compiled loops. Its recurrence removes factors of two by
repeated division. It shares no executable code with path A.

Both use base primes through 45,823, namely every prime at most
`isqrt(2,100,000,000-1)`. In either segmented sieve, every composite below the
exclusive search bound 2,100,000,000 has a prime divisor no larger than its
square root and is therefore marked. Marking starts no earlier than the base
prime's square, so a prime is never removed. Hence the survivors, traversed in
increasing order, are exactly the primes in the searched segments. Each path
stops only after independently reaching its 100,000,000th survivor; both obtain

\[
 p_{100000000}=2{,}038{,}074{,}743<2{,}100{,}000{,}000.
\]

Starting with `(n,a)=(0,0)`, each survivor is fed once and in order into the
stated recurrence. Thus induction on the processed prime index proves that the
recorded state is the defined `a_n`. Arithmetic is unsigned 64-bit exact, with
an overflow test before every addition. The largest state encountered was
2,037,477,755, so the recorded run stayed far inside that range; the explicit
guards did not fire.

Each program records every occurrence of `a_n=1`, rather than sampling only at
checkpoints. The complete list from both paths is

`1, 2, 5, 12, 14, 20, 75, 33900, 78493252`.

In particular it contains no member of the target interval. Both paths also
reproduce the endpoint witness

`p_78493252=1579691809`, `a_78493251=567791839`, and
`1579691809+567791839=2147483648=2^31`.

## Comparison and reproducibility

The clean full runs agree on all 100 checkpoints at multiples of one million,
on the complete hit records (including prime, preceding state, sum, and power
of two), on the maximum state, and on the terminal tuple

`(n,p_n,a_n)=(100000000,2038074743,1626692547)`.

They also agree on the FNV-1a stream digest `dff8f7323f83836a`, computed from
every little-endian uint64 tuple `(n,p_n,a_n)`. This digest is an integrity
cross-check, not a collision-free mathematical proof; exhaustiveness rests on
the two inspectable enumeration/replay algorithms and their complete hit logs.
The separate anchor runs stop exactly at 78,493,252 and agree at 79 recorded
checkpoints and on all nine hits. A further full stress pair changes path A's
odd-segment capacity from 4,194,304 to 1,234,567 and path B's full-integer
segment width from 2,000,003 to 1,000,003; `stress_comparison.json` still gives
the same 100 checkpoints, complete hit list, and terminal digest. A clean
default rerun also reproduced both full JSON records byte-for-byte.

From the project directory, reproduce the decisive full comparison with:

```sh
python3 evidence/path_a_numpy.py --target 100000000 --output /tmp/a114216_full_a.json
python3 evidence/path_b_numba.py --target 100000000 --output /tmp/a114216_full_b.json
python3 evidence/compare_exact_runs.py /tmp/a114216_full_a.json /tmp/a114216_full_b.json --output /tmp/a114216_full_comparison.json
```

The scripts require Python 3, NumPy, and Numba. `full_comparison.json` binds
the exact full-run records by SHA-256 and reports an empty target-interval hit
list. Runtime is printed to standard output but excluded from the deterministic
records, so unchanged code and parameters reproduce their bytes exactly.
