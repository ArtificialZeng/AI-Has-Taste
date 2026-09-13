# Gate 5 independent referee report

Date: 2026-08-29 (Asia/Shanghai)  
Role: independent referee; no participation in witness construction or prose
polishing  
Endpoint audited: problem/formal_statement.md, statement (N9)  
Final disposition: **PASS — no open fatal or major mathematical/certificate
issue**

The audited artifacts support the terminal classification
CERTIFIED_FINITE_RESULT: for every graph \(G\) on nine vertices with
\(e(\overline G)\le 6\), \(q(G)=2\). They also independently reconstruct the
published \(n=7,8\) baselines. This is a finite theorem only; it is not a proof
of the all-orders conjecture.

## Independence and frozen inputs

I read the complete prove-or-disprove-math skill and its
research-workflow.md, research-governance.md, and certificate-playbook.md
before auditing. I did not import any module under discovery/, did not use a
cached floating-point objective, and did not use the discovery enumeration
output as a premise.

Final hashes checked in this audit were:

| Artifact | SHA-256 |
|---|---|
| certificates/n9_exact_frames.json | d78b49e23eaebba29d0ab70661df9688a09baabce7e0333040b43186a808fd5d |
| verification/verify_n9_certificate.py | 5b298d8cac3eb4a890308475aa0f93f2dd0565e76d6150902b7737e3f2b49613 |
| verification/test_fail_closed.py | 5c4b4d28409e5e88720995d7dd3337172db6e0a8d6d6d1fd4aae9cac6859175a |
| problem/formal_statement.md | 3e60ff660097b314c63ca2a3fffb4874b58ba3df51fd4b092c41da70efdd02a9 |
| literature/claim_ledger.md | d13f3a01a672897ea539fb5669a154fc7c9d0a20fbc9c84f812f8759d1baf3f2 |

The local journal PDFs for Barrett et al. and Fallat–Mojallal had hashes
c1adfc9bfcc3882c15cd53395d78de73032ac943b3f14ae7a4cf1350262e3962 and
45158aa30bd2f938e70c0a60948bdc6bbc353fe75a3714f70e8d1f231d1bde8a,
respectively. I also independently retrieved the open repository copy of
Levene–Oblak–Šmigoc, *Distinct eigenvalues are realizable with generic
eigenvectors*, from the University of Ljubljana repository; that PDF had
SHA-256
371e9870b4d4febc74fa81e03a2eec178c2798f0ff93fa8810fba3fd7cd1a53b.

## Reconstruction from the definitions

### 1. Isomorphism reduction and complete enumeration

