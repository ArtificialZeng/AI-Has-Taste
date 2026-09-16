# Precise reading

## Frozen target

The source is read in the monotone hypergraph sense used in arXiv:2609.03508v1, §3.1–3.2. An input instance is a finite indexed family

\[
F=(V;(C_j)_{j=1}^m),\qquad C_j\in {V\choose 4}.
\]

Thus every clause contains four **distinct, unnegated** Boolean variables. An assignment is a map \(s:V\to\{-1,+1\}\). It satisfies \(C_j\) exactly when the four values are not all equal, equivalently

\[
\sum_{x\in C_j}s(x)\in\{-2,0,2\}.
\]

The indexed formulation allows repeated clause occurrences; these are non-linear because two distinct indices can have intersections larger than one. A formula is **linear** when \(|C_i\cap C_j|\leq 1\) for every \(i\ne j\).

The problem asks whether there exist an absolute constant \(B\) and a deterministic algorithm \(T\) such that, for **every** finite monotone 4-uniform NAE instance \(F\), \(T(F)=F'=(V';(C'_k))\) has the following properties:

1. \(V\subseteq V'\), and every \(C'_k\) is a four-element subset of \(V'\) interpreted by the same NAE predicate above.
2. \(F'\) is linear.
3. For every \(s\in\operatorname{Sat}(F)\), there exists \(s'\in\operatorname{Sat}(F')\) with \(s'|_V=s\).
4. For every \(s'\in\operatorname{Sat}(F')\), \(s'|_V\in\operatorname{Sat}(F)\). Equivalently,
   \[
   \{s'|_V:s'\in\operatorname{Sat}(F')\}=\operatorname{Sat}(F).
   \]
5. Each occurrence whose replacement is used to eliminate a multi-variable intersection costs at most \(B\) fresh variables and at most \(B\) fresh clauses, and the total construction has polynomial size and running time (indeed this local bound should give linear overhead in the number of repaired occurrences).

“Offending repeated variable occurrence” therefore means an occurrence in one indexed clause that, together with another shared variable, makes that clause and another distinct clause intersect in at least two variables. It does **not** mean a repeated variable within one clause, which is excluded by \(C_j\in{V\choose4}\). A natural permitted operation is to retain one occurrence as the original variable \(x\), replace another by a fresh copy \(x'\), and attach a fresh-auxiliary gadget whose satisfying terminal projection is exactly \(x=x'\). The proof must also establish that all such gadgets compose while preserving global linearity; a stand-alone equality truth table is not sufficient.

A complete positive answer must give the clauses, a full exact terminal/auxiliary truth-table or equivalent local certificate in both directions, the global incidence argument, and the size/time bound. A negative answer must give either a finite exact counterexample to a proposed universal construction or a rigorous impossibility obstruction for the quantified gadget class, and must identify the consequence for the paper: without a valid source reduction to linear monotone NAE-4-SAT, Lemma 1 is unsupported, so the reduction in §3.2–3.4 does not by itself justify NP-hardness (and hence the claimed NP-completeness) of recognizing Max-Cut SDP exactness for simple unweighted graphs. This does not affect the separate weighted-graph reduction in §2.

## Scope exclusions

- No signed literals, lower-arity clauses, duplicated variables inside a clause, constants, or non-NAE constraints may be introduced.
- Equisatisfiability alone is weaker than the required equality of projected solution sets.
- A construction valid only for bounded occurrence, a pre-linear subclass, or another promise problem does not resolve the frozen target.
- The target is the missing source reduction, not the correctness of the subsequent \(K_6\) calculation conditional on receiving a linear instance.

## Literature triage (retrieved 2026-09-07)

- Bhardwaj, arXiv:2609.03508v1, §3.1 Lemma 1, states that fresh copies are tied by intermediate NAE equality clauses but gives no clauses, arity-four certificate, or composition proof: <https://arxiv.org/html/2609.03508v1>.
- Darmann and Döcker, arXiv:1908.04198v2, Lemma 3 and Theorem 2, give a 12-clause, six-auxiliary **3-uniform** linear monotone NAE gadget forcing four terminals equal, and use it to prove hardness of linear Monotone NAE-3-Sat-E4: <https://arxiv.org/html/1908.04198v2>. This is the nearest explicit prior construction found, but its clauses have arity three, so it does not establish the required 4-uniform statement.
- Nakajima and Živný, arXiv:2204.05628v3, Proposition 3, linearize a promised LO-2-colourable 3-uniform hypergraph by merging vertices after two edges share a pair: <https://arxiv.org/html/2204.05628>. This is neither a vertex-splitting equality gadget nor an assignment-projection-preserving reduction for monotone NAE-4-SAT.

No primary source establishing the exact quantified 4-uniform replacement assertion was found in the bounded exact/equivalent searches above. This is a source-status assessment (`status-uncertain`), not a priority or open-problem claim.

## Admitted research target

Nearest prior result: the Darmann–Döcker linear monotone NAE-3 equality construction. Proposed delta: an explicit linear monotone NAE-4 equality/replacement gadget satisfying the stronger projection and global-composition requirements above, or an exact obstruction/counterexample. Verification route: exhaustive Boolean enumeration of each proposed gadget's terminal projection, mechanical pairwise clause-intersection checks, followed by a symbolic composition proof and exact tests on minimal two-clause overlaps of sizes 2, 3, and 4.
