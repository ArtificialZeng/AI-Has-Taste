# Precise problem statement

## Frozen source

The original wording is preserved verbatim in `source.md` (SHA-256
`1fcadd16a0f6d7f663da0591cc6110bac15c17c5d40d0a81d90753dd2f105dd0`).
This file records its mathematical interpretation and does not replace it.

## Definitions and quantifiers

Let \((a_n)_{n\in\mathbb Z_{\ge 0}}\) be the unique integer sequence defined by

\[
a_0=1,\qquad a_{n+1}=a_n^2+2\quad(n\in\mathbb Z_{\ge0}).
\]

The task is constructive: exhibit an integer \(q\) such that

1. \(q\) is prime;
2. \(1<q<a_{22}\); and
3. \(a_{22}\equiv0\pmod q\).

Equivalently, exhibit a proper prime divisor of the positive integer \(a_{22}\).
Because \(a_0\ge1\) and \(a_{n+1}>a_n\), all terms are positive and strictly
increasing; hence a displayed proper divisor proves that \(a_{22}\) is
composite. The first terms, useful for checking indexing, are
\(a_0=1,a_1=3,a_2=11,a_3=123,a_4=15131,a_5=228947163\).

## Required certificate and scope

A successful answer must give the explicit decimal integer \(q\), together with:

- a deterministic, independently checkable proof that \(q\) is prime;
- an exact modular computation starting with \(r_0=1\), applying
  \(r_{n+1}\equiv r_n^2+2\pmod q\) for every \(0\le n<22\), and ending with
  \(r_{22}=0\); and
- an exact justification of \(q<a_{22}\) (a rigorous lower bound for \(a_{22}\)
  exceeding \(q\) is enough).

Probable-prime output, floating-point computation, a search log with no factor,
or a modular relation not carried through all 22 indexed steps does not meet the
claim. The task asks only for one certified factor; it does not ask for the full
factorization of \(a_{22}\), the primality status of the cofactor, or any assertion
about \(a_n\) for \(n>22\).

## Prior-result boundary and status

The supplied bibliographic lead is Zijian Zeng, *A Certified Prime Factor of A
20 in the Recurrence A N +1 = A 2 N + 2*, DOI
[`10.2139/ssrn.7395382`](https://doi.org/10.2139/ssrn.7395382). The local routing
record reports the certified divisor \(7{,}795{,}379\mid a_{20}\) and a consequence
that \(a_5,\ldots,a_{21}\) are composite, while explicitly reporting no assertion
for \(n\ge22\). The full paper was not locally cached, so these theorem details
remain unverified and must not be used as proved facts without inspecting the
paper.

Accordingly, the present source status is **status-uncertain**: the supplied lead
does not settle \(a_{22}\), and the limited exact-phrase/sequence searches recorded
in `evidence/triage-search.md` did not locate a reported factor of \(a_{22}\), but
that negative search is not proof that no factor has already been published.

## Triage target

Nearest prior result: the reported certified factor of \(a_{20}\) above.
Proposed delta: one certified proper prime divisor of \(a_{22}\).
Verification route: deterministic primality certificate plus the 22-step exact
modular recurrence. The first discriminating research test is a targeted search
of primary factor databases/papers for an already reported \(a_{22}\) factor;
if none is found, run a bounded exact small-factor/ECM search while recording its
coverage and treating failure only as a search outcome.
