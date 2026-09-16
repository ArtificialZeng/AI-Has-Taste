# Triage evidence

Date: 2026-09-07  
Job: `win-00056-p02-triage-cd01ec955c74`

## Source integrity and primary-source inspection

- `source.md` SHA-256 before and after triage: `b378ab7be4089df007c5db90e906371714e0ccbc58e33fc3b6f8a424eb066e4b`.
- The project source is byte-identical to the immutable batch intake source.
- Local primary PDF inspected: `/home/ailab/4math-open-problems/batches/inbox/bigWin-56-materials/2609.04050.pdf`, SHA-256 `dcb0d9a0b6643986f4b56a623e853e82d8d88da667386e872c5414eb33ba2972` (the hash stated in `source.md`).
- Official record inspected: <https://arxiv.org/abs/2609.04050>, retrieved 2026-09-07. It identifies version 1, submitted 2026-09-03, and authors Massimiliano Fasi and Behnam Hashemi.
- PDF equation (2), page 2, defines \(\kappa_2(X)=\sigma_1(X)/\sigma_r(X)\) with \(\sigma_r\) the smallest nonzero singular value. Proposition 1, page 11, gives the diagonal/Hadamard representation. Example 6, page 21, uses exactly the four matrices in the frozen statement, tests 30 logarithmically spaced \(\delta\)'s in \([10^{-6},1]\), and reports observed orders \(\delta^{-2},\delta^{-1},1,1\). Inspection found no exact constants, asymptotic proof, or error bounds there.
- Bibliographic obstacle: `source.md` gives the wrong author list for the correct arXiv identifier. The official record and the hash-matched PDF agree on Fasi--Hashemi, so this is a metadata error rather than mathematical ambiguity. The immutable source was not edited.

## Cheap exact checks

From the four explicit matrices, symbolic rational determinant expansion gives
\[
\det X_1=\det X_4=\frac1{117(\delta+3)},
\]
\[
\det X_2=\frac{5(\delta+9)(\delta+19)}{5928\delta(\delta+3)(\delta+6)},\qquad
\det X_3=-\frac{5(17\delta+115)}{11856(\delta+3)(\delta+6)}.
\]
All are nonzero for \(0<\delta\le1\), so all four condition numbers use \(\sigma_3\), not a rank-deficient exception. The failed `python` invocation was operational only; the check succeeded with `python3`/SymPy and is not itself evidence of any asymptotic claim.

## Literature and registry screen

- Web queries for the title/arXiv identifier, the exact Example 6 assertion, and the distinctive \(I+E_{12}\), \(\mathbf1-E_{12}\) data returned no relevant primary mathematical source beyond arXiv:2609.04050. This limited screen does not establish novelty or priority.
- Registry comparison found the same normalized `win-00056-p02` intake and its project/source copies, but no separate project with a mathematically overlapping four-case exact-asymptotic claim. This is a duplicate check, not a literature result.

## Triage conclusion

Advance. The target is precise, the nearest prior result is strictly weaker (finite numerical observations), exact symbolic evidence is available, and the first research test is bounded. No mathematical resolution is claimed at triage.

