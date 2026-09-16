# Structural triage evidence

Job: primary-20260913-nfa-asymmetry-triage-46dc24ebd607. Date: 2026-09-13.
These are owner-derived arguments for a research admission, not an independently
audited candidate. The original growth problem remains unresolved.

## Target and imported theorem

For integer q>=3 let A_one(q) be A(q) restricted to ordered distinct pairs
w=0^a 1 0^b, x=0^c 1 0^d, where a,b,c,d are nonnegative integers and a+b=c+d.
Put H=(q-1)^2+1 and L=lcm(1,...,q). The target suggested by this triage is

    A_one(q) = H+1 = (q-1)^2+2.

The upper argument uses the following **imported classical theorem**: every
q-by-q Boolean matrix B satisfies B^(H+L)=B^H. Multiplication is Boolean.
Zajac and Jokay, printed p.1331, Theorems 1-2, explicitly report the universal
index H and the universal period as the lcm of the lcms of all partitions of q.
That period is L: every part is <=q, while each r<=q occurs in a partition
(r,1,...,1). Thus the reported period both divides and is divisible by L.
Multiplication by further powers gives periodicity for every exponent >=H.
This applies to arbitrary, possibly reducible and nilpotent matrices, not only
primitive matrices. A witness with fewer than q states can be padded with
isolated unreachable states.

The local reporting paper was read and its bytes verified. Schwarz's original
1974 proof was not accessible in this job. Before freezing a candidate, verify
the imported theorem from an original proof or an equivalent authoritative
account. The exact finite checks below do not replace that task.

## Upper bound: complete dichotomy

Suppose a q-state NFA accepts x and rejects w. Let B and C be its zero and one
transition matrices. Set Delta=a-c, which is nonzero; b-d=-Delta.

1. If L does not divide Delta, some r in {2,...,q} does not divide Delta.
   Use an r-state zero-cycle, initially at residue 0, and one new final state f.
   Only the cycle state congruent to a modulo r has a one-transition, to f;
   f has a zero-loop. All other transitions are missing. This accepts w and
   rejects x, with r+1<=q+1<=H+1 states. Choosing residue c gives the opposite
   direction as well. No claim about its behavior on other words is needed.

2. If min(a,c)=k<H, the words first differ at position k+1. To accept the word
   with the earlier marker, a chain on k zeros followed by a one-edge into a
   final state with a zero-loop uses k+2 states. The rejected word has zero
   instead of one at that edge, so its path dies. To accept the later-marker
   word, use a chain on k+1 zeros ending in a final state with both loops;
   the earlier marker kills the rejected word's path. Again there are k+2
   states. This includes k=0 and requires no rejecting sink in a partial NFA.
   If instead min(b,d)=k<H, apply these constructions to the reversed words.
   Each constructed automaton has one final state; reversing edges and swapping
   its initial and final states preserves its state count and gives one initial
   state. Thus a short block anywhere gives at most k+2<=H+1 states.

3. Otherwise L divides Delta and all four exponents are >=H. Periodicity gives
   B^a=B^c and B^b=B^d, hence B^a C B^b=B^c C B^d. The words then have identical
   transition relations, and no choice of initial/final states separates them.
   This contradicts the assumed q-state separator.

The three cases cover every pair, both signs of Delta, and zero-length blocks.
They establish the upper bound conditional on the imported theorem.

## Matching lower-bound route: strengthen the published pumping argument

This argument does not use the imported matrix-index theorem. For s=q-1>=2 put

    M=s^2, T=2^(M+1), P=lcm(1,...,T),
    u=0^M 1 0^(T+P), v=0^(M+P) 1 0^T.

These slightly change Nicol's T (his T is 2^M). Consider any NFA with m<=M+1
states accepting u, and fix an accepting path. Its first zero-segment has M
edges. If it repeats a vertex, it contains a simple zero-cycle of length <=m.
If it does not repeat a vertex, it visits M+1 distinct states, forcing m=M+1
and visiting every state. The final zero-segment is longer than m and contains
a simple zero-cycle, whose vertex therefore occurs on the initial segment.
In either case a vertex of the initial segment supports a zero-cycle of length
h<=m. Since h divides P, insert P/h traversals at that vertex to lengthen the
initial segment by P without changing its terminal state.

Let z be the state immediately after the one-edge, and S_j the subset reachable
from z by j zeros. This deterministic subset sequence has <=2^m<=T values.
It is periodic at time T with period c<=T. Because c divides P,
S_T=S_(T+P), so the old final accepting state is reachable after T zeros too.
Together the modified segments accept v. Thus no NFA with <=M+1 states accepts
u while rejecting v, and nsep(u,v)>=M+2. A prefix chain gives the matching
upper bound M+2 for this pair directly.

For the easy direction reuse Nicol's q=s+1 state zero graph: vertices 0,...,s,
edges i->i+1 for 0<=i<s, and s->0, s->1. Add only the one-loop at vertex 0;
vertex 0 is both the initial and sole final state. Positive zero return lengths
are precisely as+b(s+1), with a>=0,b>=1. In residue b modulo s, choose
b in {1,...,s}; the last excluded length in that residue is b(s+1)-s.
The overall largest excluded length is s^2=M. Hence the machine rejects u and
accepts v, whose two zero blocks both exceed M. This gives nsep(v,u)<=q.

If this derivation survives research verification, it yields both the exact
one-marker formula and the minor general lower improvement A(q)>=H+1. The
constant improvement alone is not the proposed publishable contribution; the
uniform sharp classification of the entire natural witness class is the target.

## Verification and boundaries

`triage-structural-check.py` checks every Boolean relation for dimensions
1,2,3,4 (2,16,512,65536 matrices respectively). It found no failure of the
universal identity B^(H+L)=B^H. Independently it checks that, when B has a cycle,
B^(m-1) is entrywise contained in B^(m-1+lcm(1,...,m)); no failure occurred.
It also checks the return-length characterization for the explicit witness
graph for s=2,...,12 and lengths 0,...,4s^2, with last excluded length s^2.
These are exact finite observations only; the all-size arguments are above.

The upper bound does not extend to arbitrary words: a general word is not of
the form B^a C B^b, and matching a single displacement no longer determines its
transition relation. No result about unrestricted A(q)'s asymptotic growth is
claimed. No novel theorem has been accepted and no manuscript was created.
