# Reproduction notes / 复现说明

> **Git distribution update:** Manuscript LaTeX is now local-only and Git-ignored, including copies inside reproduction bundles. Earlier clean-build/syntax/link results describe the complete local snapshot. See the [upload policy](../../UPLOAD_GUIDE.md) and the current Git-upload validation; they are not a claim that Git contains LaTeX.

The final PDFs are unchanged historical submission manuscripts. Their source packages are source-and-evidence distributions, not copies of the original machine environments. These notes do not replace the mathematical audits.

本轮 41 份 LaTeX 的独立洁净构建全部通过，页数全部匹配（280 页），没有缺失引用、依赖或 LaTeX 错误。552 个 Python 文件在 Python 3.12 下通过静态语法检查；只对 5 个小型精确检查做了隔离执行，不是对全部论文重新验证。

Use Python 3.12 or later for the archive's full Python syntax coverage. Individual verifiers may support older versions, but not every historical discovery tool does. Dependencies such as Singular, SymPy, GMP, nauty, Z3 or DRAT/LRAT checkers must be installed separately where the relevant program requires them. Nothing is installed automatically.

## Known wrapper / dependency limitations

| Package | What requires attention |
|---|---|
| [AI15 P02](../../reproducible_source_code/BigMac1/BM1-AI15-P02/) | The historical `make verify` also calls a machine-specific LaTeX skill audit. Prefer the relative mathematical verifier and independent verifier; the machine-specific release helper is not portable. |
| [AI15 P11](../../reproducible_source_code/BigMac1/BM1-AI15-P11/) | The old aggregate checks bind omitted original binaries and a nauty source tarball. Included census records are not a replacement for those bound inputs. Fetch the pinned upstream release, rebuild locally and document any portability adaptation for full replay. |
| [AF03 P03](../../reproducible_source_code/BigMac1/BM1-AF03-P03/) | Historical `experiments/run_exact.sh` assumes a Homebrew Singular path. `certificates/verify_certificate.py` accepts `--singular` to select a local Singular executable. |
| [AF03 P04](../../reproducible_source_code/BigMac1/BM1-AF03-P04/) | The optional `make audit` targets the original machine's skill installation. It is distinct from the mathematical `make verify` entry. |
| [AF03 P14](../../reproducible_source_code/BigMac1/BM1-AF03-P14/) | `src/verify_all.py` and several shebangs assume the original Python installation. Invoke individual scripts using a suitable Python, rather than the old absolute-path aggregate. The independent referee accepts the `SINGULAR` environment variable. |
| [AF04 P02](../../reproducible_source_code/BigMac1/BM1-AF04-P02/) | A discovery helper assumes a local `labelg` installation. The independent finite certificate verifier is a separate route and does not depend on that discovery helper. |
| [AF04 P03](../../reproducible_source_code/BigMac1/BM1-AF04-P03/) | The old wrapper binds 162 omitted graph files (about 2.09 GB) and an old binary. The included C++ source can reconstruct the graph from definitions; see the bounded manual entry below. |
| [MAN P06 — ES7](../../reproducible_source_code/BigMac1/BM1-MAN-P06/) | The small ES5 CNF/DRAT/LRAT files are included, but their wrapper still requires locally built DRAT/LRAT checker tools. About 1.41 GB of large ES6 traces are omitted; encoding/count checks are not full trace verification. |
| [MAN P07 — Lehmer](../../reproducible_source_code/BigMac1/BM1-MAN-P07/) | Two optional C++ test scripts assume Homebrew GMP include/library locations. Adjust those build flags for the local GMP installation; the main certificate script is a distinct entry. |

## AF04 P03: direct source replay interface

The actual search source is [`exact_clique.cpp`](../../reproducible_source_code/BigMac1/BM1-AF04-P03/source/code/exact_clique.cpp), not just the historical Python wrappers. From a disposable copy of that package's `source/`:

```sh
mkdir -p local-replay
c++ -std=c++20 -O3 code/exact_clique.cpp -o local-replay/exact_clique
```

The executable accepts `LOG_JSONL WITNESS_JSON [FIXED_VARIABLE]`. For example, the following runs **one branch**, not the full theorem:

```sh
local-replay/exact_clique local-replay/fixed1.jsonl local-replay/fixed1-witness.json 1
```

The program's normal UNSAT completion uses exit code **20**; a found clique uses **10**. Inspect the result rather than treating every nonzero exit as a crash. A full negative replay must cover the 162 representatives recorded in the global fixed-cover manifest and independently check their coverage. No such full replay was run during packaging. This interface does not make the old binary/graph-bound wrapper pass unchanged.

## Five isolated exact smoke checks

- MATH15 P13: split-graph witness.
- AI15 P01: rational Hadamard factors.
- AF04 P01: annihilator certificate.
- MAN P03: ternary Borsuk certificate.
- DM01 P13: finite Clausen/Legendre diagnostics.

All five completed successfully in disposable copies; source bytes remained unchanged. The last item is finite diagnostic evidence, not a fresh independent proof of the whole supercongruence theorem.

## Documentation versus provenance

Legacy manifests inside source folders refer to the original full release layout. The new [package manifest](package-manifest.json) binds the copied subset. Never bypass a missing-file check in a legacy verifier and relabel that as successful reproduction. The PDF's scope, limitations and authorship remain exactly as in the final manuscript.
