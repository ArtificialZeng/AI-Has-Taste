# Fail-closed and dependency audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Scope: `src/builder_symbolic_checks.py`,
`tests/referee_low_degree_identities.py`, and the imports of every Python file
under `src/` and `tests/`.  This audit does not assess the mathematical prose
or extend the proved endpoint.

## Result

**Fail-closed result: PASS for both audited verifiers under the declared
Anaconda interpreter.**  Both scripts contain zero Python `assert` statements.
Their successful verification paths exit zero under normal, optimized,
isolated, and optimized-isolated execution.  Their explicit injected-failure
paths exit nonzero under all four modes, so `python -O` does not erase the
checks.

**Dependency declaration result: PASS.**  The proof-critical third-party
dependencies are now pinned in `requirements-verification.txt`, the numerical
diagnostic dependencies are separately pinned in
`requirements-diagnostics.txt`, and `VERIFICATION.md` records CPython 3.13.5,
the clean-install command, successful verification commands, and the required
four-mode injected-failure behavior.  A clean temporary virtual environment
was successfully reconstructed from the verification requirements during this
re-audit.

The stdlib-only independent referee verifier remains independent of all
third-party packages.

## Bound source files

| File | SHA-256 | `ast.Assert` count |
|---|---|---:|
| `src/builder_symbolic_checks.py` | `fd8e983f79b22ec2dd2be056e2ae4515f9a46e8321ac89bd6c73f6c5d1775a99` | 0 |
| `tests/referee_low_degree_identities.py` | `e8e37c700e625342a46bcf15778237f2bc182a66e60c4399166c51750564d3a4` | 0 |

Dependency/reproduction declarations bound by this re-audit:

| File | SHA-256 |
|---|---|
| `requirements-verification.txt` | `a1a2d4229b1b08e843c7adce90b7577c2570530af7f283ecd36633c8d933bd02` |
| `requirements-diagnostics.txt` | `84533959b687a846519786e365b27508c37914aa9fc6cc2d64ca70eede3ed331` |
| `VERIFICATION.md` | `b981b80ea1f33663f4c22de02080d23aafdc52837bda8ac6ac077330542f6a10` |

Two independent static checks were used:

```text
rg -n --glob '*.py' '\bassert\b' \
  src/builder_symbolic_checks.py tests/referee_low_degree_identities.py
```

returned no matches, and an AST walk counted nodes of type `ast.Assert`,
returning zero for each file.  The scripts instead call explicit `check(...)`
or `check_zero(...)` functions, which call `fail(...)` and raise
`SystemExit("VERIFICATION FAILED: ...")`.

## Interpreter and package versions

The four-mode matrix below used this exact interpreter:

```text
/opt/anaconda3/bin/python
Python 3.13.5 | packaged by Anaconda, Inc. |
(main, Jun 12 2025, 11:23:37) [Clang 14.0.6]
CPython cache tag: cpython-313
prefix: /opt/anaconda3
```

Imported third-party packages:

| Distribution | Version | Module path | Installer metadata |
|---|---:|---|---|
| SymPy | 1.13.3 | `/opt/anaconda3/lib/python3.13/site-packages/sympy/__init__.py` | conda |
| mpmath (SymPy runtime requirement) | 1.3.0 | `/opt/anaconda3/lib/python3.13/site-packages/mpmath/__init__.py` | conda |
| NumPy | 2.2.3 | `/opt/anaconda3/lib/python3.13/site-packages/numpy/__init__.py` | pip |
| SciPy | 1.15.3 | `/opt/anaconda3/lib/python3.13/site-packages/scipy/__init__.py` | conda |

The installed SymPy metadata declares `mpmath>=1.1.0,<1.4`.  SciPy 1.15.3
declares `numpy>=1.23.5,<2.5`; the installed NumPy 2.2.3 satisfies this range.
NumPy and SciPy are not imported by either of the two proof-critical scripts;
they occur only in numerical discovery/diagnostic sources described below.

## External-directory execution matrix

All 16 required executions were rerun after the dependency repair with
absolute script paths from the fresh external directory
`/var/folders/kh/3l44w5_56q36j9p6cyg1fgy00000gq/T/tmp.hWeGLhBMN5`.
No project working directory or `PYTHONPATH` was relied upon.

For each script, the successful commands were:

```text
/opt/anaconda3/bin/python SCRIPT
/opt/anaconda3/bin/python -O SCRIPT
/opt/anaconda3/bin/python -I SCRIPT
/opt/anaconda3/bin/python -O -I SCRIPT
```

The failure tests appended `--inject-failure` to each of those exact command
forms.  `SCRIPT` was, separately, each absolute path:

