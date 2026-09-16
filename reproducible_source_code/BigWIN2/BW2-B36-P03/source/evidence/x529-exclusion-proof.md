# Exact exclusion of 42 columns at \(x=529\)

## Claim

There are no \(d>0\) and \(42\)-element
\(V\subseteq\{2,\ldots,529-d\}\) for which the 84 integers \(v,v+d\)
(\(v\in V\)) are all distinct and pairwise coprime. Consequently
\(L_{42}\geq 530\), so the frozen claim \(L_{42}=529\) is false.

## Reduction

Nonempty \(V\subseteq\{2,\ldots,529-d\}\) forces \(1\leq d\leq527\).
If \(d\) is odd, each column contains one even integer. Two of the 42
distinct even entries would have gcd at least 2, contradicting pairwise
coprimality. Thus only \(d=2,4,\ldots,526\) need be considered.

For an even such \(d\), an admissible start must belong to

\[
C_d=\{v\in\{2,\ldots,529-d\}:\gcd(v,v+d)=1\}.
\]

Join distinct \(v,w\in C_d\) when the four integers
\(v,v+d,w,w+d\) are distinct and all six of their unordered pairs have gcd
1. This is exactly the graph \(G_{529,d}\) defined in `problem.md`. The starts
of any 42-column witness would therefore form a 42-clique in this graph.

## Exact certificate

`x529-coloring-certificate.json` records, for each of the 263 even gaps in
strict order, the complete list \(C_d\) and a color assigned to each vertex.
The certificate uses at most 41 colors in every gap. A proper coloring with
at most 41 colors proves \(\omega(G_{529,d})\leq41\), since all vertices of a
clique require distinct colors.

The dependency-free verifier `verify_x529_coloring.py` does all of the
following with Python integers and `math.gcd`:

1. checks the certificate's canonical payload SHA-256;
2. checks that the gap list is exactly \(2,4,\ldots,526\);
3. recomputes every \(C_d\) from the endpoint and internal-gcd predicates;
4. checks that at most 41 distinct colors occur for every gap; and
5. directly tests every same-color pair, rejecting if its four entries are
   distinct and all six gcds equal 1.

Run from the project directory:

```sh
python3 evidence/verify_x529_coloring.py evidence/x529-coloring-certificate.json
```

The recorded payload SHA-256 is
`891877322b99abeb51b5fe38f883ce73625c8cb6017b69a58193e85188b60673`.
The verification checks all 263 gaps and 147,843 same-color vertex pairs. It
returns `verified: true`. A second implementation in
`x529_coloring_certificate.py` recomputes all 955,648 compatible edges and
also verifies the coloring; its maximum color count is 41, attained only at
\(d=42\).

Therefore no admissible gap has a 42-clique, so no 42-column witness exists
at \(x=529\). Any witness with \(x\leq529\) would also satisfy the endpoint
condition at \(x=529\). Hence \(L_{42}>529\), and integrality gives
\(L_{42}\geq530\).

This proof does not use the inaccessible claimed result \(L_{41}=529\) or any
auxiliary data from that paper.
