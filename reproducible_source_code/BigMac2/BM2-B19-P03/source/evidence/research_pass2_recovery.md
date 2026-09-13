# Research pass 2 recovery record

- Job: `bigMac-00019-p03-research-6ab541841e47`
- Role/model: research, `gpt-5.6-sol`, `ultra`
- Start: 2026-09-08T16:31:35Z
- End condition: 25-minute infrastructure timeout; no `result.json`
- Imported usage: unknown
- Immutable `source.md`: unchanged

## New exact artifacts and bounded solver observations

The two-local-maximizer restriction `good_edge.cnf` has 812 variables and
665,028 clauses. Kissat 4.0.4 reported UNSAT in 4.24 seconds (17,901
conflicts), but no proof trace was requested or retained; this rejects only
that restriction at solver-status level.

`build_compact_orientation_cnf.py` created an unrestricted sequential-counter
encoding with 124,236 variables (2,436 original and 121,800 auxiliary),
459,186 clauses, and SHA-256
`8a146dc41b7cf6775c8eacfe704e377efdc9bfe6848f11e55ce937f35e7a050f`.
CaDiCaL's 300-second SAT-targeted run ended `UNKNOWN` after 860,626 conflicts.
No model or proof exists, and no small exhaustive equivalence fixture was
completed before the timeout.

`build_search_instance.py` emitted 812 exactly-one rows and 7,308 cycle rows
in `orientation_search_instance.tsv`; its SHA-256 is
`0da29a40b4569089ebf23eb47f5bdd13519e928d579f4915ceaee9bf9e0e8208`.
The row requirement is `33-2L`, and each cycle row contains precisely the
unique outside-neighbour choice type for each of its vertices.

SciPy/HiGHS 1.8.0 reported the resulting 2,436-binary model infeasible at one
root node after 14,129 LP iterations, with no incumbent and no generated cuts.
The separate C++ program `extract_lp_dual_ray.cpp` used HiGHS 1.15.1 with
continuous variables, presolve disabled, and simplex; it also reported
infeasibility and wrote 1,996 nonzero decimal row multipliers to
`lp_dual_ray.txt`, SHA-256
`65dbf463002e2978e500375938014e442d1c1c25899f0e92fd6b6e0bf44bab21`.

## Epistemic status and recovery decision

The agreement of two HiGHS interfaces strongly motivates an exact certificate
reconstruction but is not itself a proof. The dense decimal ray has not been
rationalized, checked against all primal columns and bounds, or replayed by an
independent persisted exact-arithmetic implementation. A separate read-only
spot replay suggests nearest-integer row weights give a very large exact
margin, which is the concrete test for the next worker, not a current claim.

This new LP signal and the explicit next test justify the third and final
research pass with counters preserved. That pass must either deliver a
standalone rational Farkas/weighted-sum certificate plus independent checker,
or park the unresolved project. Further bare SAT/MILP runs are not a valid
next test.