```text
/Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/08_sheil_small_self_inversive_cover/src/builder_symbolic_checks.py
/Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/08_sheil_small_self_inversive_cover/tests/referee_low_degree_identities.py
```

Observed exits:

| Script | Mode | Normal exit | Injected exit | Normal output | Injected stderr |
|---|---|---:|---:|---|---|
| builder | normal | 0 | 1 | `builder symbolic identities: OK` | `VERIFICATION FAILED: injected fail-closed self-test: residual 1` |
| builder | `-O` | 0 | 1 | same | same |
| builder | `-I` | 0 | 1 | same | same |
| builder | `-O -I` | 0 | 1 | same | same |
| referee | normal | 0 | 1 | ten `PASS` records, (3.3) through (5.6) | `VERIFICATION FAILED: injected fail-closed self-test` |
| referee | `-O` | 0 | 1 | same ten records | same |
| referee | `-I` | 0 | 1 | same ten records | same |
| referee | `-O -I` | 0 | 1 | same ten records | same |

All successful runs had empty stderr.  All injected runs had empty stdout and
only the displayed failure record on stderr.  In particular, isolated mode
did not uncover a hidden project-local import for either verifier.

## Generic `python3` dependency test

The generic interpreter is:

```text
/opt/homebrew/bin/python3
Python 3.14.7 (main, Aug 5 2026, 10:29:49)
[Clang 21.0.0 (clang-2100.1.1.101)]
```

From a separate fresh external temporary directory:

```text
/opt/homebrew/bin/python3 /absolute/path/src/builder_symbolic_checks.py
```

exited 1 before verification with:

```text
ModuleNotFoundError: No module named 'sympy'
```

This is correct fail-closed behavior, but it is **not** a verification pass.
It demonstrates that a generic `python3` invocation is insufficient *before*
the installation step.  This is now explicitly addressed by
`VERIFICATION.md`, whose clean-environment instructions first run
`python3 -m pip install -r requirements-verification.txt`.

By contrast,

```text
/opt/homebrew/bin/python3 /absolute/path/tests/referee_low_degree_identities.py
```

exited 0 with all ten `PASS` records, and appending `--inject-failure` exited 1
with `VERIFICATION FAILED: injected fail-closed self-test`.  This confirms
that the independent referee implementation is genuinely stdlib-only.

## Project import/dependency inventory

Standard-library imports (`argparse`, `dataclasses`, `fractions`, `hashlib`,
`json`, `math`, `os`, `pathlib`, `platform`, `sys`, `time`, and `typing`) are
provided by the selected Python runtime.  `__future__` is language support,
not a separately installed distribution.

| Files | Non-stdlib or local imports | Classification | Declaration status |
|---|---|---|---|
| `src/builder_symbolic_checks.py` | `sympy` (transitively `mpmath`) | **Proof-critical exact symbolic cross-check** | Pinned in `requirements-verification.txt` |
| `tests/referee_low_degree_identities.py` | none | **Proof-critical independent exact verifier** | stdlib-only |
| `src/search_self_inversive.py` | `numpy`, `scipy`, `scipy.ndimage`, `scipy.optimize`, `scipy.spatial` | Diagnostic numerical discovery | Pinned separately in `requirements-diagnostics.txt` |
| `src/search_n3_canonical_mesh.py` | `numpy`, local `search_self_inversive` | Diagnostic numerical discovery; transitively needs SciPy | Third-party requirements pinned separately |
| `src/search_refine_candidates.py` | `numpy`, local `search_self_inversive` | Diagnostic numerical refinement; transitively needs SciPy | Third-party requirements pinned separately |
| `src/verify_breaker_search.py` | `numpy`, `scipy.ndimage` | Diagnostic numerical recomputation, explicitly not a theorem certificate | Pinned separately in `requirements-diagnostics.txt` |
| `tests/breaker_test_search.py` | `numpy`, local `search_self_inversive` | Diagnostic evaluator regression test; transitively needs SciPy | Third-party requirements pinned separately |

No dynamic imports were found.  The three files importing
`search_self_inversive` explicitly add the project `src/` directory to
`sys.path`; this is a local-source coupling rather than a third-party package
declaration.

The source comments and artifact labels correctly classify the NumPy/SciPy
calculations as numerical discovery or diagnostics.  Their exact versions are
now recorded separately from the minimal proof-verification environment, so
installing the proof checker does not unnecessarily enlarge its trust base.

## Environment consistency check

Running

```text
/opt/anaconda3/bin/python -m pip check
```

exited 1 with:

