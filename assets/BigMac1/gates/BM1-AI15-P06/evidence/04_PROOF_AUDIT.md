# Gate 5 proof and dependency audit

Date: 2026-08-29  
Terminal mathematical result: **PARTIAL_THEOREM**  
Frozen conclusion: every hypothetical eleven-point equilateral set in
\(\ell_1^5\) has at least \(19\) positive consecutive coordinate gaps,
equivalently at least \(24\) coordinate levels in total.

## Scope

The audit supports only the structural theorem above and the separate finite
box theorem for \(\{0,1,2,3,4\}^5\). It does not prove
\(e(\ell_1^5)=10\), construct eleven points, or exclude the strata
\(t\ge19\). The unreviewed exploratory file 'proof/t19_branch.md' is not
part of the frozen proof, manuscript, manifest, or source release.

## Frozen proof chain

| Layer | File / evidence | Disposition |
|---|---|---|
| Coordinate orders, ties, cut metrics, Parseval frame, Naimark and spectral deficit | 'proof/builder_notes.md', 'proof/structural_reduction.md', 'audit/referee_round1.md', 'audit/referee_round1_diff.md' | PASS |
| \(t=15\) endpoint split and singleton compression | 'proof/t15_dense_branch.md', 'audit/referee_round2_t15.md', exact checker | PASS |
| \(t=16\) zero-set compression | 'proof/t16_branch.md', Round 3 audits, exact checker | PASS |
| \(t=17\) rank-nine reciprocal-kernel obstruction | 'proof/t17_branch.md', Round 4 audits, exact checker | PASS |
| \(t=18\), 88-to-8 partitions, endpoint loss, \(R=10\) antichain | 'proof/t18_branch.md', SHA-256 2a50ff367e65652e43e58a44319a86fdff61e04ca41b106260e192c6ee3f20c9; 'audit/referee_round5_t18.md', SHA-256 ea272fe49fa614b6fce89a9893a1ed6c9a1f10ebfaf989cab4db07896a222da3 | PASS |

## Requested local edge cases

- **One-gap / \(h=1\) boundary.** The Naimark chain-length proof explicitly
  says that a coordinate with one positive gap satisfies the bound
  immediately. In singleton compression, \(|Z|=1\) gives a zero-dimensional
  kernel and rank ten, already contradicting \(R\le9\).
- **Strict positivity of the three coefficients.** In the private-direction
  lemma, a zero dependence coefficient would make its inner product with the
  omitted Naimark vector equal both zero and a strictly negative sum. Thus
  all three coefficients are strictly positive before strict block decrease
  is inferred.
- **Cut orientation and repetition.** Complementing a cut changes
  \(v_S\) only by sign. In the \(R=10\) proof, orientation away from an
  arbitrary reference label turns two cuts from a chain into nested or
  disjoint blocks. The inverse identity makes distinct copies intersecting
  and incomparable; equality of two blocks is also containment and is
  excluded.

## Round 5 adversarial targets

The independent referee and checker specifically attacked:

1. ambient-space versus \(V=\mathbf1^\perp\) kernels and ranks;
2. zero-set boundary cases, including a singleton zero set;
3. potentially negative \(c_r\) before the rank-ten step;
4. orientation by cut complementation;
5. repeated/complement cuts and repeated singleton labels;
6. strict versus non-strict endpoint-deficit sums.

No gap was found. In the rank-ten case, the off-diagonal entries of
\(D_p+c_pJ=B_pGB_p^T\), for arbitrary \(p\), first prove every \(c_p>0\);
the Sherman--Morrison argument is used only afterward.

The final manuscript received a separate hash-bound referee PASS:
'paper/main.tex' SHA-256
966399c07fcd415707b2b20be50d16fa88c1ac69408cebb56e6d156a8d0ae923.
The report is 'audit/final_hash_referee.md'. It additionally forced an
explicit \(Z=[11]\) boundary sentence before the zero-set complement
orientation.

## Exact finite certificates

- Foundational fail-closed matrix:
  'logs/fail_closed_matrix.json', SHA-256
  948c38a191cff81ea55bb6b7c64f6bd6343a6dd1eb3a0ce0573d333c6a60a129.
  It records 12 cases in each of four interpreter modes, 48/48 expected
  outcomes. Tampering includes deleted fields, changed \(m,d\), gap count,
  one point coordinate, one claimed distance, and frame data.
- Full transcript:
  'logs/fail_closed_matrix_full.json', SHA-256
  06c14c25caa3eab24a7a8b3e835524bad1a97fc70b0a7c177fbdb6749301fc25.
- \(t=18\) endpoint manifest matrix:
  'logs/t18_fail_closed_matrix.json', SHA-256
  4fc5bf85e65215a658181903323d7404eb42b0879952c13fdadc0a9761bb65de;
  60 expected outcomes.
- Independent Round 5 checker matrix:
  'logs/referee_t18_check_matrix.json', SHA-256
  de8252d3e184357d889bc68e9cfc3503c3b87aa2255a5dc14536fbb9e0810d16.

The decisive Python sources contain zero AST Assert nodes. Their
mathematical decisions use explicit conditions followed by exceptions or
nonzero exits, so optimization does not erase them.

## Finite-box theorem

'certificate/integer_box_side5.json' and
'certificate/verify_integer_box.py' reconstruct all \(3125\) vertices of
\(\{0,1,2,3,4\}^5\) and prove that the maximum equilateral subset over all
integer distances is \(10\). The certificate SHA-256 is
8c9501f60eb3eddf03f32fc96e1c61fd761fecf025440cd1d72781db27b80a24;
the verifier SHA-256 is
7f1918241417c90bdadfa3e56ee6f86350b179d84809d3b8d3d69c841e532337.
An external '-O -I' run with Homebrew Python 3.14.7 passed. This is only a
finite-box theorem and has no implication for arbitrary coordinates.

## Dependencies and proof-assistant disclosure

- Python requirement: **Python 3.10 or newer**. The side-five verifier uses
  'int.bit_count'; Apple system Python 3.9 exits fail-closed with a clear
  version error.
- All decisive verifiers use the Python standard library only.
- PDF build: TeX Live 2026 ('latexmk', 'pdflatex', BibTeX) and Poppler for
  rendering/inspection.
- No proof assistant, SMT solver, SAT solver, CAD system, or Gröbner-basis
  package was used in the final proof.
