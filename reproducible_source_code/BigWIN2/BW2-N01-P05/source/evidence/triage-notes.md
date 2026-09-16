# Exact triage observations and reduction boundary

Job `newwin-00001-p05-triage-39e6415a55b0`, 2026-09-12.
Reproduce with `python3 evidence/triage-recheck.py` from the project directory.
No random input or floating-point arithmetic is used in the mathematics.
The unqualified `python` executable is unavailable; `python3` works.

The complete RGS enumeration revisited all 44,933 inputs at k=3,4 and lengths
2k,2k+1,2k+2. The literal stack and first-letter recursion agree at each
iteration. Enumerated totals match Stirling numbers; witness sets match the
inherited JSON exactly. A third stack implementation checks every triple of
the proposed stack on all 353 excess-two witnesses, through iteration k.
All witnesses are unsorted at k-1 and sorted at k. This is exact finite evidence,
not a new all-k theorem or an independent referee pass.

| k | counts at 2k,2k+1,2k+2 | witnesses by initial truncation length 2k,2k+1,2k+2 |
|---|---|---|
| 3 | 1,12,81 | 21,42,18 |
| 4 | 1,22,272 | 36,126,110 |

## A known consequence that removes run expansions

Let P_k denote the number of target representatives with no equal adjacent
letters. Truncation compatibility (source Proposition 3.1) implies by induction
that run expansion preserves sortedness after each fixed number of iterations.
A run-free representative of length m has exactly binom(n-1,m-1) expansions to
length n, by positive compositions of n into its m run lengths; truncation is
the unique inverse and relabeling introduces no multiplicity. Theorem 1.1
excludes target cores shorter than 2k. The unique core at 2k and Theorem 1.2
therefore give, for every k>=3,

    M_k = P_k + (3/2) k(k-1)(2k+1).

Indeed, the run-free count at 2k+1 is
binom(k+1,2)+2 binom(k,2)-2k=k(3k-5)/2. Expanding the 2k and 2k+1 cores to
2k+2 contributes binom(2k+1,2)+(2k+1)k(3k-5)/2. Thus P_3=18 and P_4=110.
This elementary deduction from known results is a bookkeeping reduction, with
no novelty claim. Classifying all P_k would address the full original target
via the unique expansions; it is not an arbitrary restricted substitute.

## First-letter reduction and the unresolved membership step

For a target w let x be its first letter, m its multiplicity, and define
q=trunc(v), where phi(w)=v x^m. Lemma 2.1 guarantees this terminal block.
The exact check records the following (m, |q|-2(k-1)) counts:

- k=3: (2,0):23; (3,0):39; (4,0):19.
- k=4: (2,0):82; (2,1):9; (3,0):117; (3,1):20; (4,0):44.

The length bound |q|<=2(k-1)+1 holds by an elementary argument for all k>=3.
For m>=3 it follows from |v|=2k+2-m. For m=2, write w=x s_1 x s_2,
allowing empty segments. At least one other letter has multiplicity >=3, so
some s_i contains a repetition. Any word s with a repetition has an adjacent
equal pair in phi(s): induct on length using Lemma 2.1, either the first letter
repeats and contributes its terminal block, or it occurs once and the suffix
contains the repetition. Since v=phi(s_1)phi(s_2), truncation removes at least
one position. Furthermore C(phi(w))=1 by journal Corollary 2.2, so every letter
of q has at least two distinct runs. Hence |q|>=2(k-1).
These are direct deductions from the source, not a claim of novel classification.

What is not established here: q must itself remain unsorted after k-2 passes
for arbitrary k>=4. It does so for all 272 k=4 witnesses. It does not do so at
k=3: all 81 reduced q sort after one pass. For example,

    w = 00012012
    phi(w) = 21210000
    phi^2(w) = 10000122  (unsorted)
    phi^3(w) = 00002211  (sorted),
    q = 2121, phi(q) = 1122 (sorted).

Thus an unqualified deletion-of-terminal-block induction is false at the
two-letter boundary. This is a diagnostic example for a proposed reduction,
not a counterexample to the original problem or the cited k>=3 theorems.

## One next test

Prove or refute the following precise bridge: for every k>=4 and every target
w, the q above satisfies phi^{k-2}(q) unsorted. The length bound is already
justified, so this would put q into exactly the known two layers on k-1
letters. First test the bridge exhaustively on the k=5 multiplicity types
(4,2,2,2,2) and (3,3,2,2,2), then seek a proof controlling the effect of the
terminal clumped letter. Keep k=3 as an explicit base. A counterexample must
include the complete w and q orbits. If the bridge holds, inverse multiplicity
and overlap control, especially for run-free cores, are the remaining counting
tasks; the bridge alone is not the requested classification.
