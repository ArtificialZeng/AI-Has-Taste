# Submission audit

Status: PASS, 2026-08-30.

- Scope: the complete fixed \(d=4\) task only; the full all-\(d\) conjecture is
  explicitly excluded.
- Mathematical claim: matches the frozen formal theorem and is proved for the
  exhaustive ranges \(1\le k\le7\) and \(k\ge8\).
- Proof dependencies: every internal lemma is proved; Solomyak's strict
  conjugate bound is cited to its primary publisher record.
- Exactness: all decisive finite checks use integers/rationals; neither
  verifier imports floating-point discovery output.
- Independent verification: standard-library rational-interval and
  SymPy/Sturm implementations both pass; the archive repeats both checks.
- Literature: pre-result and post-result primary-source/fingerprint searches
  are logged through 2026-08-30; novelty is stated only as exact certification
  of previously reported computational evidence.
- Authorship: Zijian Zeng; Institute of Computer Science and Digital
  Innovation, UCSI University, Kuala Lumpur 56000, Malaysia; both requested
  email addresses are present.
- Disclosure: the manuscript accurately reports the role of generative AI and
  distinguishes exploration from the exact proof and certificate.
- Reproducibility: source, bibliography, exact JSON certificate, two verifiers,
  and build instructions are included in the LaTeX ZIP.
- PDF: final metadata, fonts, extracted text, citations, and all seven rendered
  pages pass `audit/PDF_AUDIT.md`.
- Prohibited manuscript content: no SHA-256 value, internal route/role ID,
  completion/confidence field, or internal audit phrasing occurs in the PDF.

Verdict: the fixed-case manuscript and its exact certificate satisfy the
mathematical, citation, bounded-novelty, reproducibility, PDF, and packaging
gates for submission.
