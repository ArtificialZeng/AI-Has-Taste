# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` scope. The original workflow
status remains **unresolved**. This decision accepts the sharp additive-one
comparison for every nonempty finite graph complex, including disconnected and
non-bipartite graphs and isolated vertices. It does not resolve the original
assertion in arbitrary dimension.

Review date: 2026-09-14 UTC. Referee job:
`primary-20260914-knill-dirac-domination-referee-2aa0419486ac`.
Snapshot digest:
`fd4e45729afdbe23ff2bcd923c0b1c6a813052376b6b8e8a5b2fe21888539f65`.
All 15 snapshot file hashes and the canonical mapping digest were independently
checked before and after the computations. The immutable `source.md` still has
SHA-256 `090d0d1a2566ee0740d33fd1791b7e36c2778e5122f1ca41d48aaf008101ae83`.
No claim, proof, source, or other frozen evidence was modified.

The review used `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`,
the listed proof, source-comparison file, computational programs and serialized
data, and the relevant primary-source passages. The snapshot-listed research
pass summary was not used to establish any conclusion. No checkpoint, state,
earlier audit, or job transcript was consulted. No additional agents or model
processes were used. This is a fresh review pass, not a claim of statistical
independence, external peer review, or formal proof-assistant certification.

The exact statement reviewed is

\[
 S_k(L_G)\geq S_k(D_G)+1\qquad(1\leq k\leq |G|)
\]

for every nonempty finite abstract simplicial complex whose faces have
cardinality at most two, using the face-intersection matrix and unaugmented
oriented-incidence Dirac matrix in `problem.md`. Sharpness is asserted at
\(k=1\) for one edge and its two vertices. No equality classification beyond
that witness is part of the claim.

## Reconstruction of the decisive argument

Write \(v,e,c\) for the vertex, edge, and component counts, with isolates
included in \(c\), and \(n=v+e\). Nonemptiness gives \(v\geq c\geq1\).
The abstract-complex hypothesis makes the graph simple: there are no loops or
parallel edges. Let \(B,C\) be the unsigned and signed vertex-by-edge incidence
matrices. Entrywise reconstruction gives

\[
 L=\begin{pmatrix}I&B\\B^{\mathsf T}&B^{\mathsf T}B-I\end{pmatrix},
 \qquad D=\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix}.
\]

The bottom-right formula uses both the diagonal value two of
\(B^{\mathsf T}B\) and the fact that distinct edges share at most one vertex.
Thus it is justified throughout the frozen class. Put
\(Q=BB^{\mathsf T}=\Delta+A\), \(H=CC^{\mathsf T}=\Delta-A\),
and let \(q_i,h_i,\delta_i\) be their respective descending eigenvalue and
degree lists, each of length \(v\).

For a positive singular value \(s\) of \(B\), the corresponding block of
\(L\) is \(\left(\begin{smallmatrix}1&s\\s&s^2-1\end{smallmatrix}\right)\).
Its trace is \(s^2\), determinant is \(-1\), and its eigenvalues are
\(f(s^2)\) and \(-1/f(s^2)\), where
\(f(t)=(t+\sqrt{t^2+4})/2\). The kernels of \(B^{\mathsf T}\) and
\(B\) supply the remaining eigenvalues \(+1\) and \(-1\).
Consequently \(L\) has exactly \(v\) positive and \(e\) negative
eigenvalues, with its positive list equal to \(f(q_i)\), including
\(f(0)=1\). In particular,

\[
 S_k(L)=\sum_{i\leq k}f(q_i)\quad(k\leq v),
 \qquad S_k(L)\geq\operatorname{tr}L=n\quad(k\geq v).
\]

The second statement follows by subtracting the omitted negative eigenvalues
from the trace; its inequality direction is correct.

For \(D\), singular values of \(C\) give eigenvalue pairs
\(\pm\sqrt{h_i}\) for the positive \(h_i\). With
\(r=\operatorname{rank}C\leq e\), there are \(n-r\geq v\)
nonnegative Dirac eigenvalues. Therefore the zero-padded identity

\[
 S_k(D)=\sum_{i\leq k}\sqrt{h_i}\quad(k\leq v)
\]

is valid even when \(k>r\). No negative Dirac eigenvalue has inadvertently
entered this range.

