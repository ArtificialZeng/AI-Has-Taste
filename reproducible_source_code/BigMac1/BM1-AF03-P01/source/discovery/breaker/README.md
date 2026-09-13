# Breaker route: exact pseudo-Boolean feasibility

This route starts from the literal 0--1 system

\[
x_E+x_{E'}\le 1\quad(E\cap E'=\varnothing),\qquad
\sum_{E\supset S}x_E\ge2\quad(S\in\tbinom{[n]}3).
\]

`generate_pb_witness.py` emits that system in OPB format.  For use with the
locally available CaDiCaL solver, it also emits an equisatisfiable CNF using
pair-witness auxiliary variables.  This encoding is structurally independent
of the no-auxiliary long-clause encoding in `code/generate_cnf.py`.

For each triple, its CNF block contains one auxiliary variable for every pair
of extensions.  A cover clause requires one auxiliary variable, and two
binary implications force the corresponding primary extension variables.
Thus a satisfying assignment has two selected extensions.  Conversely, any
primary assignment satisfying the OPB inequality can make one witness for a
selected pair true.

The boundary `n=8` is included as a positive control.  At `n=8`, disjoint
4-sets are exactly complementary pairs, so the intersecting constraints reduce
to 35 independent at-most-one constraints.  A SAT model is extracted as a
literal family and checked from the definitions by `verify_family.py`, which
does not import the generator.

Run `python3 discovery/breaker/rerun.py` from the project root.  The exact
subcommands, solver statuses, counts, and SHA-256 hashes are recorded in
`run_log.json`.  Run `python3 discovery/breaker/test_verify_family.py` for the
positive-control check and five fail-closed mutation tests.
An `UNSATISFIABLE` solver status in this breaker directory is discovery
evidence only; it is not an LRAT/DRAT certificate.
