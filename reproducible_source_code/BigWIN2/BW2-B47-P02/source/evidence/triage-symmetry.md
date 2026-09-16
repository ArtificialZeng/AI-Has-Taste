# Exact slope-scaling test

Provenance: `win-00047-p02-triage-e96d6e840dbf` (triage observation, not an
independent referee decision).

For \(a,b\in\mathbb F_7^*\), put \(u=b/a\). Multiplication by \(u\) maps
\(S_a=\mathbb F_7^*\setminus\{a\}\) bijectively to
\(S_b=\mathbb F_7^*\setminus\{b\}\). Consider

\[
  \phi_u:\Omega_a\longrightarrow\Omega_b,\qquad
  (\alpha,r,x)\longmapsto(u\alpha,u^{-1}r,x).
\]

This is a bijection. For \(\alpha\ne\beta\), the common symbol of rows
\(r,s\) is

\[
  K_{\alpha\beta}(r,s)
  =\frac{\alpha\beta(r-s)}{\beta-\alpha}.
\]

Therefore

\[
 K_{u\alpha,u\beta}(u^{-1}r,u^{-1}s)
 =\frac{u^2\alpha\beta\,u^{-1}(r-s)}{u(\beta-\alpha)}
 =K_{\alpha\beta}(r,s).
\]

Thus \(\phi_u\) leaves the Hadamard outer-product block used by the \(A_2\)
relation unchanged. It also preserves equality/inequality of slopes and of
row labels, hence preserves the \(A_4\) relation. Consequently it preserves
every adjacency under the explicit reading in `problem.md`.

If this calculation passes an independent research reconstruction and fresh
referee audit, it yields one isomorphism class, with \(G_1\) as the designated
representative and the six pairwise maps above as symbolic certificates. It
has not yet been independently checked against generated 280-vertex adjacency
lists.
