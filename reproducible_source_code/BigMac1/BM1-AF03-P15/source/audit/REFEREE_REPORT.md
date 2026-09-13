# Independent full-DAG referee report: D9 normalized-flow endpoint

Date: 2026-08-29 (Asia/Shanghai)  
Endpoint: **`Abs(D_9) admits a normalized flow with unit vertex weights`**  
Decision: **PASS — certified finite result**  
Unresolved severity counts: **fatal 0; major 0; local 0; expository 0**

This decision is only for the fixed (D_9) endpoint in
`problem/formal_statement.md`. It is not an all-(n) theorem, a uniqueness
claim, a strict-positive-on-every-cover claim, or a rank-symmetry claim. No
proof assistant was used.

## 1. Trust boundary and frozen hashes

I did not import or execute anything in `src/`, `discovery/`, or `tests/`, and
did not import or execute `certificates/verify_d9_flow.py`. The two
cross-check-only code/data paths were hashed as raw bytes and were not used as
mathematical evidence. I did not use a discovery output in the proof.

The first check was the following raw command:

```console
$ shasum -a 256 certificates/d9_normalized_flow.json certificates/verify_d9_flow.py problem/formal_statement.md discovery/d9_orbit_flow_candidate.json tests/verify_breaker_orbit_candidate.py literature/sources/carter-1972.pdf
d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f  certificates/d9_normalized_flow.json
a076f7dc4a715d0adb9d1c7b7946431a7f63de744b53a8782a6c50ed7580c706  certificates/verify_d9_flow.py
a423a584b8a229845dc64dbca6233df9d7d36ca7d9a0c1a5de55571d54aca084  problem/formal_statement.md
1139852c155f754f6b998b15bf3fcd0f42942351a609e283615cb7599002beca  discovery/d9_orbit_flow_candidate.json
fb1e14209cbdb299a98c7049c8c0b23c8ad0467070c3ef06b9d445fbeb6284da  tests/verify_breaker_orbit_candidate.py
9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5  literature/sources/carter-1972.pdf
```

Every value equals the corresponding value frozen in
`certificates/PRIMARY_D9_BINDING.json`. The starting human artifacts have
these additional byte hashes:

```console
6440797ce594b1e07365e97f251b6796d0d3afc5acc8a23a63ca22d99de75e57  certificates/PRIMARY_D9_BINDING.json
c8d28ef4ed688098a4383bc8f46653ea325a72058d958c2d07a38a694a12e666  proof/proof_dag.md
38974a62bd726cc28907327131326887153a4093561a5e1d71080cbb698d0efa  proof/carter_binding.md
```

Thus the certificate, formal statement, frozen release verifier, frozen
cross-check artifacts, and Carter dependency were all byte-consistent before
the mathematical audit began.

## 2. Independent verifier and raw result

I wrote `audit/referee_verify_d9.py` from a fresh signed-permutation model.
It uses only Python's standard library. Its only serialized mathematical
input is the primary JSON certificate; it reads its own source only to report
the verifier hash. It accepts no discovery file and imports no project
module.

The code builds one canonical signed permutation for each signed-cycle type
and right-multiplies it by every one of the 72 reflections. It repeats this
from both endpoints of each adjacent-rank pair, rather than encoding the
three schematic cover rules. Consequently source degree, target degree,
support, and edge count are independently reconstructed.

Raw command and output:

```console
$ python3 -I -S audit/referee_verify_d9.py
{"allowed_orbit_pairs":609,"allowed_pairs_by_layer":[1,3,9,22,50,97,156,175,96],"endpoint":"Abs(D_9) admits a normalized flow with unit vertex weights","full_hasse_covers":3344302080,"full_hasse_covers_by_layer":[72,5112,154728,2603160,26569368,168006888,640430712,1338965640,1167566400],"group_order":92897280,"input_sha256":"d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f","integer_scales_by_layer":[72,13320,7086240,369518688,26070515856,7585974219600,1641936765600,106340457307680,12545192860200],"mutation_tests":{"altered_rank_size":"REJECTED","hash_mismatch":"REJECTED","missing_flow":"REJECTED","missing_layer":"REJECTED","negative_rational":"REJECTED","noncanonical_rational":"REJECTED","wrong_edge_count":"REJECTED","wrong_multiplicity":"REJECTED","wrong_orbit_endpoint":"REJECTED"},"n":9,"orbits":150,"positive_flows_by_layer":[1,3,7,15,27,45,65,72,49],"positive_orbit_flows":284,"rank_orbit_counts":[1,1,3,5,11,17,29,35,34,14],"rank_sizes":[1,72,2220,38304,405174,2702448,11228300,27491616,34812945,16216200],"rank_symmetric":false,"reflections":72,"status":"VERIFIED","verifier_sha256":"2b2ff8f48853ed534c7d98dc6e8aab45b0413871029b35ba80f1cbd62078a8c4"}
```

