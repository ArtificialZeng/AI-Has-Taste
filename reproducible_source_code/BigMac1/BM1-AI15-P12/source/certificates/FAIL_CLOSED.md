# Fail-closed certificate verification

Both `verify_n3_sos_stdlib.py` and `verify_n3_sos.py` bind the exact bytes of
`n3_sos_certificate.json` to SHA-256
`b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0`.
They reject a mismatched hash before parsing or computing.  After the hash
gate, they reject duplicate JSON keys, non-finite JSON constants, non-UTF-8
input, every extra or missing top-level or normal-form key, wrong JSON types,
and any change to theorem-bound values.  They then independently reconstruct
the 3-by-3 and duplicated 6-by-6 permanents by their permutation definitions.

Run the positive and negative checks from the project root:

```sh
python certificates/verify_n3_sos_stdlib.py
python certificates/verify_n3_sos.py
python certificates/test_fail_closed.py
```

The negative test uses temporary copies only.  Its named cases are:

- `badhash`: semantically identical JSON with different bytes;
- `extra`: an unexpected top-level key;
- `drop`: a missing nested normal-form key;
- `tamper`: a changed projective row parameter.

It also tests duplicate-key and `NaN` parser inputs.  Every CLI negative case
must return nonzero and fail at the embedded hash gate; schema-invalid cases
must additionally fail the directly imported strict schema validator.
