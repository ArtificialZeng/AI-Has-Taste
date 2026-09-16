# Independent triage recheck of the \(\mathsf E(8,4)\) obstruction

Provenance: `win-00082-p01-triage-b7e14c8d20d1`  
Date: 2026-09-09

This is triage evidence, not an accepted proof or a novelty determination.

## Source and statement checks

- `source.md` remained byte-for-byte unchanged, with SHA-256
  `c04e65d2ff0ba7de84944b7066312494cbb8b9d49bd8f1a68e2125aa6dac4ae9`.
- No file matching `literature/*handoff*.md` was present.
- The live arXiv v1 HTML at <https://arxiv.org/html/2609.06724> was inspected on
  2026-09-09. Definition 1.1 agrees with `problem.md`; Lemma 2.2 states
  \(\lambda(T-mb)=0\); and Conjecture 7.1 says
  \(\mathsf E(n,k)\iff\gcd(n,k)=1\) while the text explicitly leaves higher
  uniformities open.

## Independent algebra check

Assume the frozen ordering exists and let \(S\) be its eight distinct shifts.
At each time exactly four vertices occur, hence
\(1_S*1_D=4\). Every two distinct vertex supports meet in exactly
\(\binom62=15\) times. Lemma 2.2, with \(m=8\) and \(\lambda=15\), gives
\(15(T-8b)=0\) for each \(b\in S\). Subtraction gives
\(120(b-b')=0\pmod {70}\). The kernel is exactly
\(7\mathbb Z_{70}\), since \(\gcd(120,70)=10\). Replacing
\((S,D)\) by \((S-b_0,D+b_0)\) preserves every support \(D+s\), so
\(S=7A\) for an eight-set \(A\subset\mathbb Z_{10}\).

Writing \(t=j+7x\) and
\(D_j=\{x:j+7x\in D\}\), membership has the checked sign
\(x-a\in D_j\). Thus the meeting is
\(A\cap(x-D_j)\), and \(1_A*1_{D_j}=4\). Summation forces
\(|D_j|=5\). For \(B=\mathbb Z_{10}\setminus A\), this is equivalent to
\(1_B*1_{D_j}=1\).

Counter-translating the two factors normalizes \(B=\{0,d\}\) without changing
the tiling equation or the number of reconstructed columns. Its indicator
equation alternates around the orbits of translation by \(d\). Hence \(d\) has
even order, equivalently \(d\) is odd. If \(d\ne5\), it generates
\(\mathbb Z_{10}\); the only templates are the two parity classes, and a slice
repeats just two meetings. If \(d=5\), every template is a transversal of the
five antipodal pairs, while every meeting chooses one vertex from each of the
four pairs comprising \(A\). Only \(2^4=16\) meetings can occur, fewer than the
required 70. Both cases contradict bijectivity.

## Exact corroboration and literature boundary

`evidence/triage_enumerate.py` was rerun under Python 3 and exited zero. It
tested all \(45\cdot252=11{,}340\) pairs, found 200 valid slice pairs over 25
choices of \(A\), and asserted that no \(A\) accesses all 70 columns. Its
SHA-256 is
`e16911836fb1bc6290570e81aa4f0d10e62238bcb67eeb7e0e13342dc9b5401f`.
Exact web searches found only the 2026 source for this terminology and no later
primary-paper resolution. This limited search is not proof of novelty; the
source's cited single-track literature still needs a fuller release-stage
comparison.
