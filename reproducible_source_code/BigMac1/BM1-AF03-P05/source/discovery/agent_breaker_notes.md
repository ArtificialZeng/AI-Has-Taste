# Breaker branch: exact enumeration and counterexample search

Date: 2026-08-29 (Asia/Shanghai)  
Role: counterexample hunter / canonical-enumeration checker  
Status: discovery plus two exact structural obstructions; **not a proof of (N9)**

## 1. Scope and conclusion

This branch independently enumerated the non-bipartite complements
\(H=\overline G\) on nine vertices with at most six edges, and searched the
corresponding projection equations in every rank stratum that can matter.

The main breaker outcome is negative: no candidate counterexample was found.
Every one of the 36 isomorphism types has a well-separated floating-point
rank-four projection candidate in two parameterizations.  This is discovery
evidence only.  It is not an exact witness and is not promoted to a theorem.

Three graphs provably cannot be realized in rank three.  They all have
rank-four numerical candidates and all are covered by the builder's join
criterion, so they are not counterexamples to \(q(G)=2\).

## 2. Isomorph-free enumeration

### 2.1 Generator and independent checks

The generator was Homebrew nauty 2.9.3:

```sh
geng -q 9 0:6
geng -q -b 9 0:6
```

The unrestricted stream contains 108 isomorphism types and the bipartite
stream contains 72.  `breaker_enumerate.py` independently implements:

1. strict small-\(n\) graph6 decoding and round-trip encoding;
2. exact edge counts;
3. BFS bipartiteness;
4. an exact canonical label obtained by trying every permutation inside
   degree cells, with the cells themselves fixed in increasing degree order.

Any isomorphism preserves degrees, so the fourth check loses no possible
isomorphism.  The 108 unrestricted canonical labels are pairwise distinct.
The pure-Python bipartite subset is exactly the canonical set emitted by
`geng -b`.  Subtraction gives:

| \(e(H)\) | all | bipartite | non-bipartite |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 5 | 4 | 1 |
| 4 | 11 | 9 | 2 |
| 5 | 25 | 17 | 8 |
| 6 | 63 | 38 | 25 |
| total | 108 | 72 | 36 |

The graph6 list and a record-by-record manifest are
`breaker_n9_nonbip_e_le6.g6` and `breaker_enumeration_manifest.json`.

Important limitation: the independent Python canonicalizer proves that the
emitted stream has no isomorphic duplicates and verifies every filter.  It
does not independently prove that nauty's canonical augmentation omitted no
isomorphism class.  Completeness of the enumeration still relies on `geng`
2.9.3.  A release-grade finite certificate should either cite/audit nauty's
algorithm or reproduce the same canonical set with a genuinely independent
complete generator.

### 2.2 Reproduction and fail-closed tests

From the project root:

```sh
python3 discovery/breaker_enumerate.py
python3 discovery/breaker_enumerate.py --verify
python3 discovery/breaker_test_enumeration.py
```

The verifier freezes the expected non-bipartite profile
\((0,0,0,1,2,8,25)\), checks the graph6 SHA-256, and reconstructs all graph
properties from the list rather than importing generator metadata.  Mutation
tests confirm rejection of a stale hash, a duplicate canonical graph, a
truncated record, an invalid byte, a bipartite intruder, and a coordinated
deletion accompanied by forged hash/count/record metadata.

## 3. Exact rank reduction for the breaker

Write an involution as \(A=I-2P\), where \(P=P^\top=P^2\).  If
\(P=UU^\top\) has rank \(r\), let \(x_i\in\mathbb R^r\) be row \(i\) of
\(U\).  The exact pattern condition is

\[
  x_i^\top x_j=0 \quad\Longleftrightarrow\quad ij\in E(H)
  \qquad(i\ne j).
\]

Every \(x_i\) is nonzero: since \(d_H(i)\le6<8\), vertex \(i\) has some
non-neighbor \(j\) in \(H\); a zero \(x_i\) would create the forbidden extra
zero \(x_i^\top x_j=0\).

This disposes of the low ranks exactly.

- Rank zero and rank nine give \(A=\pm I\) and the wrong dense support.
- Rank one is impossible because \(H\) has an edge but two nonzero real
  scalars cannot be orthogonal.
- Rank two is impossible for non-bipartite \(H\).  Along an edge, a nonzero
  direction in \(\mathbb R^2\) must alternate with its unique perpendicular
  direction.  An odd cycle would force a direction to equal its perpendicular.
