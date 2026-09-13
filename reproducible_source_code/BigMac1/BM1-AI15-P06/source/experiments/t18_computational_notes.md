# Exact finite computation for the `t=18` endpoint branch

Date: 2026-08-29  
Scope: the chain-size, sorted-partition, and endpoint-category arithmetic at
total positive-gap count `t=18`.  This computation is independent of the
separate structural argument for the remaining rank-ten case.

## Certified result

The exact enumeration has the following two conclusions.

1. Of the 88 sorted five-part partitions of 18 with every part between 0 and
   the Naimark upper bound 9, exactly eight are not pruned by the rational
   spectral-deficit lower bounds.
2. Exhausting all `R/O/N` endpoint categories for those eight partitions
   proves that five patterns have at most nine non-singleton cut copies.  The
   endpoint bounds alone still permit exactly ten non-singleton copies for
   the other three patterns.

Here the serialized category `R` means a chain with two singleton endpoints;
it should not be confused with the proof notation \(R_{\rm ns}\) below for
the *total number of non-singleton cut copies*.

| Sorted gap-count partition | General lower numerator | Compatible endpoint assignments | Minimum singleton copies \(S\) | Maximum \(R_{\rm ns}=18-S\) | Exact endpoint conclusion |
|---|---:|---:|---:|---:|---|
| `(7,3,3,3,2)` | 7,933,248,737 | 1 | 10 | 8 | \(R_{\rm ns}\le9\) |
| `(6,4,3,3,2)` | 7,880,422,701 | 2 | 9 | 9 | \(R_{\rm ns}\le9\) |
| `(5,5,3,3,2)` | 7,871,578,829 | 2 | 9 | 9 | \(R_{\rm ns}\le9\) |
| `(5,4,4,3,2)` | 7,834,373,983 | 3 | 9 | 9 | \(R_{\rm ns}\le9\) |
| `(4,4,4,4,2)` | 7,797,169,137 | 7 | 8 | 10 | \(R_{\rm ns}=10\) not excluded |
| `(6,3,3,3,3)` | 7,719,940,827 | 6 | 9 | 9 | \(R_{\rm ns}\le9\) |
| `(5,4,3,3,3)` | 7,673,892,109 | 12 | 8 | 10 | \(R_{\rm ns}=10\) not excluded |
| `(4,4,4,3,3)` | 7,636,687,263 | 21 | 8 | 10 | \(R_{\rm ns}=10\) not excluded |

All lower numerators in this note have common denominator \(10^9\).  The
deficit budget is exactly 8, so a partition is rigorously pruned when its
lower numerator is at least \(8\cdot10^9\).  The other 80 partitions are
pruned by that rule.

Consequently the exact lists are

\[
\begin{aligned}
R_{\rm ns}=10\text{ not excluded}:\quad &
(4,4,4,4,2),\ (5,4,3,3,3),\ (4,4,4,3,3),\\
R_{\rm ns}\le9:\quad &
(7,3,3,3,2),\ (6,4,3,3,2),\ (5,5,3,3,2),\\
& (5,4,4,3,2),\ (6,3,3,3,3).
\end{aligned}
\]

The second line becomes an exclusion only after importing the separately
proved singleton-compression obstruction for \(1\le R_{\rm ns}\le9\).  The
certificate here checks the finite endpoint arithmetic, not that theorem.

## Complete parameterization and treatment of ties

A coordinate with \(\ell\) positive gaps determines a strictly increasing
sequence of prefix cardinalities

\[
1\le k_1<\cdots<k_\ell\le10.
\]

Coordinate ties create zero gaps and hence do not appear in this sequence;
each tied level is represented by the jump between successive prefix sizes.
Thus deleting zero gaps does not silently assume a strict coordinate order.
Conversely, every increasing cardinality sequence is realized by some nested
chain of label subsets, so these sequences are complete for any lower bound
that depends only on cut sizes.  Label incidence is deliberately forgotten
at this stage and is part of the open gap stated below.

