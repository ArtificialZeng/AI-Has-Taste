#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Export the numerically selected d=6 square basis as exact integers."""

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mixed_lp_search import build


def main() -> None:
    basis = np.load("evidence/mixed_d6_basis_rows.npz")
    support = [int(x) for x in basis["support"]]
    selected_rows = [int(x) for x in basis["rows"]]
    _, _, rows, _, _, _, _, _ = build(6)
    lines = [f"{len(support)} {len(support)}"]
    for row_index in selected_rows:
        _, coefficients, rhs = rows[row_index]
        lines.append(" ".join(str(coefficients.get(j, 0)) for j in support))
        lines.append(str(rhs))
    Path("evidence/mixed_d6_basis_matrix.txt").write_text("\n".join(lines) + "\n")
    print({"dimension": len(support), "rows": len(selected_rows)})


if __name__ == "__main__":
    main()
