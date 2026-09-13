# Final status: PROVED

Date: 2026-08-29 (Asia/Shanghai)

## Conclusion

For every word \(u\in\{1,2,3\}^*\) containing each of \(1,2,3\), every finite
word \(w\) on the positive integers (including \(w=\varepsilon\)), and every
integer \(k\geq3\),

\[
u^k w\equiv w u^k
\quad\Longleftrightarrow\quad
u^3 w\equiv w u^3.
\]

Equivalently, \(C(u^k)=C(u^3)\) for all \(k\geq3\).  Thus every 3-packed word
is 3-stable.

The prompt's source number is corrected: packed stability is Conjecture 3.8
in the locally archived Sagan--Zhao source; Conjecture 4.6 there is a
log-concavity conjecture.

## Proof and independent audit

The rank-three theorem uses the faithful Cain--Klein--Kubat--Malheiro--Okniński
tropical embedding.  Interval-subsequence matrices lie in an exact cone; the
power formula and adjacent commutation conditions reduce the corner equality
to all thirteen weak diagonal orders, with every transient term removed by
explicit inequalities.  A column-factor tail-isolation lemma then lifts the
rank-three statement to arbitrary positive-letter witnesses once \(u^k\)
contains the decreasing subsequence 321, which holds for \(k\geq3\).

The user-requested G02 branch is also complete: all rank-three SSYT are uniquely
parametrized by feasible sextuples, the row word is proved directly, and each
of the six insertion batches gives the stated coordinate product formula by
literal row-insertion induction.

audit/FULL_DAG_REFEREE.md reconstructs D0--D22 and G1--G9 independently.  It
reports fatal=0 and major=0, and the same referee gives a written hash-bound
post-repair PASS for the manuscript and proof snapshot.  The raw-RSK and finite
enumerations are adversarial diagnostics only; no computation is used as a
proof step.

## Limitations and provenance

- The novelty conclusion is dated and bounded by the providers and queries in
  literature/search_log.md; it is not a proof that no unindexed solution
  exists.
- The independent referee reports are rigorous project audits, not external
  journal peer review and not a promise of acceptance.
- No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization
  claim is made.
- Z3 and exact finite enumeration were used only for discovery and diagnostics.

## Release artifacts and gates

- manuscript source: paper/main.tex, paper/references.bib, paper/main.bbl;
- final PDF: output/pdf/Stability_of_3-Packed_Words.pdf;
- source ZIP: output/source/Stability_of_3-Packed_Words-source.zip;
- final manifest: manifests/release.json;
- proof audit: audit/FULL_DAG_REFEREE.md;
- citation/build audit: audit/CITATION_AUDIT.md;
- pagewise PDF audit: audit/PDF_AUDIT.md;
- independent ZIP rebuild: audit/SOURCE_AUDIT.md.

The final PDF SHA-256 is
1d634d4f8dadcafbb491e2a05e8dfaf612c609999cced9b3d6ec188db9fb0f17.
The source ZIP SHA-256 is
54cfa052462a4d963817592af0e499ed0d07f09cf1ddf5682b2d42df11e837ed.

## Reproduction

From the project root:

    cd paper
    latexmk -C
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

    cd ../experiments/breaker
    make test

    cd ../..
    python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
      . manifests/release.json

The active append-only session log under logs/ is intentionally excluded from
the release manifest; every mathematical, code, certificate, audit, LaTeX,
PDF, and source-ZIP artifact is bound.