Reversing a coordinate replaces a sequence by

\[
(k_1,\ldots,k_\ell)\longmapsto
(11-k_\ell,\ldots,11-k_1).
\]

This preserves every deficit term and swaps the two endpoints, so retaining
the lexicographically smaller representative loses no chain-size or endpoint
category.  For lengths zero and one there are respectively 1 and 5 canonical
types.  For lengths 2 through 9 all increasing subsets of
\(\{1,\ldots,10\}\) are enumerated before reflection quotienting.  The
resulting canonical counts by length 0 through 9 are

```text
1, 5, 25, 60, 110, 126, 110, 60, 25, 5.
```

Finally, all combinations with repetition of five lengths in
\(\{0,\ldots,9\}\) summing to 18 are generated, then written in decreasing
order.  This is exactly the quotient by coordinate permutation and yields
88 sorted partitions.  Every survivor has length at least two in every
coordinate.  For each survivor all \(3^5=243\) assignments of the exhaustive
endpoint categories are checked:

- `R`: prefix sizes include both 1 and 10, hence two singleton copies;
- `O`: exactly one of sizes 1 and 10 occurs, hence one singleton copy;
- `N`: neither occurs, hence no singleton copies.

Equal chain lengths cause some redundant assignments, but no assignment is
omitted.  Across eight survivors the verifier reconstructs 1,944 assignments.

## Exact rational deficit bounds

For adjacent cut sizes \(a<b\), put

\[
q_{a,b}=\frac{a(11-b)}{b(11-a)},\qquad
f_{a,b}=\frac{2\sqrt{q_{a,b}}}{1+\sqrt{q_{a,b}}}.
\]

For each of the 45 pairs, the manifest stores the unique largest integer
\(N_{a,b}\) such that

\[
\frac{N_{a,b}}{10^9}<f_{a,b}.
\]

The independent verifier does not evaluate a square root.  It proves the
lower bound and its maximality using only integer and `Fraction` arithmetic:

\[
q_{a,b}>
\left(\frac{N_{a,b}/10^9}{2-N_{a,b}/10^9}\right)^2,
\quad
q_{a,b}\le
\left(\frac{(N_{a,b}+1)/10^9}{2-(N_{a,b}+1)/10^9}\right)^2.
\]

The generator uses a floating square root only to choose a nearby starting
integer; exact comparisons move that integer in either direction until the
two displayed conditions hold.  The verifier reconstructs all 45 values
independently, so floating point is not part of the certificate.

Summing adjacent term numerators and minimizing over the complete canonical
chain list gives the following bounds.  Entries are numerators over
\(10^9\); a dash means the category is impossible at that length.

| \(\ell\) | General | Minimizing sizes | `R` | `O` | `N` |
|---:|---:|---|---:|---:|---:|
| 0 | 0 | `()` | -- | -- | -- |
| 1 | 0 | `(1)` | -- | -- | -- |
| 2 | 181,818,181 | `(1,10)` | 181,818,181 | 259,463,815 | 363,636,363 |
| 3 | 962,587,023 | `(1,5,10)` | 962,587,023 | 1,115,343,461 | 1,282,807,583 |
| 4 | 1,903,837,739 | `(1,3,7,10)` | 1,903,837,739 | 2,079,310,053 | 2,263,626,239 |
| 5 | 2,882,293,301 | `(1,2,5,8,10)` | 2,882,293,301 | 3,066,609,487 | 3,257,702,991 |
| 6 | 3,869,592,735 | `(1,2,4,7,9,10)` | 3,869,592,735 | 4,060,686,239 | 4,254,539,413 |
| 7 | 4,863,669,487 | `(1,2,3,5,7,9,10)` | 4,863,669,487 | 5,057,522,661 | 5,252,595,489 |
| 8 | 5,860,505,909 | `(1,2,3,4,6,8,9,10)` | 5,860,505,909 | 6,055,578,737 | 6,251,027,625 |
| 9 | 6,858,561,985 | `(1,2,3,4,5,7,8,9,10)` | 6,858,561,985 | 7,054,010,873 | -- |

