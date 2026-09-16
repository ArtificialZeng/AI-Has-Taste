# Immutable source: win-00062-p02

## Frozen problem

Consider the unweighted marriage problem on the complete bipartite graph `K_{3,3}`, with three men and three women. Every agent regards all three agents on the opposite side as acceptable and assigns them one of the 13 total preorders (weak orders, so ties are allowed). Being unmatched is strictly worse than every acceptable partner. Matchings need not be perfect; hence the instance has exactly

`sum_{k=0}^3 binom(3,k)^2 k! = 34`

matchings.

Use the definition in arXiv:2509.25150v3: for a set `C` of matchings, an agent compares its best partner among the matchings in `C` with its partner in an alternative matching `M'`; ties contribute to neither side. The set `C` is popular winning when, for every alternative `M'`, at least as many agents strictly prefer their best partner in `C` as strictly prefer their partner in `M'`. The popular dimension of an instance is the least cardinality of such a set.

Determine exactly

> the maximum popular dimension over all `13^6` preference profiles on this fixed `K_{3,3}`.

Theorem 3.3 of the source implies the answer is either 2 or 3. If it is 3, return a canonical extremal profile, prove that no singleton or pair is popular winning, and exhibit a popular winning triple. If it is 2, certify for every profile a popular winning singleton or pair and also provide a profile with no popular matching so that the maximum is exactly 2.

The finite proof must cover all profiles and all 34 alternative matchings. Record the weak-order encoding, unmatched convention, symmetry reductions, exact domain count before and after reduction, software/runtime versions, deterministic hashes, and an independently implemented verifier. Sampling or floating-point optimization is not sufficient.

## Primary source

- Frank Connor, Louis-Roy Langevin, Ndiamé Ndiaye, Agnès Totschnig, Rohit Vasishta, and Adrian Vetta, *The Popular Dimension of Matchings*, arXiv:2509.25150v3, §1.1, Table 1, and Theorem 3.3.
- URL: https://arxiv.org/abs/2509.25150
- Local evidence: `batches/inbox/bigWin-62-materials/2509.25150.pdf`
- PDF SHA-256: `1707cb5423c732793ebc688f84b5663dee15ad7ae330ccb6b10cdd210a76bfd2`.

The source proves only the global `{2,3}` range for unweighted marriage instances with ties. Novelty and prior finite censuses must be checked before any paper claim.

