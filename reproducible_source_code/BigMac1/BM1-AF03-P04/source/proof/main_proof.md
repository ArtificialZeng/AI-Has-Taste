# Componentwise proof of the transitive-array conjecture

## Theorem

Let \(n\geq1\), let \(\mathfrak g\) be a Lie algebra over a field, and let
\(\{r^{(c)}\}_{c\in C}\subset\mathfrak g\otimes\mathfrak g\) satisfy
\[
 T(c,c',c'')=[r^{(c)}_{12},r^{(c')}_{13}]
 +[r^{(c)}_{12},r^{(c'')}_{23}]
 +[r^{(c')}_{13},r^{(c'')}_{23}]=0
\]
whenever \(c'\in\{c,c''\}\).  If
\(a=(a_{ij})\in C^{n\times n}\) satisfies
\(a_{ik}\in\{a_{ij},a_{jk}\}\) for all \(i,j,k\), then
\[
 R=\mathbf r^{(a)}=\sum_{i,j=1}^n
 (r^{(a_{ij})})^{j,i}\in
 \mathfrak g^{\oplus n}\otimes\mathfrak g^{\oplus n}
\]
satisfies the ordinary CYBE.  In particular, the assertion holds for
\(n=5\).

## Proof

Set \(\mathfrak h=\mathfrak g^{\oplus n}\).  Let
\(\iota_p:\mathfrak g\to\mathfrak h\) be the inclusion into the \(p\)-th
summand and use the same symbol for the induced map
\(U(\mathfrak g)\to U(\mathfrak h)\).  For \(p,q,s\in[n]\), write
\[
 \Phi_{p,q,s}=\iota_p\otimes\iota_q\otimes\iota_s:
 U(\mathfrak g)^{\otimes3}\longrightarrow U(\mathfrak h)^{\otimes3}.
\]
Elements supported in different direct summands commute:
\[
 [\iota_p(x),\iota_q(y)]=
 \begin{cases}
 \iota_p([x,y]),&p=q,\\
 0,&p\ne q.
 \end{cases}
\]
Expand the three commutators in \(\operatorname{CYB}_{\mathfrak h}(R)\).
Only pairs whose supports agree in the commutator tensor factor survive.
Consequently,
\[
 [R_{12},R_{13}]
 =\sum_{j,i,k=1}^n
 \Phi_{j,i,k}
 \bigl([r^{(a_{ij})}_{12},r^{(a_{kj})}_{13}]\bigr),
\]
\[
 [R_{12},R_{23}]
 =\sum_{j,i,k=1}^n
 \Phi_{j,i,k}
 \bigl([r^{(a_{ij})}_{12},r^{(a_{ki})}_{23}]\bigr),
\]
and
\[
 [R_{13},R_{23}]
 =\sum_{j,i,k=1}^n
 \Phi_{j,i,k}
 \bigl([r^{(a_{kj})}_{13},r^{(a_{ki})}_{23}]\bigr).
\]
Adding gives the exact component identity
\[
 \operatorname{CYB}_{\mathfrak h}(R)
 =\sum_{j,i,k=1}^n
 \Phi_{j,i,k}
 \bigl(T(a_{ij},a_{kj},a_{ki})\bigr).                 \tag{*}
\]
Apply transitivity to the ordered triple \((k,i,j)\):
\[
 a_{kj}\in\{a_{ki},a_{ij}\}.
\]
Thus every term on the right side of (*) is one of the assumed
transitive-CYBE relations and is zero.  Therefore
\(\operatorname{CYB}_{\mathfrak h}(R)=0\).

The argument permits \(j=i\), \(i=k\), \(j=k\), or \(i=j=k\): the three
copies of \(U(\mathfrak h)\) in its tensor cube remain separate, and each
\(\Phi_{j,i,k}\) is defined with repeated labels.  No linear independence of
the images of the \(\Phi_{j,i,k}\) is used; every preimage in (*) vanishes
before it is embedded.  This also covers constant arrays, repeated colors,
and zero tensors.  \(\square\)

## Exact identity certificate for n=5

The serialized certificate enumerates all 4,573 transitive equality types
modulo color relabeling.  The independent verifier checks 571,625 instances
of the local label condition in (*).  This finite certificate is not needed
for the all-\(n\) proof, but it reproduces the source's \(n\leq4\) baseline
and gives an exact machine check of the requested \(n=5\) endpoint.
