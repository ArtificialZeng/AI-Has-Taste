# Frozen release policy

The source ZIP and release manifest are built from explicit, sorted static
whitelists.  Directory scans are forbidden for the final release.

- `source_whitelist.txt` is the complete source-ZIP payload.
- `manifest_whitelist.txt` is the complete signed release payload and adds only
  the final PDF and final source ZIP.
- `build_source_zip.py` creates a deterministic ZIP with fixed member
  timestamps and permissions.
- `make_static_manifest.py` hashes exactly the manifest whitelist.
- `verify_static_manifest.py` requires exact equality between the whitelist
  and manifest key set before checking every size and SHA-256.

Both builders reject `logs`, `tmp`, build directories, caches, bytecode, TeX
auxiliary files, symlinks, absolute paths, and parent traversal.

`TASK_STATUS.json`, `FINAL_STATUS.md`, and `research_state.json` are live
control-plane metadata and are deliberately outside both frozen payloads.
This avoids an impossible self-reference: those status files must record the
final ZIP and manifest hashes, so including them inside either hashed object
would change the hashes they record.

Reproduction from the project root:

```bash
python3 release/frozen/build_source_zip.py . \
  release/frozen/source_whitelist.txt \
  output/source/a383733_zero_set_sources.zip
python3 release/frozen/make_static_manifest.py . \
  release/frozen/manifest_whitelist.txt release/manifest.json \
  --label A383733-zero-set-PROVED-static-2026-08-29
python3 release/frozen/verify_static_manifest.py . \
  release/frozen/manifest_whitelist.txt release/manifest.json
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  . release/manifest.json
```
