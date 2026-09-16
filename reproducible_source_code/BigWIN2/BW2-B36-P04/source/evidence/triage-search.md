# Triage search record

Date: 2026-09-06 (Asia/Shanghai)

Purpose: check whether a factor of \(a_{22}\) for
\(a_0=1,\ a_{n+1}=a_n^2+2\) was readily reported, and identify the nearest prior
result. This was a bounded discovery search, not an exhaustive literature review.

Queries inspected through web search:

- `"a_22" "a_n^2+2" factor`
- `"a22" "7795379" recurrence`
- `"a_{22}" "a_{n+1}=a_n^2+2"`
- `site:oeis.org 1, 3, 11, 123, 15131`
- `"10.2139/ssrn.7395382"`
- `"Certified Prime Factor" "a_20" recurrence`
- `"1, 3, 11, 123, 15131, 228946163"`

No search result inspected stated a prime divisor of \(a_{22}\). Generic results
were largely unrelated. OEIS entry A378395 was relevant only as an independently
visible occurrence of the initial recurrence-derived values through 228947163;
it did not report factors of \(a_{22}\).

Primary/authoritative leads and access status:

- SSRN record DOI `10.2139/ssrn.7395382`: supplied locally in
  `literature/user-library-record.md` and `literature/source.bib`; the full paper
  was not in the local cache. Direct web discovery did not return the identified
  abstract page during this job. Therefore its reported theorem details were not
  verified from the paper.
- OEIS A378395: <https://oeis.org/A378395>, inspected 2026-09-06. It concerns a
  Pythagorean-triple construction and displays related initial values, not the
  factorization target.

Conclusion: no already-reported \(a_{22}\) factor was located in this limited
search. This supports advancing to a focused source/database check and factor
search, but does not support novelty or open-status claims.
