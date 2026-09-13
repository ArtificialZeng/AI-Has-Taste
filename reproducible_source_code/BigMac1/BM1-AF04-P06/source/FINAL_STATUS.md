# CERTIFIED_FINITE_RESULT

## Conclusion

For \(\zeta=e^{2\pi i/105}\), there are exactly two affine--Galois orbits of
nonempty inclusion-minimal vanishing subsets of distinct 105th roots at weight
20.  Canonical representatives are

\[
\begin{aligned}
\{&0,1,3,9,11,24,26,30,41,42,45,46,61,63,71,72,76,84,87,93\},\\
\{&0,1,3,11,12,16,24,33,41,42,45,46,54,63,71,75,76,84,86,87\}.
\end{aligned}
\]

Their orbit sizes are 210 and 315, respectively, with stabilizer sizes 24 and
16.  Together with the seven reproduced lower-weight orbits, they are exactly
the nine minimal affine--Galois orbits of weight at most 20.

## Certificate

The seven-fiber lemma reduces vanishing to equality of seven exact subset sums
of 15th roots.  The finite enumeration covers all 1,209,813 normalized
vanishing tuples of total weight at most 20.  Each contains one of 1,331 affine
images of the nine verified minimal representatives; the unblocked count is
zero.  The manifest SHA-256 is
`886b29e4c3f149b66f9ce6f9a0ad1ada63a31f08194af4495fd400d51f63519c`.

The release verifier uses only the Python standard library, imports neither
discovery nor builder code, reconstructs the cyclotomic arithmetic and affine
orbits, checks inclusion-minimality by meet-in-the-middle sums, and independently
replays the complete enumeration.  Destructive-input tests pass and fail
closed.

## Reproduction

Fast test:

```text
python3 tests/test_verifier_fail_closed.py
```

Full independent verification:

```text
python3 certificates/verify_weight20.py certificates/weight20_certificate.json
```

Expected decisive fields are `status=VERIFIED`,
`normalized_vanishing_tuple_count=1209813`, and
`unblocked_tuple_count=0`.

Clean manuscript build:

```text
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Independent audit and publication gates

- Baseline through 19 reproduced exactly.
- Discovery and certification use different routes.
- No-import verifier replay passed.
- Fail-closed mutation tests passed.
- Second novelty search completed and recorded with dated limitations.
- Four citations individually verified; BibTeX and `.aux` are consistent.
- LaTeX audit and clean build passed.
- All six final PDF pages were visually inspected.
- Release manifest is generated and independently reverified at handoff.

## Limitations

This finite theorem concerns subsets, so roots are distinct and coefficients
are 0 or 1.  It excludes the empty set, includes weight 20, and makes no claim
about weights 21 and above, multisets, general integer coefficients, or the
complete unbounded conductor-105 classification.  The novelty conclusion is a
dated database-bounded search result, not proof against unindexed work.

No Lean or other proof assistant was used.