- Replacing \(P\) by \(I-P\) preserves every off-diagonal zero and nonzero
  while changing the rank from \(r\) to \(9-r\).

Consequently only ranks 3 and 4 need to be searched; ranks 6 and 5 are their
duals, and ranks 7 and 8 are already impossible.

## 4. Floating-point discovery

### 4.1 Environment and command

The isolated environment `/tmp/n9_breaker_venv` used CPython 3.14.7,
NumPy 2.5.2, and SciPy 1.18.1 on arm64 macOS.  The deterministic seed was
`2026082905`; `PYTHONHASHSEED=0`, `OMP_NUM_THREADS=1`, and
`VECLIB_MAXIMUM_THREADS=1` were set.

```sh
python3 -m venv /tmp/n9_breaker_venv
/tmp/n9_breaker_venv/bin/python -m pip install numpy scipy
PYTHONHASHSEED=0 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  /tmp/n9_breaker_venv/bin/python \
  discovery/breaker_projection_search.py \
  --starts 12 --max-nfev 1600
```

The complete seeds, parameters, attempt diagnostics, retained matrices, graph
invariants, and input hash are in `breaker_projection_results.json`.

### 4.2 Two parameterizations

The first parameterization solves for \(U\in\mathbb R^{9\times r}\):

\[
 U^\top U=I_r,\qquad (UU^\top)_{ij}=0\quad(ij\in E(H)).
\]

After QR retraction it checks \(A=I-2UU^\top\) independently, including the
minimum magnitude over all required nonzeros.  There are 12 Gaussian starts
for every graph and each of ranks 3 and 4.

The second parameterization fixes \(a_{ij}=0\) on \(E(H)\), treats all other
upper-triangular entries of a symmetric \(A\) as free, and solves the distinct
polynomial residual

\[
 (A^2-I)_{ij}=0\qquad(1\le i\le j\le9).
\]

It is initialized from the first candidate but neither uses a Stiefel factor
nor an orthogonality residual.  Thus it is a useful evaluator and
parameterization cross-check, though not an independent global search.

### 4.3 Results and hard cases

- Rank 4: 421 of 432 Stiefel starts met the frozen discovery thresholds.  All
  36 graphs had at least 9 hits out of 12.
- Rank 4 direct refinement: all 36 retained candidates have maximum
  involution error at most \(3.11\times10^{-15}\), exact stored zero entries
  on \(H\), and minimum required-nonzero magnitude at least
  \(1.4835\times10^{-2}\).
- Rank 3: 307 of 432 starts were hits.  Exactly three graphs had no hit, and
  their impossibility is proved independently below.  Direct refinement
  retained valid-pattern candidates for each of the other 33 cases.

The lowest rank-four basin count was case 13, graph6 `H????KZ`, with 9/12
hits.  Its component sizes are \((6,1,1,1)\), degree sequence
\((4,3,2,1,1,1,0,0,0)\), and it has one triangle.  Cases 3 (`H????CN`), 18
(`H???GON`), and 26 (`H??G?Cr`) had 10/12 hits.  These are optimizer-basin
diagnostics, not evidence of mathematical near-infeasibility.

At a diagnostic singular-value cutoff \(10^{-7}\), the direct rank-four
Jacobian has rank 25 in every case.  Its nullity is \(20-e(H)\), exactly the
generic dimension of the rank-four involution orbit minus the zero
constraints.  For the 33 valid rank-three cases, the corresponding rank is
27 and the nullity is \(18-e(H)\).  This is consistent with positive-dimensional
solution strata and argues against treating a floating-point point as an
isolated algebraic solution.  It is still not an exact transversality proof.

## 5. Three exact rank-three obstructions

The following use only the row-vector formulation and exact real linear
algebra.  Vertex labels are 0-based, as decoded by the scripts.

### Case 14: `H???GKF`

The edge set is

\[
\{56,57,67,58,68,78\},
\]

so \(H=K_4[\{5,6,7,8\}]\cup5K_1\).  Four nonzero mutually orthogonal
vectors cannot lie in \(\mathbb R^3\).  Hence rank three is impossible.

### Case 15: `H???GKJ`

The edge set is

\[
\{56,57,67,48,68,78\}.
\]

