# Decisive-code freeze

Freeze time: 2026-08-29 03:45:48 UTC.

The decisive verifier, C replay, adversarial harness, pair generator, input,
pair table, and canonical certificate are frozen at the hashes in
`verification/FROZEN_CODE_MANIFEST.sha256`.  Gate 5--6 may edit only
literature, audit, manuscript, status, manifest, and release-artifact files.
Any change to a frozen file invalidates all four decisive replays and requires
Gate 4 to be repeated.

Freeze check from the project root:

```text
shasum -a 256 -c verification/FROZEN_CODE_MANIFEST.sha256
```

At freeze time, the four normal/optimized/isolated decisive stdout logs were
byte-identical to the canonical certificate, SHA-256
`19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3`.
