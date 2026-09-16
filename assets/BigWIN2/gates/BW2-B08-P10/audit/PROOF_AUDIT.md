# Final independent proof and certificate audit

Audit date: 2026-08-31. Role: independent referee. The audit reconstructed the statement and certificate chain from definitions and did not assume the discovery outcome.

## Verdict

**PASS as a certified finite result.** The retained artifacts prove the following finite theorem:

> Every finite simple connected graph \(G\) with \(|V(G)|=9\) satisfies
> \[
> 2s(L(G))\le c(G)+1,
> \]
> where \(s=n_+-n_-\) is the adjacency signature and \(c=|E|-|V|+1\).

Exactly 261,074 isomorphism classes satisfy the inequality strictly and exactly six attain equality. There are no violations in the order-nine universe.

This is not a proof of the universal conjecture. The universal gap remains open and must not be closed by the census.

No fatal or major mathematical/certification gap remains for the finite theorem. One stale tracking entry and minor hardening points are listed below; none changes the finite result.

## 1. Statement audit

`problem/formal_statement.md` fixes the required domain: finite, undirected, simple, connected root graphs; ordinary unsigned line graphs; eigenvalues counted with algebraic multiplicity; zeros omitted from signature; and order nine meaning \(|V(G)|=9\). It correctly distinguishes the finite theorem from the universal conjecture.

From the unsigned incidence matrix \(B\),
\[
B^{\mathsf T}B=A(L(G))+2I,
\qquad BB^{\mathsf T}=Q(G).
\]
Accounting for the extra zero singular values and shifting by 2 gives, for connected \(G\),
\[
s(L(G))=\operatorname{sig}(Q(G)-2I)-c(G)+1.
\]
This includes the bipartite case: the zero eigenvalue of \(Q\) becomes a negative eigenvalue of \(Q-2I\), while the rectangular incidence correction cancels exactly as displayed. The formula used in both full traversals is therefore correct.

`proof/builder_notes.md` independently derives the equivalent formula
\[
s(L(G))=2a+z-m,
\]
where \(a,z\) count signless-Laplacian eigenvalues above and equal to 2. These two derivations agree. The builder's dense theorem is also correct: from \(s\le2n-m\), the condition \(3m\ge5n-2\) implies the conjectured inequality. At order nine this covers \(m\ge15\). The final computation nevertheless traverses all edge counts \(8\le m\le36\), so the certified result does not depend on the pruning theorem.

Minor presentation issue: several inline formulas in `problem/formal_statement.md` use ordinary parentheses where Markdown math delimiters were apparently intended. The mathematical meaning remains unambiguous.

## 2. Enumeration completeness and graph6 audit

The generation log records

```text
tools/nauty-bin/usr/bin/nauty-geng -cd1D8 n=9 e=8-36
261080 graphs generated
```

For a connected simple graph of order nine, minimum degree at least 1, maximum degree at most 8, and edge count between 8 and 36 are automatic. Thus the options impose no additional restriction beyond connectedness. `geng` emits one representative per isomorphism class. The observed count 261,080 agrees with Brendan McKay's published standard count.

The preserved input `experiments/data/connected_n9_all.g6` has:

- 261,080 records;
- 261,080 distinct raw graph6 strings;
- SHA-256 `fe73f2b8aad1a653b6f3bee799efff369cc486688df5aeade62ce0b3b5889eb5`;
- independently decoded records all having nine vertices, connectedness, and no self-loops;
- edge-layer counts summing to 261,080, over every \(m=8,\ldots,36\).

The breaker copy has the identical full-file digest. The retained Debian packages identify nauty `2.7r3+ds-1` (the executable reports Nauty & Traces 2.7001 when run with its preserved libraries). The exact command and generation log are preserved.

The parser in `experiments/exact_census.py` implements the short graph6 order correctly: bits are read most-significant first and assigned in the sequence \((0,1),(0,2),(1,2),(0,3),\ldots\). All records are in the short \(n=9\) format. A wholly separate NetworkX graph6 decoder is used by the breaker traversal and returns the same universe and conclusions.

Hardening note: the primary and FLINT parsers do not reject surplus non-padding bits or independently test connectedness. This is not a gap for the hashed `geng` output, which was independently decoded and validated, but a reusable verifier should add strict record-length/order/connectivity checks.

## 3. Primary exact inertia computation

`experiments/exact_census.py` constructs the integral matrix \(M=Q-2I\) exactly and applies symmetric congruence elimination over `fractions.Fraction`.

The elimination is valid in both pivot cases:

