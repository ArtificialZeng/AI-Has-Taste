# Exact certificate

`n9_exact_frames.json` is the decisive serialized exact input for the finite
result.  It contains no decimal used by the proof.  For each graph not routed
through one of the two source-verified published theorems, it stores rational
vectors \(w_i\in\mathbb Q^3\) and positive rational weights \(x_i\) satisfying

\[
  \langle w_i,w_j\rangle=0
  \iff ij\in E(H),\qquad
  \sum_i x_iw_iw_i^\top=I_3.
\]

Put the \(i\)-th row of \(V\) equal to \(\sqrt{x_i}w_i^\top\).  The two
displayed identities imply \(V^\top V=I_3\), so \(P=VV^\top\) is a rank-three
orthogonal projection.  Then \(Q=I-2P\) is a real symmetric involution and,
off the diagonal, \(Q_{ij}=0\) exactly on the edges of \(H=\overline G\).
Thus \(Q\in S(G)\) and has the two eigenvalues \(+1,-1\).

The verifier does not import or execute the discovery generator.  It:

1. parses every rational in reduced canonical form and rejects unknown or
   missing schema fields;
2. recomputes all support and Parseval identities with `fractions.Fraction`;
3. rebuilds all sparse graph types from multisets of connected graph-atlas
   representatives;
4. independently checks enumeration counts by a Burnside calculation over
   conjugacy classes of symmetric groups;
5. checks the bipartite and balanced-connected-join routing predicates; and
6. prints hashes of both the exact input and the verifier.

Run from the project root:

```bash
python verification/verify_n9_certificate.py certificates/n9_exact_frames.json
python verification/test_fail_closed.py
```

The discovery provenance is retained in `discovery/`; its floating-point
fields locate rational reconstructions and make no logical contribution to
the verifier.
