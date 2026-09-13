# Checkpoint

Provenance: `bigMac-00004-p01-research-3ba5da36b35c`  
Phase: research, pass 3  
Decision: **candidate (`result-note`)**; the original six-point claim remains
**unresolved/status-uncertain**.

## Durable evidence

- `source.md` remains unchanged with SHA-256
  `2183039719540ca0e5653a79785209d40ef2cb70d28ab6807a23d0790736b527`.
  `problem.md` freezes the interpretation and finite extreme-ray reduction.
- `evidence/typeII_s4_exact_bound.md` proves that for the normalized type-II
  ray associated with \(h=(-2,-1,1,1,1,1)\), the supremum on the full
  \(S_4\)-invariant matrix family is exactly
  \(8/(3\sqrt3)<2\). This is a sharp restricted-family theorem, not a
  full-domain bound.
- `evidence/typeII_geometric_symmetrization_obstruction.md` gives an exact
  family \(P_r\) with inertia \((1,1,4)\) whose orbit-geometric average has
  inertia \((2,4,0)\). At \(r=8\), all input entries are integers and the
  averaged eigenvalues are explicit. Thus the averaging step that would
  reduce the full problem to the symmetric family is false, while the
  type-II monomial is preserved and equals 1.
- **New exact proof-class obstruction.** Define
  \[
  \Lambda(x)=3x_{12}+\sum_{k=3}^6x_{1k}
  +2\sum_{k=3}^6x_{2k}
  +2\sum_{3\le i<j\le6}x_{ij}.
  \]
  `evidence/typeII_product_proof_class_dual.md` exhausts all 60 triangular
  and 60 pentagonal lifts and proves
  \(\Lambda(q_T)\le0\), \(\Lambda(q_P/2)\le0\), and
  \(\Lambda(-e_{ij})<0\), whereas
  \(\Lambda(q(h)/4)=1/2>0\) for the type-II target. Therefore the direct
  type-II inequality cannot be obtained from any nonnegative product of the
  sharp lifted triangular/pentagonal inequalities and \(p_{ij}\ge1\), even
  if the stipulated total normalized weight cap of one is removed.
  `evidence/check_typeII_product_dual.py` verifies the exhaustive finite
  check over integers: the triangular values are
  \(-4\ (4),-2\ (46),0\ (10)\), and the pentagonal values are
  \(-6\ (12),-4\ (28),-2\ (16),0\ (4)\).

## Remaining gap

None of these results bounds an arbitrary nonsymmetric type-II matrix, and
the new type-I ray has not been treated. Hence they neither prove nor
disprove the frozen claim and do not classify its equality extreme rays.
The dual certificate is an obstruction only to the precisely stated product
proof class.

## One next test

Send the exact three-part subsidiary statement frozen in `claim.json` to a
fresh referee. The referee should independently recompute the 120 values of
\(\Lambda\), then audit the inertia and sharp-supremum arguments in the two
earlier evidence files; any failure revises the candidate rather than changing
the unresolved status of the original problem.
