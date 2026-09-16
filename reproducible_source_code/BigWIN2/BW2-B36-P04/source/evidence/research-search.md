# Focused primary-source/database search

Date: 2026-09-06 (Asia/Shanghai)

Two research passes searched the exact DOI `10.2139/ssrn.7395382`, its supplied
title, the recurrence, `a22`, the earlier factor `7795379`, and the newly found
factor `108099707` through web discovery. No inspected result reported a factor
of (a_{22}). Exact-title and DOI searches did not surface the cited record.
Direct attempts to retrieve the DOI landing page and corresponding SSRN
abstract/PDF were blocked by the available web fetcher (unsafe-URL/403
responses); a command-line Crossref/SSRN fetch also failed because outbound
network access was unavailable. Thus the paper's full text was not verified.

The exact recurrence entry OEIS A102847 was freshly inspected in pass 2. Its
version shown as last modified 2026-09-03 states the recurrence, lists terms
through (a_8), and retains a 2006 comment that (a_{20}) was unknown. It contains
no factor or status assertion for (a_{22}). FactorDB-specific discovery did not
surface a record for the recurrence or `108099707`, while direct FactorDB query
URLs were rejected by the available fetcher. These are documented access and
search outcomes, not evidence that the factor is new.

This is a bounded negative literature/database search, not a priority or novelty
claim. The mathematical resolution does not depend on the inaccessible paper or
database: the explicit factor, primality proof, and divisibility chain are
certified in `a22-certificate.md` and `verify_a22_certificate.py`. Pass 2 also
added `a22-independent-trial-verification.py`, which avoids the Pocklington data
and proves primality by exhaustive trial division through
(\lfloor\sqrt{108099707}\rfloor=10397) before recomputing the recurrence.
