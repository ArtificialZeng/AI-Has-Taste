# Dependency-boundary audit

Audit date: 2026-08-29.  Status: **PASS for the strict finite increment only**.

## Imported mathematical prerequisite

The project imports one necessary-condition chain from Scott D. Hughes's
`erdos647-proof-chain` at the immutable commit
`be657cf1b89aebb98bbb8117f29c0456a8435ac6`:

1. `Erdos647BridgeV1.lean`, theorem `erdos647_div_2520`, proves that a candidate
   above the stated small range is divisible by \(2520\).
2. `Erdos647ReductionChain.lean`, theorem
   `bridge_candidate_to_isErdos647`, converts the original prefix condition to
   the local divisor inequalities used by the bridge.
3. The same file's theorem `bridge_isErdos647_to_sieve` sends a candidate
   \(n=2520N\) to one of the residue classes surviving the twelve elementary
   congruence forms.
4. `Erdos647SieveCertificate.lean` defines the twelve coefficients, the four
   primes, \(M=46189\), and the survivor predicate, and checks that the
   survivor set has cardinality \(96\).

The fixed source inspected is linked directly in the bibliography and can be
viewed at the
[audited commit](https://github.com/scottdhughes/erdos647-proof-chain/tree/be657cf1b89aebb98bbb8117f29c0456a8435ac6).
The local verifier independently reconstructs the survivor set from those
displayed definitions, checks its cardinality is \(96\), and checks the full
\(96\times529\) pair table.  This independent enumeration is a consistency
check; it does not replace the imported all-candidate implication.

## Explicitly excluded dependencies

The finite increment does **not** use:

- the later split into \(55\) closed and \(41\) open residue classes;
- any problem-specific axiom for the \(41\) open classes;
- the later universal-closure table;
- a claim that a finite computation decides the infinite tail.

The decisive input uses all \(96\) elementary survivors.  A source search for
the open-residue assumption and for the 41-element set found no reference to
either in the local verifier, C replay source, input, pair generator, or
certificate.

## Earlier-prefix boundary

Benjamin Tordjman's public artifact at fixed commit
`f727ab831abd533d36260f36f0b3433d8db0715e` reports exclusion through

`9,174,471,185,880,000,000`.

This project inspected its source, pair data, two full logs, validation slices,
and exceptional factorizations, but did not rerun the full earlier scan.  The
locally decisive theorem is therefore only the strict interval

`9,174,471,185,880,000,000 < n <= 9,180,628,549,092,000,000`.

The larger statement beginning at \(24\) is a *reported combined computational
frontier* and inherits the earlier artifact's trust.  This separation is
stated in the abstract, theorem/corollary split, and scope section.

## Toolchain boundary

- New replay: Apple clang plus Python 3.14, exact integer arithmetic, and a
  deterministic signed-64-bit domain.
- Proof assistant: **not used locally**.  Lean 4 occurs only in the imported
  Hughes prerequisite.  Its residue-cardinality proof uses `native_decide`;
  the local verifier independently checks the same finite set.
- Randomness: none.  Miller--Rabin bases and Pollard--rho schedules are fixed.
- Network access: used for source/citation/novelty inspection only, not for the
  decisive replay.

## Decision

The dependency closure is adequate for terminal state `NEW_STRICT_BOUND` at
`9,180,628,549,092,000,000`.  It is not adequate for, and is not presented as,
a solution of Erdős Problem 647.
