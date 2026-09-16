# Exact computation for f3(127)

Date: 2026-09-06. All integer and GCD operations are exact.

## Encoding

`search_127.py` introduces one Boolean variable `x_i` for each integer
`i` in `[127]`. For every unordered triple `a<b<c` satisfying

`gcd(a,b) = gcd(a,c) = gcd(b,c)`, 

it adds the clause `(-x_a OR -x_b OR -x_c)`. The script enumerates all
`C(127,3)` triples and finds 119,176 forbidden triples, so these clauses are
definitionally equivalent to feasibility. PySAT's totalizer encoding adds the
constraint `sum_i x_i >= k`. For `k=17`, the resulting DIMACS file has 1,015
variables and 128,066 clauses (119,176 GCD clauses and 8,890 totalizer clauses).

## Lower bound

The explicit set

`{14,20,21,24,25,30,36,40,48,63,80,90,96,98,108,125}`

has size 16. `verify_witness.py` checks its 560 unordered triples directly
from the problem definition and finds no forbidden triple. This proves
`f3(127) >= 16` without using the cited paper.

## Upper bound and certificate

CaDiCaL 1.9.5, called through PySAT 1.8.dev24, returned UNSAT for the `k=17`
DIMACS instance and emitted `k17.drat`. The trace has 4,570,751 lines.
The standard `drat-trim` checker independently checked the DIMACS file and
trace, exiting 0 and reporting:

```
c parsing input formula with 1015 variables and 128066 clauses
c finished parsing
c detected empty clause; start verification via backward checking
c 114515 of 128066 clauses in core
c 1794649 of 2273067 lemmas in core using 98745797 resolution steps
c 0 RAT lemmas in core; 1028875 redundant literals in core lemmas
s VERIFIED
c verification time: 125.467 seconds
```

Thus the exact CNF has no assignment selecting at least 17 feasible integers,
which proves `f3(127) <= 16`. Combined with the witness, this gives
`f3(127)=16`.

## Reproduction

```
python3 evidence/verify_witness.py
python3 evidence/search_127.py --n 127 --k 16
python3 evidence/search_127.py --n 127 --k 17 --proof \
  --proof-file evidence/k17.drat --cnf-file evidence/k17.cnf
evidence/drat-trim evidence/k17.cnf evidence/k17.drat
```

SHA-256:

```
0cb13fa6ae1150ac812631deea5473272f16606e258f9a4ffb685c57d300ccc1  evidence/search_127.py
8b79ee1c4a921f27dfdb7d4c6d9581ff98860b85d1caf903b5a500de6763a8c2  evidence/k17.cnf
57ae38a8f6ff606ef716bdaa488cf2d93a74c35ec9e16b9437aaac587ba69718  evidence/k17.drat
58d9e80ab37de5373fdc8ddb72d7b87485b54da47ae99ce8f1d54e16b229e332  source.md
```

## Literature-access limitation

Exact-title, DOI, SSRN-ID, and author/title searches did not expose the full
text of DOI `10.2139/ssrn.7395458`; direct command-line network retrieval was
also unavailable. Therefore this pass does not assert novelty or claim what
that inaccessible paper says beyond the frozen source's supplied lead. The
direct lower and upper bounds above do not depend on that paper.
