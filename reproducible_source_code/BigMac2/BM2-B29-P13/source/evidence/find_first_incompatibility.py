#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Find the first locally feasible, nonextendible survivor family exactly."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from prop36_generator import generate_survivors, mask_digest, mask_to_set
from theorem30_csp import (
    build_instance,
    instance_record,
    irreducible_unsat_core,
    is_local,
    solve,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=80)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    source = root / "source.md"
    expected_source = "a4e8a9bb1fdaa7a9e9b0266a518a1ee0d134f343adf5c7f056e20034d68aa67e"
    if sha256(source) != expected_source:
        raise RuntimeError("source.md hash mismatch")

    transcript: dict[str, object] = {
        "method": {
            "generator": "Proposition 36 bit-set union recurrence",
            "csp": "direct Omega/domain and omitted-point clause backtracking",
            "arithmetic": "exact Python integers only",
        },
        "source_sha256": expected_source,
        "searched_n": [],
        "first_layer": None,
    }

    for n in range(1, args.max_n + 1):
        survivors, stages = generate_survivors(n)
        exceptions = []
        local_count = 0
        extendible_count = 0
        extendible_masks: list[int] = []
        local_masks: list[int] = []
        for mask in sorted(survivors):
            a_values = mask_to_set(mask, n)
            instance = build_instance(n, a_values)
            local = is_local(instance)
            sat, model, tree = solve(instance)
            if sat:
                extendible_count += 1
                extendible_masks.append(mask)
            if local:
                local_count += 1
                local_masks.append(mask)
            if local and not sat:
                core = irreducible_unsat_core(instance)
                core_sat, _, core_tree = solve(instance, core)
                assert not core_sat
                record = instance_record(instance)
                record.update(
                    {
                        "survivor_mask_hex": f"{mask:x}",
                        "irreducible_core": list(core),
                        "core_clauses": {
                            str(m): record["clauses"][str(m)] for m in core
                        },
                        "unsat_tree": tree,
                        "core_unsat_tree": core_tree,
                    }
                )
                exceptions.append(record)
        layer = {
            "n": n,
            "N": len(survivors),
            "survivor_sha256": mask_digest(survivors),
            "survivor_masks_hex": [f"{mask:x}" for mask in sorted(survivors)],
            "extendible_count_csp": extendible_count,
            "extendible_survivor_masks_hex": [f"{mask:x}" for mask in extendible_masks],
            "local_count": local_count,
            "local_survivor_masks_hex": [f"{mask:x}" for mask in local_masks],
            "exception_count": len(exceptions),
            "prop36_stages": stages,
        }
        transcript["searched_n"].append(layer)
        print(
            f"n={n} N={len(survivors)} E_csp={extendible_count} "
            f"L={local_count} G={len(exceptions)}",
            flush=True,
        )
        if exceptions:
            transcript["first_layer"] = {"n": n, "exceptions": exceptions}
            # Independent consistency check from Definition 26/Theorem 27:
            next_survivors, _ = generate_survivors(n + 1)
            x_new_bit = 1 << n
            extendible_by_next = {
                mask
                for mask in survivors
                if (mask | x_new_bit) in next_survivors
            }
            transcript["first_layer"]["definition26_crosscheck"] = {
                "next_N": len(next_survivors),
                "csp_extendible_count": extendible_count,
                "next_layer_extendible_count": len(extendible_by_next),
                "sets_agree": len(extendible_by_next) == extendible_count
                and all(
                    solve(build_instance(n, mask_to_set(mask, n)))[0]
                    == (mask in extendible_by_next)
                    for mask in survivors
                ),
            }
            break

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(transcript, indent=2, sort_keys=True) + "\n")
    if transcript["first_layer"] is None:
        raise SystemExit(f"no exception found through n={args.max_n}")


if __name__ == "__main__":
    main()
