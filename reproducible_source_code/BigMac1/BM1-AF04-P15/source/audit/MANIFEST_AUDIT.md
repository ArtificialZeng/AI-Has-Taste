# Release manifest audit

The release manifest is generated from a byte-for-byte staging copy of the
workspace with relative paths preserved. The following nonrelease state is
excluded:

- logs/, because the batch scheduler appends to its active session log after
  every command;
- manifests/release_manifest.json, because a manifest cannot contain its own
  final hash;
- transient cache and rendered-review directories.

The staging copy includes the formal and source statements, literature and
claim ledgers, proof and gap ledgers, route registry, source code, discovery
records, exact certificates, independent verifiers, tests, serial role
audits, final status, manuscript source, final PDF, source ZIP, and
reproduction notes.

After generation, the standard skill verifier is run against the real
workspace root. It must report no missing, changed, or size-mismatched file.
Unrecorded extra files do not affect verification.
