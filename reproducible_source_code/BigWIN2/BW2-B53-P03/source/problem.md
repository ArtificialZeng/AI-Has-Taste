# Precise problem — the `M ≡ 4 (mod 8)` order gadget

## Frozen claim and quantifiers

For every integer `M` such that `M >= 20` and `M ≡ 4 (mod 8)`, the full order gadget `OG(M)` below is infeasible. Equivalently, for every integer `q >= 2`, `OG(8q+4)` is infeasible. The first instances are `M=20,28,36,44,...`.

This is a universal nonexistence assertion about finite strict total orders. A strict total order `≺` is irreflexive, transitive, and compares every two distinct elements.

## Exact definition of `OG(M)`

Let

`I_M = (M,2M] ∩ Z = {M+1,M+2,...,2M}`,

and write `b_j=M+j` (a bottom) and `t_i=2M-i` (a top; `t_0=2M` is allowed). The gadget asks for a strict total order `≺` on `I_M` satisfying both conditions:

1. For every `a,b,c ∈ I_M` with `a<b<c` and `a+c=2b`, neither `a≺b≺c` nor `c≺b≺a` holds. Equivalently, the arithmetic midpoint `b` is not between its two endpoints in the order.
2. All fifteen guard–bottom precedence constraints hold:

   - attacks from `x=15`: `t_13≺b_1`, `t_11≺b_2`, `t_9≺b_3`, `t_7≺b_4`, `t_5≺b_5`, `t_3≺b_6`, `t_1≺b_7`;
   - attacks from `x=16`: `t_14≺b_1`, `t_12≺b_2`, `t_10≺b_3`, `t_8≺b_4`, `t_6≺b_5`, `t_4≺b_6`, `t_2≺b_7`, `t_0≺b_8`.

In the source's uniform notation these are `t_(x-2j)=2M+2j-x ≺ b_j=M+j` for `x∈{15,16}` and integral `1<=j<=x/2`. At every target `M>=20`, both endpoints of every listed pair are distinct elements of `I_M`; a guard can equal a *different* bottom at the smallest scales, which Definition 15 explicitly permits.

`OG(M)` is feasible if such an order exists, and infeasible otherwise.

## What constitutes resolution

- A proof must establish infeasibility uniformly for all `M=8q+4`, `q>=2`. A list of finite SAT outcomes is insufficient. Any SAT conflict pattern used must be turned into a mathematical lemma or supplied with a proof-producing certificate checker.
- A disproof needs one target value `M` and one explicit strict total order of `I_M`, together with a complete checker that verifies total-order validity, every in-block 3-AP constraint, and all fifteen precedence constraints.
- Proving any subset of the fifteen precedence constraints already inconsistent with AP-freeness suffices for the frozen claim. Conversely, finding an order for a proper subset (including the source's three-constraint core `C3`) does not refute the full-gadget claim.

## Scope and boundary checks

The problem is only the full finite gadget on the residue class `M≡4 (mod 8)`. It neither asks whether the weaker `C3` core is feasible nor decides the Erdős–Graham two-set permutation problem. The lower bound `M>=20` is within Definition 15's nondegenerate range `M>=16`; `M=20` is the first member of the requested residue class.

For every listed attack, `2b_j-x=2M+2j-x=t_(x-2j)` lies in `I_M`; the endpoint case `(x,j)=(16,8)` gives `2M`. Thus the list has exactly the in-block completions induced by the attackers 15 and 16.

## Primary source, current status, and nearest result

William Kasel, *Structural rigidity in the Erdős–Graham two-set permutation problem*, arXiv:2609.02939v1, submitted 2026-08-31, inspected 2026-09-07: <https://arxiv.org/abs/2609.02939>. The inspected local PDF has SHA-256 `22997afac6b8922d994dbfc8fb111d7ea45321cb49bf6b4a44c71c3a09ad61c9`.

- Definition 15 (printed p. 7) gives exactly the gadget above.
- Proposition 18 (printed p. 8) reports CaDiCaL infeasibility for every `16<=M<=200` and for `M=512`; hence it covers the target values through `M=196`, but only as finite machine verification. An eager transitivity encoding was independently cross-checked at the relevant residue representative `M=44`.
- Proposition 19 (printed pp. 8–9) reports that the four-attack subsystem

  `C4={t_13≺b_1, t_11≺b_2, t_5≺b_5, t_10≺b_3}`

  is infeasible at every swept `M≡0 (mod 4)`. On the target residue this explicitly includes `M=44,52,60,68,76,84,92,100,108`. This is finite evidence, not a theorem.
- Theorem 22 (printed p. 9 onward) proves only the different three-attack core `C3={t_5≺b_5,t_3≺b_6,t_10≺b_3}` for `M≡0 (mod 8)`. The source explains that its FLIP argument fails for `M≡4 (mod 8)` because flood-center classes and leader statuses swap.
- Remark 30 (printed p. 14) explicitly conjectures full `OG(M)` infeasible for every `M>=16` and says nonzero residue classes need different attack subsets. Thus the frozen claim is an `open-supported` source refinement, not a known theorem in the inspected source.

Exact-assertion and equivalent-language web searches on 2026-09-07 found no separate primary paper addressing this gadget; they returned the same six-day-old arXiv source. This records the search result, not a claim of priority or proof that no other result exists. A local normalized-statement search across project `source.md`, `problem.md`, and `checkpoint.md` files found no overlapping lead.

## Triage target

Nearest prior result: Theorem 22 proves a residue-0 `C3` obstruction, while Proposition 19 finitely supports `C4` on all multiples of four that it swept. Proposed delta: prove the `C4` subsystem uniformly infeasible for `M≡4 (mod 8)`, handling `M=20,28,36` separately if its uniform lemmas begin later; this would imply the frozen full-gadget claim. Verification route: first run an exact eager/lazy SAT comparison for `C4` at the three below-sweep targets `M=20,28,36`, the next target after the reported `C4` cases (`M=116`), and a post-Proposition-18 target (`M=204`); then extract relation-level conflict supports and test whether the added `t_13≺b_1,t_11≺b_2` seeds repair the class swap that breaks Theorem 28.
