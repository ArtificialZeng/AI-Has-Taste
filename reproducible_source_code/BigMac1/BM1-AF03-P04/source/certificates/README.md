# Exact certificate

`transitive_arrays_n_le_5.json` contains every transitive equality pattern
modulo color relabeling for \(2\le n\le5\).  Index permutations are deliberately
not quotiented, which keeps the completeness reconstruction transparent.

Run:

```bash
python verifier/verify_certificate.py certificates/transitive_arrays_n_le_5.json
python verifier/verify_symbolic_expansion.py certificates/transitive_arrays_n_le_5.json
python tests/test_verifier.py
```

The first verifier does not import discovery code.  It strictly parses the
serialized input, reconstructs the complete type set by an independent
implementation of the source's classification, checks transitivity and every
local residual label, and prints input/code hashes.  The second verifier starts
from the \(n^2\) terms of \(R\), expands all ordered pairs in each of the three
commutators, and checks the component formula.  The corruption suite requires
fail-closed rejection of malformed, missing, duplicate, nontransitive,
digest-corrupted, and unknown-field inputs.