The main comparison has two distinct inputs. The rank-\(k\) projection
variational formula, applied to a coordinate projection onto the largest
degrees of \(Q\), gives \(\sum_{i\leq k}q_i\geq\sum_{i\leq k}\delta_i\).
Also \(2\Delta-H=Q\succeq0\), so the eigenvalue min-max principle gives
the **ordered** inequalities \(h_i\leq2\delta_i\). These statements do
not equate the signed and unsigned spectra.

Writing \(R(t)=(\sqrt{t^2+4}-2)/2\), so that
\(f(t)=1+t/2+R(t)\), yields for \(1\leq k\leq v\)

\[
\begin{aligned}
 S_k(L)-S_k(D)
 &\geq\sum_{i\leq k}R(q_i)
       +k+\tfrac12\sum_{i\leq k}\delta_i
       -\sum_{i\leq k}\sqrt{2\delta_i}\\
 &\geq R(q_1)+\tfrac12\sum_{i\leq k}
                    (\sqrt{\delta_i}-\sqrt2)^2.
\end{aligned}
\]

Every replacement has the required direction. In particular,
\(1+\delta/2-\sqrt{2\delta}=(\sqrt\delta-\sqrt2)^2/2\), and the
discarded \(R(q_i)\) are nonnegative.

If the graph is non-bipartite, it contains an odd cycle of length \(\ell\).
The unit vector equal to \(1/\sqrt\ell\) on that cycle and zero elsewhere
has \(Q\)-Rayleigh quotient at least four, since its cycle edges contribute
exactly four and every other edge contributes a nonnegative term. Thus
\(q_1\geq4\), and the displayed gap is at least
\(R(4)=\sqrt5-1>1\). This works unchanged in disconnected graphs.

If the graph is bipartite, the diagonal matrix of its vertex colors conjugates
\(H\) to \(Q\), including all zero eigenvalues and isolated vertices.
Here \(h_i=q_i\), and
\(f(t)\geq1+t/2\geq\sqrt t+1/2\) gives gap at least \(k/2\)
for \(2\leq k\leq v\). The remaining endpoint \(k=1\) follows from
the entrywise relation \(|D|+I\leq L\): replacing a real unit vector by
its coordinatewise absolute value and applying Rayleigh's principle gives
\(\lambda_1(D)\leq\lambda_1(L)-1\). This argument uses entrywise
nonnegativity only on a nonnegative vector; it makes no false Loewner-order
inference.

For the tail, the quadratic form of \(H\) shows that its kernel consists
exactly of functions constant on each connected component, so \(r=v-c\).
For every \(k\), \(S_k(D)\) is at most its positive spectral sum. Since
\(\sqrt t\leq(t+1)/2\) and \(\operatorname{tr}H=2e\), that sum is at
most \(e+r/2\). Hence for \(v\leq k\leq n\),

\[
 S_k(L)-S_k(D)\geq n-e-r/2=(v+c)/2\geq1.
\]

The ranges cover every asserted \(k\), including their common endpoint.
For an edgeless nonempty complex, one can additionally check directly that
\(L=I_v,D=0\), so the gap is \(k\). The empty complex is outside the
candidate's nonempty domain. Orientation changes and face permutations only
produce orthogonal conjugations of the relevant matrices. An unfilled
triangle is included; a filled triangle is outside this theorem.

Finally, direct exact diagonalization for one edge gives
\(\operatorname{spec}L=(1+\sqrt2,1,1-\sqrt2)\) and
\(\operatorname{spec}D=(\sqrt2,0,-\sqrt2)\). The top-eigenvalue gap is
exactly one. This verifies the sharpness asserted in the frozen claim.

## Independent computations actually performed

The new program `audit/referee-verifier.py` imports no proposer program and
writes only `audit/referee-verification.json`. It was run successfully as

```sh
OPENBLAS_NUM_THREADS=1 python3 audit/referee-verifier.py
```

Its exact checks reconstruct matrices entry by entry from face intersections
and oriented subset incidence. For the supplementary five-vertex census it
independently enumerates the downset lattice by allowable single-face
additions, obtaining 7,579 nonempty complexes. Every complex can be reached
by adding its faces in increasing cardinality, which justifies completeness.
The 208 recorded representatives have pairwise disjoint permutation orbits
whose union is precisely that enumeration, with all orbit sizes matching.

