# Fresh mathematical referee report

Job: `win-00084-p06-referee-bd41c29f92c9`  
Snapshot: `31f0a32cb1b348eddb876fb4af69904e60cc68ad82dfd11fa263b648b326fd04`  
Candidate: `resolution-paper`  
Verdict: **accept**

## Frozen scope and source comparison

I reviewed the exact claim that no rank-six matrix in
\(\mathbb F_3^{6\times 11}\) has four pairwise-disjoint recovery sets for
every column. I recomputed every hash in `audit/snapshot.json`; all fourteen
bindings, including `claim.json`, the source PDF, encoder, CNF, DRUP trace,
replayer, and validation report, match the frozen snapshot.

I inspected the cited primary-source statements themselves. Definitions 1--2
give the recovery-set and all-symbol notions, and Lemma 3 justifies invertible
left multiplication. For odd \(q\), Theorem 23 specializes at \(k=6,q=3\)
to
\[
11\leq \operatorname{ASP}(6,4,3)\leq
\operatorname{ASB}(6,4,3)\leq 12,
\]
since \(\lceil(1+\sqrt{49})/2\rceil=4\). The discussion following Remark 25
reports exhaustive nonexistence only for the binary cell
\(\operatorname{ASP}(6,4,2)>11\), not the ternary cell. Thus the asserted
nonexistence settles the full frozen alternative and implies
\(\operatorname{ASP}(6,4,3)=12\).

The bounded literature dossier reports no later primary resolution in its
specified searches. That is an honest search limit, not a priority proof. The
candidate makes no unconditional priority claim. Its precise delta from the
nearest checked result is the closure of the source's ternary one-unit interval,
which is a substantive and usable contribution.

## Reconstruction of the reduction

Assume a putative length-eleven matrix \(G\) exists.

1. A zero column can be deleted without lowering rank. Removing that coordinate
   from the recovery sets of every remaining target preserves spans and
   disjointness (and zero targets remain recoverable). This would produce a
   length-ten rank-six four-all-symbol PIR matrix, contradicting the checked
   lower bound eleven. Hence every column is nonzero.
2. Select six basis columns, permute them first, and left-multiply by the inverse
   basis matrix. This preserves every recovery equation and gives
   \(G=(I_6\mid A)\). Each of the five nonzero columns of \(A\) may then be
   independently scaled by a nonzero field element, with recovery coefficients
   rescaled inversely, so its first nonzero entry can be normalized to one.
   There is no division by zero in this step.
3. For any nonzero target \(g_i\), four disjoint recoveries exist exactly when
   there are three disjoint recoveries avoiding \(i\), together with
   \(\{i\}\). From four sets, at most one contains \(i\); replace it by the
   singleton, or, if none contains \(i\), discard one and add the singleton.
   The converse is immediate.
4. Apply this to the systematic target \(e_1\). Each of its three avoiding
   recovery equations must use a parity column whose first coordinate is
   nonzero, because the other five systematic columns contribute zero in that
   coordinate. Disjoint coefficient supports force three distinct such parity
   columns. Projective normalization makes their first entries one. A parity
   column permutation can therefore put three of them first and all remaining
   first-row-one columns before the first-row-zero columns.

These operations cover every putative matrix and justify exactly the matrix
normalizations imposed by the CNF; no unproved row, column, or projective
symmetry is used.

## Reconstruction of the CNF equivalence

The encoder represents every field value by an exact-one triple. Its nonzero
and leading-entry clauses give precisely the five normalized nonzero parity
columns. The three first-row unit clauses and adjacent ordering clauses impose
only the convention established above.

For each of eleven targets and each of three nontrivial recoveries, coefficient
trits are fixed to zero at the target. Pairwise binary clauses prohibit two
recoveries for the same target from using the same coordinate. An exact-one
minimum choice forces every support to be nonempty, identifies its least used
coordinate, and strictly orders the three minima; this removes only the
permutation symmetry among three disjoint nonempty supports.

For every target, recovery, and row, the arithmetic circuit enforces
\[
c_r+\sum_{p=0}^4 c_{6+p}a_{r,p}=(g_t)_r\pmod 3,
\]
with the target's systematic coefficient omitted when it is already fixed to
zero. For a parity target the right side is the corresponding entry of \(A\).
Each multiplication and addition implication covers all nine input pairs; exact
one-hot inputs and outputs therefore make these gates functional, not merely a
relaxation.

Consequently, a model decodes to \((I_6\mid A)\), three disjoint
target-avoiding coefficient supports for every nonzero target, and hence four
recovery sets after adjoining the singleton. Conversely, from a normalized
putative matrix, choose coefficient representations inside the three avoiding
recovery sets, delete zero-coefficient coordinates, order the resulting
nonempty supports by their distinct minima, and set each gate to its actual
\(\mathbb F_3\) value. This satisfies every clause. Thus the frozen CNF is
satisfiable if and only if the forbidden matrix exists.

## Checks actually performed

- I regenerated the complete encoding in memory from the frozen encoder. It has
  7,428 variables and 34,731 clauses. The generated clause list equals the
  parsed frozen CNF exactly, and its DIMACS rendering with the terminal newline
  is byte-identical, with SHA-256
  `a0b8624f0f8b19b8f114b266f87cb72879add9ec60ed3fd555f9cfd549e821be`.
  All literals are within the declared range and the input has no empty clause.
- I reviewed the separate projective-kernel oracle. For
  \((I_6\mid A)\), all kernel directions are uniquely parameterized by
  \((-Ax,x)\) with \(x\in\mathbb F_3^5\); a direction nonzero at the target
  gives exactly a target-avoiding recovery support. Its exact disjoint-packing
  dynamic program and the frozen targetwise SAT encodings agree on all 550
  recorded checks across 25 normalized matrices, eleven targets, and two SAT
  backends, with both positive and negative target instances. This is a useful
  semantic test, not the nonexistence proof.
- I audited the DRUP replayer. For each addition \(C\), it requires unit
  propagation to conflict under all assumptions \(\neg C\) before retaining
  \(C\). Ignoring deletion lines is sound here: inductively every retained
  clause is entailed by the input, so keeping an otherwise deleted entailed
  clause does not change the model set. An accepted empty clause therefore
  proves the input CNF inconsistent.
- I ran a fresh full replay under this referee job ID with Minisat22 used only
  as the propagation engine. It independently checked 426,775 RUP additions,
  retained 406,667 deletions implicitly, and accepted the empty clause at proof
  line 833,442. The replay bound the same CNF hash above and proof SHA-256
  `4c97d3c4b46ddbbe6f286a151b91a2ff8f16fb7452054685ac806160e57a84a3`.
  It exited successfully after 96.425701 seconds.
- I also attempted a redundant replay with the CaDiCaL 1.9.5 propagation
  backend. It had not terminated after six minutes and I stopped that attempt
  to respect the bounded review. It supplied no evidence either way and is not
  used in this verdict.

## Gap assessment and verdict

I found no quantifier, degeneracy, symmetry, encoding, certificate, or source
scope gap in the frozen claim. The only limitation is the explicitly bounded
literature search, which bars an unconditional priority assertion but does not
weaken the proved finite nonexistence result or the claimed source delta.

**Verdict: accept.** The exact frozen `resolution-paper` scope is correct: no
rank-six \(6\times11\) ternary four-all-symbol PIR matrix exists, and the cited
upper bound then gives \(\operatorname{ASP}(6,4,3)=12\).
