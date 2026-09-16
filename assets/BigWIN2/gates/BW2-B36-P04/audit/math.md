# Fresh mathematical referee report

Job: `win-00036-p04-referee-0e19e5591da4`

Snapshot: `196ae7428cf276ea1334c195be4e735971bc434bb3c4af7865c569323682d0fc`

## Scope reviewed

The frozen source asks for one prime integer \(q\) with \(1<q<a_{22}\) and
\(q\mid a_{22}\), where \(a_0=1\) and \(a_{n+1}=a_n^2+2\).  The submitted
resolution-paper claim gives \(q=108099707\).  It does not claim a complete
factorization, any fact about the cofactor or later terms, or novelty.  Thus the
candidate has the full constructive scope of the original problem and does not
silently substitute a subsidiary claim.

I checked the SHA-256 digest of each of the ten files in the frozen snapshot.
Every file hash agrees with `audit/snapshot.json`.  I also recomputed the
canonical sorted compact JSON hash of its `files` mapping; it is the snapshot
digest displayed above.

## Reconstruction and independent checks

### Primality

I independently computed

\[
\left\lfloor\sqrt{108099707}\right\rfloor=10397,
\qquad
10397^2<108099707<10398^2.
\]

A fresh standard-integer loop tested every integer divisor \(d\) in the closed
range \(2\le d\le10397\), 10,396 divisors in all, and found
\(108099707\bmod d\ne0\) in every case.  If this positive integer were
composite, it would have an integer (indeed prime) divisor at most its square
root.  The exhaustive result therefore proves that \(q=108099707\) is prime.
This reproduces the method in
`evidence/a22-independent-trial-verification.py` without using the Pocklington
data; I separately executed that frozen verifier and it returned `PASS` with
largest tested divisor 10,397.

I also inspected and executed `evidence/verify_a22_certificate.py`.  Its exact
factorization checks are

\[
34361-1=2^3\cdot5\cdot859,
\qquad
q-1=2\cdot11^2\cdot13\cdot34361,
\]

and its modular-power and gcd assertions reproduce every row of the two-level
Pocklington certificate in `evidence/a22-certificate.md`.  The proof first
certifies 859 by trial division and 34361 by Pocklington, then certifies \(q\).
This is a second valid deterministic proof.  The independent exhaustive proof
above is already sufficient and avoids any possible circular use of the
intermediate prime.

### Divisibility and indexing

Starting afresh with \(r_0=1\), I applied exactly 22 transitions
\(r_{n+1}=(r_n^2+2)\bmod q\).  The resulting residues, indexed from 0 through
22, were

```text
1 3 11 123 15131 12747749 4130680 59509522
53448106 101159942 81091708 50080613 13474761
51643108 36226811 44888898 33268166 18262376
80442749 68864772 83683223 103702901 0
```

They agree entry-for-entry with both frozen verification scripts and the
certificate table.  Induction on \(n\), using the defining integer recurrence,
gives \(a_n\equiv r_n\pmod q\) for every \(0\le n\le22\).  Hence
\(a_{22}\equiv0\pmod q\).  There is no omitted transition or indexing shift.

### Properness

I independently recomputed

\[
(a_0,a_1,a_2,a_3,a_4,a_5)
=(1,3,11,123,15131,228947163).
\]

Thus \(1<108099707<228947163=a_5\).  The recurrence preserves positivity, and
for every positive integer \(x\), \(x^2+2>x\), so the sequence is strictly
increasing.  Consequently \(q<a_5<a_{22}\).  Together with primality and
divisibility, this makes \(q\) a proper prime divisor and proves \(a_{22}\)
composite.  No limiting argument, division, external data, or unexamined
degenerate case occurs.

## Source comparison and contribution

The supplied nearest-prior-result description concerns a reported factor of
\(a_{20}\) and explicitly does not assert a result for \(n\ge22\).  The bounded
search report did not find a published \(a_{22}\) factor, but access to the cited
paper and some databases failed.  I therefore draw no novelty or priority
conclusion from that search.  This limitation does not affect the frozen claim:
the claim expressly disclaims novelty, and its mathematical contribution is the
requested explicit certified factor resolving the original constructive task.
No cited research result is needed in the proof.

## Verdict

**Accept.**  The frozen candidate proves its exact full-scope resolution claim.
Its primality, divisibility, indexing, and strict proper-divisor inequality all
survive independent deterministic recomputation.  I found no mathematical gap
requiring revision and no unresolved issue within the claimed scope.
