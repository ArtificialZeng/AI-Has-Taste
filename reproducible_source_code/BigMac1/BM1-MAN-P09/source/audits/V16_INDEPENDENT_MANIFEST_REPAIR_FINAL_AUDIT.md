# V16 independent manifest-repair final audit

Date: 26 August 2026  
Candidate: `output/source_packages/common_metric_three_positivity_islands_submission_2026-08-26-v16/`  
Mode: read-only, fail-closed repair audit

## Verdict

**PASS — fatal 0 / major 0 / minor 0.**

The sole fatal finding in the preceding independent submission audit has been
closed. The rebuilt top-level JSON release manifest binds the complete current
package, including the preserved failed-audit history and the v16 build report,
without changing the previously audited manuscript, PDF, README, or exact
certificate artifacts.

This verdict covers the package directory and the assigned manifest-repair
gate. No PDF or ZIP was generated or modified. A later archive, if produced,
still requires its own fresh-extraction verification as stated in the build
report.

## Manifest identity and complete-file-set verification

```text
RELEASE_MANIFEST.sha256
c816ad32c109278a01a0f2981fe288ce55510fa03037c647f595dc32cb9517fc
```

The package-local command

```sh
python verify_release_manifest.py
```

returns:

```text
PASS JSON release manifest: 881/881 records
```

An independent reader then recomputed the file set, byte counts and SHA-256
digests without relying on the verifier's result:

```text
manifest entries                 881
actual files excluding manifest  881
extra files                        0
missing files                      0
byte/hash mismatches               0
```

The JSON creation timestamp is `2026-08-26T00:00:00+00:00`. The manifest is
self-excluding as documented, and every other regular file below the package
root is represented exactly once by path, byte count and digest.

## Previously audited primary bytes are unchanged

The current bytes agree with the expected hashes from the preceding audit:

| file | current and expected SHA-256 |
|---|---|
| `main.tex` | `a1c132ac2f167ad5a969d3a1fcd5949d2434c61a8292837a7ed3f107ceaa018c` |
| `main.pdf` | `a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be` |
| `README.md` | `bf7e2ebc349d6519500600f0c9ca9553d23cefc563a01f2930d519cbe3f05b68` |

Therefore the manifest repair did not alter the mathematical statement,
scope limitations, theorem numbering, exact constants, rendered paper, or
replay instructions that passed the first audit.

## Required newly bound records

The independent manifest lookup confirms that all requested records are
present with their current byte counts and digests, including:

| record | manifest SHA-256 |
|---|---|
| `audits/BUILD_TEST_REPORT_2026-08-26_V16.md` | `f4ab50c7edbf34bc7aa8945b59c443be22116d74f877411d48abcea1c70e7ac4` |
| `audits/V16_INDEPENDENT_FINAL_SUBMISSION_AUDIT.md` | `b2511796fc93ad6f6c30e531f7dca2e5242ce16a5b570f468feef0433245485d` |
| `BIBLIOGRAPHY_AUDIT.md` | `785112289908011e55d7b8406b0abf33b9f831483f9697b763e79aeebd37b1a6` |
| constant-`Z` frozen source | `a99072346ca9d92e3a5e45600d1de371b2609185bef60b2c069d2a400e1d9322` |
| constant-`Z` source manifest | `e573ff4ab4ab1f2065ff6c40289aacd19e8629e3bbe53b177cd996c7624d7840` |
| constant-`Z` independent referee | `4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3` |
| constant-`Z` referee manifest | `378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3` |
| constant-`Z` referee report | `cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f` |

The preserved failed audit accurately records the original stale-manifest
failure rather than silently rewriting audit history. The new build report
accurately describes its repair and makes the subsequent archive/fresh-
extraction gates explicit.

## Nested exact-certificate regression

The nine recentered/constant source manifests and nine independent-referee
manifests were replayed serially from the packaged
`certificate_workspace/`. All eighteen manifest commands pass, covering
**295/295** nested file records. In particular, the source 8/8 and referee
41/41 closures for the constant-`Z` cell remain intact.

No source, referee, test result, attack log, report or nested manifest changed
as a consequence of the top-level repair.

## Independent clean-build regression

A fresh temporary copy was cleaned and rebuilt with:

```sh
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 latexmk -C main.tex
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build exits zero and reproduces the packaged PDF byte-for-byte:

```text
a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be  main.pdf
```

The final `.log` and `.blg` contain no LaTeX/package warning, undefined
citation/reference, overfull/underfull box, or BibTeX warning. The mechanical
bibliography gate still reports 5 cited keys, 5 database keys, 5 resolved AUX
keys, and no missing or unused key.

The previous audit's 36-page visual, font, bookmark, authorship, disclosure,
scope and exact-constant findings remain applicable because `main.tex` and
`main.pdf` are byte-identical to that audited candidate.

## Closure of the prior fatal finding

The prior failure had four changed bound records, 250 unbound extras and a
629-entry manifest for a larger v16 directory. The repaired state has no
changed record, no extra, no missing file, and 881/881 verified records.
Accordingly the prior fatal release-integrity finding is **closed**.

Final classification for this manifest-repair audit:

```text
fatal 0
major 0
minor 0
PASS
```

The audit created only this external report. It did not write inside the
candidate package and did not create or modify any PDF or ZIP.
