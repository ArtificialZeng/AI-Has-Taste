# Radius-seven exchange certificate package

This archive accompanies “Certified radius-seven exchange rigidity for a
binary subspace code” by Zijian Zeng.

The finite theorem, scope limitation, and reproduction commands are in
`FINAL_STATUS.md` at the project root.  The decisive acceptance command is:

```bash
python3 verification/verify_radius6.py \
  --radius 7 \
  --result experiments/radius7_search_diagnostic.json
```

The verifier uses only the Python standard library and exact binary/integer
arithmetic.  No proof assistant was used.
