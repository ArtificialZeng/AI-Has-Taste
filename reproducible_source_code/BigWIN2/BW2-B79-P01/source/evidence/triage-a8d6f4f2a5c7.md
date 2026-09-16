# Triage verification for `win-00079-p01-triage-a8d6f4f2a5c7`

This is screening evidence, not a proof, referee report, or novelty certificate.

## Frozen input and recovery check

- `source.md` has SHA-256
  `0106369cec2d01113c6dc3c4ff452985dbc82e092b29df12ad49a776946f7201`.
- Enumeration found exactly one `literature/*handoff*.md` file:
  `literature/triage-timeout-recovery-handoff.md`. Its stated hashes for
  `source.md`, `problem.md`, `checkpoint.md`, and
  `evidence/triage-014f8020790a.md` all matched the live pre-update files.
  The handoff was treated as a lead and checked independently.

## Primary-source check

The official arXiv v1 HTML at
<https://arxiv.org/html/2609.04258v1> was inspected on 2026-09-10.
Proposition 2.1 states that all vertices are ideal at
`alpha_0=arccos(1/3)`. Proposition 2.3 constructs the regular endpoint cube,
but its uniqueness assertion is only for `alpha>alpha_0` and its proof says
that endpoint uniqueness is not needed. Proposition 5.1 and Remark 5.2 again
restrict isometric uniqueness to `alpha>alpha_0`. Thus this paper neither
proves nor disproves the frozen endpoint claim.

The limited negative literature search documented in
`evidence/triage-226b85b4cb78.md` was not repeated as a claim of exhaustiveness;
it does not certify openness, novelty, or priority. The appropriate source
status is `new-question`.

## Independent exact check

A fresh exact `python3`/SymPy calculation formed the 8-by-8 symmetric matrix
whose diagonal entries are `1`, whose four opposite-pair entries are `-5/3`,
and whose remaining off-diagonal entries are `-1/3`. It returned

```
rank: 5
eigenvalues: -8/3 (1), 0 (3), 8/3 (4)
nullity: 3
exact_check: PASS
```

This independently confirms the rank and Lorentzian signature asserted in the
earlier evidence. The algebra in `evidence/triage-gram-check.md`, together with
the non-obtuse/intersection and irredundancy argument in
`evidence/triage-226b85b4cb78.md`, provides a bounded route forcing all four
opposite-facet products to `-5/3`.

## Admission boundary

The input is precise, the proposed delta beyond Proposition 2.3 is explicit,
and the remaining test is bounded. No complete proof is claimed at triage. The
next research pass must audit that equality of the spanning Gram configurations
defines a time-orientation-preserving Lorentz isometry and maps every oriented
halfspace, hence the entire intersection, to the Klein cube.
