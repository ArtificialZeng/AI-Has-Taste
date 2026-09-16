# Bounded primary-literature and status check

Date: 2026-09-10 (Asia/Shanghai)  
Job: `win-00086-p05-research-236d0a28a39b`

- The official arXiv record for Zhiwen He and Jiayan Wu,
  *Nonexistence Results and Constructions for Signed Difference Sets*,
  <https://arxiv.org/abs/2608.22936>, was inspected live. It listed only v1,
  submitted 2026-08-24. Its definition (1.1), principal equation (2.3), and
  character equation (2.4)/Lemma 2.1 agree with the frozen problem. Its
  conclusion reports the four broad nonexistence criteria and three settled
  construction cases, and leaves further open cases; it does not state the
  present `SDS(9,8,1,C_3^2)` resolution.
- The authors' official repository
  <https://github.com/zhiwenhe94/sds-open-case-verification> was inspected
  live. The current page showed four commits and described `sds.json` as the
  fixed database snapshot used in the paper; its README defines `Open` as
  unresolved. The 4.95 MB JSON could not be rendered or fetched through the
  available interfaces, so the exact row was not re-extracted in this pass.
  The immutable `source.md` records that row as `Open` at commit
  `de57332884c7bf417544285dee9a2cbb015a5fae`.
- Exact-title, exact-parameter, equivalent-notation, arXiv, and official
  repository searches found no later primary paper or database update that
  states this resolution. This is a bounded literature screen, not a claim
  of priority or proof that no such source exists.

No local primary-source PDF or text is identified or present in the project;
the complete mathematical proof in `evidence/research-proof-audit.md` derives
the character condition directly and does not rely on an uncopied external
theorem.
