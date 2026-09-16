# Immutable source statement: win-00049-p02

## Title

Strong optimality of two-color Permutation Wordle at (n=3)

## Original lead (preserved)

> Decide the first nontrivial multicolor Permutation Wordle instance exactly, horizon by horizon.

This is a finite special case of a published conjecture. It must not be represented as the general multicolor theorem.

## Exact game

Let
\[
\Omega=S_3\times\{0,1\}^{[3]}.
\]
A secret is ((\sigma,\kappa)\in\Omega), where (sigma:[3]\to[3]) is a permutation and (kappa(j)) is the color of value (j). A legal guess is ((\gamma,c)\in\Omega). Its feedback against the secret is
\[
U(\gamma,c;\sigma,\kappa)=\{i\in[3]:\gamma(i)=\sigma(i)\text{ and }c(\gamma(i))=\kappa(\sigma(i))\}.
\]
A deterministic adaptive strategy chooses each next legal guess from all earlier feedback. A secret is solved in a round exactly when the guess equals the secret, equivalently the feedback is ([3]). Randomized strategies need not be considered for the uniform distribution because a mixture cannot beat the best deterministic strategy at a fixed horizon.

For every integer (r\ge1), let (N_r) be the largest number of the 48 secrets that any deterministic adaptive strategy can solve within (r) guesses. Compute every (N_r) until it equals 48 and prove that the multicolor `CircularShift` strategy of Kutin–Smithline attains (N_r) simultaneously for every (r). If this statement is false, give the least (r) for which it fails and an explicit strategy tree attaining a strictly larger value.

The required result is strong distributional optimality, not only optimal expected time or worst-case time. The initial guess may be normalized by a proved symmetry, but the completeness computation must still cover all legal adaptive strategies.

## Primary sources and nearest results

- Samuel Kutin, Lawren Smithline, and Vincent Vatter, *Permutation Wordle*, arXiv:2609.01874v1, especially §2, Theorem 10, and §7.
- Samuel A. Kutin and Lawren M. Smithline, *Permutation Wordle*, arXiv:2408.00903v1, especially Definitions 4.1 and 4.3, Lemma 4.4, Conjecture 2.2, and §7.
- Official endpoints: <https://arxiv.org/abs/2609.01874>, <https://arxiv.org/pdf/2609.01874>, <https://arxiv.org/abs/2408.00903>, and <https://arxiv.org/pdf/2408.00903>.
- The 2026 paper proves strong optimality for the monochrome game for every (n), but §7 still states the multicolor extension as conjectural. The public older version contains the full multicolor rules and shows that `CircularShift` takes
  (1+operatorname{exc}(\sigma)+\sum_i\kappa(i)) rounds on a secret.

## Precise delta and status

The delta is only ((n,s)=(3,2)), with all 48 secrets and legal colored-permutation guesses. Do not infer the general (n) or (s) conjecture. Do not enlarge the guess alphabet to repeated ranks; that is a separate relaxation parked as DW49-15. Literature status is supported by the cited §7, but priority of the exact (n=3) finite case still requires checking related multicolor work cited as “in preparation.”

## Required certificate

1. List all 48 secrets and 48 legal guesses in a canonical encoding.
2. For every guess and current viable-secret set, compute the exact feedback partition.
3. Implement the Bellman recurrence for the maximum number solved by each horizon, with memoization over exact secret masks and no pruning that can remove an optimal branch.
4. Emit a digestible proof table: canonical state, horizon, optimal value, chosen guess or upper-bound decomposition, and symmetry mapping for each omitted equivalent state.
5. Independently simulate the explicit `CircularShift` strategy on every secret and report its exact completion-time distribution.
6. Compare cumulative values for every relevant (r); include a replay verifier independent of the discovery implementation.

## Cheapest decisive test and falsification

Normalize the first guess using the transitive relabeling/color symmetries, then recurse on feedback cells. The maximum `CircularShift` time is at most six from the quoted formula, so horizons (1,dots,6) suffice. Any valid strategy tree solving more secrets at some horizon disproves strong optimality. Any Bellman pruning rule lacking a proof, or a state table that omits non-equivalent feedback cells, cannot certify optimality.

## Frozen primary materials

- `batches/inbox/bigWin-49-materials/2609.01874.pdf`, SHA-256 `60deb7c79de482af9967dd0006b471a7f457167d8d422ad38bc7c8c57ab14705`.
- `batches/inbox/bigWin-49-materials/2408.00903.pdf`, SHA-256 `119c0fbdcc6eb4dd2582bd7edd43539fcb7eaee7d82d70c55525bbf6c475fcdb`.
- Retrieved from official arXiv PDF endpoints and checked on 2026-09-07.

