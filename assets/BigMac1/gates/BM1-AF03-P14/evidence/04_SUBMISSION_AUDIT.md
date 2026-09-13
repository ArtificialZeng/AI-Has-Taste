# Submission audit

Status: **PASS — submission-ready**  
Date: 2026-08-30 (Asia/Shanghai)

## Exact and referee gates

- Terminal mathematical state: PROVED; original endpoint complete.
- Primary exact master: 23/23 PASS, exit 0; log SHA-256
  18f6a4fb55480a3d097d6b96b2d69fa7497f4e7ccf88b689083b267139de4903.
- Independent verifier: PASS on 17/17 hash-bound inputs; result SHA-256
  333821801a789688976abea57f6d76475f4b6c8eb955e4a6008ca4983289ff6b.
- Independent semantic mutations: 10/10 rejected.
- Independent parser attacks: 4/4 rejected.
- Full hostile referee: PASS, fatal/major/local/expository = 0/0/0/0.
- Release-delta machine verdict: PASS and submission_gate_delta PASS,
  fatal/major/local/expository = 0/0/0/0.
- Current paper SHA-256 1bcccfa9a6db0660c1e3d349351ad4740ea7f9ea5b90e050701c94bb7f19bd58.
  Proof and all nine decisive certificate files are unchanged.

## Citation and novelty gates

- Second database-bounded novelty search completed on 2026-08-30.
- Five citation keys reconciled against official DOI/publisher records and
  corrected primary texts: 5/5 PASS.
- Frozen claim audit: 11/11 verified, 0 unverified.
- Final build reconciliation: 5 cited keys = 5 BibTeX keys = 5 auxiliary
  bibcite keys; no missing or unused key.

## Build and PDF gates

- Two clean builds started with no auxiliary files and both converged.
- Both produced the identical 8-page PDF:
  183ff0236e53de460de80a9c97ace776aba06eb681bd79315ab344827a55d7eb.
- Final logs contain no undefined citation/reference, BibTeX omission,
  repeated entry, LaTeX error, fatal stop, undefined control sequence,
  runaway argument, multiply defined label, or overfull/underfull box.
- PDF metadata names Zijian Zeng as the sole author; all fonts are embedded.
- Pagewise rendered visual inspection: 8/8 PASS.

## Archive gates

- Clean source ZIP contains no generated PDF, LaTeX auxiliary file,
  __pycache__, or third-party source PDF.
- Internal source manifest: 101/101 PASS.
- unzip integrity test: PASS.
- Fresh extraction manifest check: 101/101 PASS.
- Clean archive rebuild: PASS; final PDF is byte-identical to the release PDF.
- PDF SHA-256:
  183ff0236e53de460de80a9c97ace776aba06eb681bd79315ab344827a55d7eb.
- Source ZIP SHA-256:
  dbbbbe24fe08d770c06f95b9b6cc3275e6eba459ce030026b043a921fb57284f.
- Archive rebuild log SHA-256:
  88f91648c89e9862423064efc99ad06d53f2fad87e1ebeda001b0bc13c552863.

## Proof-assistant disclosure

No Lean, Coq, Isabelle, Agda, or other interactive proof assistant was used.
No formalization endpoint is claimed.
