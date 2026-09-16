# Precise problem reading

## Provenance and frozen assertion

- Triage job: `win-00065-p02-triage-e35c19e61734`.
- The immutable statement is `source.md` (SHA-256
  `b71158a55cdb4fa03de594447a51ba4e88261de47df066fe822dc14354abf8b6`).
- Its mathematical assertion is, verbatim,
  > `ex^+_{L2}(m,Reg5) = ||d^+_{T_4(m)}||_2^2`.
  The quantifier is: for every integer `m>=1`.

## Objects and conventions

1. A digraph is a pair \(D=(V,A)\) with finite \(V\) and
   \(A\subseteq\{(u,v)\in V^2:u\ne v\}\). Thus there are no loops and each
   ordered arc occurs at most once. Both \((u,v)\) and \((v,u)\) may occur.
   Equivalently, its adjacency matrix is a \(0,1\) matrix with zero diagonal,
   with no constraint relating opposite off-diagonal entries.
2. The out-degree and objective are
   \[
   d_D^+(v)=|\{w:(v,w)\in A\}|,\qquad
   L_2^+(D)=\sum_{v\in V}d_D^+(v)^2.
   \]
3. Fix a representative of the regular tournament on five vertices by taking
   vertex set \(\mathbb Z/5\mathbb Z\) and arcs \(i\to j\) when
   \(j-i\pmod 5\in\{1,2\}\). This is `Reg5`; it is the unique five-vertex
   tournament with every out-degree equal to two, up to isomorphism.
4. A copy is not required to be induced: \(D\) contains `Reg5` exactly when
   there is an injection \(f:\mathbb Z/5\mathbb Z\to V(D)\) such that every
   arc \(i\to j\) of `Reg5` gives the arc \(f(i)\to f(j)\) of \(D\). Extra
   arcs, including reverse arcs, do not invalidate the copy. `Reg5`-free means
   that no such injection exists.
5. Therefore
   \[
   \operatorname{ex}_{L_2}^+(m,\mathrm{Reg5})=
   \max\{L_2^+(D): |V(D)|=m,\ D\text{ is Reg5-free}\}.
   \]
6. \(T_4(m)\) is the balanced complete four-partite directed graph: its four
   independent parts have sizes differing by at most one, and each pair of
   vertices in different parts has both opposite arcs. Empty parts are allowed
   when \(m<4\).

## Exact claim and elementary lower bound

Write \(m=4q+r\), where \(q\ge0\) and \(r\in\{0,1,2,3\}\). The claim is
\[
\operatorname{ex}_{L_2}^+(m,\mathrm{Reg5})=
r(q+1)(3q+r-1)^2+(4-r)q(3q+r)^2,
\]
namely
\[
\begin{array}{c|c}
r&\text{claimed value}\\ \hline
0&36q^3\\
1&36q^3+27q^2+3q\\
2&36q^3+54q^2+22q+2\\
3&36q^3+81q^2+57q+12.
\end{array}
\]
Indeed, a vertex in a part of size \(s\) has out-degree \(m-s\). Also,
\(T_4(m)\) is `Reg5`-free: among any five selected vertices, two lie in one
part and have neither arc between them, whereas a tournament copy requires an
arc for every pair. Thus the displayed value is an unconditional lower bound;
the unresolved content is the matching upper bound (or a counterexample).

For \(1\le m\le4\), `Reg5`-freeness is vacuous and
\(L_2^+(D)\le m(m-1)^2\), with equality for the complete bidirected graph,
which equals \(T_4(m)\). Hence the claim is already elementary for these four
orders. The assertion concerns the value only; it does not assert uniqueness
of the extremal digraph.

## Literature status and research scope

- Ai--Chen--Chen--Yan--Zhao, *Palette extremality via degree-square Turán
  problems*, arXiv:2606.03520v2, lines/§1 and §9 (retrieved 2026-09-07),
  defines the same non-induced, digon-permitting degree-square problem and asks
  for exact values for self-converse tournaments. It does not settle `Reg5`.
  <https://arxiv.org/abs/2606.03520>
- Daniel Iľkovič, *\(L_2\) Turán Problems for Small Tournaments and Stability*,
  arXiv:2609.05042v1, Conjecture 3.3 on PDF p.4 (retrieved 2026-09-07), states
  exactly the present formula; its conclusion on PDF p.13 says a formal proof
  remains future work. The inspected local PDF has the source-specified SHA-256
  `8d45a6dc1d9b672641e96492fa55dcf79afcd8fac6dfff945234551c07717666`.
  <https://arxiv.org/abs/2609.05042>

Accordingly the source status is **open-supported** as of this bounded search,
not proved open by the search itself. Exact-assertion and equivalent-language
searches found no later primary proof or disproof, but this is not a priority
claim. The nearest result is Conjecture 3.3 itself. The proposed delta is a
certified counterexample at the least exhaustively checked order, or a matching
upper bound for all orders. The first verification route is exact enumeration
from \(m=5\); the adjacent `TT4` and `R4` theorems are not evidence for the
required upper bound.
