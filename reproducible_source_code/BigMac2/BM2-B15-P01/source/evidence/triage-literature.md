# Literature and duplicate triage, 2026-09-08

Primary paper: Zheng Zhang and Na Zhang, Representation Redundancy and
Structural Complexity in Finite-Field Inversion, arXiv:2609.04583v1.
URLs inspected: https://arxiv.org/html/2609.04583v1 and
https://arxiv.org/abs/2609.04583 . The versioned abstract URL initially
returned a browser retrieval error; the unversioned abstract and versioned
HTML subsequently loaded. This is not evidence about mathematical status.

The supplied local PDF was copied without modification to
`evidence/2609.04583v1.pdf`; its extracted text is adjacent. The authoritative
mathematical content was inspected directly, not inferred from snippets:

- Definition 11, Proposition 12, printed p.11: full Boolean adjugate extension
  and degree upper bound 3(n-1).
- Definitions 13–14, pp.11–12: vector coefficient support and ordering leap.
- Theorem 17, pp.14–15: all support degrees at least n, proved by rank and
  zero-operand cases in the coefficient subset sum.
- Experiment 0, p.17; Table 1, p.18: exact n=3,4 computations, not a
  universal upper bound.
- Appendix A.3, Tables 7–8, pp.27–28: short support prefixes cover all input
  variables for those two computations. The n=3 final support has size 4;
  the n=4 final support has size 7. This does not prove the equality for all n.
- Conclusion, final paragraph before Appendix A: general raw ANF values
  are among the stated further directions.

Search queries included the exact title, `"joint" "ANF" "leap" inversion`,
`"finite-field inversion" "joint ANF leap"`, `"adj(P)" "leap" inversion`,
and `"2609.04583" "upper bound"`. Relevant hits led back to the named
primary paper; broad searches produced substantial unrelated noise.
No equivalent general equality was found in the inspected primary source.
This is a narrow literature screen, not proof of priority or an assertion
that no such theorem exists elsewhere.

The historical registry at /Users/mac/4prove-or-disprove-math/registry/problems.jsonl
was searched and normalized entries were compared. The self-entry
bigMac-00015-p01 matches the frozen claim. The finite-field F-set entries
bigMac-00007-p11 and bigMac-00014-p03 concern irreducible-polynomial closures
and widths. bigMac-00009-p15 concerns elementary generation over a Laurent
ring. Their objects, quantifiers and invariants differ from Boolean ANF
support ordering. No matching predecessor was identified in this screen;
the external registry was not modified.

Suitability: admit the precise universal equality for a bounded proof pass.
Nearest prior result: L>=n. Delta: an explicit n-term cyclic prefix proving
L<=n while leaving only one matrix row unseen. Verifier: exact Boolean
coefficient sums and a short symbolic partial-permutation argument.
