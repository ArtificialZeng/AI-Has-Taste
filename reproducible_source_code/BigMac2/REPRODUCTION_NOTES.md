# BigMac2 reproduction notes / 复现说明

The final PDFs are unchanged historical gate-passed releases. The packaging tests below check source portability and selected computations, not novelty, external peer review or the whole quantified proof. No research queue was restarted.

最终PDF字节不变。以下检查验证材料完整性、源码构建和选定计算，不代表重新审查所有数学证明或完成母题。未重新启动研究。

## How to use the packages

1. Follow the [English catalog](../../README.md#bigmac2) or [中文目录](../../README.zh-CN.md#bigmac2) for PDF, LaTeX and code links.
2. Use `python3 reproducible_source_code/BigMac2/prepare.py PAPER_ID --output NEW_DIRECTORY` from the repository root to materialize a working copy. Stored and uncompressed hashes are both checked; an existing destination is refused.
3. Run only the appropriate program below, from that new working directory. Scripts may regenerate evidence; do not run in the checked-in archive. `python3` stands for a compatible interpreter, not a fixed host path.
4. Full search/census programs can be much larger than a short verification. Dependencies are listed per package. Binary/provenance assertions are not bypassed.
5. Source-only mathematical proofs need no fabricated program. Where no standalone code was archived, the package supplies the original problem/proof evidence and says so.

Large scientific data are losslessly gzipped; the source script paths stay unchanged after materialization. Compiled executables, environments, credentials, worker transcripts, old PDFs and downloaded third-party papers are not included. Python source was syntax-checked, and the exact copied subset is bound by [the package manifest](../../assets/BigMac2/package-manifest.json).

## Per-package checks

| Paper | Selected command in a materialized working copy | Packaging test | Scope / limitations |
|---|---|---|---|
| [BM2-B03-P01](BM2-B03-P01/) | `python3 audit/referee_check.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B03-P02](BM2-B03-P02/) | `No short replay selected` | not_run | Only floating discovery searches are archived as Python. The proof is in Markdown/LaTeX; no positive exact checker offered. |
| [BM2-B04-P01](BM2-B04-P01/) | `python3 evidence/check_typeII_product_dual.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B04-P02](BM2-B04-P02/) | `No short replay selected` | not_run | Full n=4..8 biconnected census invokes geng plus high-precision spectral computations; not a small smoke test. Dependencies: nauty geng, NetworkX, mpmath, SymPy. |
| [BM2-B04-P03](BM2-B04-P03/) | `python3 evidence/verify_family_formula.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B05-P02](BM2-B05-P02/) | `python3 evidence/cut_lp_certify.py verify evidence/J_m_1_certificates.json` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B05-P04](BM2-B05-P04/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B06-P03](BM2-B06-P03/) | `python3 evidence/research_b5_independent.py` | pass | Independent code is finite evidence supporting the analytic theorem; finite checks are not an infinite proof. |
| [BM2-B06-P04](BM2-B06-P04/) | `python3 evidence/independent_theta_audit.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B07-P01](BM2-B07-P01/) | `python3 evidence/fixed_shape_certificate.py --max-k 20` | pass | Suggested max-k20 is an explicitly REDUCED smoke test, not replay of every archived default-k200 instance nor proof of the all-k formula. |
| [BM2-B07-P02](BM2-B07-P02/) | `python3 evidence/check_finite.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B07-P04](BM2-B07-P04/) | `No short replay selected` | not_run | Compile C11 verifier/auditor. Auditor recomputes large trace/correlation tables and direct 8192x8192 count checks; do not promise20 seconds. Retain n14_certificate.tsv and short n14_run.log/n14_audit.log. |
| [BM2-B08-P02](BM2-B08-P02/) | `python3 evidence/time8_exact.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B08-P04](BM2-B08-P04/) | `python3 audit/referee_independent.py` | not_run | Referee checker is a fresh exact implementation; review its archived input expectations before running a copied subset. |
| [BM2-B09-P03](BM2-B09-P03/) | `No short replay selected` | not_run | C++17 verifier reconstructs entire alphabet/frontiers. Compiler invocation c++ -O3 -std=c++17 evidence/verify_certificate.cpp -o replay-verify; then ./replay-verify evidence/frontier_certificate.txt replay-report.txt. No external linked libraries. |
| [BM2-B10-P02](BM2-B10-P02/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B10-P03](BM2-B10-P03/) | `python3 evidence/check_curvature.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B11-P01](BM2-B11-P01/) | `python3 evidence/verify_grade6_identities.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B11-P02](BM2-B11-P02/) | `python3 evidence/verify_mixed_sign.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B11-P03](BM2-B11-P03/) | `python3 evidence/s4_certificate.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B11-P04](BM2-B11-P04/) | `python3 evidence/verify_symbolic.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B12-P02](BM2-B12-P02/) | `python3 evidence/verify_d4_alternating.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B12-P04](BM2-B12-P04/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B13-P03](BM2-B13-P03/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B14-P01](BM2-B14-P01/) | `python3 evidence/verify_exact.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B14-P02](BM2-B14-P02/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B14-P04](BM2-B14-P04/) | `python3 evidence/verify_certificate.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B15-P01](BM2-B15-P01/) | `python3 evidence/exact_triage.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B15-P02](BM2-B15-P02/) | `python3 evidence/exact_recurrence.py 1 2 10` | pass | N=1,2,10 is a bounded smoke test, not all archived default cases. No change to claimed analytic scope. |
| [BM2-B16-P02](BM2-B16-P02/) | `No short replay selected` | not_run | Requires external Singular; supports --singular PATH. Full table default uses /opt/homebrew/bin/Singular. Preserve generated Singular inputs/results; computation is finite evidence, not a new proof. |
| [BM2-B17-P01](BM2-B17-P01/) | `python3 evidence/resolution_check.py` | not_run | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B18-P03](BM2-B18-P03/) | `No short replay selected` | not_run | Archived numerical_sanity.py is explicitly floating-point sanity only; no exact replay interface is claimed. |
| [BM2-B19-P02](BM2-B19-P02/) | `No short replay selected` | not_run | No cheap complete proof replay. C++17 search uses nauty geng input streams; exhaustive nonexistence audit records are short evidence/pass2_A_m{0,1,2}.log. Keep them. Crosscheck C++ files include geng_excess2_search.cpp relatively. Avoid rerunning full graph streams. Large A_m0_test.cnf/.cycles are discovery data, preserve gzip if including. |
| [BM2-B19-P03](BM2-B19-P03/) | `python3 evidence/replay_exact_weight_certificate.py evidence/exact_cycle_weights.tsv evidence/cycles_14_16.tsv evidence/orientation_search_instance.tsv replay-packaging.json` | pass | Two exact weight replay paths are stdlib and do not depend on SciPy/HiGHS. Discovery requires SciPy/NumPy, CaDiCaL and C++ HiGHS headers/library. Avoid orientation CNF/MILP searches in a smoke check. |
| [BM2-B20-P01](BM2-B20-P01/) | `No short replay selected` | not_run | No code archived; mathematical proof is the manuscript and proof dossier. |
| [BM2-B20-P03](BM2-B20-P03/) | `python3 evidence/check_q3_certificate.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B21-P05](BM2-B21-P05/) | `python3 evidence/verify_resolution.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B22-P01](BM2-B22-P01/) | `python3 evidence/verify_exact_dual.py` | pass | Exact verifier has no numerical dependencies; optional SDP discovery uses NumPy/SciPy/CVXPY/SymPy. Do not treat SDP solver success as proof. |
| [BM2-B22-P03](BM2-B22-P03/) | `python3 evidence/verify_five_supports.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B22-P04](BM2-B22-P04/) | `python3 evidence/diamond_n3.py --output replay-diamond` | pass | Writes regenerated exact cellular matrices and Smith certificates into explicit replay-diamond output, leaving archived evidence intact in a disposable copy. |
| [BM2-B23-P06](BM2-B23-P06/) | `python3 evidence/replay_n32.py evidence/n32_manifest.json replay-packaging.json` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B24-P01](BM2-B24-P01/) | `python3 evidence/verify_orbit_threshold.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B24-P02](BM2-B24-P02/) | `python3 evidence/exact_resolution_verify.py` | pass | Exact-resolution verifier distinct from NumPy/SciPy numerical PEP discovery; smoke check does not replace analytic quantified case argument. |
| [BM2-B25-P01](BM2-B25-P01/) | `python3 audit/referee_recompute.py` | pass | 3^12 enumeration is finite but may exceed20 seconds depending on implementation/hardware; enforce timeout and label timeout, not failure of the theorem. |
| [BM2-B25-P03](BM2-B25-P03/) | `python3 evidence/independent_verify.py evidence/exhaustive_certificate.json --report replay-packaging.json` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B26-P02](BM2-B26-P02/) | `python3 evidence/exact_regression.py` | pass | Exact regression uses SymPy; graph6_crosscheck uses NetworkX. Full reproduce.sh is machine-specific (old project/interpreter/Homebrew/private-tmp/compiler paths). Provide a new documented portable wrapper; retain original bytes as provenance. Full modular census C++ requires C++20 and nauty geng/labelg. |
| [BM2-B26-P03](BM2-B26-P03/) | `python3 evidence/verify_certificates.py --subgroups evidence/gl32_subgroup_irreducibility.json --weak-ekr evidence/gl32_weak_ekr_classification.json --output replay-packaging.json` | not_run | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B26-P04](BM2-B26-P04/) | `No short replay selected` | not_run | paley13_lc_orbit.bin is SCIENTIFIC DATA, not executable. Preserve it losslessly. Python verifier uses NumPy/NetworkX and checks915,623,280 five-subsets; C++20 independent verifier does the same. Both are long replays, not smoke checks. Compile c++ -O3 -std=c++20 audit/referee_verify.cpp -o replay-verify. Then pass the literal graph6 string LlthgsL`mEkLkL as argv1 and evidence/paley13_lc_orbit.bin as argv2 (use an argument array or single shell quotes; the backtick must not execute). |
| [BM2-B27-P01](BM2-B27-P01/) | `python3 evidence/verify_profiles.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B27-P02](BM2-B27-P02/) | `python3 evidence/verify_22.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B27-P03](BM2-B27-P03/) | `python3 evidence/verify_h4_certificate.py` | pass | verify_h4_certificate.py checks metadata/counts/word digests and representative bounds only. It expressly does NOT repeat the1.48-billion-signature C++ sweep; label coverage accurately. |
| [BM2-B27-P04](BM2-B27-P04/) | `No short replay selected` | not_run | All three evidence Python verifiers/producer and audit/referee_recheck.py enforce old absolute interpreter path. Evidence verify_order8_certificate.py also hardcodes /opt/homebrew/bin/showg. Do not classify original wrappers as portable or strip checks without disclosed patch provenance. |
| [BM2-B28-P04](BM2-B28-P04/) | `python3 evidence/coefficient_vector_recheck.py --output replay-packaging.json` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |
| [BM2-B29-P01](BM2-B29-P01/) | `python3 evidence/verify_d7_farkas_independent.py` | not_run | Independent Farkas/primal verifier uses NumPy, exact integer/Fraction arithmetic, reconstructs1771x1771 transform; bounded timeout may be exceeded. Primal checker imports local verify_d7_farkas_independent.py. Optional discovery: highspy/NumPy/SciPy; solve_basis_flint.c needs FLINT (-lflint,with local compiler/header flags). |
| [BM2-B29-P13](BM2-B29-P13/) | `python3 evidence/independent_audit.py` | pass | Finite exact supporting checks only; consult the proof dossier for the full quantified claim. |

