# Formal statement

## Objects and conventions

For every integer \(N\ge 1\), let \(S_N\) be the permutations of
\([N]=\{1,\ldots,N\}\).  Pattern containment and avoidance are classical
(not consecutive): a word with distinct entries contains \(123\), for
example, when some three entries in increasing index order are increasing in
value.

For a permutation \(\pi=\pi_1\cdots\pi_N\), the right-greedy map
\(s_{123,132}\) processes the input from left to right.  It pushes the next
entry whenever the stack, read top to bottom after the push, avoids both
\(123\) and \(132\); otherwise it pops the current stack top to the output and
tries the same input entry again.  Once the input is exhausted, it pops the
remaining stack to the output.  Equivalently, because the stack already
avoids both patterns, an entry \(x\) may be pushed exactly when the current
stack contains at most one entry larger than \(x\).

Write \(s=s_{123,132}\).  A permutation \(\rho\in S_N\) is periodic if
\(s^r(\rho)=\rho\) for some integer \(r\ge 1\).  Define its transient length
by
\[
 t_N(\pi)=\min\{k\in\mathbb Z_{\ge0}:s^k(\pi)\text{ is periodic}\}.
\]
The published theorem of Zhang gives
\[
 \max_{\pi\in S_N}t_N(\pi)=L_N:=2\left\lfloor\frac{N-1}{2}\right\rfloor.
\]
Thus the minimally-sorted set used here is
\[
 M_N:=\{\pi\in S_N:t_N(\pi)=L_N\}.
\]
By Berlow's periodic-point theorem, periodicity is equivalently the exact
condition
\[
 \pi_{N-1}\pi_{N-3}\cdots\pi_{3-(N\bmod 2)}=12\cdots
 \left\lfloor\frac{N-1}{2}\right\rfloor,
\]
where the displayed word is empty when \(N\le2\).

## Conjectured endpoint

The quantified conjecture is
\[
 \forall n\in\mathbb Z_{\ge1},\qquad
 |M_{2n}|=(n+1)|M_{2n-1}|.
\]
The requested first relation beyond the range reported in the 2025 paper is
the exact integer equality
\[
 |M_{14}|=8|M_{13}|.
\]

## Normalization, deletion, and insertion notation

For a word \(w\) with distinct entries, \(\operatorname{std}(w)\) denotes
its standardization.  For \(q\in S_{2n-1}\) and \(j\in[2n]\), define
\[
 E_j(q)=(q_1+\mathbf 1_{q_1\ge j})\cdots
        (q_{2n-1}+\mathbf 1_{q_{2n-1}\ge j})j.
\]
This is the unique permutation in \(S_{2n}\) whose last entry is \(j\) and
whose first \(2n-1\) entries standardize to \(q\).  The natural candidate
map is
\[
 D:S_{2n}\to S_{2n-1},\qquad
 D(\pi)=\operatorname{std}(\pi_1\cdots\pi_{2n-1}).
\]

## Edge and degenerate cases

For \(N=1,2\), \(L_N=0\), every permutation is periodic, and hence
\(M_1=S_1\), \(M_2=S_2\).  The conjecture at \(n=1\) is therefore
\(2=2\cdot1\).  No division, limiting convention, probabilistic convention,
or floating-point comparison occurs in the statement.  Empty permutation
words above are interpreted as the unique identity of length zero.

The source paper's separate Conjecture 4.3, as printed without a lower bound
on \(N\), is not part of the endpoint and fails for \(N=3,4\) under the
published definitions (for example \(123\in M_3\) but its first entry is
less than \(2\)).  Its stated tail conditions may therefore be used only
after an independent proof in the range where they are invoked.
