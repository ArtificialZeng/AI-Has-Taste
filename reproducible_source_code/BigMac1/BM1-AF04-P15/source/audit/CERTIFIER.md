# Certifier record

Role completed after Breaker: 2026-08-30T04:54Z.

## Independent finite-census replay

Command:

    python3 certificates/verify_finite_census.py certificates/census_max5.json

Terminal record:

    {"certificate_sha256": "ebeb72ca4f04e377de266f4c403f6e2480bed3232feabb923d1436685057ce19", "records": 7, "status": "VERIFIED", "verifier_cpp_sha256": "dc8c5e25393fd58456ab72178b79cd636ec6f4006ccdfd80a4b363e1c766ef19"}

The coordinator compiled certificates/independent_tail_dfs.cpp in a temporary
directory. That program uses right-tail cumulative sums and receives only each
serialized alphabet. It reconstructed node count, leaf count, maximum depth,
maximizer count, the SHA-256 digest of the complete ordered maximizer list,
and membership of the supplied witness for every one of the seven records.
The full replay was rerun after the coordinator was strengthened to require
the exact seven-alphabet coverage, and the displayed terminal record is from
that final run.

## Independent 2-uniform replay

Command:

    python3 certificates/verify_uniform2_no_go.py certificates/uniform2_no_go.json

Terminal record:

    {"certificate_sha256": "02ece3207d0ed799dc0b23e8770cc9aaa598c668a46bfa75ad31f27f2a454e76", "morphisms": 16384, "status": "VERIFIED", "verifier_sha256": "3aeb26e99c475b4f65544e7b2466d926951c1942c1c1358f8680fd4074c30a91"}

This verifier independently enumerates all seven free image positions and
compares adjacent blocks with Python Counter multisets, rather than prefix
Parikh arrays.

## Fail-closed checks

The command

    python3 tests/test_fail_closed.py

returned:

    FAIL_CLOSED_TESTS_OK valid_cases=2 rejected_corruptions=7

The rejected inputs cover missing and unexpected fields, floating numeric
claims, nonprimitive alphabets, inconsistent maximizer counts, and malformed
digests. The seventh test deletes an entire v2 record and verifies that
canonical scope coverage is enforced. A separate full-replay test increased
the first record's node count by one; the verifier rejected it with:

    REJECTED: exact replay mismatch for [0, 1, 2, 3]: nodes

## Build and arithmetic checks

All three C++20 kernels compiled under clang++ with
Wall, Wextra, and pedantic diagnostics enabled and produced no diagnostics.
All Python sources compiled with py_compile. The certificate arithmetic is
signed exact integer arithmetic, there is no randomness, and neither
floating-point tolerances nor modular projections are used in a theorem-level
claim.

Proof assistant: none used.

Disposition: PASS for the finite census and the stated restricted morphism
class. No certification is asserted for the original infinite problem.
