# Immutable source: win-00060-p01

## Frozen problem

Let the NAE-4-SAT linearization invoked in §3.1, Lemma 1 of arXiv:2609.03508v1 be interpreted exactly as required by the subsequent K6 reduction. Construct an explicit bounded-size replacement gadget for every offending repeated variable occurrence such that:

1. every resulting clause is a NAE clause of arity four under the paper's truth convention;
2. any two distinct clauses share at most one variable;
3. every satisfying assignment of the original instance extends to one of the transformed instance;
4. every satisfying assignment of the transformed instance restricts to one of the original instance; and
5. the transformation has polynomial size and time.

Either prove all five assertions with a complete truth-table/local-composition certificate, or give an exact counterexample and state precisely which downstream NP-hardness claim is no longer justified. Do not weaken the task to equisatisfiability on a special subclass.

## Primary source and locator

- Paper: *On the Complexity of Recognizing SDP Exactness for the Maximum Cut Problem*, arXiv:2609.03508v1.
- Locator: §3.1 Lemma 1 and §3.2 K6 reduction.
- Local evidence: `batches/inbox/bigWin-60-materials/2609.03508.pdf`.
- PDF SHA-256: `cf9afc784c8abdd81e6a1ed78042e3f078aa3795d3247fd03647b42fc3f73a55`.

The source paper calls the linearization standard but does not print the full gadget proof. Whether an equivalent result already appears elsewhere is unverified and must be checked in triage.
