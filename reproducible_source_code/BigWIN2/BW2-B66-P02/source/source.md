# win-00066-p02 — Minimum Abelian Cayley order with a Goemans–Linial gap

For a finite Abelian group `Gamma`, let `S` be a repetition-free symmetric subset of `Gamma\{0}` that generates `Gamma`, and let `G=Cay(Gamma,S)` be the resulting connected simple unweighted undirected graph. Use the uniform-demand Goemans–Linial SDP and sparsest-cut normalization of arXiv:2609.05368v1.

Determine the least possible `|Gamma|` for which

> `psi(G) > SDP_GL(G)`.

The source proves that `Cay(Z_10,{±1,±3})` has ratio `16/15`, so a complete resolution must prove exactness for every eligible presentation of order at most nine and classify every non-exact graph of order ten up to graph isomorphism (with distinct Cayley presentations recorded), or exhibit and certify a smaller counterexample.

Primary evidence: `batches/inbox/bigWin-66-materials/2609.05368.pdf`, SHA-256 `c21f216511526cc3f0fa4a7d4bc177037bd748272b0bcb497e756c5a412787c0`, especially Corollary 4.7, §6.4, and §7 Questions 7.1–7.2. The source supplies a small ten-vertex witness but does not claim minimality or classify order ten.

Every claimed optimum needs an exact certificate: complete finite-group/generator-set orbit coverage, exhaustive cut optimum, and an exact primal/dual or algebraic certificate for the GL relaxation. Floating-point SDP values may guide the search but cannot decide equality.

