# Fresh mathematical referee report

## Frozen scope

I reviewed the snapshot with digest
`41aa6272465aa28207998c11eef954c164073b3e59d81e633559cdfdc3470c81`.
Its recorded SHA-256 values agree with `claim.json`, the immutable source and
interpretation, and every listed evidence file.  The claim is exactly the
negative branch of the frozen problem: for the recurrence beginning at
\(a_0=0\), there is no \(n\) in
\(\{78{,}493{,}253,\ldots,100{,}000{,}000\}\) for which \(a_n=1\).
The open lower endpoint is handled correctly, and the claim makes no assertion
past 100,000,000.

## Reconstruction of the decisive argument

Both replay programs start from index zero and state zero.  Their exclusive
integer search bound is \(B=2{,}100{,}000{,}000\), and both construct all base
primes through
\(\lfloor\sqrt{B-1}\rfloor=45{,}825\): there are 4,746 of them and the
largest is 45,823.  Every composite \(m<B\) has a prime divisor at most
\(\sqrt m\), so marking by this complete base-prime set removes every
composite.  Starting each progression at the greater of the prime's square and
the first multiple in the segment does not remove a prime.

Path A obtains the base set by a dense Eratosthenes sieve, handles 2 separately,
and marks odd-only NumPy segments.  Its segment endpoint calculation covers
each odd integer below \(B\) once, without a gap or overlap that affects prime
enumeration.  Path B obtains its base set by trial division and marks all
integers in consecutive, irregular-width segments using scalar loops.  The
first segment begins at 2.  Thus the two paths independently enumerate the
primes in increasing order.  Each stops only on its 100,000,000th enumerated
prime, recorded as
\(p_{100000000}=2{,}038{,}074{,}743<B\).

For each enumerated prime, Path A replaces the positive sum \(s=a_{n-1}+p_n\)
by `s / (s & -s)`, while Path B repeatedly divides the sum by 2.  These are
independent exact implementations of \(s/2^{v_2(s)}\).  Each checks unsigned
64-bit addition for wraparound.  The largest state is 2,037,477,755 and every
prime processed is below 2.1 billion, so the corresponding sums are also far
below the unsigned 64-bit limit.  Induction on the increasing prime stream
therefore identifies the computed state after step \(n\) with the defined
integer \(a_n\).

The hit test is executed for every recurrence step, not only at checkpoints.
Both complete records contain precisely the indices

`1, 2, 5, 12, 14, 20, 75, 33900, 78493252`.

The last hit has
\(p_{78493252}=1{,}579{,}691{,}809\),
\(a_{78493251}=567{,}791{,}839\), and sum \(2^{31}\).  There is no hit after
that index through 100,000,000.  The paths agree on all 100 million-step
checkpoints, the full structured hit records, the maximum state, the terminal
state \(a_{100000000}=1{,}626{,}692{,}547\), and the per-step tuple-stream
FNV-1a digest `dff8f7323f83836a`.  I treat the digest only as an integrity
cross-check; exhaustiveness follows from the inspected enumeration and replay
loops.

## Checks performed in this review

- I recomputed all frozen SHA-256 file digests and found no mismatch with the
  snapshot.
- I reran Path A from zero through index 100,000,000 with a new odd-segment
  capacity of 3,141,593.  The run found the same nine hits, terminal state,
  maximum state, 100 checkpoints, and final stream digest.  Its temporary JSON
  SHA-256 was
  `a7e247bbd4c71b9736cfa718c45c4577f2b9f6f580e26c69c75348fb90005868`.
- I separately reran Path B from zero through index 100,000,000 with a new
  full-integer segment width of 1,777,777.  It produced the same decisive data;
  its temporary JSON SHA-256 was
  `b25f687674e51ffc8fda77e17df12bb3012c1423ae38d4d3bca0d52d85487261`.
  The frozen comparison program strictly compared these fresh outputs and
  reported agreement, 100 checkpoints, nine complete hits, and an empty hit
  list on the target interval.
- As a separate prime-index check, I used SymPy 1.14.0's exact `isprime` and
  `primepi` routines on every prime recorded in the 100 frozen checkpoints.
  All 100 values were prime and each satisfied \(\pi(p)=n\).  In particular,
  the lower-frontier and terminal primes have prime counts 78,493,252 and
  100,000,000 respectively.
- I compared the default, anchor, and altered-segment records.  The two default
  paths have identical hit and checkpoint arrays; the altered-segment records
  have the same arrays; and the anchor records agree with the full-run prefix
  and add the exact nonperiodic endpoint checkpoint at 78,493,252.

## Scope and contribution assessment

The computation proves the universal finite exclusion requested by the
original source, rather than a sampled or probabilistic substitute.  It is
anchored at \((0,a_0)=(0,0)\), independently reconstructs prime indices and
recurrence checkpoints, and supplies inspectable code and deterministic
records.  Reproducing the prior endpoint event is an additional anchor, not an
assumption.  The claim is appropriately described as a resolution of this
finite computational task and does not make a priority claim, an infinitude or
last-occurrence claim, or a claim for any larger index.  External OEIS context
in `problem.md` is not needed for correctness of the exclusion.

I found no unresolved mathematical or computational gap within the frozen
scope.  The NumPy and Numba dependencies are disclosed and do not make the
calculation opaque: both algorithms are short, inspectable, separately
implemented exact replays, and their key prime indices were additionally
checked by an exact independent library implementation.

## Verdict

**Accept.**  The frozen `resolution-paper` claim is correct at its exact stated
scope, resolves the original problem's negative branch, and has adequate
reproducible exhaustive evidence.
