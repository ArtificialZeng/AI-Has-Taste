# Exact SAT/UNSAT certificates

The mathematical proof in `proof/main_proof.md` is independent of these
files.  The certificates separately bind the original requested endpoints.

## Canonical encoding

Variables are the lexicographically ordered four-subsets of \([n]\).
For every disjoint edge pair the CNF contains \((-x_E\lor-x_{E'})\).  If a
triple has extension variables \(x_1,\dots,x_m\), degree at least two is
encoded without auxiliaries by
\[
 \bigwedge_{i=1}^m\bigvee_{j\ne i}x_j.
\]
This conjunction is true exactly when at least two extension variables are
true.  `verification/verify_instance.py` reconstructs the entire ordered CNF
from definitions and imports no generator code.

| n | variables | disjoint clauses | degree clauses | total clauses | CNF SHA-256 |
|---|---:|---:|---:|---:|---|
| 9 | 126 | 315 | 504 | 819 | `957acb8bedc7e47df7bc2b46c0754cc66612cc731c87db44f2757070f1cb07da` |
| 10 | 210 | 1575 | 840 | 2415 | `b5cd1a2b73f76f2bd4753943dc74347bc2690ad1c5490df84c5414550dad7e8d` |

## LRAT proofs

| n | proof | SHA-256 | addition/deletion lines |
|---|---|---|---:|
| 9 | `ekr_k4d3_n9.lrat` | `44d28573280a35b81f46000e57aa7da676b4b1f844469ea130a48289992d6c9c` | 184 / 28 |
| 10 | `ekr_k4d3_n10.lrat` | `1df5a6c057fd6b4fed51dfd6512433a146b9ce322586434e09ba550123459240` | 81 / 8 |

CaDiCaL 3.0.1 generated textual LRAT with `--lrat --no-binary
--checkproof=3`.  Independent checking uses Marijn Heule's `lrat-check.c`
from pinned drat-trim commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; the source hash is
`bf07c2ac96b9035da1ebcc578cb95e956a2b795629d613154cdb307f8a8f4a95`.
The wrapper verifies source hashes, reconstructs the canonical instance,
strictly parses the proof, requires the final empty-clause addition, compiles
the pinned C source into a fresh temporary executable, and then runs exactly
that executable.  It accepts only `c VERIFIED` with exit status zero.  Thus a
stale or substituted repository binary is outside the verification trust
path.

## Reproduction

```bash
sh verification/fetch_lrat_checker.sh
python verification/verify_lrat.py instances/ekr_k4d3_n9.cnf certificates/ekr_k4d3_n9.lrat --n 9
python verification/verify_lrat.py instances/ekr_k4d3_n10.cnf certificates/ekr_k4d3_n10.lrat --n 10
python tests/test_verify_instance.py
python tests/test_verify_lrat.py
```

`build_lrat_checker.sh` remains available as a convenience for direct manual
checking, but the fail-closed wrapper does not use that persistent binary.

The SAT trace for \(n=8\) is kept under `baseline/`, not here.  The same
external checker rejects it because no empty clause is derived.  The literal
\(n=8\) family is instead verified from definitions under
`discovery/breaker/`.
