# Static release freeze audit

**Status:** PASS.

The release uses the two explicit whitelists under `release/frozen/`.  No
directory traversal or broad recursive scan is permitted.  The source
whitelist contains only manuscript sources, formal statements, proof notes,
exact certificates, verification programs and raw results, literature
records, audits, and the whitelist tooling itself.  The manifest whitelist
adds only the final PDF and final source ZIP.

The builders fail closed on `logs`, `tmp`, `build`, caches, bytecode, TeX
auxiliaries, symlinks, absolute paths, and parent traversal.  Live status files
are excluded to avoid self-referential hashes, as explained in
`release/frozen/README.md`.

Final acceptance requires:

1. both whitelist files are sorted, duplicate-free, and contain no forbidden
   path;
2. `unzip -t` passes and `unzip -Z1` contains no forbidden entry;
3. all four released theorem verifiers pass in normal and optimized isolated
   Python from a clean extraction;
4. the primary fail-closed harness passes from the clean extraction;
5. the LaTeX citation audit reports `cited=4 bib=4 missing=0 unused=0`;
6. the frozen-manifest verifier and the skill's independent generic manifest
   verifier both pass;
7. the final PDF remains byte-identical to the visually inspected five-page
   artifact with SHA-256
   `29d3ce3524c49628d613a749d5c05673eb47b8c69749107f74e8dc8efccce83b`.

No proof assistant is used.

## Exact replay result

The whitelist-built ZIP contains 41 entries.  Both `unzip -t` and an exact
member-name scan passed; the latter found zero entries under `logs/`, `tmp/`,
`build/`, caches, or bytecode, and zero TeX auxiliary suffixes.

From a newly created extraction directory, without importing project-worktree
code, the following four verifiers each passed in normal and `-O -I` modes:

1. `certificates/verify_builder_construction.py --max-n 10000`;
2. `verifier/verify_zero_set.py verifier/certificate.json`;
3. `verification/primary_verify.py certificates/zero_set_certificate.json`;
4. `verification/verify_transfer_automata.py certificates/transfer_automata_certificate.json`.

The builder, primary, and transfer outputs were byte-identical between modes;
the independent verifier printed its PASS header in both modes.  The primary
fail-closed harness was also run normally and under `-O -I` from the
extraction; both result files reported PASS with empty
`unmet_expectations` and `remaining_vulnerabilities`.

The LaTeX audit run against the extracted `paper/main.tex` and
`paper/references.bib` reported
`cited=4 bib=4 missing=0 unused=0`.  The static manifest then contained
exactly the 43 paths in `manifest_whitelist.txt`; both the fail-closed static
verifier and the skill's separate generic manifest verifier passed.

The release was rebuilt once more after this audit text and the gap ledger
were finalized, and the same clean-extraction and manifest tests were repeated
before the external live status files were returned to `PROVED`.
