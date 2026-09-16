# Immutable source: win-00062-p04

## Frozen problem

Fix an integer `n>=1` and a real parameter `0<=alpha<1`. Let the bandwidth distribution on `[0,1]` be

`P_alpha = (1-alpha) Unif[0,1] + alpha delta_1`,

and let quality be `Q(B)=B`. Choose a strictly increasing encoding ladder

`0=R_0<R_1<...<R_n<=1`.

At bandwidth `B`, the client selects the greatest ladder value not exceeding `B`,

`R(B)=max{R_i:R_i<=B}`,

and incurs one-sided quality loss `B-R(B)`. Determine exactly, for every `(n,alpha)`,

`inf E_{B~P_alpha}[B-R(B)]`,

whether the infimum is attained under the stated strict inequalities, and every attaining ladder when it is attained. Give a piecewise closed form, including all transition values of `alpha` and the endpoint cases.

A proof may introduce gaps

`Delta_i=R_{i+1}-R_i` for `0<=i<n`, and `Delta_n=1-R_n`,

but must derive—not assume—the correct objective, constraints, and contribution of the atom at `B=1`. It must resolve the distinction between `Delta_n=0` (that is, `R_n=1`) and a vanishing interior gap, and must not silently relax `R_0<R_1<...<R_n`. Verify the general formula against exact direct optimization for `n=1,2` and the cases `alpha=0`, the active-set transition, and `alpha` approaching 1.

This is a strict special case of the source's proposed extension to distributions with atoms; do not claim the full Graf–Luschgy-generality atom problem is solved.

## Primary source

- Yuriy A. Reznik, *A Quantization Problem Posed by Adaptive Streaming*, arXiv:2609.03745v1, Eq. (1), Proposition 1, Example 1, Remark 1, and the concluding open problems.
- URL: https://arxiv.org/abs/2609.03745
- Local evidence: `batches/inbox/bigWin-62-materials/2609.03745.pdf`
- PDF SHA-256: `9204ad1b5dccb6812c5374d4041982ce44ce6c8a3c6486e71bee4cbbbc48523e`.

The source treats `C^1` densities on a compact interval and explicitly identifies atoms as an open extension. A fresh literature audit is still required for this exact one-atom specialization.

