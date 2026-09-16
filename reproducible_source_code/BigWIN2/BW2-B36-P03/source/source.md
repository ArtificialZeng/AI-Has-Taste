# Win36-03 — Decide whether the two-row pairwise-coprime threshold L42 equals 529

For n>=1, let L_n be the least integer x for which there exist an integer d>0 and an n-element set V contained in {2,...,x-d} such that the 2n integers

    v and v+d, for v in V,

are all distinct and pairwise coprime.

Decide whether L_42=529. If equality is false, prove the strict lower bound L_42>=530.

The supplied primary lead is Zijian Zeng, *The Exact Two-Row Pairwise-Coprime Grid Threshold Is L 41 = 529*, DOI 10.2139/ssrn.7395519, recorded in row 50 of `resources/user-bibliography/registry.json`. It proves L_41=529. Hence L_42>=529. At x=529, an explicit feasible 42-row pair proves equality; a complete exclusion for every admissible d proves L_42>=530.

Use exact gcd predicates and a completeness certificate. First verify the cited definition, the admissible d range, and whether the paper's auxiliary data already determines the 42-row case.

