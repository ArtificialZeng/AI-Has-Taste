# Literature and dedup screening

Job: primary-20260913-subtree-annulus-triage-1ad02ce248b4.
Retrieval/inspection date: 2026-09-13 +08 (2026-09-12 UTC).

1. Brown and Mol, On the roots of the subtree polynomial, arXiv:1810.08655v1:
   https://arxiv.org/pdf/1810.08655v1 . Live PDF access succeeded. Read physical
   pp.1–3 (definitions, path/star formulas, forest and rooted recursions), p.4
   Lemma 2.1 (radial local bound), and p.14 Conjecture 4.2. The target agrees
   exactly with the source reading; n<=18 is the authors' prior report.
   Local original capture: brown-mol-1810.08655v1.pdf, SHA256 verified against
   the supplied intake hash; derivative plain text has the matching basename.
2. Jin, Ma and Wang, A proof of a conjecture on subtree roots,
   https://arxiv.org/html/2608.07898v1 . Live access succeeded; local original
   HTML hash verified. Read introduction, Sections 2–3 (fixed-modulus recursive
   comparison), and Section 5. Theorem 1.3 is the radial upper bound and
   Conjecture 5.1 is the shifted annulus. The paper's method bounds moduli of
   local polynomials using |z|>=2, so these estimates do not directly furnish
   the shifted disk's geometry. Section 4's short radial lower-bound argument
   was inspected but is not used as a proof of shifted inner exclusion.
3. CURRENT VERSION CORRECTION: the live abstract
   https://arxiv.org/abs/2608.07898 records v2, 14 August 2026, with new title
   Proof of a Brown-Mol conjecture on subtree roots. Read v2 Theorem 1.3 and
   the Section 3 equality argument, plus Section 5 Conjecture 5.1 at
   https://arxiv.org/html/2608.07898v2 . The radial equality classification is
   already known there: equality precisely for even-order stars, with unique
   boundary root -1-(n-1)^(1/(n-1)). The stronger shifted annulus is STILL a
   conjecture in v2. This newer version was absent from the supplied packet;
   do not propose radial equality classification as a novel delta. A saved
   live tool-rendered capture, including Sections 3–5 and source URL, is
   jmw-v2-live-web.txt. It is labelled as a rendered capture, not original HTML.

Bounded live searches used: subtree roots annulus Brown Mol conjecture 2026;
subtree polynomial Hurwitz; subtree roots double star; subtree Conjecture 4.2
proof; subtree polynomial double roots; subtree roots diameter; subtree annulus
double; node reliability trees Hurwitz. Search results were mostly irrelevant
or derivative; they are leads, not mathematical evidence. No equivalent
all-double-star shifted-annulus result was found in the inspected primary
sources. This is a limited negative search, not a priority claim. The native
source's relation to connected-set/node-reliability polynomials remains a
useful equivalent-language lead for a later focused novelty check.

Source classification: open-supported. No prior full resolution was found.
Suitability: advance the explicit natural double-star family, with the scalar
estimate in structural-test.md, for a bounded research verification pass.

Dedup: parsed 639 current native registry rows read-only; the only match to
subtree|Brown.{0,20}Mol|annulus|子树 was this intake. Inspected three native
neighbor records: win-00063-p04 and win-00075-p07 concern independence roots;
win-00085-p10 concerns domination coefficients. Their counted vertex sets and
targets differ, so their results do not settle this problem. The two smallmac
neighbors and the 2883-row Excel screen remain supervisor-supplied information
from admission.md; that full corpus comparison was not independently repeated.
The evidence and limits are in registry-screen.json. No project-local
literature/*handoff*.md existed at enumeration. The separately supplied
admission packet was read and copied, and its v1-only boundary was corrected
against live evidence. The designated conversation remains unchecked.
