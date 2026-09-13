# Project approach registry

The machine-readable route state is `routes/registry.json`.

| ID | Route | Status | Current discriminating test |
|---|---|---|---|
| RG10-P01 | Principal-core reduction and exact isotropic-profile compatibility graph | active globally; closed through bicyclic cores | If resumed, move to connected tricyclic ten-vertex cores without weakening the exact target-53 gate. |
| RG10-D01 | Search one-edge/two-edge/orbit/random deformations of nonsingular ten-vertex cores | active | Exact decision search for a compatible clique of size 63 (53 noncore profiles). |
| RG10-D02 | Direct one-vertex extension of the five standard order-62 graphs | closed negative within its stated scope | All 1024 binary profiles per graph have been classified exactly; zero accepted. |
| RG10-A01 | Independent arithmetic, maximum-clique, manuscript, citation, and PDF audit | closed PASS for the tree-core theorem | Preserve the frozen hashes and repeat only after a mathematical or metadata change. |
| RG10-R02 | Connectedness and connected nonsingular-core reduction | closed exact deduction | Disconnected rank partitions give order at most 32; search only connected nonsingular ten-vertex induced cores. |
| RG10-P02 | All nonsingular ten-vertex tree principal cores | closed exact independently audited theorem | Preserve the frozen source/replay/independent-audit/fail-closed hashes; do not extend the claim to cyclic cores. |
| RG10-P03 | All nonsingular connected ten-vertex unicyclic principal cores | closed exact independently implemented theorem | Preserve the 657-object source, 136-core no-import audit, fail-closed hashes, and 62-vertex sharpness certificate; the next finite layer is bicyclic. |
| RG10-P04 | All nonsingular connected ten-vertex bicyclic principal cores | closed exact independently implemented theorem | Preserve the 2,678-object source, 719-core no-import audit, five fail-closed attacks, theorem referee and 62-vertex sharpness witness; do not extend the claim to denser cores. |

Exact audited update: all 45 one-edge toggles of the standard core have been
classified; 9 are singular and all 36 nonsingular cases have independently
reconstructed negative 63-clique decisions.  The no-import verifier rebuilt
every core, determinant, integer adjugate, profile set, and compatibility
graph, then excluded the target after a cyclic relabelling in 4,120,195 exact
search calls.  Two-edge deformations are now the active disproof search.

The one-edge family audit and its theorem document now pass a separate
structural audit with 0 fatal, 0 major, and 0 minor findings.  The same audit
checks all eleven disconnected rank partitions and the precise attribution
of the Wang--Guo connected-core theorem.

The all-tree pass generated all 106 free trees by AHU canonical leaf
extension, cross-checked the classical rooted and free-tree counts, found
exactly 15 nonsingular cores (all determinant `-1`), and excluded a
53-profile noncore clique for all 15.  A deterministic no-import replay
reconstructed 882,626 source nodes; a second no-import engine regenerated
the tree set, used different representatives plus cyclic relabelling, and
closed the 15 targets in 760,220 calls after 1,500 brute-force engine tests.
Four corrupted inputs fail closed.  The tree-core theorem is therefore
promoted exactly within its stated scope.

The fixed standard-core subproblem is now closed exactly: two separately
implemented integer reconstructions agree, both clique engines have been
cross-checked against literal brute force on all labelled graphs through six
vertices and randomized larger cases, and six deliberately corrupted inputs
fail closed.  This audit does not enlarge the fixed-core scope.

The complete unicyclic layer is now closed exactly.  Tree-plus-nonedge and
cycle-decoration generators agree on 657 isomorphism classes; 136 are
nonsingular.  Discovery excludes target 53 in 9,987,213 exact branch nodes.
A no-import bracket-code generator, cofactor-adjugate reconstruction, and
cyclically relabelled clique engine independently exclude all 136 targets in
11,600,208 calls after 1,500 engine self-tests.  Five corrupted inputs fail
closed.  A certified 62-vertex equality graph contains a nonsingular
five-cycle-core witness, so the unicyclic structural theorem is sharp.  The
serial theorem referee reports `0 fatal / 0 major / 0 minor`; the 220-file
milestone manifest verifies independently.  No new PDF was created because
this result does not settle the unrestricted conjecture.

The complete bicyclic layer is also closed exactly.  Unicyclic-plus-nonedge
and tree-plus-two-nonedges generation agree on 2,678 isomorphism classes,
split into 345 dumbbells, 514 figure-eights and 1,819 theta types.  Exactly
719 are nonsingular.  Discovery closes all target-53 instances in 48,967,729
integer branch nodes; an independently generated and canonicalized domain
recomputes all determinants, adjugates, profiles and compatibility graphs and
closes them again in 41,704,342 calls.  Five corruptions fail closed.  The
certified order-62 equality graph contains a nonsingular bicyclic ten-core,
so the class theorem is sharp.  The unrestricted problem is still open for
connected nonsingular ten-cores with at least twelve edges.
