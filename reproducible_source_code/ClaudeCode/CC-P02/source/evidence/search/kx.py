"""Crossings of knight moves: basic tools.
A move is an unordered pair of cells a knight's move apart, drawn as the segment between the cell centres.
Two moves cross if the segments meet at a point interior to both."""
import itertools
MOVES8 = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
HALF = ((1, 2), (2, 1), (-1, 2), (-2, 1))          # one direction of each line
def orient(p, q, r):
    v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return (v > 0) - (v < 0)
def cross(e, f):
    (a, b), (c, d) = e, f
    if a == c or a == d or b == c or b == d: return False
    return orient(a, b, c) * orient(a, b, d) < 0 and orient(c, d, a) * orient(c, d, b) < 0
def edges_of(cells):
    cs = set(cells); out = []
    for (x, y) in cells:
        for dx, dy in HALF:
            c2 = (x + dx, y + dy)
            if c2 in cs: out.append(((x, y), c2))
    return out
def crossing_pairs(edges):
    """all crossing pairs (i, j), i < j, by bucketing on bounding boxes"""
    byrow = {}
    for k, ((a, b)) in enumerate(edges):
        byrow.setdefault((min(a[0], b[0]), min(a[1], b[1])), []).append(k)
    out = []
    for k, e in enumerate(edges):
        x0, y0 = min(e[0][0], e[1][0]), min(e[0][1], e[1][1])
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for k2 in byrow.get((x0 + dx, y0 + dy), ()):
                    if k2 > k and cross(e, edges[k2]): out.append((k, k2))
    return out
def count_crossings(edge_list):
    return len(crossing_pairs(list(edge_list)))
if __name__ == "__main__":
    # how many moves cross a given move in the plane
    big = [(x, y) for x in range(-6, 8) for y in range(-6, 8)]
    E = edges_of(big)
    e0 = ((0, 0), (1, 2))
    cr = [f for f in E if cross(e0, f)]
    print("moves crossing (0,0)-(1,2):", len(cr))
    from collections import Counter
    print(Counter((f[1][0] - f[0][0], f[1][1] - f[0][1]) for f in cr))
