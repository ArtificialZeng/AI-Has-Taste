# Checkpoint

Job: `bigMac-00007-p04-research-a16ca3c16293`  
Phase: research, pass 1  
Decision: propose an exact finite resolution for fresh referee audit

## New exact evidence

- `source.md` remains unchanged, with SHA-256
  `ad1b1a9988509a06970cb4c361e84510b2f825f390b56d9ca9b8942bf080b8b1`.
- `evidence/verify_n14.c` is a self-contained, single-threaded, integer-only
  verifier. It uses the polynomial basis
  \(K=\mathbb F_2[\alpha]/(\alpha^{14}+\alpha^5+1)\), encoded by coefficient
  bits. Its Rabin check obtained \(X^{2^2}=\mathtt{0x0010}\),
  \(X^{2^7}=\mathtt{0x08c5}\), and
  \(X^{2^{14}}=\mathtt{0x0002}=X\) modulo the polynomial, with both required
  gcds equal to \(1\). Thus the modulus is irreducible. The program also
  verifies a full nonzero-element orbit for generator `0x0007`.
- For each of \(k=3,5\), the program enumerated all \(2^{14}\) inputs to
  \(\delta_k\), found exactly 8192 distinct outputs, and additionally checked
  that every image value has multiplicity exactly two.
- `evidence/n14_certificate.tsv` records all 16,384 exact Walsh coefficients
  for each \(k\) and all 16,382 exact normalized counts for each \(k\). Every
  nonzero-character correlation is exactly zero, hence every full character
  sum is \(8192^3=549755813888\), divisible by 16384, and every count is
  \(33554432=2^{25}\). Coverage parsing found 16,384 spectrum rows and 16,382
  count rows per \(k\), with no nonzero correlation or bad count.
- Internal checks include trace-pairing bijectivity, Parseval, direct character
  sums at nine fixed encoded coefficients per \(k\), and direct
  \(8192^2\)-pair enumeration at `rho=0x0002` and `rho=0x2000` for each \(k\).
  All four direct triple counts equal 33,554,432. The run transcript is
  `evidence/n14_run.log`.
- `evidence/audit_n14.c` is a separately structured checker. It certifies the
  modulus by excluding all 127 possible factors of degrees at most 7, uses
  carryless products plus polynomial long division, reconstructs both Delta
  sets, directly recomputes all 32,768 Walsh coefficients, parses and rechecks
  all 32,764 correlation rows via linear multiplication maps, and directly
  checks the held-out `rho=0x1555` and `rho=0x3ffe` for both \(k\)'s. Every
  comparison passed (`evidence/n14_audit.log`). Sanitized builds were clean,
  and a fresh producer run was byte-identical to the saved certificate.
- `evidence/n14_verification.md` supplies the exact certificate argument,
  scope limitation, reproduction commands, and decisive SHA-256 values.

## Remaining gap / obstacles

No mathematical or computational gap is known in this finite resolution.
NumPy was unavailable for the initially proposed independent implementation;
this operational limitation was bypassed by the separate exact C checker above
and is not used as mathematical evidence. The result has not yet received the
workflow's required fresh referee review, and it is not a result for arbitrary
\(n\) or a claim of priority.

## One next test

Have a fresh referee audit the exact scope in `claim.json`, independently check
the character-orthogonality reduction and field/coverage arguments, compile
and rerun both C programs, and verify the saved certificate hash and complete
row domains before accepting or revising the proposed resolution.
