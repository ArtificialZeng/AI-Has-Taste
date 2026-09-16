# win-00065-p01 — Exact preperiod on an even-parameter subtraction-game boundary family

For every integer `K>=1`, put `c=10K+1`, `S_K={4,6,c}`, and let `G_{S_K}` be the Sprague–Grundy sequence under exactly the conventions of Grossman, arXiv:2609.05358v1. Prove or disprove:

> The least preperiod of `G_{S_K}` is `q=20K+7=2c+5`, and its least eventual period is `p=5`.

The family has `0<a<b<c`, `a=4>=2`, `gcd(4,6,c)=1`, is non-additive, and has angle `rho=c mod(a+b)=1`. It lies in the non-admissible necessity gap of Conjecture 50 for `a<b<2a`; the source's cited ultimately-bipartite family covers odd `a`, not this even boundary. Exact screening for `1<=K<=25` found the displayed `(q,p)`, but that discovery range is not evidence for the universal quantifier. A proof must give a uniform SG-word/recurrence argument and certify minimality of both `q` and `p`; a disproof must return the least `K` found and an exact replayable sequence certificate.

Primary evidence: `batches/inbox/bigWin-65-materials/2609.05358.pdf`, SHA-256 `39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`, especially Theorem 32/Table 1 on PDF pp.21–22 and Conjectures 50, 54 and 55 on PDF pp.33–35.