The reduction to one representative per graph-isomorphism class is valid:
if a permutation matrix \(\Pi\) relabels \(G\) to \(G'\), then
\(A\mapsto\Pi A\Pi^\top\) is a spectrum-preserving bijection from \(S(G)\)
to \(S(G')\). Hence \(q(G)=q(G')\).

Let \(H=\overline G\). Every nontrivial connected component \(C\) of an
\(H\) with at most six edges satisfies

\[
 |V(C)|-1\le |E(C)|\le 6,
\]

so it has at most seven vertices. Thus every possible nontrivial component
occurs among the connected graph-atlas entries of orders \(2,\ldots,7\) with
at most six edges. Isolated vertices are then forced by the remaining order.

The recursive enumeration chooses a nondecreasing multiset of catalogue
indices. It has no repetition: the catalogue is checked pairwise for
isomorphic duplicates, and uniqueness of decomposition into connected
components makes two different component-type multisets nonisomorphic. It is
complete because every \(H\) has exactly such a multiset.

The verifier adds a genuinely different exact cardinality check. For every
cycle type of \(S_n\), it computes the orbits of the induced permutation on
unordered vertex pairs. A fixed edge set is a union of these orbits, so its
edge enumerator is

\[
 \prod_O(1+x^{|O|}).
\]

Weighting by exact conjugacy-class sizes and dividing by \(n!\) is Burnside's
lemma. The resulting counts agree edge-by-edge with the component-multiset
enumeration. I additionally reran nauty geng, independently of both the atlas
and the stored discovery output, obtaining totals \(19,44,108\) for
\(n=7,8,9\), respectively. A separate bit-graph implementation reproduced
the route split, and nauty canonical labeling showed that the residual
classes and stored witnesses agree as exact sets, with no duplicate witness.

| \(n\) | all classes | bipartite route | join route | exact-frame route |
|---:|---:|---:|---:|---:|
| 7 | 19 | 16 | 2 | 1 |
| 8 | 44 | 33 | 10 | 1 |
| 9 | 108 | 72 | 24 | 12 |

The exact edge-stratum totals independently obtained were
\((1,1,2,5,10)\), \((1,1,2,5,11,24)\), and
\((1,1,2,5,11,25,63)\). In the \(n=9\) exact-frame route, one witness has five
edges and eleven have six; this is compatible with claim C13 because C13 is
the *literature-only* frontier, while the verifier deliberately routes only
through the bipartite and balanced-join theorems before using frames.

### 2. Bipartite route

The sparse graph enumerated by the verifier is \(H=\overline G\), not \(G\).
For each of the 72 \(n=9\) classes detected as bipartite, the hypotheses are
exactly

\[
 H=\overline G\text{ bipartite},\qquad e(H)\le 9-3.
\]

Barrett–Fallat–Furst–Nasserasr–Rooney–Tait, Theorem 3.7, states precisely
that this implies \(q(G)=2\) for order \(n\ge3\). The source, theorem number,
inequality endpoint, and complement direction all match. This validates C04
and the bipartite_complement binding in the certificate.

### 3. Balanced connected-join route

Suppose the verifier partitions the connected components of \(H\) into two
nonempty unions \(H_L,H_R\). There are no \(H\)-edges between these unions,
so complementation gives the exact identity

\[
 G=\overline H=\overline{H_L}\vee\overline{H_R}.
\]

The code checks that \(X=\overline{H_L}\) and
\(Y=\overline{H_R}\) are connected and that
\(\bigl||V(X)|-|V(Y)|\bigr|\le2\). Levene–Oblak–Šmigoc, Theorem 3.4,
with \(k=1\), then states \(q(X\vee Y)=2\). I checked this in the primary
paper, not only in Barrett et al.'s Proposition 1.6 restatement. The theorem
also permits a one-vertex connected factor, so no endpoint used by the code is
lost. Claim C09 and the external-theorem certificate binding are exact.

### 4. Exact Parseval-frame route

For a stored witness, let \(w_i\in\mathbb Q^3\) be its direction row and let
\(x_i\in\mathbb Q_{>0}\) be its weight. Define the real matrix

\[
 V_{i\bullet}=\sqrt{x_i}\,w_i,\qquad P=VV^\top.
\]

The verifier checks, using fractions.Fraction only,

\[
 \sum_i x_iw_iw_i^\top=I_3.
\]

Hence \(V^\top V=I_3\), and consequently

\[
 P^2=V(V^\top V)V^\top=P,\qquad \operatorname{rank}P=3.
\]

For \(i\ne j\),

\[
 P_{ij}=\sqrt{x_ix_j}\,\langle w_i,w_j\rangle.
\]

Positivity of both weights proves, without a numerical tolerance, that
\(P_{ij}=0\) iff the rational dot product is zero. The verifier checks that
this happens iff \(ij\in E(H)\). Therefore \(Q=I-2P\) is real symmetric,

\[
 Q^2=I,\qquad
 Q_{ij}\ne0\iff ij\notin E(H)\iff ij\in E(G)\quad(i\ne j).
\]

Thus \(Q\in S(G)\). Since \(0<3<n\), the eigenvalues of \(Q\) are
\(-1\) with multiplicity \(3\) and \(+1\) with multiplicity \(n-3\). Both
occur, so \(q(Q)=2\). As every graph in the endpoint is nonempty,
\(q(G)\ne1\), and hence \(q(G)=2\).

I recomputed all six entries of \(V^\top V\) and every pairwise rational dot
product for all 14 witnesses with a second implementation using SymPy
Rational. All 14 passed. This second implementation did not import the
verifier or discovery code.

### 5. Baselines and literature ledger

The exact enumeration and witness checks above cover the full endpoints
\(n=7,e(H)\le4\) and \(n=8,e(H)\le5\), so the baselines are reconstructed
rather than assumed. Fallat–Mojallal Theorems 22 and 23 independently state
the same two endpoints, as recorded in C05.

The checked theorem claims C02–C05 and C09 match their primary sources. C13
is also correct: a nonbipartite nine-vertex graph with at most five edges has
at least two isolated vertices (a nonbipartite component consumes at least
three edges, and the remaining at most two edges can cover at most four more
vertices). Observation 5.1 plus the order-at-most-eight baseline therefore
leaves only the nonbipartite six-edge literature frontier. Negative novelty
claims C06–C07 remain explicitly limited to the recorded searches; they are
not mathematical premises of this finite certificate and still require the
contracted second search before release.

## Adversarial parser and trust audit

The original verifier accepted malformed-but-semantically-shadowed JSON,
including duplicate keys, nonstandard JSON constants in ignored provenance,
and incorrect JSON scalar types. This was a **major fail-closed gate issue**,
reported immediately. After the first repair I found further bypasses:
a float in endpoint.orders_certified, noncanonical extended-order or nonzero
padding encodings of graph6, and noncanonical diagnostic decimal strings.
These were also reported immediately.

Both issues are resolved in the final verifier hash recorded above. The
parser now rejects duplicate keys at every nesting depth, NaN and
±Infinity, unknown/missing keys, wrong null/bool/float types, noncanonical
rationals, noncanonical graph6 encodings, malformed route counts, and
noncanonical diagnostic decimals. The valid certificate passes and all 18
maintained mutation tests are rejected. I then reran a separate sweep of the
10 earlier bypass strings; all 10 were rejected.

The verifier does **not** trust discovery floating point. The only decisive
quantities are rebuilt from graph6, exact rational directions, and exact
positive rational weights. discovery_only and discovery_provenance are
schema-checked diagnostics and do not control enumeration, routing, support,
Parseval, or success. No discovery module is imported.

## Findings by severity

### Fatal

None found.

### Major

1. **REF-M01 — fail-closed JSON/type violations. Resolved.** Duplicate keys,
   nonstandard constants, and loose integer typing were initially accepted.
   The final parser rejects them and regression tests cover them.
2. **REF-M02 — endpoint/graph6 canonicality violations. Resolved.** A float
   endpoint order and alternate graph6 encodings were initially accepted.
   Strict endpoint typing and graph6 round-trip equality now reject them.

There is no open major issue after the final rerun.

### Local

None affecting correctness. orthogonality_order and the discovery diagnostics
are algebraically unused metadata; retaining them is harmless because their
schemas are checked and no proof branch reads their numerical claims. They
must continue to be described as non-certifying provenance.

### Expository

1. The human proof should explicitly state permutation-similarity invariance
   and uniqueness of the connected-component multiset; the code is correct,
   but these two sentences make the enumeration proof self-contained.
2. It should say immediately that each graph6 string encodes
   \(H=\overline G\), so the zero/nonzero direction of the frame condition
   cannot be reversed by a reader.
3. It should distinguish the 12 residuals after the verifier's two routing
   theorems from the smaller literature-only frontier; the former includes
   one five-edge witness and this is not a contradiction.
4. The projection argument should state the multiplicities \(3\) and \(n-3\),
   rather than only saying that both eigenvalues occur.

## Commands rerun

The following commands were rerun:

    python verification/verify_n9_certificate.py certificates/n9_exact_frames.json
    python verification/test_fail_closed.py
    geng -q 7 0:4 | wc -l
    geng -q 8 0:5 | wc -l
    geng -q 9 0:6 | wc -l

The final verifier printed status VERIFIED, the route counts in the table
above, 14 frame witnesses, certificate and verifier hashes, and
proof_assistant none. The mutation suite printed:

    PASS: valid certificate accepted; 18 damaged certificates rejected

No Lean, Coq, Isabelle, or other proof assistant was used. The certified
endpoint is supported by exact rational arithmetic, exact finite graph
enumeration, two verified published theorems, and independent executable
cross-checks.
