# Orbit search record

Date: 2026-09-06  
Job: `win-00040-p03-research-837d53ce3818`

The previous checkpoint requested optimization on low-dimensional vectors
constant on Hamming-weight and facet-layer orbits. Running

```text
python3 evidence/orbit_search.py
```

gave:

```text
volume distribution {0: 1360, 1: 2672, 2: 320, 3: 16}
FAMILY Hamming-weight: 5 orbits
  2-level partitions tested=15; best ratio=0.820312500000006; orbit colors=(0, 1, 1, 0, 0); log-values=(1.74492651263607e-08,)
  3-level partitions tested=25; best ratio=0.999999997433264; orbit colors=(0, 1, 2, 2, 2); log-values=(24.0, 12.0)
  full-orbit optimization best ratio=0.999999908728825; log-values=(17.999999989114052, 9.624262627189076, 0.910662272944871, -17.52921899064676); orbit multiplicities=[1, 4, 6, 4, 1]
FAMILY fixed-facet-layer: 8 orbits
  2-level partitions tested=127; best ratio=0.937499999999714; orbit colors=(0, 0, 0, 0, 1, 1, 1, 1); log-values=(28.0,)
  3-level partitions tested=966; best ratio=0.999999999999886; orbit colors=(0, 0, 0, 1, 0, 0, 2, 1); log-values=(-20.603906250000172, 30.0)
  full-orbit optimization best ratio=1; log-values=(-17.831101527561366, -15.087583432018917, 1.4963354251792085, 17.89672476190843, -17.686096224179213, -17.71348473738723, -17.719150852122908); orbit multiplicities=[1, 3, 3, 1, 1, 3, 3, 1]
```

The program enumerates all orbit-level set partitions but uses floating-point
local/global optimization over their positive values. Therefore the reported
ratios are observations, not certified suprema. No strict reversal was found.
The exact all-two-valued theorem obtained by extending the search to all
(32767) vertex bipartitions is documented separately in
`two-level-result.md`.
