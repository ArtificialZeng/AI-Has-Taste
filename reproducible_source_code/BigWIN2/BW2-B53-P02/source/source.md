# Immutable source — win-00053-p02

## Original lead

Find the smallest integral circulant counterexample to the assertion that a uniquely colorable circulant graph must satisfy `chi=omega`.

## Precise frozen statement for triage

For a positive integer `n` and a set `D` of proper divisors of `n`, let `ICG_n(D)` have vertex set `Z_n`, with distinct `x,y` adjacent exactly when `gcd(x-y,n)∈D`. Determine the least `n` for which some `ICG_n(D)` is uniquely 3-colorable and has clique number `omega=2`, and classify all such divisor sets `D` at that least order up to equality of graphs.

Minimality requires exhaustive coverage of every `n` below the witness and every legal divisor set, with exact connectivity/chromatic/clique/unique-coloring checks. A witness must include its unique color-class partition and independently replayable certificates. Enumeration must account for duplicate divisor descriptions only if they induce identical graphs.

## Primary source and delta

- Milan Bašić, *On uniquely colorable Cayley graphs*, arXiv:2609.03184v1, Theorem 3.1 and Section 5: https://arxiv.org/abs/2609.03184
- Local PDF: `batches/inbox/bigWin-53-materials/2609.03184.pdf`
- SHA-256: `eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2`
- Retrieved 2026-09-07.

The source proves that `ICG_{12p}({2,p})` has the desired properties for every prime `p>=5`, hence gives an order-60 witness, but does not claim order-minimality or classify smaller integral circulants. The proposed delta is the sharp finite boundary, not a reproof of the infinite family.
