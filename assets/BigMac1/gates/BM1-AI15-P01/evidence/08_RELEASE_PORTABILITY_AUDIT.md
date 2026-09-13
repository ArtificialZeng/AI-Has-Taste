# Release portability audit

Audit date: 2026-08-29 (Asia/Shanghai). Status: **PASS after repair**.

## Defect and repair

The first source ZIP incorrectly contained
`certificates/__pycache__/builder_verify_counterexample.cpython-313.pyc`.
That archive was removed from `release/` and deleted after the corrected
archive passed all tests.  The workspace cache file and its empty directory
were also removed.

The corrected archive is built from the 28-file whitelist
`release/SOURCE_FILELIST.txt`; recursive directory packaging is no longer
used.  The archive has 39 ZIP entries including directories and contains no
`__pycache__`, `*.pyc`, `*.pyo`, `.venv`, `.lake`, `.pytest_cache`, or
temporary-directory entry.

## Final source archive

- Path: `release/hadamard_rank22_rational_factorization_source.zip`
- Size: 45,247 bytes
- SHA-256: `10a4d0fe5c1f6389a904af683272e81782a47612c4c038138df28e79eefc1d1a`
- `unzip -t`: PASS
- forbidden-entry scan: PASS
- workspace cache scan after verification: PASS

## Clean-extraction exact tests

The final archive was extracted into a newly created `/tmp` directory.  From
that directory, with no project-relative fallback, the following passed:

1. `python3 -I verifier/verify_rational_decomposition.py`;
2. `python3 -I certificates/builder_verify_counterexample.py certificates/builder_counterexample.json`;
3. `python3 -I certificates/breaker_verify.py certificates/breaker_decomposition.json`.

The primary certificate/verifier hashes reconstructed from the ZIP remain

- certificate: `49ba2cc16daa5c883de57f4e0b6a7f972800797bbebc5f721ea4e18bbe9cf1e2`;
- verifier: `5c2812ed231c3bb55174770f8e536130b60189e21f3b1594bc80c9baa85f05f8`.

A fail-closed mutation test changed serialized `A[0][0]` from 1 to 2.  The
isolated verifier exited with code 1 and printed `FAIL: A != U V`.

## Clean-extraction LaTeX test

From the same extraction:

- LaTeX citation audit: `cited=1 bib=1 missing=0 unused=0`;
- `latexmk -pdf -interaction=nonstopmode -halt-on-error`: PASS in a fresh
  output directory;
- final TeX log warning/error/overfull/underfull scan: PASS;
- output: 3 unencrypted US-Letter pages;
- extracted-build PDF text equals the released PDF text exactly under
  `pdftotext -layout`.

The mathematical PDF and its source were not edited during this portability
repair.  The released PDF hash remains
`bd271cefe03202471b6b93fa8b7d9812e3da48cbc4bf7ec7bc1df23f8749d53a`,
so the existing three-page visual audit remains bound to the same bytes.

## Log hashes

- ZIP integrity: `861f65209c2577ff692f61c02cc7c0410f3f5f3dfc1856d6bd2983fadea26451`
- isolated verifiers: `09fd98d90c1ce0262167501867e93c5a9eceaf28bf1258331a6695f66708ea66`
- tamper test: `0f0250023de9073699d12d9091df21e5d51dc48d715bf3ec3bd4e9c5bcbbd354`
- LaTeX audit: `453fd86fafaded00a85394ce02e0647593873b1cd7c387d90c110fecf9bca51d`
- clean build transcript: `01fcb91013eb0bad612303e49459dcdde54eee7eeafcf07f77fbc065e0455bd4`
- clean PDF metadata: `347581d8bc78716852a382dfd7af58ac806a9cd23636be19f6ad4a75ba61b3f5`

All extraction and build directories were deleted after the checks.