```text
numba 0.61.0 has requirement numpy<2.2,>=1.24, but you have numpy 2.2.3.
```

No audited source imports `numba`, so this conflict was not exercised by the
two proof-critical checks.  The broad Anaconda prefix should not itself be
presented as a clean locked release environment; the successful clean virtual
environment reconstruction below is the relevant verification result.

## Re-audit of the reproducibility repair

The checked-in minimal verification requirements are exactly:

```text
Python 3.13.5
sympy==1.13.3
mpmath==1.3.0
```

`requirements-verification.txt` contains the two package pins, while
`VERIFICATION.md` records the required Python version.  A fresh virtual
environment rooted at
`/var/folders/kh/3l44w5_56q36j9p6cyg1fgy00000gq/T/tmp.2kyVyDGjUL/venv`
was created with `/opt/anaconda3/bin/python -m venv`.  Running

```text
VENV/bin/python -m pip install -r requirements-verification.txt
```

successfully installed exactly SymPy 1.13.3 and mpmath 1.3.0.  From an
external working directory, the clean-venv command

```text
VENV/bin/python -O -I /absolute/path/src/builder_symbolic_checks.py
```

exited 0 with `builder symbolic identities: OK`; the same command with
`--inject-failure` exited 1 with the expected explicit failure message.

The numerical packages are separately pinned as `numpy==2.2.3` and
`scipy==1.15.3` in `requirements-diagnostics.txt`.  They are not part of the
proof-critical environment.

The dependency repair is therefore sufficient for the claimed verification
scope.  The stdlib referee is portable without installation, and the SymPy
cross-check is reproducible after following the recorded clean-environment
installation step.

No proof, manuscript, status, or search artifact was modified during this
audit.

---

## Serialized exact-certificate audit

Re-audit date: 2026-08-29 (Asia/Shanghai)  
Scope: `certificates/low_degree_identities.json`,
`certificates/low_degree_certificate_manifest.json`,
`tests/verify_serialized_low_degree_certificate.py`, and
`tests/gate4_serialized_tamper_matrix.py`.

This section records the original canonical-digest audit together with its
Gate 4 strengthening.  The earlier digest-only result must not be cited by
itself as a strict-schema or independently rooted certificate verdict; the
current controlling evidence is `audit/GATE4_SERIALIZED_CERTIFICATE.md`.

### Verdict

**Canonical artifact verdict: PASS, identified by the exact hash below.**
The checked-in certificate has the stated variables and conjugation, contains
all three low-degree groups and 11 nontrivial checks, and the stdlib verifier
recomputes those checks exactly over a rational multivariate Laurent ring.  It
passes in normal, `-O`, `-I`, and combined `-O -I` modes.  An explicit injected
failure and a one-coefficient mutation both exit nonzero in every mode.

**Serialized-input fail-closed verdict after Gate 4: PASS.**  The verifier
pins a separate manifest digest and the canonical certificate digest, rejects
unknown or missing fields at every schema level, verifies the frozen
formal/builder/referee/manuscript hashes, rejects duplicate JSON keys and
labels, and requires exactly the declared 11-check inventory.  The full
genuine/badhash/extra-field/drop-check/change-expression matrix exits as
expected in all four interpreter modes.

### Bound files

| File | SHA-256 |
|---|---|
| `certificates/low_degree_identities.json` | `92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720` |
| `certificates/low_degree_certificate_manifest.json` | `a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3` |
| `tests/verify_serialized_low_degree_certificate.py` | `5244545747cd200b07c87730b0188927e7193da2bf73d760dc4c8d62f7f81153` |
| `tests/gate4_serialized_tamper_matrix.py` | `43fb7d56d563667f2153d6392eec7a776ce860bcc2e58fdb3f4666108a73f384` |

The verifier is stdlib-only (`argparse`, `ast`, `fractions`, `hashlib`,
`json`, and `pathlib`) and was run with `/opt/anaconda3/bin/python`, CPython
3.13.5.  Python optimization cannot remove its checks because it uses explicit
`check(...)`/`fail(...)` calls rather than `assert`.

### Parser and arithmetic inspection

The exact arithmetic core is sound for the checked-in metadata:

- coefficients are `fractions.Fraction` values;
- monomials are integer exponent tuples, so negative Laurent powers remain
  exact;
- division is accepted only by a nonzero integer literal;
- powers must be literal integers, and a negative power is accepted only for
  a single monomial;
- function calls, attributes, subscripts, floating constants, and other AST
  syntax reach the explicit `disallowed certificate syntax` failure path;
- equality compares the complete sparse monomial-to-rational dictionaries.

