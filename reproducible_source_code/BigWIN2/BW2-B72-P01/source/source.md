# win-00072-p01 — Least positive layer of the P4/Paw blow-up coefficient system

## Immutable primary-source record

- Primary source: Feifan Gong, Kehua Wang, and Wei Wang, *The Distance Spectrum Does Not Determine Bipartiteness*, arXiv:2608.17311v1 [math.CO], 18 August 2026.
- Official abstract: <https://arxiv.org/abs/2608.17311v1>.
- Official PDF: <https://arxiv.org/pdf/2608.17311v1>.
- Locations: independent-set blow-ups in §2; the reduced \(P_4\) and Paw quartics and coefficient system in equations (3.1)–(3.3), printed pp.3–4; the order-61 witness in Theorem 3.1, pp.4–5; the source-stated minimum-order and positive-solution-classification follow-ups in Conclusion, p.7.
- Access record: the official arXiv PDF was inspected on 2026-09-08 and is archived as bigWin-72-materials/2608.17311.pdf, SHA-256 583250e3cb9e80c5177343cc2ad9b1580c050be2caaf9ce0122b97b9df2d4b84.

## Frozen assertion

For \(a=(a_0,a_1,a_2,a_3)\) and \(b=(b_0,b_1,b_2,b_3)\) in \(\mathbb Z_{>0}^4\), consider
\[
\begin{aligned}
b_0+b_1+b_2+b_3&=a_0+a_1+a_2+a_3,\\
3b_0b_1-5b_0b_3+3b_1b_2+3b_2b_3
 &=3(a_0a_1+a_0a_2+a_0a_3+a_1a_2),\\
8b_0b_3(b_1+b_2)&=2a_1a_2(a_3-2a_0),\\
4b_0b_1b_2b_3&=a_0a_1a_2a_3.
\end{aligned}
\]
Let \(s=\sum_i b_i=\sum_i a_i\). Determine the least possible \(s\), and classify every ordered positive-integer solution at that least value.

For reporting orbit representatives, the only identifications allowed are the two visibly system-preserving involutions
\[
(b_0,b_1,b_2,b_3)\mapsto(b_3,b_2,b_1,b_0),
\qquad
(a_0,a_1,a_2,a_3)\mapsto(a_0,a_2,a_1,a_3).
\]
The complete ordered solution list must still be recorded before quotienting by these involutions.

## Nearest result and exact contribution boundary

The source exhibits
\[
b=(1,16,8,36),\qquad a=(4,9,16,32),
\]
with \(s=61\), which yields connected distance-cospectral \(P_4[b]\) and
\(\operatorname{Paw}[a]\) having opposite bipartiteness. It does not prove that 61 is the minimum within equation (3.3), nor classify the least layer.

This project is restricted to the positive-integer coefficient system (3.3). Even a complete answer does not determine the minimum order among all connected distance-cospectral graph pairs of opposite bipartiteness.

## Desktop prescreening observation — not accepted evidence

Two independent screening implementations enumerated the positive ordered four-tuples on both sides through \(s=61\) and joined their exact coefficient signatures. They reported:

- exactly \(\binom{61}{4}=521{,}855\) positive ordered four-tuples with sum at most 61 on each side;
- no matching pair with \(s<61\);
- at \(s=61\), exactly four ordered pairs, all generated from the displayed source pair by the two involutions above;
- shared signature \((61,1116,6912,18432)\), using the common sum and the three matched coefficient values.

The worker must independently rebuild this computation from the frozen equations. The prescreen is a lead, not a proof and not a certificate imported into the mathematical gate.

## Cheapest decisive attack and certificate contract

Enumerate every positive ordered four-tuple with sum at most 61. Compute, separately for \(b\) and \(a\), the common-sum value and the three integer coefficient expressions in the frozen system; perform an exact signature join.

A complete positive result needs:

1. source code with the exact domain, integer formulas, version, and no random seed;
2. per-side domain cardinalities, per-layer signature counts, the full ordered match list, and stable digests;
3. a second independent verifier or independently derived SMT/SAT certificate that confirms coverage, every hit, and absence below 61;
4. a short mathematical explanation that the signature equality is exactly equivalent to system (3.3), not merely necessary.

Any exact solution with \(s<61\) disproves the expected minimum and should stop the \(s=61\) proof route. Any additional \(s=61\) orbit disproves the expected uniqueness classification.

## Novelty and value risks

- The source explicitly asks both a global minimum-order question and a classification of all positive solutions. This project answers only the first layer of its fixed \(P_4/\mathrm{Paw}\) ansatz.
- A finite enumeration can be rigorous but still too small or direct for a paper. Fresh referee must assess whether the sharp minimum plus equality classification is a meaningful new contribution or should remain a reproducible result asset.
- Current-literature checking must confirm that no later version or related computational note already reports this least layer.

## Semantic boundary

No registered project concerns arXiv:2608.17311, equation (3.3), the \(P_4/\mathrm{Paw}\) blow-up signature, or its least positive layer.

