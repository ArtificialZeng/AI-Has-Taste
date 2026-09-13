# Final manuscript hash referee

Date: 2026-08-29  
Role: independent read-only mathematical referee  
Final manuscript: 'paper/main.tex'  
Final SHA-256:
d55cdd3cd7a6785bbacdb23b3817868af0ca973651532ed8aa5da0d26d163b11

## Verdict

**PASS.** No fatal or major issue was found. One local omission in the
first snapshot was repaired and independently checked by hash-preserving
reverse reconstruction.

## Adversarial checks

1. Ambient \(\mathbb R^{11}\) versus \(V=\mathbf1^\perp\) kernels, nullities,
   and ranks are used correctly.
2. The one-gap Naimark boundary and singleton-compression case \(|Z|=1\)
   are explicit and correct.
3. Potentially negative \(c_r\) are not excluded prematurely. In the
   \(R=10\) branch, the proof first obtains every \(c_p>0\) from the
   off-diagonal design identity and \(g_a>0\), and only then applies
   Sherman--Morrison.
4. Complement orientation sends two cuts from a chain to nested or disjoint
   blocks in all three positions of the reference label.
5. Repeated/complement cuts and repeated singleton labels create no
   cancellation or hidden distinct-label assumption; singleton coefficients
   are aggregated in \(\alpha_r\), while endpoint counts are by copy.
6. Strict and non-strict endpoint-deficit inequalities are accumulated with
   their correct signs, including both non-strict \(\ell=2\) cases.
7. The finite enumeration is presented as exact rational finite checking,
   not numerical sampling, and the stated conclusion \(t\ge19\) follows.

## Repaired boundary

The first audited snapshot, SHA-256
0fe1ce96a22ba779d72327e7d56bc612cfe992c62d822e00488546a68836b235,
did not explicitly say why \(Z=[11]\) is impossible before orienting cuts
into \(W=[11]\setminus Z\). The final manuscript adds the exact argument:
constancy on all eleven labels would make every remaining cut empty or full,
contradicting \(R\ge1\) and properness. The referee removed that sentence
in memory and reconstructed the old hash exactly, proving it was the only
change. The final hash above received PASS.

The referee also independently reran the exact \(t=15,16,17,18\) referee
checkers from '/tmp' with Homebrew Python 3.14.7 under '-O -I'; every process
exited zero and reported PASS with matching frozen proof hashes.

The referee supports release of the support-\(19\) **partial theorem**.
Kusner's original \(n=5\) problem remains open.

## Final layout-only delta

Immediately before release, the source received exactly three nonmathematical
changes: removal of the global '\\emergencystretch=2em', an unambiguous PDF
metadata title using “five-dimensional ell-one,” and a local shortening of
the AI-disclosure paragraph that had produced a 14.97638 pt overfull box.
The independent referee reversed those three edits in memory and recovered
the preceding audited SHA-256
'966399c07fcd415707b2b20be50d16fa88c1ac69408cebb56e6d156a8d0ae923'
exactly. The mathematical statements, proof, limitations, and citations are
unchanged. The manuscript neither cites nor incorporates the unaudited file
'proof/t19_branch.md'. The final hash printed above received **PASS**.
