# Research pass 2 audit

Date: 2026-09-06  
Job: `win-00036-p02-research-f94efdc38a91`

## Exact certificate rerun

All computations below were rerun in this pass from the project root.

`python3 evidence/verify_witness.py` checked the stated 16-element set, all
560 of its unordered triples, and returned `passed: true` with an empty
`bad_triples` list.

`python3 evidence/audit_encoding.py` regenerated the forbidden triples and
PySAT totalizer clauses and compared the resulting clause list byte-for-byte
with `evidence/k17.cnf`. It returned:

```
ENCODING VERIFIED
forbidden_triples=119176 totalizer_clauses=8890
variables=1015 clauses=128066 sha256=8b79ee1c4a921f27dfdb7d4c6d9581ff98860b85d1caf903b5a500de6763a8c2
```

`evidence/drat-trim evidence/k17.cnf evidence/k17.drat` exited 0 and returned:

```
c parsing input formula with 1015 variables and 128066 clauses
c finished parsing
c detected empty clause; start verification via backward checking
c 114515 of 128066 clauses in core
c 1794649 of 2273067 lemmas in core using 98745797 resolution steps
c 0 RAT lemmas in core; 1028875 redundant literals in core lemmas
s VERIFIED
c verification time: 106.738 seconds
```

The rerun therefore reproduces both exact bounds in `evidence/computation.md`.
It is researcher evidence, not the required fresh-referee audit.

## DOI comparison attempt

The requested full text of DOI `10.2139/ssrn.7395458` was not obtained.
Exact DOI, exact title, SSRN-ID, author/title, ResearchGate, Qeios, GitHub, and
Zenodo web searches returned no inspectable primary copy. The SSRN landing page
returned HTTP 403 to the available web reader, and command-line retrieval could
not connect. A filesystem search found only the supplied bibliography records
and existing project/job mentions, not a paper PDF or source.

The supplied workbook-derived record in `literature/user-library-record.md`
does give an abstract that defines `f3(N)` as the maximum size of a subset of
`[N]` with no three distinct elements whose pairwise GCDs are equal, and says
the paper proves `f3(126)=16` by an explicit lower bound and a Boolean/DRAT
upper bound. This abstract-level definition agrees with `problem.md`. It says
the result concerns only the stated finite value and does not mention N=127.
However, that record explicitly warns that it is a routing lead rather than a
substitute for the full paper. Consequently the paper's formal definition,
theorems, tables, and computational data at N=127 remain unverified, and no
novelty claim is made.

SHA-256 of immutable `source.md` after the pass:
`58d9e80ab37de5373fdc8ddb72d7b87485b54da47ae99ce8f1d54e16b229e332`.
