# Triage progress

Job: primary-20260913-level-rook-fibres-triage-4e5c62cdde68.
Date: 2026-09-13 Asia/Shanghai.

The frozen source SHA256 is
`0d9344b0f088a0d374302c97799c3d24e842950554cba9a17bc1af1702f2c20f`.
The supplied BLRS PDF hash matches its source declaration. Its printed
pages 2–5 (definitions and singleton reduction) and 21 (Section 6.2) were
inspected through pdftotext; the live arXiv HTML also contains the fibre
question. BLRS 1308.4081 Theorem 5.2 counts singleton boards in an
equivalence class, not arbitrary boards in a fibre. Barrese 1812.00533v2,
Section 3, explicitly identifies added leading zero columns.

An independently derived lead for m=2 is to write the conjugate row lengths
in pairs with prescribed sums s_i, then set d_i=floor(s_i/2)-r_(2i).
The candidate constraints are d_i>=0, d_i+d_(i+1)<=a_i for i<t,
d_t<=a_t, where a_i=floor(s_i/2)-ceil(s_(i+1)/2), s_(t+1)=0.
This needs an exact comparison with direct board enumeration and a
contribution screen beyond merely giving a dynamic program.

A live search found Jiang–Wen–Zhong, arXiv:2607.14887v1 (16 July 2026),
on alternating adjacent-sum polytopes. Its introduction and scope were
inspected. It is a concrete novelty lead for this reduction and must be
compared before advertising a new path-polytope theorem.

No candidate or resolution is asserted. The next immediate check is an
independent exact test of the m=2 reduction, including odd sums and zeros.
