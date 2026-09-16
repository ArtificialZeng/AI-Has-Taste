# Resolving the CircularShift color-update discrepancy

Primary source: Kutin--Smithline, arXiv:2408.00903v3, project copy
`evidence/external/2408.00903v3.pdf`, SHA-256
`119c0fbdcc6eb4dd2582bd7edd43539fcb7eaee7d82d70c55525bbf6c475fcdb`.
The relevant material is Definition 4.3 on PDF page 8, Figure 6 and the proof
of Lemma 4.4 on PDF page 9.

## The discrepancy

The two displayed color-update conditions in Definition 4.3 do not implement
the operational description immediately above them.  For an exact minimal
example, take the two-color secret `213-000`.  The first guess `123-000` has
feedback \(U_1=\{3\}\), so \(a_1=1,a_2=2\) and the next permutation is 213.
The displayed cyclic condition has
\(i=\gamma_2(a_1)=2\) and \(a_1\leq\gamma_2(a_1)\), so it increments the color
of rank 2 and submits `213-010`.  This conflicts with Lemma 4.4, which gives
completion time
\(1+\operatorname{exc}(213)+0=2\), and with the prose rule that a color is
incremented only after the rank has completed a circuit.

This is not merely a transcription artifact: the displayed formula is visible
in the frozen primary PDF.  Accordingly, the literal displayed cases are not
used silently in the candidate theorem.

## The intended rule determined by the same primary source

The prose before Definition 4.3 says that rank \(i\)'s color is incremented
when it loops all the way around to its starting position, namely position
\(i\) in the identity first guess.  The proof of Lemma 4.4 makes this precise.
If the active positions are
\(a_1<\cdots<a_\ell\), then for
\(i=\gamma_k(a_j)\), \(j<\ell\), it increments the color exactly when
\[
  a_j<i\leq a_{j+1}.
\]
For the cyclically moved rank \(i=\gamma_k(a_\ell)\), the proof increments
exactly in the two cases
\[
  i>a_\ell\quad\hbox{or}\quad i\leq a_1.
\]
Equivalently, when a rank moves clockwise from old position \(p\) to new
position \(q\), increment its color exactly when the circular arc \((p,q]\)
contains its identity position.  When \(p=q\), the sole active rank has made a
full circuit and the condition is true.

Figure 6 independently fixes the same interpretation.  For secret permutation
32514 with colors `11001` by rank, its six displayed guesses are

```
12345-00000
51234-00000
35124-00000
32514-01000
32154-11000
32514-11001
```

`evidence/circular_shift_sim.py` reproduces these rows before running the
48-secret census.  Thus the candidate's use of “CircularShift” means the
operational prose/proof/Figure 6 algorithm just stated, while explicitly
recording that Definition 4.3's displayed color cases contain an apparent
typographical error.
