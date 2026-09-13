# Exact \(D_4\) baseline reconstruction

## Purpose

This baseline reconstructs a smallest standard type-\(D\) instance from
signed permutations before relying on the \(D_9\) orbit reduction.  It is not
imported from Gaetz--Gao, whose published \(n\leq8\) report has no attached
certificate.

## Element-level reconstruction

The independent program `discovery/breaker_element_audit.py` enumerates all
\(2^3 4!=192\) even signed permutations and all 12 type-\(D_4\) reflections.
It constructs every upward cover by right multiplication, obtaining 1,152
directed cover edges.  It then checks, using integers and
`fractions.Fraction` only:

- the rank vector \((1,12,50,84,45)\);
- all 11 signed-cycle \(B_4\)-orbits and their class-size formula;
- the 13 actual \(D_4\)-conjugacy classes, including split classes;
- the three signed-cycle cover surgeries and every orbit-pair edge count;
- biregularity of every nonempty orbit-pair cover graph;
- a lifted normalized flow at every one of the 338 vertex-side equations
  across the four adjacent-rank layers.

The separate program `discovery/bruteforce_transition_check.py` uses a
different signed-window representation and independently checks class sizes
and transition support.

## Serialized baseline and fail-closed checker

`certificates/d4_baseline_flow.json` contains 14 positive exact rational orbit
flows.  `certificates/verify_d9_flow.py --expected-n 4` does not import any
discovery module.  It regenerates all partitions, ranks, class sizes, cover
multiplicities and per-edge lift values.  At the canonical scale

\[
L_i=\operatorname{lcm}(|P_i|,|P_{i+1}|),
\]

it also verifies the cleared integer equations

\[
L_i\sum_DF(C,D)=|C|\frac{L_i}{|P_i|},\qquad
L_i\sum_CF(C,D)=|D|\frac{L_i}{|P_{i+1}|}.
\]

## Reproduction

```bash
python src/discover_orbit_flow.py 4 certificates/d4_baseline_flow.json
python discovery/bruteforce_transition_check.py 4
python discovery/breaker_element_audit.py 4 \
  --output discovery/breaker_d4_element_audit.json
python certificates/verify_d9_flow.py \
  --expected-n 4 certificates/d4_baseline_flow.json
python tests/test_verify_d9_flow.py
```

Expected compact records include:

```text
elements=192, reflections=12, upward_directed_edges=1152, orbit_types=11
result=VERIFIED, endpoint=Abs(D_4) normalized flow,
cleared_integer_orbit_equations=18, lifted_vertex_equations=338
PASS: D4 and D9 certificates accepted; endpoint mismatch and 9 corruptions rejected
```

Hashes at this milestone:

- D4 certificate: `c5a5ff62b12182a7b56c13f76f0b866e67f0646de1c3b53cc3ab7f200596213f`;
- element-level audit JSON: `5ad30295397179277bba491260d444f509f6f0aaaecfdc8e182f2429b9027bfa`;
- independent checker: `a076f7dc4a715d0adb9d1c7b7946431a7f63de744b53a8782a6c50ed7580c706`.
