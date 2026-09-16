# Fresh mathematical referee report

## Verdict

**Accept.** The frozen `resolution-paper` claim is correct at its exact scope. The supplied finite certificate and the independent replay establish that the fixed complex has no one- or two-circuit decomposition, while the three displayed cyclic words give a decomposition. The optional census and automorphism quotient are also correctly certified.

## Snapshot and scope checked

I checked every file named by `audit/snapshot.json`; its SHA-256 values agree with the current bytes, and the snapshot digest is `001486e0d5b233dbc792008992600c6371b83e08560b75c86d85c127f9ffd3ed`. The claim concerns only the 18 frozen unordered facets in `source.md`, with the circuit definition made precise in `problem.md`. It makes no assertion about arbitrary triangulated tori.

The source PDF's Definition 1 agrees with the frozen circuit interpretation. Figure 1 supplies the three words `105374(10)`, `216587(21)`, and `023648(02)`, and says only that the absence of an Euler 2-circuit is left to the reader. The inspected pages do not give a two-circuit exclusion or the exact census. The bibliographic mismatch already disclosed in `problem.md` is real: the hash-matched PDF is by Jens Harlander and Maizie Quatrone and has the plural title *Circuit Decompositions for Triangulations of Surfaces*. This metadata defect does not change the facet list or the mathematical claim, but it should be corrected in any manuscript.

## Reconstruction of the decisive argument

Let \(\Omega\) be the 108 ordered triples obtained by ordering each of the 18 facets in all six ways. Direct incidence reconstruction from the frozen facet list gives 27 edges, with exactly two incident facets at every edge. Thus the map

\[
P(a,b,c)=(b,c,d),
\]

where \(\{b,c,d\}\) is the other facet incident to \(\{b,c\}\), is well-defined and bijective.

For any admissible cyclic word \(W=(v_i)\), set \(s_i=(v_i,v_{i+1},v_{i+2})\). Consecutive facet windows are distinct because all facet windows in a circuit are required to be distinct. They share the edge \(\{v_{i+1},v_{i+2}\}\), so the two-facet edge incidence forces \(s_{i+1}=P(s_i)\). Cyclic closure gives \(P^n(s_0)=s_0\), and facet injectivity prevents either stopping before the state orbit closes or traversing an orbit more than once. Hence every circuit is exactly a full orbit of \(P\) whose facet projection is injective. Conversely, every such orbit produces a valid cyclic word. This proves that the transition-orbit enumeration is complete and addresses the essential quantifier; it is not merely a bounded prefix search.

The serialized enumeration contains 18 directed \(P\)-orbits. All have length six and injective facet projection. Reversal pairs them into exactly nine circuits modulo cyclic rotation and reversal. Exhausting all \(2^9=512\) subsets gives exactly three facet-exact covers, each with three circuits:

1. `014735`, `023648`, `127856`;
2. `015684`, `028753`, `126347`;
3. `032615`, `041728`, `346857`.

There are therefore zero one-circuit covers and zero two-circuit covers. The first cover is the displayed source decomposition after permitted rotations and reversals, so \(c(S)\leq 3\); the exhaustive exclusion gives \(c(S)\geq 3\). Thus \(c(S)=3\).

## Checks actually performed

I inspected both enumeration programs and the complete JSON certificate, including the facet input, edge-incidence table, transition construction, orbit validation, exact-cover test, automorphism test, and serialized outputs. I then ran

```text
python3 evidence/replay_certificate.py
```

from the project root. It printed `REPLAY OK`. This checker does not import the generator. It independently rebuilds edge incidence, recomputes the ordered transition table and its digest, walks from all 108 ordered facets, reconstructs the nine unoriented circuits, tests all 512 circuit selections with facet multiplicities, and exhausts all \(9!\) vertex permutations.

The replay found 108 automorphisms. Their induced actions on the three minimum covers realize each of the six permutations of those covers 18 times, so the action is transitive. Equivalently, the Burnside fixed-point sum is 108 and the orbit count is \(108/108=1\). This validates the claimed count of three labeled minimum decompositions under the stated circuit symmetries and one class after quotienting by \(\operatorname{Aut}(S)\).

I found no unhandled empty case, repeated-facet case, division, limiting argument, cited theorem dependency, or mismatch between the checked finite object and the frozen statement. The certificate uses only exact finite set/integer operations. Successful replay is not by itself a proof; acceptance rests on the proved orbit-completeness reduction together with the independently reconstructed exhaustive enumeration.

## Contribution assessment

At the frozen scope, the result completely answers the original finite question, provides the required independently replayable exclusion certificate for every smaller number, and certifies the optional exact quotient count. The source supplies only the upper bound and an unsupported one-circuit assertion, so the two-circuit exclusion and census are a genuine, precisely identified delta relative to the inspected source. No broader priority claim is needed for this acceptance.