- a nonzero diagonal pivot contributes its sign and the exact scalar Schur complement;
- if all diagonals vanish but an off-diagonal entry \(d\ne0\) exists, the principal block \(\begin{psmallmatrix}0&d\\d&0\end{psmallmatrix}\) is a hyperbolic plane of inertia \((1,0,1)\), and the implemented two-by-two Schur complement is exact;
- a remaining zero matrix contributes its full dimension to nullity.

Sylvester's law of inertia therefore justifies every returned triple. No floating-point arithmetic or tolerance is used. The correction
\[
\texttt{signature}=(p-q)-c+1
\]
matches the proved incidence formula.

The serialized result reports:

```text
graph_count = 261080
strict      = 261074
equality    = 6
violation   = 0
```

Its edge-layer totals independently sum to the full graph count.

## 4. Independent FLINT characteristic-polynomial/Sturm verifier

`certificates/verify_census_flint.py` does not import the primary evaluator. It independently decodes graph6, reconstructs \(Q-2I\), obtains the exact integer characteristic polynomial using FLINT, square-free factors it, and uses Sturm sequences to count roots on \(( -\infty,0)\) and \((0,\infty)\).

The treatment of multiplicities is correct. Sturm counts distinct roots of each square-free factor, and the code multiplies each count by that factor's square-free multiplicity. A linear factor \(x\) contributes its multiplicity to nullity. Zeros occurring in a Sturm sequence at the endpoint are removed before sign-variation counting, as required. Independent referee tests on repeated positive roots, repeated negative roots, zero roots, and a hyperbolic pair all returned the expected inertia.

The verifier was rerun during this audit over all 261,080 records. It returned

```text
PASS {"graph_count": 261080,
      "totals": {"strict": 261074, "equality": 6},
      "equality": 6}
```

The newly generated JSON was byte-for-byte identical to `certificates/verify_n9_flint.json`. That certificate records Python 3.10.12 and python-flint 0.9.0. It checks the input digest, graph count, totals, and absence of violations.

## 5. Breaker and explicit-line-graph cross-checks

The breaker branch is meaningfully independent in two respects:

1. its full traversal uses NetworkX's graph6 parser and a separately written exact congruence routine; it obtains the same input digest, minimum margin zero, and exactly six minimum-margin graphs;
2. its cross-check constructs \(A(L(G))\) explicitly and uses SymPy exact characteristic polynomials/root isolation, bypassing both the \(Q-2I\) correction and the primary inertia code. It reports `CROSSCHECK_OK 105` on a deterministic stride sample across the full file.

For the six equality graphs, `experiments/breaker/src/verify_equality.py` performs the explicit-line-graph/SymPy route on every candidate. All six pass with line-graph inertia \((5,0,4)\), signature 1, \(m=9\), \(c=1\), and margin zero. The graph6 list exactly matches the six FLINT equality certificates:

```text
H?`@C`w
H?`@E_w
H?`DA`g
H?`DA_w
H?`D@`g
H?bB@_W
```

Since these records arise from the nonisomorphic `geng` census, they are six distinct isomorphism classes. `certificates/breaker_equality_order9.json` retains their edge lists, exact line-graph characteristic polynomials, inertias, signatures, and margins.

The breaker code contains an apparently unusual but correct formula `below + m - n` for the negative line-graph inertia. In the bipartite case, `below` already includes the \(Q=0\) eigenvalue shifted to \(-2\); removing that one and adding the rectangular incidence nullity yields the same net `m-n` correction. It is not a bug.

## 6. Gap classification

### Fatal gaps

- **Finite order-nine theorem:** none open.
- **Universal conjecture:** G01 remains open, correctly; this prevents any universal claim but does not affect the certified finite status.

### Major gaps

- Enumeration completeness (G03): closed by unrestricted connected `geng` generation, the standard count, preserved full input/digest, and independent record validation.
- Definition/source ambiguity (G04): closed by the formal statement and source audit.
- Single-evaluator dependence (G02): scientifically closed by the full FLINT characteristic-polynomial/Sturm rerun and the breaker checks. `proof/gap_ledger.md` still labels G02 “in progress”; this is a stale governance entry and should be changed to `resolved` with `certificates/verify_n9_flint.json` as resolution evidence before release.

### Minor/expository items

- Do not claim absolute historical priority; the literature audit supports only a carefully qualified novelty statement.
- State prominently that the six equality graphs all have \(c=1\), and that the finite theorem does not classify equality at other orders.
- A future generic verifier should enforce strict graph6 record length and graph-domain validation internally, even though the present hashed input was independently validated.

## 7. Release recommendation

The mathematical and computational evidence is sufficient to use the terminal status **Certified finite result** for order nine. It is not sufficient for **Proved** in the universal sense. Before calling a manuscript submission-ready, update the stale G02 ledger status and complete the separate citation, build, PDF visual, archive, and clean-rebuild audits required by the project workflow.
