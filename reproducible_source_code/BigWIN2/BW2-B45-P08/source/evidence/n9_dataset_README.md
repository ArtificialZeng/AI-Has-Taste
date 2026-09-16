# Supervisor-staged primary data for win-00045-p08

- Official repository: `https://github.com/Leonardini/Tournaments`
- Pinned commit: `f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b`
- Repository path: `data/n9_margin1only_tournaments.rds`
- Raw URL: `https://raw.githubusercontent.com/Leonardini/Tournaments/f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b/data/n9_margin1only_tournaments.rds`
- RDS SHA-256: `f633b784eb573ab142f0f7e4c1bb9e9e97d7a0953405c28a7f0aa0a95d0115a6`
- Transparent JSON SHA-256: `2eac211945224efb485ec4dc59bde3af4ae9427fa63b34bd39e8992f2aa0ce63`
- Export script SHA-256: `88c283c38f9634e407f1490a92804d95237675e4f2dbe9ac439a1f0fa60368bf`

The export used Python 3.10.12, NumPy 2.2.6, and the project-local `rdata` 0.11.2 parser.  It verifies exactly 254 distinct `9 x 9` binary tournament adjacency matrices, zero diagonal, with each off-diagonal pair summing to one.  Research workers should consume the transparent JSON and independently recount its invariants before SAT classification.

