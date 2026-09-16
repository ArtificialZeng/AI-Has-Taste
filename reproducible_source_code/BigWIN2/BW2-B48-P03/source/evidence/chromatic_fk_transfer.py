#!/usr/bin/env python3
"""Full chromatic polynomial of a grid strip by an FK connectivity transfer.

This implementation does not use deletion--contraction.  It evaluates

    chi_G(q) = sum_{A subseteq E} (-1)^|A| q^k(A)

by introducing vertices and edges in column-major order and retaining only the
connectivity partition of the live frontier.  Coefficients are exact integers.
"""

from collections import defaultdict
import argparse


def grid_edges(rows, cols):
    edges = []
    for c in range(cols):
        for r in range(rows - 1):
            edges.append((c * rows + r, c * rows + r + 1))
    for c in range(cols - 1):
        for r in range(rows):
            edges.append((c * rows + r, (c + 1) * rows + r))
    return sorted(edges)


def normalize(labels):
    rename = {}
    out = []
    for x in labels:
        if x not in rename:
            rename[x] = len(rename)
        out.append(rename[x])
    return tuple(out)


def merge(labels, i, j):
    a, b = labels[i], labels[j]
    if a == b:
        return labels
    return normalize(tuple(a if x == b else x for x in labels))


def add_poly(dst, src, scale=1):
    for i, x in enumerate(src):
        dst[i] += scale * x


def times_q(poly):
    return [0] + poly


def chromatic_polynomial(rows, cols):
    n = rows * cols
    edges = grid_edges(rows, cols)
    earlier = [[] for _ in range(n)]
    last = list(range(n))
    for u, v in edges:
        earlier[v].append(u)
        last[u] = max(last[u], v)
        last[v] = max(last[v], u)

    # At each stage all states have the same ordered tuple `active`.
    active = []
    states = {(): [1]}
    max_state_count = 1
    for v in range(n):
        active.append(v)
        states = {labels + (max(labels, default=-1) + 1,): p
                  for labels, p in states.items()}

        # For each newly available edge, exclude it or include it.  Inclusion
        # has FK weight -1 and merges the endpoint components.
        for u in earlier[v]:
            ui, vi = active.index(u), active.index(v)
            nxt = {}
            for labels, poly in states.items():
                for newlabels, sign in ((labels, 1), (merge(labels, ui, vi), -1)):
                    if newlabels not in nxt:
                        nxt[newlabels] = [0] * len(poly)
                    add_poly(nxt[newlabels], poly, sign)
            states = {s: p for s, p in nxt.items() if any(p)}

        # Close vertices with no incident edge reaching a later vertex.  A q
        # factor is emitted exactly when the last live vertex of a component
        # is forgotten.
        for u in list(active):
            if last[u] <= v:
                i = active.index(u)
                nxt = {}
                for labels, poly in states.items():
                    closes = labels.count(labels[i]) == 1
                    newlabels = normalize(labels[:i] + labels[i + 1:])
                    outpoly = times_q(poly) if closes else poly
                    if newlabels not in nxt:
                        nxt[newlabels] = [0] * len(outpoly)
                    if len(nxt[newlabels]) < len(outpoly):
                        nxt[newlabels] += [0] * (len(outpoly) - len(nxt[newlabels]))
                    add_poly(nxt[newlabels], outpoly)
                states = {s: p for s, p in nxt.items() if any(p)}
                active.pop(i)
        max_state_count = max(max_state_count, len(states))

    assert active == [] and list(states) == [()]
    coeff = states[()]
    coeff += [0] * (n + 1 - len(coeff))
    assert len(coeff) == n + 1
    return coeff, edges, max_state_count


def eval_poly(coeff, q):
    ans = 0
    for a in reversed(coeff):
        ans = ans * q + a
    return ans


def format_poly(coeff):
    terms = []
    for degree in range(len(coeff) - 1, -1, -1):
        a = coeff[degree]
        if not a:
            continue
        sign = "+" if a > 0 else "-"
        mag = abs(a)
        if degree == 0:
            body = str(mag)
        elif degree == 1:
            body = ("" if mag == 1 else str(mag) + "*") + "q"
        else:
            body = ("" if mag == 1 else str(mag) + "*") + f"q^{degree}"
        terms.append((sign, body))
    if not terms:
        return "0"
    sign, body = terms[0]
    text = ("-" if sign == "-" else "") + body
    for sign, body in terms[1:]:
        text += f" {sign} {body}"
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--cols", type=int, default=9)
    args = ap.parse_args()
    coeff, edges, max_states = chromatic_polynomial(args.rows, args.cols)
    value = eval_poly(coeff, -1)
    ao = (-1) ** (args.rows * args.cols) * value
    print(f"graph=P_{args.rows} square P_{args.cols}")
    print(f"vertices={args.rows * args.cols}")
    print(f"edges={len(edges)}")
    print("vertex_numbering=(column*rows+row), zero_based")
    print("edge_list=" + repr(edges))
    print("coefficients_low_to_high=" + repr(coeff))
    print("chromatic_polynomial=" + format_poly(coeff))
    print(f"chi(-1)={value}")
    print(f"acyclic_orientations={ao}")
    print(f"acyclic_orientations_mod_4={ao % 4}")
    print(f"max_frontier_partition_states={max_states}")


if __name__ == "__main__":
    main()
