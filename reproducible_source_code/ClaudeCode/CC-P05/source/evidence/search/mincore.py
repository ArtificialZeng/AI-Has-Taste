from classes import feasible, classes, rep
Q = list(range(21))
# try removing the classes far from the corners first (higher index = closer to the centre in our numbering)
for c in sorted(range(21), reverse=True):
    if c not in Q: continue
    trial = [d for d in Q if d != c]
    st = feasible(trial, 120)
    print(f"without class {c} ({rep(classes[c])}): {st}", flush=True)
    if st == "INFEASIBLE": Q = trial
print("minimal infeasible set:", [(c, rep(classes[c])) for c in Q], flush=True)
