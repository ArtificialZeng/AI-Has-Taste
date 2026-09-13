# FINAL STATUS

Terminal class: CERTIFIED_FINITE_RESULT

Original prompt complete: true

## Conclusion

The existence of an infinite additive-square-free word over some finite
integer alphabet is not proved or disproved here. It remains open in the
primary-source corpus checked on 2026-08-30.

This project establishes the following exact finite theorem. For every
primitive normalized four-letter integer alphabet with maximum at most 5,
modulo reflection, the exact maximum ASF lengths are:

| Alphabet | Exact maximum |
|---|---:|
| \(\{0,1,2,3\}\) | 50 |
| \(\{0,1,2,4\}\) | 62 |
| \(\{0,1,3,4\}\) | 55 |
| \(\{0,1,2,5\}\) | 86 |
| \(\{0,1,3,5\}\) | 88 |
| \(\{0,1,4,5\}\) | 55 |
| \(\{0,2,3,5\}\) | 55 |

The values 86 and 88 were not located in the dated result-specific search;
this is not a priority claim.

A second exact result rules out every fixed point of a four-symbol 2-uniform
endomorphism prolongable on a letter: each contains an abelian square ending
within its first 19 symbols, hence an additive square under every integer
weighting. This does not cover codings from more hidden states, nonuniform
morphisms, or uniform length at least 3.

## Exact certificates

Principal certificate:

    certificates/census_max5.json

SHA-256:

    ebeb72ca4f04e377de266f4c403f6e2480bed3232feabb923d1436685057ce19

Independent C++ evaluator SHA-256:

    dc8c5e25393fd58456ab72178b79cd636ec6f4006ccdfd80a4b363e1c766ef19

Restricted morphism certificate:

    certificates/uniform2_no_go.json

SHA-256:

    02ece3207d0ed799dc0b23e8770cc9aaa598c668a46bfa75ad31f27f2a454e76

## Independent audit

Builder, Breaker, Certifier, and Referee roles were completed serially in
audit/. The independent census verifier imports no discovery output and
rebuilds all seven trees using right-tail cumulative sums. The separate
morphism verifier uses direct multiset comparison. Seven corrupted schema or
coverage inputs and one changed numeric invariant were rejected.

The Referee found that an early coordinator did not enforce complete
seven-alphabet coverage. The coordinator was repaired, a record-deletion test
was added, and the full seven-tree replay was rerun successfully.

## Reproduction

Full finite census:

    python3 certificates/verify_finite_census.py \
      certificates/census_max5.json

Expected terminal status: VERIFIED with records=7.

Restricted morphism class:

    python3 certificates/verify_uniform2_no_go.py \
      certificates/uniform2_no_go.json

Fail-closed tests:

    python3 tests/test_fail_closed.py

Expected terminal line:

    FAIL_CLOSED_TESTS_OK valid_cases=2 rejected_corruptions=7

Clean paper build:

    cd paper
    latexmk -C main.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error \
      -file-line-error main.tex

## Manuscript and limitations

The retained manuscript is paper/main.pdf. It is a five-page paper about the
certified finite census and restricted morphism theorem, not a paper claiming
to solve the infinite problem. The LaTeX audit reports nine cited and nine
defined entries with no missing or unused keys. Every final PDF page was
rendered and inspected; metadata, author, affiliation, and both email
addresses match the user's specification.

No proof assistant was used.
