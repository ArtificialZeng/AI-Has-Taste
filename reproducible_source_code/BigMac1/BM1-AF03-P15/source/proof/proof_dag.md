# Proof dependency graph

## Certified finite endpoint

**T-D9.** The absolute order \(\operatorname{Abs}(D_9)\) admits a normalized
flow with unit vertex weights.

### Dependencies

1. **L1 (automorphism action).** \(D_n\triangleleft B_n\), and conjugation by
   \(B_n\) preserves the \(D_n\)-reflection set.  Hence \(B_n\) acts by
   rank- and cover-preserving automorphisms of \(\operatorname{Abs}(D_n)\).
   Proof: `notes/builder.md`, Section 3.
2. **L2 (orbit classification and mass).** The \(B_n\)-orbits in \(D_n\) are
   the signed cycle bipartitions \((\lambda,\mu)\) with
   \(|\lambda|+|\mu|=n\) and \(\ell(\mu)\) even, of size
   \[
   c(\lambda,\mu)=
   \frac{2^n n!}{2^{\ell(\lambda)+\ell(\mu)}z_\lambda z_\mu}.
   \]
   Proof and small-rank exhaustive audit: `notes/builder.md`, Sections 4--5;
   `discovery/bruteforce_transition_check.py`.
3. **L3 (rank formula).** The rank of \((\lambda,\mu)\) is
   \(n-\ell(\lambda)\).  This uses Carter's reflection-length/codimension
   identity and the fixed-space dimension of a signed cycle.  Primary
   location: Carter, *Compositio Math.* 25 (1972), Lemma 2, journal p. 3;
   local source `literature/sources/carter-1972.pdf`.  Derivation for signed
   cycles: `notes/builder.md`, Section 4.
4. **L4 (cover classification and multiplicity).** Every upward quotient
   cover, and only such a cover, is one of
   \(P+P\to P\), \(P+N\to N\), or \(P\to N+N\).  The exact source degrees
   are formula (5.1) in `notes/builder.md`.  Direct element-level audits for
   \(D_4,D_5\), and a separate formula-versus-reflection check for all 150
   \(D_9\) orbit types, agree.
5. **L5 (quotient LP equivalence).** For each adjacent rank pair, variables
   \(F(A,B)\ge0\) on allowed orbit pairs must have row marginal
   \(c(A)/N_r\) and column marginal \(c(B)/N_{r+1}\).  This system is
   equivalent to a unit-weight normalized flow on the full poset: each
   orbit-pair cover graph is biregular, and \(F(A,B)\) lifts by assigning
   \(F(A,B)/(c(A)d^+_{A,B})\) to each individual cover.  Location:
   `notes/builder.md`, Sections 3 and 6.
6. **L6 (exact finite construction).** Clearing denominators with
   \(L_r=\operatorname{lcm}(N_r,N_{r+1})\) turns each transportation system
   into an integral max-flow problem.  Two independently written constructors
   serialize the same 284 positive rational totals in
   `certificates/d9_normalized_flow.json` and
   `discovery/d9_orbit_flow_candidate.json`; their semantic identity is a
   regression assertion in `tests/test_breaker_crosscheck.py`.
7. **L7 (independent certification).** Two no-discovery-import verifiers,
   `certificates/verify_d9_flow.py` and
   `tests/verify_breaker_orbit_candidate.py`, rebuild all types, masses,
   ranks, support, source/target degrees, and full orbit-pair edge counts.
   They check all rational marginals, the cleared integer equations, and the
   uniform \(F/E\) lift.  The latter additionally checks the global count
   3,344,302,080 of full Hasse covers.  The release certificate has 150
   orbits, 609 allowed orbit pairs, and 284 positive flows.  Independent
   element-level audits for \(D_4,D_5,D_6\) agree cell-by-cell, including
   even-rank split \(D_n\)-classes.  Both mutation suites fail closed.

### Implication graph

\[
\begin{array}{c}
\text{L1}+\text{L2}+\text{L3}+\text{L4}
   \Longrightarrow \text{finite exact quotient systems (L5)},\\[2mm]
\text{L6}+\text{L7}
   \Longrightarrow \text{all D9 quotient systems feasible},\\[2mm]
\text{L1}+\text{L5}+\text{quotient feasibility}
   \Longrightarrow \text{T-D9}.
\end{array}
\]

No proof assistant was used.  The exact endpoint is bound to serialized
certificate and verifier hashes in `notes/builder.md`, Section 10, and
`certificates/README.md`.

## Non-endpoint route

The same quotient construction is uniform in \(n\), but the release scope is
exactly \(D_9\).  No weighted-Hall proof or compatible closed flow formula has
been obtained for arbitrary \(n\).  Therefore the DAG does not contain an
implication to the full all-\(n\) conjecture, and no \(n>9\) output is retained.