For all 208 certificates, the independently built integral matrices and their
characteristic polynomials match the supplied data. Squarefree factorization
and exact rational Sturm root counts verify each stored root interval,
multiplicity, and descending order, instead of rerunning the original root
isolation code. All 3,151 representative partial-sum lower bounds recompute
exactly and are positive; the orbit coverage represents 113,716 labeled
partial sums. The minimum rational lower bound is
`1583407980/1583407981`. This verifies a finite strictly-positive observation,
not an additive-one certificate for arbitrary higher-dimensional complexes.

The independent graph screen reconstructs all 33,867 labeled graphs on one
through six vertices and checks all 453,098 partial sums and the intermediate
proof inequalities. It also tests 16 additional specified graphs, including
paths, odd cycles and stars on 33, 41 and 61 vertices, complete graphs,
complete bipartite graphs, and a triangle with a matching and 38 isolates.
All assertions passed. Matrix identities are exact integer calculations;
these spectral screens use float64 and tolerance `2e-6`. Their smallest gap,
`0.9999999999999996`, is a rounding-level screen result. The universal theorem
and exact constant follow from the proof and the symbolic one-edge witness,
not from numerical tolerances. The supplied original screen was inspected
but was not rerun to overwrite frozen evidence.

## Primary-source comparison and contribution

The live [Knill v2 paper](https://arxiv.org/html/2601.18071v2), dated 29 July
2026, was checked at Sections 1.1, 1.6--1.7 and 5.1--5.5. Its incidence
convention and decreasing spectral sums match the frozen interpretation.
Conjecture 1 states the arbitrary-dimensional comparison. The inspected
attempts supply no all-partial-sum graph proof. The archived source's Section
10.3 concerns the inverse-matrix question, which is separate from this claim.

The author's [August 2025 post](https://www.quantumcalculus.org/connection-and-dirac-matrix/),
particularly its August 17 and August 21 updates, already proposes the
additive-one inequality and sharpness as experimental observations. The
strengthening must therefore be attributed to Knill. Its conjectural
formulation is not the new contribution.

The nearest established spectral tool is the unsigned hydrogen identity in
[Knill, *The hydrogen identity for Laplacians*](https://arxiv.org/pdf/1803.01464),
Theorem 1, Section 2.4. I checked its setting and statement, Sections
1.4 and 2.1--2.7 concerning signed versus unsigned incidence and spectral
radius, and the Schur discussion in Section 2.17. These provide unsigned
spectral information and the bipartite relationship; the inspected results
do not supply the needed general signed all-partial-sum comparison. The
candidate derives its required spectral transform directly, so no disputed
or uninspected source proof is a premise.

Independent searches on 2026-09-14 included:

- `"connection" "Dirac" "spectral sums" graph proof`
- `"Knill" "majorization" "signless"`
- `"connection Laplacian" "Dirac" inequality graph`
- `"2601.18071" proof domination`
- `"connection matrix" "Dirac" "additive"`
- `"hydrogen identity" "majorization"`
- `"Knill" "S_k" "graph" "Dirac"`

No equivalent graph theorem was found in these searches and the inspected
primary sources. Search snippets and unrelated continuous-Dirac results were
not used as mathematical premises. This is a bounded literature conclusion,
not an exhaustive priority certificate.

The precise delta is a proof, with optimal uniform constant, of the entire
dimension-at-most-one subclass of a previously stated conjecture. The bridge
from unsigned incidence to all signed Dirac partial sums for non-bipartite
graphs is supplied by the degree-majorization estimate and cycle bound;
spectral-radius domination alone does not give it. This is a substantive
uniform partial theorem on a natural unrestricted graph class, rather than
a finite census or arbitrary restricted family. It can serve as the settled
graph baseline for the remaining higher-dimensional problem. Elementary
ingredients and a short proof do not remove that contribution. The overlapping
bipartite and non-bipartite arguments should remain in one coherent note.

## Gaps, limits, and disposition

No correctness, scope, or contribution gap requiring revision was found in
the frozen candidate. The review did not repair or replace any substantive
claim. The original arbitrary-dimensional assertion remains unresolved;
publication priority is limited to the explicit source search above. No
manuscript, citation/build/visual approval, or publication release is created
by this mathematical acceptance.

Next step: the runner should execute its `check-math` provenance and integrity
gate, then dispatch writing for exactly the accepted graph theorem, preserving
the attribution of the additive-one conjecture and the original unresolved
status. No further mathematical test is required for acceptance of this
snapshot.
