# Win36-04 — Find a certified prime factor of a22 in a(n+1)=a(n)^2+2

Define integers a0=1 and

    a(n+1) = a(n)^2 + 2  for n>=0.

Find a prime q satisfying 1<q<a22 and q divides a22. Such a certificate proves a22 composite.

The supplied primary lead is Zijian Zeng, *A Certified Prime Factor of A 20 in the Recurrence A N +1 = A 2 N + 2*, DOI 10.2139/ssrn.7395382, recorded in row 46 of `resources/user-bibliography/registry.json`. It gives 7,795,379|a20 and, together with an odd-index congruence, proves a5 through a21 composite; it makes no assertion for n>=22.

A successful result must include a deterministic primality proof for q and an exact modular-recursion verification ending in a22 congruent to 0 modulo q. A bounded unsuccessful factor search does not prove primality and need not produce a manuscript. First verify whether a factor of a22 has already been reported.

