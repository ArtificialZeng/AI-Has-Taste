# Citation-check pass 1: fixed claim set (revision 2)

Mode: search verification.  Source document: `paper/main.tex`.  Extraction
date: 2026-08-30.  Revision 2 was made before Pass 2 because the manuscript
gained two structural-reduction paragraphs.  This file now freezes the claim
set before any claim-by-claim verification.  Definitions, proofs stated as
arguments, hypotheses, questions, and explicitly delimited limitations are
excluded under the skill rules.

[C01] | "Yuster conjectured the displayed exact formula for `nu_3(n)`." | Attribution + existence | Introduction, paragraph 1

[C02] | "Yuster verified the conjecture for every `n <= 8`." | Attribution + statistic | Introduction, paragraph 1

[C03] | "Yuster's `n=8` verification was computational." | Attribution | Introduction, paragraph 1

[C04] | "Kabiya and Yuster proved `nu_3(n) >= (41/300)n^2(1-o(1))` using a fractional relaxation." | Attribution + statistic | Introduction, paragraph 1

[C05] | "A 2026 public computational note determined `nu_3(9)=9` and `nu_3(10)=12` by exhaustive canonical enumeration with checkable artifacts." | Attribution + temporal + statistics | Introduction, paragraph 2

[C06] | "Every tournament of order 11 has 15 pairwise arc-disjoint transitive triples, while one has no packing of size 16; hence `nu_3(11)=15`." | Existence + statistics | Theorem 1.1

[C07] | "Yuster's cyclic three-part construction specializes at part sizes `4,4,3` to an upper bound of 15." | Attribution + statistics | Section 3, paragraphs 1--2

[C08] | "The displayed 55-bit tournament and fifteen listed triples are a literal minimizer certificate." | Existence + statistics | Section 3, paragraphs 3--4

[C09] | "The literal minimizer has exactly 117 transitive triples, all hit by its 15 within-part pairs." | Statistics | Section 3, final paragraph

[C10] | "The computation used `gentourng` from nauty 2.9.3 and split the order-11 enumeration into 192 residues." | Existence + statistics | Section 4.1

[C11] | "McKay and Piperno describe the nauty framework and its canonical-labeling methods." | Attribution | Section 4.1

[C12] | "OEIS A000568 records the known numbers of unlabeled tournaments." | Attribution + existence | Section 4.1

[C13] | "Exact evaluation of Davis's formula gives `a(11)=903,753,248`." | Attribution + statistic | Section 4.1

[C14] | "The 192 generated order-11 slice counts sum exactly to 903,753,248." | Statistics | Section 4.1

[C15] | "The Builder accepted every one of the 903,753,248 canonical order-11 representatives." | Statistics + existence | Proposition 4.3

[C16] | "The independent Certifier accepted every one of the 903,753,248 canonical order-11 representatives." | Statistics + existence | Proposition 4.3

[C17] | "For each of the 192 residues, Builder and Certifier processed equal counts and produced equal SHA-256 digests of regenerated tournament streams." | Comparative + statistics | Proposition 4.3

[C18] | "Builder and Certifier executable SHA-256 digests are different." | Comparative | Section 4.4

[C19] | "The unlabeled tournament class counts for orders 3 through 11 are respectively `2, 4, 12, 56, 456, 6,880, 191,536, 9,733,056, 903,753,248`." | Statistics | Section 5, table

[C20] | "Both local programs reproduced the published `n=9,10` finite baseline." | Comparative + statistics | Section 5, paragraph after table

[C21] | "The Breaker tested all 32 stated cyclic `4+4+3` blow-ups and 100,000 deterministic random labeled tournaments with seed 20260830, finding no below-target case." | Statistics + existence | Section 5, paragraph 2

[C22] | "A full exact maximum search on the displayed minimizer returned 15." | Statistic | Section 5, paragraph 2

[C23] | "Twenty-one deliberate corruptions were all rejected by the fail-closed tests." | Statistic | Section 5, paragraph 3

[C24] | "The decisive environment was macOS 26.5 arm64, nauty 2.9.3, Apple clang 21.0.0, and CPython 3.14.7." | Existence + statistics | Section 6, paragraph 3

[C25] | "Individual per-class packing witnesses are not stored; independent verification regenerates all canonical inputs and reruns a different exact procedure." | Existence | Data, code, and computational disclosure

[C26] | "The work was carried out in one OpenAI Codex CLI research session, with no subagents, and the four roles were performed serially." | Existence | Data, code, and computational disclosure

[C27] | "No floating-point computation, optimizer, SAT solver, or proof assistant is used in the decisive lower-bound computation." | Existence | Abstract and Section 6

[C28] | "The named author is solely responsible for the mathematical claims and release decision." | Existence | Data, code, and computational disclosure

[C29] | "For a maximal packing, every triangle of the unused-pair graph is cyclic, so that leave graph is `K_4`-free; a size-`q` packing at order 11 leaves `55-3q` edges." | Statistics + existence | Section 2, structural-reduction paragraph 1

[C30] | "A 12-packing in `T-v` extends by three triples through `v` exactly when its `v`-admissible leave graph has a 3-matching; nine leave edges alone do not force such a matching." | Existence + statistic | Section 2, structural-reduction paragraph 2

Extraction status: **FIXED**.  Pass 2 must use exactly C01--C30 and must not
add claims during verification.
