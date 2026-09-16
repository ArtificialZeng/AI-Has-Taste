# Fresh mathematical referee report

## Frozen scope and provenance

- Referee job: `win-00060-p01-referee-b9ca0483e07d`.
- Snapshot digest: `e1518167a1264b647369a4be6351f8a3b26f3b414a4e299557277ef664579ee9`.
- Frozen candidate: `resolution-paper`; frozen original status: `proved`.
- Claim reviewed: the explicit 98-clause monotone NAE-4 equality gadget and its occurrence-by-occurrence composition resolve all five assertions in the frozen target.

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the permitted decisive evidence, excluding `checkpoint.md` as required. SHA-256 recomputation matched the snapshot entries for `source.md`, `problem.md`, `claim.json`, `evidence/gadget-proof.md`, `evidence/gadget_certificate.py`, `evidence/gadget_certificate.out`, and `evidence/external/2609.03508.pdf`.

## Reconstructed decisive argument

Let the 40 gadget vertices be the points of \(\mathrm{PG}(3,3)\). Its projective lines have four points, and two distinct lines have at most one common point. The evidence specifies a 99-line subhypergraph \(K\), whose first line is \(L=\{0,1,2,3\}\), and takes \(G=K\setminus\{L\}\).

The exact certificate establishes two facts:

1. \(K\) is not NAE-two-colourable.
2. \(G\) has a colouring in which all four vertices of \(L\) are zero; complementation supplies the all-one colouring.

If a colouring of \(G\) induced any nonmonochromatic pattern on \(L\), then it would also satisfy the deleted NAE edge \(L\), contradicting the non-colourability of \(K\). Hence the terminal projection of \(G\) is exactly
\[
\{0000,1111\}.
\]
Identifying terminals 0 and 1 with an original variable \(x\) and its fresh occurrence copy \(y\), while keeping terminals 2 and 3 auxiliary, therefore enforces exactly \(x=y\). Every gadget edge is a four-element unnegated NAE clause, and projective-line incidence proves internal linearity.

For every indexed occurrence, use a unique \(y\) in the copied input clause and attach a fresh copy of \(G\), sharing only terminal 0 with the original \(x\). Copied input clauses are pairwise disjoint. Gadget copies for different original variables are disjoint; copies for the same original variable share only that variable. An input-copy clause and a gadget clause share at most the unique occurrence variable belonging to that gadget. These cases exhaust all clause pairs, so the transformed formula is linear.

Given an original satisfying assignment, choose the zero-terminal witness or its complement independently in each gadget. The copied clauses then have the original truth values. Conversely, every transformed satisfying assignment has each occurrence copy equal to its original variable, so every copied clause implies the corresponding original clause. This proves equality of projected satisfying-assignment sets, including both required directions.

Each gadget copy has 40 projective vertices, one identified with an existing original variable, so it introduces 39 fresh variables, including the occurrence copy, and 98 gadget clauses. Four occurrences per input clause give \(n+156m\) variables; retaining one copied clause per indexed input clause gives \(m+392m=393m\) clauses. Fixed lookup data makes the construction linear-time. Thus \(B=98\) bounds both fresh variables and gadget clauses per occurrence.

## Checks actually performed

- Re-ran `evidence/gadget_certificate.py`; it reproduced `CERTIFICATE_OK`, core UNSAT, the complete 16-row terminal projection, projective linearity, and the overlap-2, overlap-3, and overlap-4 composition checks.
- Independently regenerated the 40 normalized projective points by direct normal-form enumeration and the 130 lines from two-dimensional spans, rather than importing the candidate generator.
- Independently encoded each NAE edge as the two CNF clauses forbidding all-zero and all-one assignments and used the installed Z3 SAT backend. It returned UNSAT for the 99-edge core, SAT for terminal patterns `0000` and `1111` in the deletion gadget, and UNSAT for all other 14 patterns. It also produced a zero-terminal witness different from the displayed candidate witness.
- Independently checked that the maximum intersection of distinct generated projective lines is one.
- Checked the global clause-pair cases symbolically and recomputed the variable and clause counts.

The candidate DPLL is complete: its only propagation assigns the fourth vertex opposite three already equal assigned vertices; conflicts reject monochromatic completed clauses; otherwise it branches both values of an unresolved vertex. The independent CNF check removes reliance on that implementation.

## Source comparison and scope

The listed source PDF's Lemma 1 states the linear NAE-4-SAT hardness step using fresh copies and unspecified intermediate NAE equality clauses, but it gives neither an arity-four gadget nor a local projection certificate. Section 3.2 then needs linearity so that its \(K_6\) clause subgraphs are edge-disjoint. The reviewed construction supplies exactly this omitted monotone four-uniform linearization step under the frozen interpretation. The candidate makes no priority or publication-novelty claim, so the absence of an independently audited broader literature claim is not being used as mathematical evidence here.

I found no unresolved mathematical gap in the frozen candidate scope. This report does not audit the later \(K_6\) calculation except to confirm the source's stated dependence on a linear input instance, and acceptance of this candidate does not certify unrelated claims in the paper.

## Verdict

**Accept.** The frozen construction is explicit, its equality projection is exact, its projective incidence and global composition establish linearity, both assignment directions hold, and the stated local and global complexity bounds are correct. It proves the frozen original claim without weakening its scope.
