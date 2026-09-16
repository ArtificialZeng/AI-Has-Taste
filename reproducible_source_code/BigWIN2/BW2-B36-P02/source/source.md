# Win36-02 — Determine the pairwise-GCD sunflower-free value f3(127)

For a positive integer N, let f3(N) be the largest cardinality of a set A contained in {1,...,N} for which there do not exist three distinct x,y,z in A satisfying

    gcd(x,y) = gcd(x,z) = gcd(y,z).

Determine f3(127).

The supplied primary lead is Zijian Zeng, *The Exact Value of a Pairwise-GCD Sunflower-Free Function At 126*, DOI 10.2139/ssrn.7395458, recorded in row 49 of `resources/user-bibliography/registry.json`. It proves f3(126)=16. Deleting 127 from any feasible set gives

    16 <= f3(127) <= 17.

The requested finite resolution is therefore either an explicit verified 17-element set or a complete proof-producing exclusion of all such sets. First verify that the cited paper uses exactly this definition and that the value at 127 is not already included in its data.

