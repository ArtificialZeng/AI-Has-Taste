# Exact matching spectrum of the three-job 11/6 tight family

## Immutable source statement

For every real parameter (0<\delta<1/6), consider the three-machine restricted-assignment instance (I_\delta) from Theorem 2 of the source, at threshold (T=1) and Step-2 threshold (\beta=2/3):

- job (q): size (1), allowed on machines {0,1}, with (x_{q0}=1/3+\delta) and (x_{q1}=2/3-\delta);
- job (h): size (1/2), allowed on machines {0,2}, with (x_{h0}=2/3) and (x_{h2}=1/3);
- job (r): size (1/3-\delta), allowed only on machine 0, with (x_{r0}=1).

Jobs are ordered on each machine by nonincreasing size. Fraction intervals and slots use the source's half-open convention, and a job is adjacent to a slot exactly when their half-open intervals have nonempty intersection. Step 2 assigns no job in this family.

Prove or disprove the following full-parameter claim:

1. the slot graph has exactly eight valid job-to-slot matchings;
2. among the schedules induced by these matchings, the minimum makespan is exactly (1);
3. the maximum makespan is exactly (11/6-\delta).

Determine the complete makespan multiset as an optional strengthening when it follows from the same exact enumeration.

## Quantifiers and scope

- The assertion is uniform for every real (\delta\in(0,1/6)), not only sampled rational values.
- The fractional point, machine/job sets, job sizes, ordering rule, half-open slot convention, and valid-matching definition are fixed as above.
- The result concerns all valid Step-3 matchings for this fixed fractional solution. It does not change the general approximation theorem or claim that an arbitrary LP solver returns this fractional point.

## Primary source and nearest result

- *The hidden output space of a classical rounding scheme* (title as given in the downloaded primary manuscript), arXiv:2609.03890v1 (2026), https://arxiv.org/abs/2609.03890.
- Local primary PDF: `batches/inbox/bigWin-55-materials/2609.03890.pdf`.
- SHA-256: `889389afa75709325024fa890fb809ad125e09e607517a963e45a4b368de6b05`.
- Locators: slot convention, PDF pp.6–9; Theorem 2 and its explicit family, PDF pp.10–11; Measurement 4, PDF p.11.
- Nearest result: Theorem 2 exhibits one valid matching with makespan (11/6-\delta) for every (0<\delta<1/6). Measurement 4 reports exhaustive counts and extrema only for (\delta\in{10^{-2},10^{-3},10^{-4}}), explicitly labeling them measurements rather than a theorem.

## Proposed contribution boundary

Upgrade Measurement 4 from three sampled parameters to a symbolic theorem over the entire open interval. This is a finite but nontrivial reproducibility result about all nondeterministic outputs of the rounding step. Do not restate Theorem 2 as new.

## Cheapest decisive test and certificates

Construct the slot-adjacency graph symbolically, list all potential ordering/contact breakpoints in (0<\delta<1/6), prove the adjacency pattern is constant on each resulting cell, enumerate every perfect job-slot matching exactly, and simplify every induced machine load as an affine function of (\delta). The certificate should contain the eight matching templates, their loads/makespans, exact interval inequalities, and an independent exact-rational replay script. A single additional valid matching, missed breakpoint, or parameter value with different extrema refutes the frozen claim.

## Provenance

Prepared on 2026-09-07 from the primary arXiv PDF during the authorized primary-literature fallback because the confirmed Chrome target tab could not be attached. This statement is frozen and may not be silently replaced by a finite sample.
