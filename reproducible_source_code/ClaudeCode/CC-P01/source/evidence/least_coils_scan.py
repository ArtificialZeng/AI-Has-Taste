"""For each n, the least c for which the SAT search finds an n x n whirling tour with c coils (c from ceil(n/2) up)."""
import subprocess, sys, math
PY = sys.executable
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for n in range(lo, hi + 1):
    res = []
    for c in range(math.ceil(n / 2), n + 1):
        try:
            out = subprocess.run([PY, "whirl_sat.py", str(n), str(c), "--out", "least_found.txt"],
                                 capture_output=True, text=True, timeout=900).stdout.strip().split("\n")[-1]
        except subprocess.TimeoutExpired:
            out = "TIMEOUT"
        tag = "UNSAT1" if out.startswith("UNSAT after 1 ") else "UNSAT" if out.startswith("UNSAT") else "TIMEOUT" if out == "TIMEOUT" else "FOUND"
        res.append(f"c={c}:{tag}")
        if tag in ("FOUND", "TIMEOUT"): break
    print(f"n={n}: " + " ".join(res), flush=True)
