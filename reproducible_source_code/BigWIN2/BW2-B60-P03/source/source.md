# Immutable source: win-00060-p03

## Frozen problem

Fix `n=4` and `a=b=1/2` in the submodular box-constrained quadratic-program instance (5) of arXiv:2609.03617v1. For the paper's relaxation (9), which incorporates the full Boolean-quadric-polytope representation rather than only the displayed McCormick inequalities, determine:

1. the exact optimum value;
2. the complete optimal face up to the manifest symmetries; and
3. matching exact primal and dual certificates proving global optimality.

The source supplies a feasible objective value `-1/100` and reports a numerical optimum near `-0.0108`. A qualifying result must close that gap exactly or find an error; merely replaying the `-1/100` certificate is not a contribution.

## Primary source and locator

- Paper: *On the Omega(n) SDP Relaxation Gap for Submodular Box-Constrained Quadratic Programming*, arXiv:2609.03617v1.
- Locator: Propositions 1--3 and 6, relaxation (9), Appendices A--B.
- Local evidence: `batches/inbox/bigWin-60-materials/2609.03617.pdf`.
- PDF SHA-256: `58b6236cad34db398b14fb1db9ead1aad4587c0a54a35fbccdb834a087d4b698`.

No claim is made here that the numerical value is wrong or that the exact optimum is absent from all prior literature; triage must verify both.
