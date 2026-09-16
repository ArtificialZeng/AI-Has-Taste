# Exact resolution and completeness argument

## Result

For the frozen 18-facet complex, \(c(S)=3\).  The displayed words

\[
105374,\qquad 216587,\qquad 023648
\]

are an explicit minimum decomposition.  After quotienting each circuit by
cyclic rotation and reversal and treating the collection as unordered, there
are exactly three labeled minimum decompositions:

1. `014735`, `023648`, `127856`;
2. `015684`, `028753`, `126347`;
3. `032615`, `041728`, `346857`.

The first is the displayed decomposition, with two words represented by a
rotation of their reversals.  The automorphism group of the fixed complex has
order 108 and is transitive on these three decompositions.  Hence the requested
count after also quotienting by automorphisms of \(S\) is exactly **one**.

## Completeness lemma

Let

\[
\Omega=\{(a,b,c):a,b,c\text{ are distinct and }\{a,b,c\}\in F(S)\}.
\]

Thus \(|\Omega|=18\cdot6=108\).  Direct edge-incidence calculation from the
frozen facet list shows that there are 27 edges and every edge belongs to
exactly two facets.  Define a transition permutation \(P\) on \(\Omega\) by

\[
P(a,b,c)=(b,c,d),
\]

where \(\{b,c,d\}\) is the unique facet other than \(\{a,b,c\}\) containing
the edge \(\{b,c\}\).  This map is bijective: its inverse crosses the edge
formed by the first two entries in the opposite direction.

If \(W=(v_i)\) is any 2-circuit, put
\(s_i=(v_i,v_{i+1},v_{i+2})\).  Consecutive facets are distinct by the
injectivity requirement and both contain \(\{v_{i+1},v_{i+2}\}\); the
two-facet edge incidence therefore forces \(s_{i+1}=P(s_i)\).  Cyclicity of
the word makes its state sequence a complete orbit of \(P\): stopping before
the orbit closes would not be cyclic, and traversing it more than once would
repeat a facet.  Conversely, a \(P\)-orbit whose underlying facet projection
is injective supplies a 2-circuit.  Thus enumerating the orbits of \(P\) is a
complete enumeration of all possible circuits, rather than a prefix search.

## Exact enumeration

`enumerate_circuits.py` constructs all 108 ordered states and all transitions
from integer set incidence.  It obtains 18 directed transition orbits.  Every
orbit has length six and has injective facet projection.  Reversal pairs these
orbits into nine circuits modulo rotation and reversal.  The script then tests
all \(2^9=512\) subcollections of those circuits.  Exactly the three
subcollections displayed above cover every facet once, and each has three
members.  In particular, the exhaustive counts for one- and two-circuit
decompositions are both zero.  This proves \(c(S)\ge3\), while the explicit
displayed decomposition proves \(c(S)\le3\).

For the optional quotient, the script tests all \(9!\) vertex permutations
against the frozen facet set.  Exactly 108 are automorphisms.  On the three
minimum decompositions, each of the six permutations occurs as an induced
action 18 times.  The action is transitive; equivalently its Burnside fixed
point sum is 108, giving \(108/108=1\) orbit.

The exact certificate is `circuit_certificate.json`.  It contains the edge
incidence table, all directed transition orbits, all nine unoriented circuits,
the three exact covers, all 108 automorphisms, the action distribution, and a
SHA-256 commitment to the full ordered transition table.

## Independent replay

Run from the project root:

```text
python3 evidence/enumerate_circuits.py
python3 evidence/replay_certificate.py
```

The replay checker imports no generator code.  It rebuilds edge incidence in a
different representation, walks from every ordered facet, checks all 512
Boolean circuit selections, exhausts all \(9!\) vertex permutations, compares
the serialized certificate, and prints `REPLAY OK`.  Both programs use only
the Python standard library and exact integer/set operations.

## Scope

This resolves only the frozen finite complex in `source.md` and `problem.md`.
The inspected primary source supplies the displayed three-circuit cover and
states the absence of an Euler 2-circuit without proof; it does not supply this
two-circuit exclusion or exact enumeration.  No broader assertion about
triangulated tori is made.
