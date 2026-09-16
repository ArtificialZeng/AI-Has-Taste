# Exact small-case triage observation

Provenance: `win-00052-p03-triage-b204f31daf37`  
Date: 2026-09-07

Running

```text
python3 evidence/triage_exact_check.py
```

with SymPy constructs the generator-sum matrices directly from the colored-word and color-position actions in `problem.md`. The script checks symmetry, sizes, row sums, and the following exact identities:

\[
\det(xI-A_{\rm Cay})
=x^{10}(x-4)(x-2)^8(x+2)^8(x+4)(x^2-8)^2,
\]

\[
\det(xI-A_{\rm Sch})
=x^3(x-4)(x-2)^2(x^2-8).
\]

Hence this enumeration places \(2\sqrt2\) immediately below \(4\) in both spectra: \(4>2\sqrt2>2\), since \(1<\sqrt2<2\). It therefore suggests the exact conclusion
\[
\psi_{4,2}=\beta_{4,2}=4-2\sqrt2.
\]

This is exact symbolic computation, not floating-point evidence. It is still only triage evidence: a research pass must independently reconstruct the matrices and audit the characteristic-polynomial certificates and group/action conventions before treating the conclusion as proved.

