# Proof audit

Audit date: 2026-08-30.  Role: Referee, run serially after Builder, Breaker,
and Certifier.  No sub-agent was used because the user required this Codex CLI
to be the sole research executor.

## Verdict

**PASS — certified finite result.**  Up to translation and multiplication by a
unit modulo 105, exactly two inclusion-minimal vanishing subsets have weight
20.  Together with the reproduced seven lower-weight orbits, they give exactly
nine orbits through weight 20.

## Dependency reconstruction

1. `problem/formal_statement.md` explicitly excludes the empty set, fixes
   distinct exponents, defines inclusion-minimality, and includes the endpoint
   20.
2. Exact vanishing is equivalent to a zero remainder modulo \(\Phi_{105}\).
   SymPy discovery and a standard-library reconstruction independently produce
   the same 48 by 105 matrix digest:
   `669ac026c32d1396ec85f4a7348a848918221d9a9c19598428011eefcfcc2744`.
3. The fiber lemma follows from
   \(\zeta_{105}=\zeta_7\zeta_{15}^{-2}\) and degree
   \([\mathbb Q(\zeta_{105}):\mathbb Q(\zeta_{15})]=6\).  It loses no data
   because the associated CRT map is bijective.
4. The builder enumerated every equal-valued seven-mask tuple with
   \(0\in S\) and \(|S|\le20\).  The independent verifier rebuilt the mask
   values by a different Gray-walk algorithm and reproduced all 1,209,813
   tuples and both stream digests.
5. The verifier reconstructs all affine images, requires the nine orbits to be
   disjoint, checks canonical representatives and orbit-stabilizer data, and
   obtains 1,331 distinct blockers.
6. Every representative vanishes exactly.  Discovery used a Gray-code scan for
   proper subsums; the release verifier independently uses meet-in-the-middle
   integer vector sums.  All nine representatives are inclusion-minimal.
7. Every normalized vanishing subset of weight at most 20 contains a verified
   blocker.  If that subset is minimal, containment forces equality.  This is
   the completeness step and closes the original question at weight 20.

## Independent replay

Command:

```text
python3 certificates/verify_weight20.py certificates/weight20_certificate.json
```

Observed result:

- status: `VERIFIED`;
- normalized tuples: 1,209,813;
- affine blockers: 1,331;
- unblocked tuples: 0;
- wall time: 84.67 seconds;
- maximum resident set size: 46,694,400 bytes.

The verifier imports neither `src/build_fiber_certificate.py` nor any discovery
program, uses only the Python standard library, binds the manifest by SHA-256,
and fails closed.

The completed source ZIP was then extracted into a new `/tmp` directory.  From
that clean tree, `latexmk` rebuilt the manuscript, the mutation suite passed,
and the full verifier again returned `VERIFIED` with 1,209,813 tuples, 1,331
blockers, and zero unblocked tuples (30.20 seconds wall time and 46,268,416
bytes maximum resident set size on that run).  No workspace cache or virtual
environment was required for the decisive replay.

## Adversarial checks

`python3 tests/test_verifier_fail_closed.py` passed.  The tests reject a wrong
conductor, unknown fields, a truncated digest, relative and absolute path
escape, a corrupted manifest binding, and a changed nonvanishing
representative.  The generic CNF/LRAT route did not finish within its resource
budget; no incomplete LRAT or CNF is retained or cited as mathematical
evidence.

## Scope and residual risk

- The theorem covers nonempty subsets of distinct 105th roots through weight
  20, with weight 20 included.
- It does not cover multisets, general integer coefficients, or weights 21 and
  above.
- This is an exact computational proof with an independently replayable finite
  certificate, not a proof-assistant formalization.
- All fatal and major entries in `proof/gap_ledger.md` are closed.

No proof assistant was used.