Static import audit and hashes:

```console
$ rg '^(from|import) ' audit/referee_verify_d9.py
from __future__ import annotations
import copy
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import sys

$ shasum -a 256 audit/referee_verify_d9.py certificates/d9_normalized_flow.json
2b2ff8f48853ed534c7d98dc6e8aab45b0413871029b35ba80f1cbd62078a8c4  audit/referee_verify_d9.py
d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f  certificates/d9_normalized_flow.json
```

The `-I -S` run disables user environment paths and automatic `site`
initialization. All calculations use integers or `fractions.Fraction`; no
floating-point value occurs in parsing or verification.

## 3. Human dependency DAG audit

### L1: the (B_9) action, including split (D_9)-classes

The product of the nine window signs is a homomorphism
(B_9\to\{\pm1\}), and (D_9) is its kernel. Hence (D_9\triangleleft B_9).
A signed coordinate permutation sends every root (pm e_i\pm e_j) to
another root of this form, so conjugation by (B_9) permutes exactly the 72
(D_9) root reflections. It therefore preserves (ell_T), absolute order,
ranks, and covers.

The orbits used here are deliberately (B_9)-orbits, not (D_9)-conjugacy
classes. A full (B_9)-class of signed-cycle type ((\lambda,\mu)) lies in
(D_9) exactly when (ell(\mu)) is even. Any splitting of a (B_9)-class
into two (D_9)-classes is therefore re-fused by the valid (B_9)
automorphism action. No split class is omitted or double counted.

### L2: orbit classification, parity, and centralizers

(B_9=C_2\wr S_9) conjugacy classes are the positive/negative signed-cycle
bipartitions. On a signed cycle, the parity of negative window entries is odd
exactly for a negative cycle; hence total window parity is
(ell(\mu)\bmod2). Exhaustive partition generation gives exactly 150 types
with (|\lambda|+|\mu|=9) and even (ell(\mu)).

For (m) signed cycles of one fixed length (k) and one fixed sign, the
centralizer contribution is ((2k)^m m!): a single signed cycle has (2k)
internal commuting signed rotations, and equal cycles may be permuted. Cycles
of different length or sign cannot be interchanged. Multiplication over all
parts gives

\[
|C_{B_9}(w)|=2^{\ell(\lambda)+\ell(\mu)}z_\lambda z_\mu,
\qquad
|B_9\cdot w|=\frac{2^9 9!}
 {2^{\ell(\lambda)+\ell(\mu)}z_\lambda z_\mu}.
\]

Every division was checked integral. The 150 orbit masses sum to
(92{,}897{,}280=2^8 9!), so orbit conservation is exact.

### L3: Carter Lemma 2 and applicability to exactly (T)

The citation claims were frozen before source checking:

| ID | Frozen claim | Type |
|---|---|---|
| C1 | The cited Carter article exists with the stated 1972 Compositio metadata. | bibliographic existence |
| C2 | Lemma 2 on journal p. 3 identifies root-reflection length with the number of non-(1) eigenvalues. | attributed theorem |
| C3 | Carter's reflection set is exactly the formal (D_9) set (T). | applicability inference |

