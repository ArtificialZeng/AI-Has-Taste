# Precise reading and triage

## Frozen claim and objects

The immutable statement is `source.md`. For each \(n\in\{6,7,8\}\), let \([n]=\{1,\ldots,n\}\), let \(S_n\) act on \([n]\), and let \(C_n\) be the conjugacy class of permutations having one cycle. Thus \(|C_n|=(n-1)!\).

A vertex will be canonically serialized as the unique cycle word
\[
(1,a_2,\ldots,a_n),
\]
where the associated permutation maps each displayed entry to its successor and maps \(a_n\) to 1. Cyclic rotations are the same cycle; reversal is not identified. Let \(s_i=(i,i+1)\) for \(1\le i<n\). The simple undirected graph \(\Gamma_n\) has an edge \(\{c,s_i c s_i\}\) whenever the endpoints differ; repeated neighbors, if any, are deduplicated. In cycle-word encoding, conjugation swaps the labels \(i,i+1\) everywhere and the result is rotated back to start with 1. No generator \((n,1)\) is allowed.

For these three values of \(n\), there are no loops or duplicate generator-neighbors. Indeed, the centralizer of an \(n\)-cycle is its cyclic subgroup. A loop would put a transposition in that subgroup. Equality of the \(i\)- and \(j\)-neighbors would put \(s_js_i\) in it; for \(i\ne j\), this is either a 3-cycle with fixed points or two disjoint transpositions with fixed points, not a power of an \(n\)-cycle when \(n\ge6\). Hence the graph is \((n-1)\)-regular, with the following mandatory construction checks:

| \(n\) | vertices | undirected edges |
|---:|---:|---:|
| 6 | 120 | 300 |
| 7 | 720 | 2,160 |
| 8 | 5,040 | 17,640 |

The graph distance is the minimum number of allowed conjugations. With \(c_n=(1,2,\ldots,n)\), the requested integers are
\[
D_n=\max_{(u,v)\in C_n^2}\operatorname{dist}(u,v),\qquad
\operatorname{Sort}_n=\max_{v\in C_n}\operatorname{dist}(c_n,v).
\]
The maxima range over all vertices (and all ordered pairs for \(D_n\)); there is no quotient by inverse cycles, reversal, or arbitrary relabeling.

## Required certificate scope

For every \(n\), the result must give an ordered pair \((u,v)\) at distance \(D_n\), a vertex \(w\) at distance \(\operatorname{Sort}_n\) from \(c_n\), and explicit shortest paths, preferably as both vertex sequences and generator-index sequences. Exhaustive BFS from \(c_n\) certifies the sorting maximum only. The diameter requires BFS from every vertex, or a separately proved symmetry reduction. Record the rooted histogram
\(H_n^{\rm root}(d)=|\{v:\operatorname{dist}(c_n,v)=d\}|\) and the all-ordered-pairs histogram
\(H_n^{\rm all}(d)=|\{(u,v):\operatorname{dist}(u,v)=d\}|\), including distance 0. Also record vertex/edge counts, deterministic serialization and SHA-256 hashes, software versions, and replay commands.

Two independently written exact implementations or verifiers are required. A natural split is (A) direct conjugation on canonical cycle words with all-source BFS and (B) a separately written permutation/coset implementation, using Remark 3.1 or Lemma 3.3 of the primary paper, that independently recomputes the same distances, extrema, histograms, and witnesses. Floating-point calculations are unnecessary.

## Nearest prior result and status

Adin--Bagno--Roichman, *Conjugating full cycles by adjacent transpositions: diameter and sorting time*, arXiv:2601.12597v2 (3 September 2026), was inspected from the supplied PDF on 7 September 2026; its SHA-256 agrees with `source.md`. Definitions 1.1 and 1.3 match the reading above. Remark 3.1 identifies \(\Gamma_n\) with the Schreier graph \(X(S_n/Z_n,\Phi_n)\), Lemma 3.3 gives an inversion-minimization distance formula, and the introduction records \(D_5=5>4=\operatorname{Sort}_5\). Theorems 4.1 and 6.1 give general upper bounds, not the requested diameter table.

Section 7, equation (7.1), explicitly says computer experiments verified \(\operatorname{Sort}_n=\operatorname{inv}(\pi_0)\) for every \(n\le12\). Its formulas therefore imply the already-claimed values \(\operatorname{Sort}_6=6\), \(\operatorname{Sort}_7=10\), and \(\operatorname{Sort}_8=13\): the corresponding \(k_t\) lists are \((3,3,3)\), \((3,4,4)\), and \((3,4,4,4)\), and \(\operatorname{inv}(\pi_0)=\binom n2-\sum_t k_t\). This prior computational assertion must be acknowledged; the frozen task still asks for independent reproducible BFS certificates, witnesses, full histograms, and the three diameter values.

Exact-assertion searches on 7 September 2026 located the arXiv paper and mirrors/index records, but no additional primary source tabulating \(D_6,D_7,D_8\). This limited search supports only `status-uncertain` for those finite diameters, not a claim of novelty or priority. The paper itself supports that the general Problems 1.2 and 1.4 remain open. Conjectures 7.1 and 7.2 are outside the claim: finite computations here neither prove nor disprove them.

## Triage decision

Advance. Nearest prior result: the paper's bounds, distance formula, and its computational assertion of the three sorting values. Proposed delta: exact \(D_6,D_7,D_8\), independent reproduction of all six requested values, and a dual-verifier certificate package satisfying the frozen specification. Verification route: exact enumeration and all-source BFS on at most 5,040 vertices, cross-checked by an independent encoding. The first bounded discriminating test is a complete \(n=6\) run of verifier A checking counts, rooted and all-pairs histograms, extrema, and replayable witness paths.
