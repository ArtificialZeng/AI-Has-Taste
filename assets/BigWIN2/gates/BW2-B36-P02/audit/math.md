# Fresh mathematical referee report

**Job:** `win-00036-p02-referee-eca6e5115c71`  
**Frozen snapshot:** `2c76db1b49c79986104a8730b2aae0d1e06f5af2ca516d149b5990494f646202`  
**Verdict:** accept

## Scope reconstructed

The frozen claim is the full-scope assertion that the largest ordinary subset
of \([127]\) having no three distinct elements with all three pairwise GCDs
equal has cardinality 16. There are no additional asymptotic, classification,
or uniqueness claims. The claimed proof is direct and does not use the supplied
lead \(f_3(126)=16\).

For a subset \(A\subseteq[127]\), let \(x_i=1\) exactly when \(i\in A\). For
every unordered triple \(a<b<c\) whose three pairwise GCDs are equal, feasibility
is equivalent to the clause
\[
  \neg x_a\lor\neg x_b\lor\neg x_c.
\]
Enumerating all \(\binom{127}{3}=333{,}375\) unordered triples therefore loses
neither an ordering case nor a distinctness case. A cardinality constraint
\(\sum_{i=1}^{127}x_i\geq17\) then makes satisfiability equivalent to the
existence of a feasible set of size at least 17.

## Checks performed

1. I checked the snapshot binding. Every permitted frozen file inspected has
   the SHA-256 recorded in `audit/snapshot.json`; in particular the CNF digest
   is `8b79ee1c4a921f27dfdb7d4c6d9581ff98860b85d1caf903b5a500de6763a8c2`,
   the DRAT digest is
   `57ae38a8f6ff606ef716bdaa488cf2d93a74c35ec9e16b9437aaac587ba69718`,
   and the checker digest is
   `fc324d360828e8af40a0f48c71062eea222658c63b87912929b7d72f45751628`.
   I also recomputed the canonical snapshot digest and obtained the value above.
   The immutable `source.md` retained digest
   `58d9e80ab37de5373fdc8ddb72d7b87485b54da47ae99ce8f1d54e16b229e332`.

2. I independently enumerated the 560 unordered triples of
   \[
   \{14,20,21,24,25,30,36,40,48,63,80,90,96,98,108,125\}.
   \]
   The entries are 16 distinct integers in \([127]\), and no triple has its
   three pairwise GCDs equal. The supplied definition-level verifier returned
   the same empty bad-triple list. This establishes \(f_3(127)\geq16\).

3. A fresh definition-level enumeration found 119,176 forbidden triples. The
   audit generator rebuilt their 119,176 negative ternary clauses and the 8,890
   clauses produced by the standard totalizer call
   `CardEnc.atleast(lits=1..127, bound=17, top_id=127)`. The resulting formula
   has 1,015 variables and 128,066 clauses and agrees with `evidence/k17.cnf`
   clause-for-clause and byte-for-byte. Thus variables 1 through 127 are exactly
   the membership variables, while the remaining variables are existential
   totalizer auxiliaries. As a supplementary off-by-one check, I isolated the
   frozen totalizer clauses and fixed all 127 input variables in 384 complete
   assignments: every count 0 through 127 in each of prefix, reverse-prefix,
   and fixed shuffled orders. MiniSat 2.2 found an auxiliary extension exactly
   for counts at least 17 in all tests. The logical cardinality interpretation
   itself is the standard totalizer semantics; the finite tests are only a
   sanity check, not a substitute for that semantics.

4. I reran the frozen checker on the serialized CNF and DRAT trace. It exited
   zero with `s VERIFIED`, using 98,745,797 resolution steps in backward
   checking. Hence the exact CNF is unsatisfiable. If a feasible set of size at
   least 17 existed, its membership vector would satisfy every forbidden-triple
   clause and, by the totalizer semantics, would extend to a satisfying
   assignment of this CNF, a contradiction. Therefore \(f_3(127)\leq16\).

The lower and upper bounds give \(f_3(127)=16\). The argument also covers sets
larger than 17 because the constraint is “at least 17”; no maximality,
monotonicity, or deletion assumption is being smuggled into the certificate.
There is no empty-domain, zero-GCD, repeated-element, or equality-case gap.

## Source comparison and limitation

The only frozen literature evidence is the workbook-derived record for Zijian
Zeng, DOI `10.2139/ssrn.7395458`. Its abstract-level text uses the same
definition and states \(f_3(126)=16\); it does not mention \(N=127\). The full
paper and its certificates were not available in the frozen evidence, so its
formal definition, tables, and possible data at 127 have not been independently
checked. Accordingly, this audit does not certify priority or novelty and does
not endorse any stronger description of that paper. This is not a correctness
gap in the candidate because neither bound above cites or uses the \(N=126\)
result, and the frozen contribution expressly makes no novelty claim.

## Verdict

**Accept.** The exact frozen resolution claim is correctly represented and
certified in its full scope. The explicit witness proves the lower bound, and
the definition-equivalent CNF together with the checked DRAT refutation proves
the upper bound. The unresolved primary-source comparison must remain disclosed
in any later manuscript and cannot support a novelty claim.
