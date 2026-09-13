# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen at snapshot digest
`122bf07d8f886c1f74935c676467e6459e53ab3ccbc0fe1a6c404086e9e6b093`.
The claim uses the reading in `problem.md`: finite simple undirected graphs,
eight vertices, disconnected and degree-zero graphs allowed, ordinary labels
bijective onto \(\{1,\ldots,8\}\), and group-magic labels required only to
span \(\mathbb F_2^3\).

**Verdict: accept.** The frozen evidence and a fresh exhaustive check establish
the claimed four-class enumeration, the ordinary distance-magic property of
exactly those classes, and the four reduced nullities. The conclusion settles
the full universal assertion in `source.md`; it is not a weakened subsidiary
claim.

## Reconstruction of the decisive argument

Let \(G\) be \(k\)-regular and let an ordinary distance-magic labeling have
constant \(c\). Summing all eight neighborhood equations counts each label
exactly \(k\) times, so

\[
  8c=k(1+\cdots+8)=36k.
\]

Thus \(c=9k/2\), and \(k\) is even. Simplicity gives \(0\leq k\leq7\), so
only \(k=0,2,4,6\) require consideration.

I checked completeness without relying on the producer's call to `geng`.
The fresh program `audit/referee_recheck.py` recursively generates every
labeled simple \(k\)-regular graph. At vertex \(i\), all edges to earlier
vertices have already been fixed; the program chooses exactly its remaining
neighbors among the later vertices. Consequently every labeled regular graph
is reached once before conversion to a set. Separately, it forms the complete
\(8!\)-relabeling orbit of each frozen adjacency matrix. For each degree, the
representative orbits were disjoint and their union equaled the freshly
generated universe:

| degree | all labeled regular graphs | frozen classes |
|---:|---:|---:|
| 0 | 1 | 1 |
| 2 | 3507 | 3 |
| 4 | 19355 | 6 |
| 6 | 105 | 1 |

This is an exact set equality, not only an agreement of totals. It proves that
the eleven frozen representatives are pairwise nonisomorphic and exhaustive
in all feasible degrees.

The same fresh check did not repeat the producer's loop over all label
permutations of each representative. Instead, it tested the fixed labeling
\(i\mapsto i+1\) on every labeled regular graph in each generated universe.
This is exhaustive because any bijective ordinary labeling transports its
underlying graph, by relabeling vertices, to a labeled graph on which the fixed
labeling is magic. The numbers of fixed-label magic graphs were respectively
\(1,3,4,1\), and they lay in exactly the orbits

\[
  \texttt{d0-1},\quad\texttt{d2-1},\quad
  \texttt{d4-1},\quad\texttt{d6-1}.
\]

Their stored adjacency matrices identify them directly as
\(8K_1,2C_4,K_{4,4},K_{2,2,2,2}\). The stored witnesses also admit immediate
hand checks:

* for \(8K_1\), every neighborhood sum is zero;
* in the displayed two copies of \(C_4=K_{2,2}\), the labels on each of the
  four bipartition sides sum to \(9\);
* the two parts of the displayed \(K_{4,4}\) each have label sum \(18\);
* the four nonedge pairs of the displayed \(K_{2,2,2,2}\) each have label
  sum \(9\), so every open-neighborhood sum is \(36-9=27\).

Hence every listed class is ordinary distance-magic, and the exhaustive
fixed-label check excludes every other regular class.

## Reduced operator and generating maps

For completeness, I reconstructed the modular criterion rather than treating
the cited theorem as a black box. Put \(V_2=\mathbb F_2^8\),
\(L=\langle\mathbf1\rangle\), and

\[
 S=\{x\in V_2:Ax\in L\}.
\]

Regularity makes \(A\) descend to \(\bar A:V_2/L\to V_2/L\), and
\(S/L=\ker\bar A\). Therefore
\(\dim S=1+\dim\ker\bar A\). A map
\(f:V(G)\to\mathbb F_2^3\) is represented by three coordinate columns
\(x_1,x_2,x_3\in V_2\). It is group-magic exactly when each \(x_i\in S\),
and its vertex labels span \(\mathbb F_2^3\) exactly when those three columns
are linearly independent. Such a map therefore exists exactly when

\[
  \dim S\geq3
  \quad\Longleftrightarrow\quad
  \dim\ker\bar A\geq2.
\]

I independently recomputed the quotient matrices in the basis
\([e_0],\ldots,[e_6]\) and obtained reduced ranks \(0,3,1,3\) on the four
ordinary-magic classes, hence nullities \(7,4,6,4\). These values also have a
short structural check. Over \(\mathbb F_2\), the full adjacency ranks of
\(8K_1,2C_4,K_{4,4},K_{2,2,2,2}\) are \(0,4,2,4\). In the last three cases
\(\mathbf1\) lies in the adjacency image, so quotienting its image by
\(L\) lowers the rank by one; in the empty case the rank remains zero. All
four nullities exceed one, proving the desired generating-map assertion.

## Checks performed and evidence comparison

I verified the SHA-256 values of `source.md`, `problem.md`, `claim.json`, and
all permitted decisive mathematical evidence files against
`audit/snapshot.json`; rerunning the two supplied verifier programs left their
frozen hashes unchanged. The supplied certificate verifier independently used
`showg`, repeated all \(443520\) label permutations, recomputed the binary
ranks, checked kernel vectors, and replayed row operations. The supplied
coverage verifier recomputed automorphism orbits and independent labeled
counts. Both passed under the required absolute research interpreter. The
fresh checker in `audit/referee_recheck.py` used neither nauty nor the
producer's labeling-search organization and produced
`audit/referee_recheck.json` with status `pass`.

The source comparison recorded in `problem.md` says that the cited general
results cover at most two generators/cube-free order, not this order-eight
\(\mathbb F_2^3\) layer. The elementary reconstruction above removes any
mathematical dependence on the unlisted source PDF. The frozen materials also
disclose a bibliographic author/title mismatch and only a limited literature
screen. Accordingly, this acceptance certifies the exact mathematical
resolution and its full scope, but does not certify priority, novelty in the
broader literature, or the erroneous bibliographic metadata. Those are
publication-stage citation questions, not gaps in the proof.

No unresolved mathematical gap remains in the frozen candidate scope.
