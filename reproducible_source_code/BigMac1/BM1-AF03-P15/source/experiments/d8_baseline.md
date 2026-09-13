# Exact reconstruction of the published \(D_8\) boundary

Gaetz--Gao report verification through \(n=8\) but do not publish their code
or flow.  This project therefore rebuilt \(D_8\) from the signed-cycle
quotient rather than importing a result.

Exact summary:

- \(|D_8|=5{,}160{,}960\);
- 95 \(B_8\)-conjugacy cells in \(D_8\);
- rank-cell counts \((1,1,3,5,11,16,24,22,12)\);
- rank sizes
  \((1,56,1316,16856,127694,578984,1505524,1984584,945945)\);
- 330 allowed quotient cover pairs and 172 positive exact orbit flows;
- all eight adjacent-rank transportation systems feasible over the integers.

The final independent check reports 177 cleared integer orbit equations and
9,375,974 lifted vertex-side equations.  The ordinary rank vector is not
palindromic; all eight layers were checked.

Reproduce with:

```bash
python src/discover_orbit_flow.py 8 experiments/d8_baseline_flow.json
python certificates/verify_d9_flow.py \
  --expected-n 8 experiments/d8_baseline_flow.json
python discovery/verify_orbit_flow.py \
  discovery/d8_orbit_flow_candidate.json
```

Recorded certificate hashes for the two independently generated formats:

- `experiments/d8_baseline_flow.json`:
  `7c7fbaa37b41b44022060bc56857a5ecf1f48695057c23e594a89d18127536c5`;
- `discovery/d8_orbit_flow_candidate.json`:
  `2b1c573972e7f8b7ff310f5093b77001379083f3e25838acc614b83afebbb2c8`.
