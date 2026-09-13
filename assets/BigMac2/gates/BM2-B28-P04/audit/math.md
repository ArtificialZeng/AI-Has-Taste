# Fresh mathematical audit of `nu(4,4)=15`

## Frozen scope and source comparison

This review concerns the exact frozen claim in `claim.json`, bound to snapshot
digest
`6103d3338e01807a90cdcdf1de4d1dcd19827711615d8f91d115fe1dbc0e6640`.
I independently recomputed the SHA-256 digest of every one of the ten frozen
files and the canonical digest of the snapshot mapping; all values agree with
`audit/snapshot.json`.

The cited Shin source defines

\[
\nu(h,4)=\min\{D\geq 0:\mathcal R(h,4)
=\{|hA|:A\subset [0,D]\cap\mathbb Z,\ |A|=4\}\}
\]

immediately before Corollary 10.5, and explicitly records
`nu(h,4)=N(h,4)-1`. Theorem 10.3 gives

\[
D_h^{\max}=\binom{h+2}{2}+\mathbf 1_{2\nmid h},
\]

and Corollary 10.5 states, for every `h>=2`,

\[
D_h^{\max}\leq \nu(h,4)\leq
\max\{h^2,D_h^{\max}\}.
\]

Thus its hypotheses apply at `h=4`, where `D_4^max=15`, and give
`15<=nu(4,4)<=16`. In particular, the definition and monotonicity of the
literal-interval spectra imply
`R_16(4,4)=R(4,4)`. The Zhang source separately states in Question 12.5 that
the all-`h` endpoint equality is open there and that the weak-type result does
not answer the label-level question. The submitted claim is correctly limited
to the single instance `(h,k)=(4,4)` and makes no all-`h` or priority claim.

## Reconstruction of the finite step

For a literal four-set `B={b0,b1,b2,b3}`, every member of `4B` is represented
by one of the 35 nonnegative coefficient vectors
`(c0,c1,c2,c3)` with coordinate sum four, and conversely. Hence taking the
number of distinct exact integer dot products computes `|4B|`; there is no
order-type, normalization, or preservation-of-relations assumption in this
step.

I performed a fresh exact computation using the mandated research Python. It
used `itertools.combinations` only to list the literal four-subsets and the
ordered Cartesian product `B^4` (256 ordered tuples for each `B`) to form the
sumset. This differs from both submitted realizations: the decisive program
uses explicit alphabet loops and coefficient vectors, while the earlier
program uses nondecreasing tuples. The fresh calculation obtained:

| endpoint `D` | four-sets checked | exact spectrum `R_D(4,4)` |
| --- | ---: | --- |
| 14 | 1365 | `{13,16,17,19,21,23,24,25,26,27,29,30,31,32,33,34}` |
| 15 | 1820 | `{13,16,17,19,21,23,24,25,26,27,29,30,31,32,33,34,35}` |
| 16 | 2380 | `{13,16,17,19,21,23,24,25,26,27,29,30,31,32,33,34,35}` |

Thus `R_15(4,4)=R_16(4,4)`. As an additional minimum check independent of
the cited lower bound, label 35 is absent from `R_14(4,4)` and is attained in
`R_15(4,4)` by `B=(0,1,11,15)`. Monotonicity then excludes every endpoint
below 15.

I also parsed both frozen JSON certificates and checked them against this
fresh computation. Specifically:

- the decisive implementation SHA-256 agrees with the digest serialized in
  its output;
- its coefficient-vector list is exactly the set of all 35 nonnegative
  four-vectors of coordinate sum four;
- the independently observed coverage counts are exactly 1820 and 2380;
- both complete frequency maps agree entry by entry with the decisive JSON,
  and their frequency totals equal the coverage counts;
- every range-checked witness in the decisive JSON was independently
  reevaluated from ordered tuples and has its stated label; and
- both complete label lists and the lexicographically first witnesses agree
  with the earlier tuple-enumeration JSON.

All these checks used exact integers. No floating-point calculation, solver
status, limiting operation, division, or empty-domain convention enters the
argument. Repetitions in `4B` are included, interval endpoints are inclusive,
and the off-by-one convention is handled by enumerating `range(D+1)`.

## Deduction, scope, and verdict

Shin's upper bound gives `R_16(4,4)=R(4,4)`, while the exhaustive equality
gives `R_15(4,4)=R_16(4,4)`. Therefore `R_15(4,4)=R(4,4)` and
`nu(4,4)<=15`. Either Shin's lower bound or the independently checked missing
label at endpoint 14 gives `nu(4,4)>=15`. Hence

\[
\boxed{\nu(4,4)=15}.
\]

The proof settles the frozen original claim at its full stated scope and the
exact certificate is reproducible and independently cross-checked. The cited
sources support the interpretation and finite reduction; they do not already
state this exact instance as resolved. No claim of exhaustive literature
coverage or priority is accepted or needed here. I find no unresolved
mathematical gap in the frozen scope.

**Verdict: accept.**
