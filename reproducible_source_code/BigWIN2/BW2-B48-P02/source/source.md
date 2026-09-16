# Immutable source statement: win-00048-p02

## Title

Four Boolean starter questions for \(q=4\) at \(r=3,7\)

## Original lead (preserved)

> q=4, r in {3,7}: Hamilton starter E_r/C_r four Boolean values.

This is a supervisor-proposed exact small-parameter split of the source paper's \(r\equiv3\pmod4\) question. The notation \(E_r,C_r\) below is frozen for this intake; it is not notation asserted to appear in the paper.

## Exact proposed statement

For odd \(r\ge1\), let
\[
\mathcal C_4(r)=\operatorname{Cay}^{\to}(\mathbb Z_{4r},\{1,\ldots,r\}).
\]
For \(j\in\mathbb Z_4\) and \(s\in[r]\), let
\[
O_{j,s}=\{x\to x+s:x\equiv j\pmod4\}.
\]
Define the following Boolean assertions.

- \(E_r\): there exists a directed Hamilton cycle \(H\) in \(\mathcal C_4(r)\) meeting every \(O_{j,s}\) exactly once. Equivalently, \(H\) is a 4-layer balanced Hamilton starter.
- \(C_r\): there exists such an \(H\) that is chain-compatible: among the developed cycles
  \[
  H,H+4,\ldots,H+4(r-1),
  \]
  one can select exactly one arc from each cycle so that the selected \(r\) arcs form a simple directed path.

Determine the exact truth-value tuple
\[
(E_3,C_3,E_7,C_7)\in\{0,1\}^4.
\]
Here \(C_r\Rightarrow E_r\), but the four requested values must still be stated and certified separately. Chain compatibility is existential; the deletion chain is not required to be the step-2 path unless that is part of the supplied witness.

## Quantifiers and conventions

- A Hamilton cycle is a simple directed cycle through all \(4r\) vertices.
- Each allowed step \(s\in[r]\) must occur four times in \(H\), with its four tails lying in the four distinct residue classes modulo 4.
- Development is translation by 4 in \(\mathbb Z_{4r}\); the \(r\) translates must cover every arc exactly once, as in Lemma 2.3 of the source.
- For \(C_r\), the selected arcs must have pairwise distinct development colours and concatenate, in some order, to one simple directed path of length \(r\), exactly as in Definition 5.1 and Lemma 5.2.

## Primary source, page locator, and nearest result

- Jianwei Jiang and Chunhua Yang, *Hamilton Starters and Path Decompositions in Directed Circulants*, arXiv:2609.01256v1.
- Authoritative pages: <https://arxiv.org/abs/2609.01256> and <https://arxiv.org/pdf/2609.01256>.
- Definition 2.1 and Proposition 2.2 on pp.2--3 define balanced starters and the arc orbits; Lemma 2.3 on p.3 proves that a starter develops to a Hamilton decomposition; Proposition 2.4 on p.4 proves the necessary condition that \(r\) be odd; Definition 5.1 and Lemma 5.2 on p.9 define and characterize chain compatibility.
- Theorem 4.7 on pp.8--9 proves \(E_r\) for \(r\equiv1\pmod4\), \(r\ge9\); Lemma 5.4 on p.10 and Theorem 5.5 on p.11 prove chain compatibility and the optimal path number in that same range.
- Section 9, p.19, explicitly asks whether a different four-layer construction exists for \(r\equiv3\pmod4\), or whether a structural obstruction occurs. It explains that the ABAB proof fails in this congruence class but does not prove nonexistence.

## Precise delta and status caution

The delta is the exact first two \(r\equiv3\pmod4\) instances, with existence and chain compatibility separated into four Boolean questions. It does not ask for all \(r\equiv3\pmod4\), and it does not identify failure of the ABAB construction with failure of \(E_r\). Although Section 9 supports the unresolved status of the general congruence class, this intake has not exhaustively verified whether the four small truth values appear elsewhere. Status is therefore **open-supported general family / exact-small-case status uncertain**, not “fully verified open.”

## Decisive certificates

For a true \(E_r\), give a cyclic step word \(w=(s_0,\ldots,s_{4r-1})\in[r]^{4r}\) whose prefix sums modulo \(4r\) are all distinct, whose total is \(0\pmod{4r}\), and for which each step \(s\) has one tail in each class modulo 4.

For a true \(C_r\), additionally list \(r\) arcs of pairwise distinct development colours that concatenate to a simple path, and provide the colour calculation from formula (18)/Lemma 5.2.

For a false \(E_r\), provide exhaustive symmetry-broken SAT/CP enumeration with an independently checkable UNSAT certificate covering all Hamilton cycles and all balance constraints. For \(E_r=1,C_r=0\), enumerate all balanced starter orbits and certify that no starter admits a rainbow simple \(r\)-arc path in the development colouring. A negative \(C_r\) certificate is invalid unless it covers every balanced starter, not only one construction.

## Cheapest decisive route

Encode successor variables on \(\mathbb Z_{4r}\), exact step counts/layer balance, one-cycle connectivity, and dihedral/translation normalization. Solve \(r=3\) first, then \(r=7\). For every starter orbit found, search the finite development-coloured digraph for a simple rainbow path of length \(r\). Export explicit witnesses for YES and DRAT/LRAT or a small canonical exhaustive table for NO.

## Fast falsification

- A displayed balanced Hamilton cycle immediately falsifies \(E_r=0\).
- A displayed compatible deletion chain immediately falsifies \(C_r=0\).
- Failure of the source's ABAB template is not evidence for either negative answer.
- A claimed \(E_r\) witness fails if any prefix repeats, the total displacement does not close, or some \((j,s)\) orbit is missed or repeated.
- A claimed \(C_r\) witness fails if selected arcs repeat a development colour or their \(r+1\) path vertices are not distinct.

## Frozen material and primary-source fallback provenance

- Local research input: `batches/inbox/bigWin-48-materials/2609.01256.pdf`.
- SHA-256: `1ec8a1fc02a7736128e659f5ea152523a2aae73a2ff1ea621555e3b451e8b63c`.
- The local PDF was checked against the official arXiv record on 2026-09-06. If it is unavailable, retrieve the primary paper from the official arXiv abstract/PDF URLs above and record the newly obtained hash.
- Any spreadsheet-only or generated-scout record is merely lead provenance. Definitions, page locators, and the nearest theorem must fall back to the cited primary PDF; neither that spreadsheet nor this intake establishes novelty of the four exact truth values.
