# Certifier notes

Certificate schema: `erdos699-i3-scan-v1`.

The serialized certificate records the exact inclusive \(n\)-range, fixed
\(i=3\), the diagnostic number of anchor candidates, and either a literal
counterexample or `null`.  The independent verifier accepts only the exact
seven-field null-result schema; it rejects missing fields, duplicated keys,
trailing payloads, changed strata, and non-null witnesses.

The C++ verifier does not read the candidate count or trust elapsed time.  It
rebuilt the complete enumeration from `n_min` and `n_max`; its frozen strict
output reports 43,631,335,536 anchor candidates.  The fast release binder then
parses the canonical JSON and strict output together, binds the exact endpoint
and \(i=3\), requires both count fields to equal 43,631,335,536, and pins the
certificate/source/output SHA-256 values and build command.  Runtime remains
untrusted.  The binder rejects changed endpoint, bad hash, changed-count
false-null, truncated output, and duplicate certificate or binding fields.