The complete category minimizers, all 45 term bounds, all 88 partition
records, and every compatible endpoint assignment are serialized in
`certificate/t18_endpoint_manifest.json` rather than relying on this summary.

## Independent verifier and fail-closed audit

`certificate/t18_verify_endpoint_manifest.py` independently reconstructs:

- the schema and fixed mathematical scope;
- the generator SHA-256 binding;
- validity and maximality of all 45 rational term numerators;
- every canonical chain and endpoint-category minimum;
- all 88 sorted partitions and exactly eight survivors;
- all 1,944 endpoint assignments and both final pattern lists.

It contains no Python `assert` statement, checks its own AST for removable
assertions, and returns a nonzero code with JSON status `FAIL` on any error.

The external runner creates all altered inputs under `/private/tmp`, outside
the project.  It ran the genuine certificate and fourteen mutations under
each of normal, `-O`, `-I`, and `-O -I` modes: 60 executions total.  The four
genuine executions passed, and all 56 tampered executions failed.  Mutations
cover missing scope, fixed-parameter changes, denominator and term changes,
chain and partition changes, endpoint results, the `R=10` list, and generator
hash binding.

## Reproduction

Run from the project root:

```bash
python3 experiments/t18_endpoint_enumerate.py | tee experiments/t18_endpoint_enumerate.log
python3 certificate/t18_verify_endpoint_manifest.py certificate/t18_endpoint_manifest.json | tee certificate/t18_endpoint_verifier.log
python3 -m py_compile experiments/t18_endpoint_enumerate.py certificate/t18_verify_endpoint_manifest.py experiments/t18_fail_closed_matrix.py
python3 experiments/t18_fail_closed_matrix.py | tee logs/t18_fail_closed_matrix.json
```

The computation is deterministic and uses no random seed.  Recorded
environment: CPython 3.14.7 on `macOS-26.5-arm64-arm-64bit-Mach-O`.

SHA-256 values before adding this note:

```text
52d1e68fa9bd32e68fa93e6a030980de982cf46c712fe2b29a2ae07c3478cc85  experiments/t18_endpoint_enumerate.py
0ca709a95df4164ed9a2106cd7502efd2613848d0c4b4544b4e99dfdce470887  certificate/t18_endpoint_manifest.json
6feb99e1fd6b6c8793011597a0f8c172e89fe838c7cc93fd08e5f77761b61a0e  certificate/t18_verify_endpoint_manifest.py
0bd4e27f3e5dc0a786b6cc6defc91298c5169126e608265ccda8c0c1f1b2df1b  experiments/t18_endpoint_enumerate.log
10113e14b556924553cda04a2f54677f459efd39456dfdb956657b080c8b1eb9  certificate/t18_endpoint_verifier.log
c0ed14acfbeabb7f52616009b867df5d94b545697996cbde6da6363643eb2d18  experiments/t18_fail_closed_matrix.py
4fc5bf85e65215a658181903323d7404eb42b0879952c13fdadc0a9761bb65de  logs/t18_fail_closed_matrix.json
```

## Strict limitation and remaining gap

This is a `CERTIFIED_FINITE_RESULT` only for the stated t=18 arithmetic.  A
record marked `R10_not_excluded` says only that independently minimizing the
five endpoint-category deficits permits eight singleton endpoint copies.  It
does **not** exhibit compatible label incidences, a uniform-cut
decomposition, an LP-feasible system, or an eleven-point equilateral set.

The three open endpoint patterns are therefore precisely
`(4,4,4,4,2)`, `(5,4,3,3,3)`, and `(4,4,4,3,3)`.  Excluding them requires an
additional exact incidence/design/rank-ten obstruction, not more numerical
precision in the present minimization.  No numerical or MILP infeasibility
claim is made.  No proof assistant was used in this branch.
