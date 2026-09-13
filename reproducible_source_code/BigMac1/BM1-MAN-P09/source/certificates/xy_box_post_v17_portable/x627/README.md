# Portable certificate: 313/500 <= x <= 627/1000

This directory is a parallel, package-local replay layer for the first
post-v17 adjacent cell.  It does not rewrite historical logs and does not
claim that the historical source/referee manifests are transitively
replayable.  Those manifests remain opaque provenance anchors.

The unchanged source and independent-referee programs are executed from the
package-local `certificate_workspace` with relative script paths.  Fresh
normal and fail-closed outputs are stored below `source/` and `referee/`.
The portable manifests bind the actual proof inputs and these fresh outputs.

Historical anchors:

- source manifest: `2ce9ef8ed0dface0c00328a65be9dc7c4c4a1f7c8cfb1053ac21ea96967ff15a`
- referee manifest: `089306b1a1bc5cb7e07f4638dcf3f29c25ae377ae4a9034d1b631f9173f5bef3`

The theorem scope remains exactly the audited local cell, with both signed-z
lifts and all stated positive scales.  No full compact-ball claim is made.
