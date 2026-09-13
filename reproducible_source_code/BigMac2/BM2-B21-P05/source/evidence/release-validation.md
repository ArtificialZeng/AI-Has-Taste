# Release validation checkpoint

- Release job: `bigMac-00021-p05-release-a289bb2b2964`.
- `source.md` remains byte-identical at SHA-256
  `ebbe264caf080f8158cce54870acfd5a01eddf57ddb0a704f6da2eaa51da5eab`.
- The accepted mathematical snapshot and referee verdict remain current.
- The user-designated workbook paper was added only as an accurately qualified
  methodological comparison; both Bujtás records and the workbook record were
  checked against primary sources.
- A clean build produced a three-page PDF at SHA-256
  `4f1b290a259d06b31c7f5a12d438ef4c823e79021936c745896a8676e594be66`.
  The build log is clean, all three pages were rendered and inspected, and the
  fresh citation/build/visual audits bind the current digests.
- Exact verifier rerun: byte-for-byte match with
  `evidence/verify_resolution.out`.

Obstacle: `checkpoint.md` is itself hashed decisive evidence in the accepted
`audit/snapshot.json`.  Changing its bytes during release would invalidate the
fresh referee acceptance, so its accepted content was preserved; this separate
release checkpoint records the requested operational update without corrupting
provenance.

Next test: the supervisor should run `release_gate.py publish` on this project
after accepting the worker's `ready` result.