Vectors \(x_5,x_6,x_7\) form a nonzero orthogonal basis of \(\mathbb R^3\).
Since \(x_8\perp x_6,x_7\), one has \(x_8=\lambda x_5\) with
\(\lambda\ne0\).  The edge 48 then gives \(x_4\perp x_5\), but 45 is not an
edge of \(H\), contradicting the exact zero/nonzero pattern.

### Case 20: `H???GSL`

The edge set is

\[
\{56,47,67,48,58,78\}.
\]

Vectors \(x_4,x_7,x_8\) form an orthogonal basis.  The exact nonedges imply

\[
x_6=a x_4+c x_8\quad(a,c\ne0),\qquad
x_5=b x_4+d x_7\quad(b,d\ne0).
\]

But the edge 56 requires
\(0=x_5^\top x_6=ab\lVert x_4\rVert^2\), a contradiction.

All three graphs lie in the builder's join class.  For case 14 group the
\(K_4\) component with one isolate against the other four isolates; the two
induced sides of \(G\) are \(K_{1,4}\) and \(K_4\).  For cases 15 and 20,
group the nontrivial five-vertex component against the four isolates.  The
five-vertex complement edge sets are respectively
\(\{45,46,47,58\}\) and \(\{45,46,57,68\}\), both connected trees; the other
side is \(K_4\).  In all cases the side orders differ by one.

## 6. Exactification and infeasibility attack plan

Because every case has a robust rank-four candidate, priority should go to a
uniform exact positive construction or the builder's structural join/SSP
theorems, not to 36 unrelated Gröbner eliminations.

For a positive algebraic certificate, serialize a squarefree primitive
polynomial \(f(t)\in\mathbb Z[t]\), a rational isolating interval selecting
one real root \(\theta\), and every matrix entry as an element of
\(\mathbb Q(\theta)\).  An independent verifier should:

1. certify the selected root by Sturm isolation;
2. reduce every entry of \(A^2-I\) modulo \(f\) and require the zero
   polynomial;
3. require each \(H\)-entry to be the zero field element;
4. require each \(G\)-entry to be a nonzero field element, with exact gcd or
   minimal-polynomial arithmetic rather than a decimal interval;
5. reconstruct the graph from the serialized graph6 record.

Rational points may be sought intrinsically via a rational full-rank
\(X\in\mathbb Q^{9\times4}\),

\[
P=X(X^\top X)^{-1}X^\top,
\]

or via a rational Cayley orthogonal matrix conjugating
\(\operatorname{diag}(I_4,-I_5)\).  Both make idempotence automatic and leave
only the six-or-fewer zero equations.  Arbitrarily rounding the stored
floating-point matrices is invalid because it destroys the forced zeros.

If a future graph genuinely lacks a candidate, use the symmetric projection
ideal at ranks 3 and 4:

\[
P^2-P=0,\quad P=P^\top,\quad \operatorname{tr}P=r,\quad
p_{ij}=0\ (ij\in E(H)).
\]

Saturate by the product of all \(p_{ij}\) for \(ij\notin E(H)\), or add
inverse variables, to encode the mandatory nonzeros.  A Gröbner basis equal
to 1 after saturation is a complex infeasibility certificate.  Otherwise,
complex nonexistence has not been shown; real infeasibility requires a real
radical, CAD, or Positivstellensatz certificate.  Ranks 1 and 2 are discharged
by the exact lemma above, and complementary ranks add no new cases.  Merely
timing out in Singular or observing optimizer failure is not a certificate.

Do not impose full graph-automorphism invariance on \(P\) without proof: a
symmetrized matrix can create accidental zeros even when a nonsymmetric
realization exists.  The high-symmetry \(K_4+5K_1\) case is a useful mutation
test for any proposed symmetry reduction.

## 7. Artifact inventory and hashes

The final hashes should be recomputed by the root manifest after all shared
work stops.  At completion of this branch the relevant files are:

- `breaker_enumerate.py`: generator wrapper and independent validator;
- `breaker_n9_nonbip_e_le6.g6`: 36 canonical records;
- `breaker_enumeration_manifest.json`: counts, invariants, records, input hash;
- `breaker_test_enumeration.py`: fail-closed mutation tests;
- `breaker_projection_search.py`: deterministic two-parameterization search;
- `breaker_projection_results.json`: raw retained numerical diagnostics.

No Lean, Coq, Isabelle, or other proof assistant was used in this branch.
