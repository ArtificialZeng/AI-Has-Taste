# Writing checkpoint

Job provenance: `bigMac-00008-p04-write-be78bf8e176d`.

- The mathematical gate accepted the frozen `resolution-paper` claim with
  original status `proved`.
- `manuscript/main.tex` and `manuscript/references.bib` give a self-contained
  four-page article at the accepted scope.  The clean build is
  `manuscript/main.pdf`; all four rendered pages were visually inspected.
- The article cites the verified Biswas--Mandal--Phukan primary source for the
  v-number boundary and the user's verified Zeng bibliography entry only for
  the finite exact-enumeration methodology that its abstract supports.
- Obstacle handled: the root `checkpoint.md` is itself included in the frozen
  accepted evidence snapshot.  Editing its bytes after mathematical acceptance
  would invalidate that audit, so it was preserved and this phase checkpoint
  was recorded separately.

Next test: run the fresh citation, clean-build, and visual release audit against
`audit/manuscript-snapshot.json`.
