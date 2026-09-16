# Precise problem: four-layer starters at \(r=3,7\)

## Frozen input and interpretation

The immutable lead is `source.md` (SHA-256
`2ac3585af423553cc0468c29eebc688307c2675f551a86cc6578710e13ea9e17`).
The target is exactly the four existence assertions at \(r\in\{3,7\}\); the
phrase “for odd \(r\ge 1\)” supplies the common definitions and does not enlarge
the requested parameter range.

Write \([r]=\{1,\ldots,r\}\), and identify \(\mathbb Z_n\) with residues modulo
\(n\).  The directed Cayley graph
\[
  \mathcal C_4(r)=\operatorname{Cay}^{\to}(\mathbb Z_{4r},[r])
\]
has vertex set \(\mathbb Z_{4r}\) and exactly the arcs
\(x\to x+s\pmod{4r}\), where \(x\in\mathbb Z_{4r}\) and \(s\in[r]\).
For \(j\in\mathbb Z_4\) and \(s\in[r]\), put
\[
  O_{j,s}=\{x\to x+s:x\equiv j\pmod4\}.
\]
These are the arc orbits under translation by \(4\), each of size \(r\).

## Exact quantifiers

For each fixed \(r\in\{3,7\}\), \(E_r\) is the assertion that there exists a
simple directed Hamilton cycle \(H\) in \(\mathcal C_4(r)\) such that
\[
  |A(H)\cap O_{j,s}|=1
  \quad\text{for every }(j,s)\in\mathbb Z_4\times[r].
\]
Thus every allowed step occurs exactly four times, once from each tail residue
class modulo \(4\).  There are \(4r\) conditions and \(4r\) arcs in \(H\).

Given such an \(H\), for \(k\in\mathbb Z_r\) define
\(H_k=H+4k\) by translating both endpoints of every arc.  Balance implies that
the \(H_k\) are pairwise arc-disjoint Hamilton cycles and partition the full arc
set of \(\mathcal C_4(r)\).

For each fixed \(r\in\{3,7\}\), \(C_r\) is the assertion that there exist:

- an \(H\) witnessing \(E_r\);
- one arc \(e_k=u_k\to v_k\in H_k\) for every \(k\in\mathbb Z_r\); and
- a permutation \(\sigma\) of \(\mathbb Z_r\),

such that \(v_{\sigma(i)}=u_{\sigma(i+1)}\) for \(0\le i<r-1\), and the
resulting \(r+1\) path vertices are pairwise distinct.  Equivalently, the chosen
arcs, reordered by \(\sigma\), form one simple directed path of length \(r\).
All quantifiers in \(C_r\) are existential, including the choice of \(H\) and of
the path; the path is not required to use step \(2\).  In particular,
\(C_r\Rightarrow E_r\), but the requested output must separately certify
\[
  (E_3,C_3,E_7,C_7)\in\{0,1\}^4
\]
in precisely that order.

## Equivalent certificate formulations

After translating a proposed cycle, an \(E_r=1\) certificate may be given by a
cyclic step word \(w=(s_0,\ldots,s_{4r-1})\in[r]^{4r}\).  Put
\(p_0=0\) and \(p_i=\sum_{h<i}s_h\pmod{4r}\).  It is valid exactly when:

1. \(p_0,\ldots,p_{4r-1}\) are pairwise distinct;
2. \(p_{4r}=p_0\); and
3. for every \((j,s)\in\mathbb Z_4\times[r]\), exactly one index \(i\) has
   \(s_i=s\) and \(p_i\equiv j\pmod4\).

For chain compatibility, balance gives a unique \(\beta_j(s)\in\mathbb Z_r\)
such that the step-\(s\) arc of \(H\) with tail residue \(j\) has tail
\(j+4\beta_j(s)\).  If \(x=j+4t\), the development colour of
\(x\to x+s\) is
\[
  \chi(x,s)=t-\beta_j(s)\pmod r.
\]
A \(C_r=1\) certificate is therefore an \(E_r\) certificate plus a simple
directed \(r\)-arc path whose colours \(\chi\) are pairwise distinct (and hence
use every colour in \(\mathbb Z_r\)).  A negative \(E_r\) result requires an
exhaustive, independently checkable enumeration or proof covering every balanced
Hamilton cycle.  A negative \(C_r\) result must additionally cover every
balanced starter, not just one starter orbit.

## Domain checks and scope

Both target values of \(r\) are odd, satisfying the source paper's necessary
condition.  The steps are nonzero and less than half the group order, so there
are no loops or reverse pairs of allowed arcs.  Balance fixes the total positive
displacement at \(4\sum_{s=1}^r s=2r(r+1)\), which is divisible by \(4r\) for
these odd \(r\); this is necessary closure but does not establish Hamiltonicity.

The problem does not ask for all \(r\equiv3\pmod4\), for an ordinary Hamilton
decomposition unaccompanied by a balanced starter, or for the path number of the
digraph.  Failure of the paper's ABAB template is not a nonexistence result for
either \(E_r\) or \(C_r\).

## Literature triage and proposed contribution

On 2026-09-06 the official record and v1 PDF of Jianwei Jiang and Chunhua Yang,
*Hamilton Starters and Path Decompositions in Directed Circulants*,
[arXiv:2609.01256v1](https://arxiv.org/abs/2609.01256), were inspected.
Definition 2.1, Proposition 2.2, and Lemma 2.3 (printed pp. 2--3) support the
definitions and development claim above.  Definition 5.1 and Lemma 5.2
(printed p. 9) give the exact chain and colour formulations.  Theorem 4.7
(printed pp. 8--9) proves \(E_r\) only for \(r\equiv1\pmod4\), \(r\ge9\), and
Lemma 5.4 proves chain compatibility there.  Section 9 (printed p. 19) explicitly
leaves the \(r\equiv3\pmod4\) four-layer family open and says only that its ABAB
mechanism fails.

Targeted searches on 2026-09-06 for the exact title/assertion, “4-layer balanced
Hamilton starter” with \(r=3\) and \(r=7\), and the equivalent “Hamiltonian orbit
transversal” language found no separate primary source settling these two cases.
This limited search is not proof of novelty or openness.  The source status is
therefore **open-supported for the general family; exact-small-case status
uncertain**.

Nearest prior result X: the paper's construction for \(r\equiv1\pmod4\),
\(r\ge9\), with chain compatibility.  Proposed delta Y: determine and exactly
certify the four Boolean values for the first two \(r\equiv3\pmod4\) cases.
Verification route Z: symmetry-broken exact successor/step search, first at
\(r=3\), with explicit words and rainbow paths for YES or a replayable exhaustive
certificate for NO; then repeat at \(r=7\).
