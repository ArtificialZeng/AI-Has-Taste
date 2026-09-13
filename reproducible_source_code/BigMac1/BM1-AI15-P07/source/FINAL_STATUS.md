# Final status: CERTIFIED_FINITE_RESULT

Terminal date: **2026-08-29**.  This is a strict finite endpoint, not a
resolution of Erdős--Szekeres problem #699.

## Result

For every

\[
8\le n\le100{,}000{,}000,\qquad 4\le j\le\lfloor n/2\rfloor,
\]

there is an odd prime \(p\) dividing both \(\binom n3\) and \(\binom nj\).
Thus the weak Erdős--Szekeres assertion is certified on the complete finite
stratum \(i=3\) through \(10^8\).  Three recorded novelty passes did not
locate an earlier public all-row \(i=3\) result at this bound; this is a
bounded literature statement, not a claim of absolute priority.

## Decisive evidence

- Exact support/Lucas completeness proof: `proof/i3_finite_theorem.md`.
- Serialized discovery result:
  `certificates/i3_scan_100m.json`, SHA-256
  `23c45255e41877ccde381d86564e991ced9b7e08b8559f48405f4a759b51f0ba`.
- Independently derived full-range Legendre verifier output:
  `certificates/i3_verify_100m_strict.txt`, exit 0, SHA-256
  `9a1a430068f5813195a90b0f22937095008b50f84c66fb311ca64ff3dc2904ab`.
- Fast fail-closed binder: `code/verify_release_binding.py` parses the
  canonical certificate and strict output together and pins
  \(n_{\min}=8\), \(n_{\max}=100000000\), \(i=3\), both counts
  `43631335536`, the certificate/source/output hashes, and the binary build
  command.  It ignores runtime.
- External-cwd tamper matrix passed in Python normal and `-O`: changed
  endpoint, bad hash, changed-count false-null, truncated output, and duplicate
  certificate/binding fields all exited nonzero.
- Direct arbitrary-precision gcd oracle: all 994,009 admissible pairs through
  \(n=2000\), no counterexample.
- Missing-field, duplicate-key, and non-null C++ input fixtures fail closed.
- Proof, citation, source, clean-build, and five-page visual PDF audits pass.

## Limitations

The original infinite conjecture is **not proved or disproved**.  The result
says nothing about \(i=3,n>10^8\) or the unsettled general strata \(i\ge4\).
The structural reductions prove \(i=1,2\) and impose necessary divisibility,
size, prime-gap, and smoothness constraints, but G01 remains fatal to a full
proof only; G01 is not a gap in this finite theorem.  No numerical runtime or
candidate count is used as an infinite extrapolation.

## Reproduction

```bash
c++ -O3 -std=c++17 -Wall -Wextra -pedantic code/scan_i3.cpp -o code/scan_i3
c++ -O3 -std=c++17 -Wall -Wextra -pedantic code/verify_i3.cpp -o code/verify_i3
code/scan_i3 8 100000000 > certificates/i3_scan_100m.json
code/verify_i3 certificates/i3_scan_100m.json
python3 code/brute_oracle.py 8 2000
python3 code/verify_release_binding.py --root . \
  --binding certificates/i3_release_binding.json
python3 code/test_release_binding.py
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  release/frozen release/MANIFEST.sha256
```

The reported environment is Apple clang 21.0.0 on arm64 macOS 25.5.0
(Apple M3 Pro), Python 3.14.7.  The computation is deterministic and has no
random seed.

## Proof-assistant disclosure

**No proof assistant was used.**  No Lean, Coq, Isabelle, or other formal
kernel checked this result.  Codex assisted with reductions, code, searches,
audits, and manuscript preparation; the decisive finite claim was rebuilt by
separately derived exact evaluators as documented above.