## Known nonportable or long replay paths

- BM2-B26-P02: the historical full-census shell wrapper hardcodes its old host paths. The C++20 source, graph6 data and exact regression checker are present. Compile the source locally and supply local nauty geng/labelg paths; the old compiled executable is intentionally absent. The short exact regression does not replay the full modular census.
- BM2-B27-P04: original scripts enforce the old Python executable path and one verifier hardcodes showg. They are preserved unchanged, not falsely labeled portable. A documented local adapter is needed before a different host can replay those wrappers.
- BM2-B27-P03: the short check verifies counts, metadata, word hashes and representative bounds. It does not rerun the 1.48-billion-signature sweep.
- BM2-B26-P04: `paley13_lc_orbit.bin` is scientific orbit data, not an executable. The complete verification includes 915,623,280 subset tests and was not restarted.
- BM2-B19-P02: compact pass2_A_m*.log files are frozen mathematical computation records, not worker transcripts. They are retained alongside C++ source. Gzip copies of large discovery instances are also retained.
- BM2-B16-P02 uses external Singular (`--singular` can select its path). Other optional discovery paths use nauty, CaDiCaL, HiGHS or FLINT; no system tools were installed by this task.

No open-source license for newly packaged author material is invented by this staging task. Existing notices remain intact; redistribution of external tool binaries or papers is not implied.
