# Certified finite result

## Theorem

Let \(G\) be the undirected simple graph whose vertices are the 80
isomorphism classes of Steiner triple systems of order 15, with two distinct
classes adjacent exactly when a single Pasch switch transforms a
representative of one into a representative of the other.  Then:

1. \(G\) has 258 edges;
2. its connected components have orders 79 and 1;
3. the isolated vertex is the unique anti-Pasch class;
4. the diameter of the 79-vertex component is
   \[
   \boxed{11};
   \]
5. the isolated component has diameter 0.

In the released canonical numbering, exactly two unordered pairs are at
distance 11:

\[
 \{\mathrm{V000},\mathrm{V006}\},\qquad
 \{\mathrm{V000},\mathrm{V028}\}.
\]

One certified geodesic is

\[
\begin{aligned}
\mathrm{V000}&-\mathrm{V047}-\mathrm{V002}-\mathrm{V027}
-\mathrm{V054}-\mathrm{V018}-\mathrm{V035}-\mathrm{V037}\\
&-\mathrm{V066}-\mathrm{V014}-\mathrm{V023}-\mathrm{V006}.
\end{aligned}
\]

## Exact proof

The certificate lists 80 normalized 35-block systems.  The independent
verifier checks that each covers every pair of points exactly once.  For
each system it reconstructs Pasches as 4-cycles in the union of two derived
one-factors.  This is different from discovery, which examined all
four-block subsets.  The verifier obtains 1,390 Pasch occurrences and the
same count multiset as the 1999 published table; exactly one system has
count zero.

For every occurrence, the verifier forms the mate by equality of the 12
covered pairs and verifies the switched 35-block set is again an STS(15).
The sorted multiset of point-Pasch incidence counts distinguishes all 80
released representatives.  After selecting the unique signature match, an
exact backtracking map of the associated Steiner quasigroup verifies an
isomorphism to that representative.  Thus every switch target is proved,
not inferred from a hash or floating-point invariant.  The reconstructed
nonloop target pairs are exactly the 258 serialized simple edges.

All-pairs BFS gives a 79-vertex component and one isolated vertex.  The
largest finite distance is 11.  The displayed 11-edge path proves an upper
bound of 11 for its endpoints; the stored BFS layer partition puts
`V006` in layer 11 from `V000`, proving no shorter path exists.  The 79
BFS rows have maximum entry at most 11, proving the global upper bound.

## Completeness and limitation

The exact graph replay is self-contained once the 80 representatives are
given.  Exhaustion of all isomorphism classes uses the classical theorem
that there are 80 STS(15) classes.  As an operational cross-check, the
released canonical incidence-graph set is exactly equal to the current
DesignTheory.org complete 80-design catalogue.  No claim is made to provide
a new self-contained proof of the century-old classification.