The [official NUMDAM record](https://www.numdam.org/item/CM_1972__25_1_1_0/)
verifies R. W. Carter, *Conjugacy classes in the Weyl group*, *Compositio
Mathematica* 25 (1972), no. 1, pp. 1–59. The official PDF and the retained
PDF are byte-identical:

```console
$ shasum -a 256 literature/sources/carter-1972.pdf /tmp/carter-1972-official.XXXXXX.pdf
9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5  literature/sources/carter-1972.pdf
9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5  /tmp/carter-1972-official.XXXXXX.pdf
$ cmp -s literature/sources/carter-1972.pdf /tmp/carter-1972-official.XXXXXX.pdf
# exit 0
```

Journal page 3 first defines (l(w)) as the minimum number of reflections
(w_r), with (r) ranging over the root system, and then states in Lemma 2
that it is “the number of eigenvalues of (w) on (V) which are not equal
to 1.” Thus C1 and C2 are verified exactly.

For (D_9), the root system is
({\pm e_i\pm e_j:1\le i<j\le9}). Roots differing by sign define the
same reflection. For each pair (i<j), the two distinct root-reflection
actions are the unsigned swap and the swap with both signs negated. These
are exactly the (2\binom92=72) members of formal (T). Therefore C3 is a
verified inference, and Carter's length is neither simple Coxeter length nor
a larger (B_9)-reflection length.

A positive signed cycle contributes one fixed dimension; a negative signed
cycle contributes zero. Disjoint cycle supports are a direct sum. Carter
therefore gives
(ell_T(w)=9-ell(\lambda)), including 1-cycles, repeated parts, the
identity, and the rank-9 types with no positive cycles.

### L4: exhaustive upward covers and multiplicities

For every one of the 150 types, the fresh verifier constructs a canonical
window representative and computes (wt) for all 72 explicitly constructed
members (t\in T). The signed-cycle type and rank of every product are
recomputed from its window. Exactly the products whose rank rises by one are
the quotient supports. Since every formal cover is, by definition, such a
right multiplication, this is exhaustive and includes no non-cover.

This representative calculation applies to a whole orbit: if
(w'=gwg^{-1}), then (t\mapsto gtg^{-1}) is a bijection of (T) and
(w'(gtg^{-1})=g(wt)g^{-1}). Thus type multiplicities are constant on each
source orbit. A separate downward enumeration from each target canonical
representative gives (d^-_{A,B}). For every support the verifier requires

\[
|A|d^+_{A,B}=|B|d^-_{A,B}=E(A,B).
\]

This establishes cover support, both degrees, biregularity divisibility, and
the full orbit-pair edge count without importing the three-rule code or its
formula. The result has 609 supported orbit pairs and 3,344,302,080 full
Hasse covers. Independently, the global count equals
(|D_9|\,|T|/2=92{,}897{,}280\cdot72/2), as it must because every
element-reflection incidence is one endpoint of exactly one cover.

### L5–L7: exact quotient flow and full-poset lift

The JSON contains 284 positive orbit-pair totals (F(A,B)); the remaining
325 supported pairs carry zero. For every serialized flow the verifier checks
strict endpoint membership, rank adjacency, reconstructed support,
(d^+), (d^-), (E), and the reduced positive rational (F). It also
checks the serialized per-edge rational is exactly (F/E).

For every orbit in every layer, the exact checked marginals are

\[
\sum_BF(A,B)=\frac{|A|}{|P_r|},\qquad
\sum_AF(A,B)=\frac{|B|}{|P_{r+1}|}.
\]

Putting (F(A,B)/E(A,B)) on each full-poset edge gives at a fixed
(x\in A)

\[
\sum_{y\in B}f(x,y)=d^+_{A,B}\frac{F(A,B)}{E(A,B)}
=\frac{F(A,B)}{|A|},
\]

and analogously (F(A,B)/|B|) at a target vertex. The verifier recomputes
these lifted sums directly and requires (1/|P_r|) and (1/|P_{r+1}|) at
every orbit type. This is the precise unit-vertex-weight normalized-flow
endpoint.

For an independent integer exactness check, every (F) is multiplied by
(L_r=\operatorname{lcm}(|P_r|,|P_{r+1}|)). Every result must be a positive
integer, and the cleared row, column, and total equations must hold exactly.
No rational normalization or sign is trusted from cached metadata.

The historical constructor-equivalence and small-(n) regression statements
inside L6–L7 were not used or endorsed: those paths are outside the mandated
trust boundary. They are unnecessary for the endpoint because the primary
certificate itself is a finite witness and the fresh verifier reconstructs
all structural and marginal claims.

## 4. Exact counts by rank layer

The 150 orbit counts by rank are

\[
(1,1,3,5,11,17,29,35,34,14).
\]

The exact full rank sizes are

\[
(1,72,2220,38304,405174,2702448,11228300,27491616,34812945,16216200).
\]

They are all nonzero and sum to (92{,}897{,}280). They are visibly not
palindromic; the verifier reports `rank_symmetric:false` and never reflects
or copies a layer.

| ranks | lower size | upper size | allowed pairs | positive (F) | (L_r) | full covers |
|---:|---:|---:|---:|---:|---:|---:|
| 0–1 | 1 | 72 | 1 | 1 | 72 | 72 |
| 1–2 | 72 | 2,220 | 3 | 3 | 13,320 | 5,112 |
| 2–3 | 2,220 | 38,304 | 9 | 7 | 7,086,240 | 154,728 |
| 3–4 | 38,304 | 405,174 | 22 | 15 | 369,518,688 | 2,603,160 |
| 4–5 | 405,174 | 2,702,448 | 50 | 27 | 26,070,515,856 | 26,569,368 |
| 5–6 | 2,702,448 | 11,228,300 | 97 | 45 | 7,585,974,219,600 | 168,006,888 |
| 6–7 | 11,228,300 | 27,491,616 | 156 | 65 | 1,641,936,765,600 | 640,430,712 |
| 7–8 | 27,491,616 | 34,812,945 | 175 | 72 | 106,340,457,307,680 | 1,338,965,640 |
| 8–9 | 34,812,945 | 16,216,200 | 96 | 49 | 12,545,192,860,200 | 1,167,566,400 |
| **total** | — | — | **609** | **284** | — | **3,344,302,080** |

## 5. Fail-closed audit

The strict parser rejects duplicate keys, floats, non-finite numbers, unknown
or missing fields, booleans in integer fields, and noncanonical rationals.
The default run first enforces the frozen primary SHA-256. The structural
mutations below intentionally bypass only that outer hash check so that a
rejection demonstrates the relevant internal check rather than a generic
hash failure.

| mutation | result | decisive check |
|---|---|---|
| append one byte / hash mismatch | REJECTED | frozen SHA-256 |
| remove a rank layer | REJECTED | exactly ranks 0 through 8 required |
| remove a positive flow | REJECTED | exact row/column marginal |
| substitute a valid orbit of the wrong rank | REJECTED | endpoint rank and support |
| alter `degree_from` | REJECTED | representative-times-reflections multiplicity |
| alter `edge_count` | REJECTED | (|A|d^+=|B|d^-=E) |
| make a numerator negative | REJECTED | positive serialized-flow convention |
| replace (1/1) by (2/2) | REJECTED | `gcd(numerator,denominator)==1` |
| alter a declared rank size | REJECTED | recomputed orbit-mass rank total |

All nine mutations are executed on every successful verifier run and are
reported individually as `REJECTED`.

## 6. Severity table and decision

“Severity if unresolved” records the consequence that a failure would have;
it is not an assertion that an issue remains.

| ID | dependency/question | severity if unresolved | result | independent closure |
|---|---|---:|---|---|
| R1 | Frozen primary and dependency hashes | fatal | PASS | all six binding values match |
| R2 | Formal statement matches certificate endpoint | fatal | PASS | exact claim, (n=9), nine layers |
| R3 | (B_9) acts by poset automorphisms; split classes handled | fatal | PASS | normality and root-set invariance; actual (B_9)-orbits |
| R4 | Signed-cycle parity, orbit count, centralizer masses | fatal | PASS | derivation plus 150-type and group-order conservation |
| R5 | Carter Lemma 2 applies to exactly (T) | fatal | PASS | official p. 3 checked; (D_9) roots give the exact 72 reflections |
| R6 | Rank formula and all rank totals | fatal | PASS | fixed spaces plus exact orbit aggregation |
| R7 | Cover support and both multiplicities exhaustive | fatal | PASS | canonical representatives × all 72 reflections in both directions |
| R8 | Biregularity and orbit edge conservation | fatal | PASS | every (|A|d^+=|B|d^-) checked |
| R9 | Quotient marginals and (F/E) full lift | fatal | PASS | exact `Fraction` and direct per-vertex equations |
| R10 | Rational/integer exactness; no rank symmetry shortcut | fatal | PASS | reduced rationals, LCM-cleared integers, all nine layers |
| R11 | Fail-closed behavior | major | PASS | nine targeted mutations rejected |
| R12 | Scope does not overclaim all (D_n) | major | PASS | endpoint and report restricted to (D_9) |

Final unresolved counts:

| severity | unresolved count |
|---|---:|
| fatal | **0** |
| major | **0** |
| local | **0** |
| expository | **0** |

Accordingly, the exact finite endpoint is accepted as a **certified finite
result**: the frozen primary JSON supplies rational nonnegative flow totals
whose independently reconstructed uniform (F/E) lift is a normalized flow
on every cover layer of (operatorname{Abs}(D_9)).
