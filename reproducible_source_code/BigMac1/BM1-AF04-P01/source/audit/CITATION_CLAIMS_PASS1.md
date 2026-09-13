# Citation-check pass 1: frozen claim extraction

Mode: search verification for external claims; exact-artifact verification for
new mathematical claims.  Document: `paper/main.tex`, complete draft read
before extraction.  Date: 2026-08-30 CST.

No verification was performed during this extraction pass.  The following
claim set is frozen for pass 2.

| ID | Claim | Type | Location |
|---|---|---|---|
| M01 | Krasko and Omelchenko gave/proved the displayed EGF for simple chord-labelled chord diagrams. | Attribution + existence | Abstract; Introduction, first paragraph |
| M02 | OEIS A278992 counts simple chord-labelled chord diagrams and gives the same EGF. | Attribution + existence | Introduction, first paragraph |
| M03 | On the access date, OEIS A278992 lists the displayed four-step recurrence as conjectural. | Attribution + temporal | Abstract; Introduction, first paragraph |
| M04 | The EGF coefficients satisfy the displayed recurrence for every integer n at least 4, with initial values (0,0,1,1); the OEIS-native form starts at n=5 with (0,1,1,21). | Existence + numerical | Theorem 1.1 |
| M05 | The first EGF summand satisfies the displayed second-order ODE, and G=(2-t)exp(-t) satisfies the displayed first-order ODE. | Existence | Equations (4) and (5) |
| M06 | The row identity produces the displayed third-order polynomial annihilator L3(F)=0. | Existence | Equations (6) and (7) |
| M07 | The noncommutative operator identity M composed with L3 equals L5, hence the displayed fifth-order ODE annihilates F. | Existence | Proposition 2.1 and proof |
| M08 | Exact EGF coefficient extraction from L5 gives precisely the five displayed recurrence coefficients. | Existence + numerical | Equation (10) and coefficient table |
| M09 | The formal expansion begins with coefficients a0,...,a6 = 0,0,1,1,21,168,1968. | Numerical | End of Section 3 |
| M10 | The standalone verifier reconstructs the stated exact identities, imports no discovery code, and rejects malformed or altered inputs. | Existence | Section 4, first paragraph |
| M11 | Direct symbolic differentiation returns L3(F)=L5(F)=0, and exhaustive perfect-matching enumeration gives the stated combinatorial coefficients for 1<=n<=7. | Existence + numerical | Section 4, first paragraph |
| M12 | No proof assistant was used. | Existence/negative provenance | Section 4, second paragraph |

Excluded under the skill's extraction rules: definitions, theorem-proof
methodology descriptions, scope limitations, and the AI-assistance disclosure
as a process description.  Mathematical claims M04--M11 will be checked
against exact project artifacts rather than treated as literature claims.
