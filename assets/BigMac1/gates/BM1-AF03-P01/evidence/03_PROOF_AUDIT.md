# Proof and certificate audit

Audit date: 2026-08-29.  Overall mathematical status: **PASS**.  The final
post-repair certificate-wrapper review is recorded below.

## Blind mathematical referee

An isolated referee reconstructed the argument from the formal definitions
without using the discovery transcript.  The verdict was PASS with zero fatal
and zero major proof gaps.  In particular, the referee checked:

- the exterior-triple identity against the fixed edge;
- the choice of distinct labels for two disjoint exterior triples when
  \(n\ge10\);
- the multiset-complement argument proving \(e\mapsto x_e\) injective at
  \(n=9\);
- all possible \(X\)-extensions of the mixed triple \(Q_a\); and
- that the final triple \(S=X\setminus\{x_0,x_j\}\) remains fixed while the
  three choices of \(a\) force \(|C(S)|\ge3\).

The only defect found was a formal-definition edge case: a displayed minimum
over triples had been written without excluding \(n<3\).  The formal statement
was repaired to define \(\delta_3\) only for \(n\ge3\); the theorem itself has
always had the endpoint \(n\ge9\).  This does not alter the theorem or proof.

The same referee independently enumerated the literal \(n=8\) family and
confirmed that it is intersecting, has 35 edges, and has triple-degree
histogram \(42\times2+14\times4\).  Thus \(\delta_3=2\) exactly.

## Independent mathematical cross-check

`proof/independent_crosscheck.md` supplies a genuinely different \(n=9\)
route.  Its six edge-disjoint graphs each have at least four edges, forcing at
least 24 graph edges on a five-vertex set, where only 10 unordered pairs
exist.  A complete \(31^4\) enumeration of the forcing-set quadruples was used
only as an exact cross-check, not as a premise of the written proof.

## Certificate referee

The certificate referee independently reconstructed the canonical instances:

| \(n\) | variables | disjointness clauses | degree clauses | total |
|---:|---:|---:|---:|---:|
| 8 | 70 | 35 | 280 | 315 |
| 9 | 126 | 315 | 504 | 819 |
| 10 | 210 | 1575 | 840 | 2415 |

For every \(m=n-3\in\{5,6,7\}\), all \(2^m\) assignments were checked to
confirm that the no-auxiliary clause block is equivalent to
\(\sum_i x_i\ge2\).  Fresh temporary regeneration was byte-identical to every
canonical CNF/JSON and to each independent witness CNF/OPB/JSON.

The pinned `lrat-check.c` source was freshly compiled outside the discovery
run.  That checker accepted both certificates and rejected the \(n=8\) SAT
trace.  The exact proof hashes are:

- \(n=9\): `44d28573280a35b81f46000e57aa7da676b4b1f844469ea130a48289992d6c9c`;
- \(n=10\): `1df5a6c057fd6b4fed51dfd6512433a146b9ce322586434e09ba550123459240`.

The referee found one major trust-boundary defect in the first wrapper: it
hashed pinned source files but executed a persistent binary without binding
that binary to the sources.  This was repaired.  The current wrapper checks
the source hashes, snapshots those verified source bytes together with the CNF
and LRAT, compiles the source snapshot into a fresh temporary executable on
every invocation, and executes exactly that path on the input snapshots.  It
also parses the instance verifier's JSON exactly, binds its reported code hash,
tracks active clause IDs, enforces the checker's integer range, and rejects
nonexistent deletion targets before entering the C checker.
The positive tests still accept both proofs, while eight truncated, altered,
non-ASCII, invalid-deletion, or cross-instance traces are rejected fail
closed.

The final defensive re-audit reported zero fatal, zero major, and zero local
defects in this scoped verification path.  The live \(n=9,10\) records are
field-for-field identical to the saved verification JSON and certification
manifest.

## Reproduction

```bash
python code/reproduce_hz_baseline.py
python tests/test_verify_instance.py
python tests/test_verify_lrat.py
python verification/verify_lrat.py instances/ekr_k4d3_n9.cnf certificates/ekr_k4d3_n9.lrat --n 9
python verification/verify_lrat.py instances/ekr_k4d3_n10.cnf certificates/ekr_k4d3_n10.lrat --n 10
python discovery/breaker/rerun.py
python discovery/breaker/test_verify_family.py
```

No Lean, Coq, Isabelle, or other proof assistant was used.  The theorem is a
human-readable finite combinatorial proof; the LRAT artifacts are an
independent exact certification of the two originally requested endpoints.