For the canonical conjugation metadata, the implementation correctly sends

```text
q -> q^-1,
d <-> D,
b <-> B,
c <-> C,
r -> r,
```

and fixes rational coefficients.  The listed variables are covered exactly,
and this particular map is an involution.  The Schur routine constructs

```text
(conjugate(h_m) H - h_0 H#) / y
```

coefficientwise, explicitly checks that the numerator's constant coefficient
is zero, and removes precisely that coefficient.  The formula agrees with the
two independent non-serialized implementations already audited above.

The schema-level false-pass surfaces are closed as follows:

1. `EXPECTED_MANIFEST_SHA256` authenticates a separate manifest that freezes
   the certificate and formal/builder/referee/manuscript inputs; the verifier
   also pins the canonical certificate path and digest.
2. `exact_keys(...)` enforces complete allowlists at every root and nested
   schema level, including kind-specific check fields.
3. `EXPECTED_CHECKS` fixes the 11 required labels.  Duplicate labels are
   rejected while scanning; afterward the seen-label set must equal the exact
   inventory and the passed count must equal 11.
4. `json.loads(..., object_pairs_hook=no_duplicate_keys)` rejects duplicate
   keys rather than silently retaining the final occurrence.

The canonical variable order, conjugation metadata, group order, definition
inventories, check order/kinds, and the special Schur-coefficient index set
are exact.  Independent nested probes confirmed that added fields at every
enforced level exit nonzero.

### External-CWD execution matrix

The canonical, injected-failure, tampered, incomplete, and tautology-only runs
were rerun after the verifier repair from the fresh external directory
`/var/folders/kh/3l44w5_56q36j9p6cyg1fgy00000gq/T/tmp.0W8bW2WQZy` using the
absolute verifier path.  The four command forms were:

```text
/opt/anaconda3/bin/python VERIFIER [CERTIFICATE]
/opt/anaconda3/bin/python -O VERIFIER [CERTIFICATE]
/opt/anaconda3/bin/python -I VERIFIER [CERTIFICATE]
/opt/anaconda3/bin/python -O -I VERIFIER [CERTIFICATE]
```

Omitting `[CERTIFICATE]` exercised the verifier's default path resolved from
`__file__`.  Injected runs used `--inject-failure`; tampered runs supplied the
absolute path of a modified copy.

| Mode | Canonical | Injected | Coefficient tamper | Incomplete | Tautology-only |
|---|---:|---:|---:|---:|---:|
| normal | 0 | 1 | 1 | 1 | 1 |
| `-O` | 0 | 1 | 1 | 1 | 1 |
| `-I` | 0 | 1 | 1 | 1 | 1 |
| `-O -I` | 0 | 1 | 1 | 1 | 1 |

Every canonical run printed 11 `PASS`/success lines followed by:

```text
serialized certificate: OK (11 checks, certificate_sha256=92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720, manifest_sha256=a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3)
```

and had empty stderr.  Every injected run had empty stdout, one explicit
failure line on stderr, and exit 1.

### Coefficient mutation test

In a copied certificate, only

```text
groups[0].checks[1].expected[0]
```

was changed from `6*D - 2` to `7*D - 2`.  The tampered-copy SHA-256 was
`580cdf541be65f404e64772a1be694c68aab82cb5a31caa3635aaac46b51d216`.
All four modes exited 1 before parsing or arithmetic, reporting that this
digest is not the audited canonical digest.  All had empty stdout and no final
certificate-OK record.

### Re-test of the former incomplete-input false passes

Two additional copies were generated solely in an external temporary
directory and were not retained as project artifacts:

- An **incomplete** copy kept the canonical metadata and degree-three
  definitions but retained only the first of 11 checks.  Its SHA-256 was
  `e17c1df81b543b8ad450e909eb3dc15942cac42e75b6b4a9d7bbf7eb132057ab`.
  It exited 1 in normal, `-O`, `-I`, and `-O -I` modes with the explicit
  noncanonical-digest failure.
- A **tautology-only** copy kept the canonical ring metadata but replaced all
  groups with one `equal` check of `0` against `0`.  Its SHA-256 was
  `ddc5bcd75c02d609c8e3d7f3fde168695347cf4d0a67e57b0edb65322f64b366`.
  It likewise exited 1 in all four modes with the explicit noncanonical-digest
  failure.

The repaired verifier therefore rejects every previously demonstrated
incomplete-input false pass.  Gate 4 additionally rejects extra fields and
synchronized self-consistent expression/manifest rewrites; the exact matrix
and independent review are in `audit/GATE4_SERIALIZED_CERTIFICATE.md`.
