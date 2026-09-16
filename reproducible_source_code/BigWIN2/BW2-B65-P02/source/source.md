# win-00065-p02 — Exact degree-square Turán problem for `Reg5`

Use exactly the source convention of loopless digraphs with no repeated arc in one direction but with antiparallel arcs allowed, and `Reg5`-free meaning no (not necessarily induced) copy of the regular five-vertex tournament. Prove or disprove, for every integer `m>=1`,

> `ex^+_{L2}(m,Reg5) = ||d^+_{T_4(m)}||_2^2`.

Writing `m=4q+r`, `0<=r<4`, the claimed values are respectively
`36q^3`, `36q^3+27q^2+3q`, `36q^3+54q^2+22q+2`, and `36q^3+81q^2+57q+12` for `r=0,1,2,3`. First attack the statement by exact small-order search. A disproof must include the least certified order found, a complete adjacency matrix, an exact objective comparison, and a replayable `Reg5`-freeness check. A proof must not infer the result merely from the adjacent `TT4` or `R4` theorems.

Primary evidence: `batches/inbox/bigWin-65-materials/2609.05042.pdf`, SHA-256 `8d45a6dc1d9b672641e96492fa55dcf79afcd8fac6dfff945234551c07717666`, especially §2 definitions, Conjecture 3.3 on PDF p.4, and the conclusion on p.13.

