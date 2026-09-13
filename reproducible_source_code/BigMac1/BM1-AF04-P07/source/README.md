# Certified finite determination of `nu_3(11)`

The result of this project is

```text
nu_3(11) = 15.
```

The lower bound is a complete canonical enumeration of all 903,753,248
order-11 tournament isomorphism classes.  Two independently written exact
integer programs use different formulations (pair-resource branching and
compatibility-graph clique search) and accept every class.  Their 192 residue
counts and regenerated input-stream SHA-256 values match exactly.  The upper
bound is a human-readable cyclic `4+4+3` construction with a literal
15-packing and an independent no-search verifier.

Start with:

- `FINAL_STATUS.md` for the terminal classification, limitations, hashes,
  audit outcome, and replay commands;
- `paper/main.tex` and `output/pdf/nu3_11_certified.pdf` for the manuscript;
- `problem/formal_statement.md` for exact definitions and quantifiers;
- `proof/proof_dag.md` and `audit/PROOF_AUDIT.md` for the proof dependency and
  referee reconstruction;
- `certificates/README.md` and `certificates/n11_sweeps_match.json` for the
  certificate chain;
- `code/README.md` for implementation and replay details;
- `literature/` and `audit/CITATION_VERIFICATION.md` for novelty and citation
  gates.

The terminal classification is `CERTIFIED_FINITE_RESULT`.  The substantive
declared external trust assumption is the correctness and completeness of
nauty 2.9.3 `gentourng` canonical generation.  Count equality alone is not
misrepresented as a proof of that implementation contract.  No floating
point, optimizer, SAT solver, or proof assistant is used in the decisive
lower-bound computation.
