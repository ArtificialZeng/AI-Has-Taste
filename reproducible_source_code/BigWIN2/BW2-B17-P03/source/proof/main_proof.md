# Exact determination of L_41

## Theorem

With the definition in `problem/formal_statement.md`, \(L_{41}=529\).

## Positive endpoint

Take \(d=42\) and the set \(V\) in `certificate/witness.json`.  It has 41
distinct members in \([2,487]=[2,529-42]\).  The independent verifier forms
all 82 integers \(v,v+42\), checks that they are distinct, and evaluates all
\({82\choose2}=3321\) gcds; every gcd is one.  Thus \(L_{41}\le529\).

## Negative endpoint

Suppose a feasible pair \((d,V)\) existed at \(x=528\).  Since \(|V|=41\),
the set is nonempty and \(1\le d\le526\).  If \(d\) were odd, each pair
\(v,v+d\) would contain an even integer.  At least two different columns
would therefore contribute two distinct even integers, whose gcd is at least
two.  Hence \(d\) is even, leaving exactly \(d=2,4,\ldots,526\).

For a fixed even \(d\), define a graph whose vertices are those
\(v\in[2,528-d]\) with \(\gcd(v,v+d)=1\).  Join \(v\ne w\) precisely when
the four integers \(v,v+d,w,w+d\) are distinct and pairwise coprime.  By
unpacking the definition, a set of vertices is a clique if and only if its
associated pairs form a feasible collection.  Thus a feasible \(V\) exists
if and only if this graph has a 41-clique.

`clique_search.py` exhausts each graph by include/exclude recursion.  At each
node it greedily partitions the remaining vertices into independent color
classes.  If there are \(c\) classes and the current partial clique has size
\(r\), no extension can exceed \(r+c\), because a clique contains at most one
vertex of each independent class.  Pruning when \(r+c<41\) is therefore
sound.  Otherwise the recursion selects each remaining vertex in turn and
recurses on exactly its neighbors, so every possible extension is either
visited or rejected by this proved upper bound.  The retained log contains an
UNSAT result for every one of the 263 even gaps.

Independently, `packing_verify.py` factors integers by trial division.  It
assigns to a candidate \(v\) the prime support of \(v(v+d)\).  Since every
integer is at least two, two pairs are compatible exactly when these supports
are disjoint.  A separately implemented exhaustive set-packing recursion,
with its own graph construction and coloring bound, also rejects size 41 for
all 263 gaps.  Both implementations were additionally compared with literal
combination enumeration on every even gap for \(8\le x\le30\) and all targets
through one above the exact optimum (568 decisions), with complete agreement.

Consequently no feasible set exists at \(x=528\), so \(L_{41}>528\).
Together with the witness, \(L_{41}=529\).

## Trust boundary

The proof uses exact integer arithmetic only.  It does not rely on solver
status strings, floating point, randomness, timeout behavior, or an external
SAT/ILP package.  Python's integer arithmetic, the short source programs, and
the mathematical completeness argument above form the trust base.  No proof
assistant was used.
