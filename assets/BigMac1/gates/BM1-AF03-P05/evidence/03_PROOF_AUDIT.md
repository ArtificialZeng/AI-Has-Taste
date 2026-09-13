# Proof audit

Date: 2026-08-29 (Asia/Shanghai)  
Endpoint: for every nine-vertex simple graph \(G\) with
\(e(\overline G)\le6\), \(q(G)=2\)  
Disposition: **PASS -- no open fatal or major issue**

## Exact proof chain

1. Permutation similarity makes \(q(G)\) invariant under graph relabeling.
2. A two-eigenvalue symmetric realization is affinely equivalent to a
   symmetric involution with the same off-diagonal support.
3. The verifier reconstructs every complement from a unique multiset of
   connected graph-atlas types.  A nontrivial connected component with at
   most six edges has at most seven vertices.
4. A separate Burnside calculation by edge stratum agrees with that
   reconstruction.  The exact totals are 19, 44, and 108 for orders 7, 8,
   and 9.
5. The disjoint priority routing is
   \(19=16+2+1\), \(44=33+10+1\), and
   \(108=72+24+12\) for BIP/JOIN/FRAME.
6. BIP and JOIN bind exactly to Barrett et al., Theorem 3.7, and
   Levene--Oblak--Šmigoc, Theorem 3.4 with \(k=1\).
7. For all 14 FRAME residuals, exact positive rational weights and rational
   directions satisfy the zero-pattern and Parseval identities.  Hence
   \(Q=I-2VV^{\mathsf T}\) is a symmetric involution in \(S(G)\).

## Executable checks

The independent verifier printed `status: VERIFIED`, certificate digest
`d78b49e23aeaebba29d0ab70661df9688a09baabce7e0333040b43186a808fd5d`,
verifier digest
`5b298d8cac3eb4a890308475aa0f93f2dd0565e76d6150902b7737e3f2b49613`,
14 frame witnesses, and `proof_assistant: none`.

The maintained mutation suite accepted the valid certificate and rejected all
18 damaged variants.  It covers arithmetic damage, missing witnesses, wrong
counts, duplicate/unknown keys, NaN, null and scalar-type confusions,
noncanonical rationals/decimals, and alternate or padded graph6 encodings.

## Independent referee

The independent referee did not import `discovery/`.  The referee separately:

- rebuilt the atlas component multiset and Burnside counts;
- reran fresh nauty totals and an independent bit-graph route classifier;
- matched the residual witness set by canonical labeling;
- recomputed all 14 frames with a second SymPy `Rational` implementation;
- attacked parser canonicality and type handling, finding two major issue
  families that were repaired before the final rerun;
- rejected the 18 maintained mutations plus 10 former bypass strings.

The signed-off report is `audit/agent_referee_report.md`.  It records no open
fatal or major issue and supports `CERTIFIED_FINITE_RESULT`.

## Trust boundary and limitations

The result depends on two source-verified published theorems, elementary
linear algebra/graph decomposition, Python exact rational arithmetic, the
graph-atlas catalogue, and the independently checked finite enumeration.
Floating-point discovery data are not read by the verifier.  This proves only
the finite \(n=9\) endpoint (while reconstructing \(n=7,8\)); it does not prove
the conjecture for \(n\ge10\).

No Lean, Coq, Isabelle, or other proof assistant was used.
