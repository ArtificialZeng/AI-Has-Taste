# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen by snapshot
`2abe4780cf2ee63a3e3d3d055f8872c214ef674ae76f40ced8f5c85ef8e20c76`.
The claim is the negative statement only for the explicitly displayed set
\(\Gamma_{34}(A,B)\); it does not concern a larger equivalence group or other
length-34 qLPs.  **Verdict: accept.**

## Reconstruction of the decisive argument

The Gray map on the four fourth roots of unity has values
\((1,1),(1,-1),(-1,-1),(-1,1)\), hence is injective.  Therefore the two Gray
rows of a quaternary word \(X\) are both reversible exactly when
\(X_j=X_{-j}\) for every \(j\in\mathbb Z_{34}\).

Every ordered pair in the frozen orbit contains, in one coordinate or the
other, a word
\[
Z=\alpha c_r d_k(A^\varepsilon).
\]
If this coordinate had two reversible Gray rows, cancellation of the nonzero
phase and injectivity of conjugation would give
\[
A_{(j-r)k^{-1}}=A_{(-j-r)k^{-1}}\quad\text{for every }j.
\]
Putting \(u=(j-r)k^{-1}\) turns this into
\[
A_u=A_{a-u}\quad\text{for every }u,\qquad
a=-2rk^{-1}\pmod {34}.
\]
Because every unit modulo 34 is odd, \(a\) is one of the 17 even residues.
I independently checked the literal word in the frozen source.  For
\(a=0,2,\ldots,32\), respectively, the candidate table's failing indices
\[
1,0,10,1,0,0,3,1,1,2,0,0,0,3,1,0,1
\]
all give unequal symbols at \(u\) and \(a-u\).  Thus no allowed transform of
\(A\) has both Gray rows reversible.  Independent choices involving \(B\)
cannot repair that coordinate, and exchange only changes its position.  This
covers every quantified parameter and proves that no orbit pair has four
reversible Gray rows.

## Exact checks performed

- I recomputed all snapshot file hashes and the canonical snapshot digest;
  all ten frozen entries matched.  In particular, `source.md` retained SHA-256
  `b5060e42bc0335514d960c510d058cf3cf21058fdb1116b3f5cdb1e829da9d65`.
- A separate direct calculation enumerated all
  \(4\cdot34\cdot16\cdot2=4352\) allowed phase/shift/decimation/conjugation
  transforms of \(A\) and found zero reversible transforms.  It also checked
  the 17 reflection-axis witnesses and all 33 qLP lag equations exactly using
  fourth-root exponents.
- I ran the stand-alone census verifier.  It reconstructed all 1,183,744
  parameter tuples as 1,183,744 distinct ordered images, reproduced canonical
  orbit SHA-256
  `633befce04711dc130f011ee6ede35e32347be63a53719933e625545d270817e`,
  and recomputed every archived failure witness.  The compressed archive hash
  was
  `636a51bd42360d70e7b9d18805ce65ef2ac6e563df3ddfd9e1f5ceb5f1c38019`
  and the uncompressed stream hash was
  `95ee5c29a52d5d1974bc427532a9a45b006bf541f5394df6bd819a27f6f49be5`.
  The census is consistent with, but not needed to rescue, the paper proof.
- The generator-preservation calculation is correct: phases and shifts leave
  each PAF unchanged; \(d_k\) sends lag \(h\) to \(hk^{-1}\); conjugation
  conjugates the PAF sum and hence fixes its real value \(-2\); exchange swaps
  the summands.  The common-decimation and simultaneous-conjugation hypotheses
  used here match the frozen definition.

## Source comparison, scope, and contribution

I inspected the frozen official source PDF.  Its Section 7 says only that the
printed length-34 orientation is not reversible and explicitly states that an
orbit argument over a full equivalence group was not carried out; Appendix A
prints exactly the two frozen words.  The present result supplies an orbit
argument for the smaller, expressly defined \(\Gamma_{34}\), and the claim
prominently preserves that limitation.  It neither imports the binary
opposite-decimation operation nor represents the answer as a statement about
all qLP equivalences.

This is a short but complete, source-motivated finite-orbit resolution.  Its
17-axis obstruction is paper-checkable, while the exhaustive certificate
provides reproducible corroboration.  The frozen evidence supports the stated
nearest-result comparison, and the candidate makes no broader priority claim.
I found no mathematical, scope, or contribution gap requiring revision.
