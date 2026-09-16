#!/usr/bin/env python3
"""Exact mixed canonical-block census for the no-face-3 SW2 case.

Proposition 7.10(2) of arXiv:2609.05349v1 decomposes an ideal,
right-angled SW2-polyhedron with no boundary face of type 3 into the
chambers around each image of the finite 1-3-4 vertex.  Such a block is
one quarter, one half, or one full ideal right-angled octahedron, hence
contains 12, 24, or 48 SW2 chambers.  This program reconstructs every
actual orientation of those blocks in the SW2 Coxeter complex and
enumerates, up to the SW2 reflection group, every connected compatible
assembly of total size at most seven quarter-octahedra.  Convexity and
boundary geometry are then checked using exact integer Lorentz arithmetic.

The finite census is a subsidiary result; it does not settle Conjecture
7.11 beyond the stated chamber bound.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

import sw2_quarter_census as base


MAXIMUM_QUARTER_UNITS = 7
E0 = (1, 0, 0, 0)
INTERIOR_POINT = (100, 30, 20, 10)
SECTOR_TEST_POINT = (100, 20, 10, 5)


def left_image(matrix, chambers):
    return frozenset(base.matrix_multiply(matrix, chamber) for chamber in chambers)


def determinant4(rows):
    """Exact determinant of four integer row vectors."""
    return sum(
        (-1 if column % 2 else 1)
        * rows[0][column]
        * base.determinant3(
            [
                [row[index] for index in range(4) if index != column]
                for row in rows[1:]
            ]
        )
        for column in range(4)
    )


class MixedCanonicalCensus:
    def __init__(self, maximum_units: int = MAXIMUM_QUARTER_UNITS):
        self.maximum_units = maximum_units
        self.reflections = tuple(base.reflection(normal) for normal in base.SW2_NORMALS)
        self.r2 = self.reflections[1]
        self.central_octahedron = frozenset(
            base.subgroup(self.reflections, (0, 2, 3))
        )
        assert len(self.central_octahedron) == 48

        # This is the no-face-3 quarter reconstructed in the pass-1
        # certificate: one sector x >= |y| of the central octahedron.
        base_quarter = frozenset(
            chamber
            for chamber in self.central_octahedron
            if (
                image := base.matrix_vector(chamber, SECTOR_TEST_POINT)
            )[1]
            >= abs(image[2])
        )
        assert len(base_quarter) == 12
        self.quarters = {
            left_image(symmetry, base_quarter)
            for symmetry in self.central_octahedron
        }
        assert len(self.quarters) == 12

        # Proposition 7.10 says that a canonical boundary through the B3
        # center has face type {1,4}.  Independently enumerate every oriented
        # mirror of those types through the center.  There are six unoriented
        # mirrors, hence twelve choices of an inward half-space.  Their cuts
        # give all twelve source halves, and the orthogonal two-cut sectors
        # give all twelve source quarters.  The equalities below independently
        # check the orbit constructions rather than assuming their counts.
        self.allowed_cut_normals = frozenset(
            base.primitive(base.matrix_vector(chamber, base.SW2_NORMALS[face]))
            for chamber in self.central_octahedron
            for face in (0, 3)
        )
        assert len(self.allowed_cut_normals) == 12
        central_interior_points = {
            chamber: base.matrix_vector(chamber, INTERIOR_POINT)
            for chamber in self.central_octahedron
        }
        cut_halves = {
            normal: frozenset(
                chamber
                for chamber, point in central_interior_points.items()
                if base.lorentz(normal, point) < 0
            )
            for normal in self.allowed_cut_normals
        }
        assert all(len(block) == 24 for block in cut_halves.values())
        assert len(set(cut_halves.values())) == 12

        # A half-octahedron is the union of the two quarters on one side
        # of one symmetry plane.  The exact boundary signature selects
        # these from the disjoint pairs, after which the B3 orbit verifies
        # that there is one orbit of twelve oriented halves.
        quarter_list = sorted(self.quarters, key=lambda item: tuple(sorted(item)))
        half_candidates = set()
        for position, first in enumerate(quarter_list):
            for second in quarter_list[position + 1 :]:
                if first & second:
                    continue
                union = first | second
                planes, _, _ = base.chamber_union_boundary(
                    set(union), base.SW2_NORMALS, self.reflections
                )
                shape = base.polyhedron_data(planes)
                signature = (
                    shape["facets"],
                    shape["vertices"],
                    shape["edges"],
                    len(shape["ideal_vertices"]),
                    len(shape["finite_vertices"]),
                )
                if signature == (7, 6, 11, 4, 2) and not shape["bad_edges"]:
                    half_candidates.add(frozenset(union))
        assert len(half_candidates) == 12
        base_half = min(half_candidates, key=lambda item: tuple(sorted(item)))
        self.halves = {
            left_image(symmetry, base_half)
            for symmetry in self.central_octahedron
        }
        assert self.halves == half_candidates
        assert self.halves == set(cut_halves.values())

        cut_quarters = set()
        for first, second in itertools.combinations(sorted(self.allowed_cut_normals), 2):
            if base.lorentz(first, second) != 0:
                continue
            sector = cut_halves[first] & cut_halves[second]
            if len(sector) != 12:
                continue
            if set(self._local_cut_signature(sector)) == {first, second}:
                cut_quarters.add(sector)
        assert cut_quarters == self.quarters

        self.block_variants = (
            self.quarters | self.halves | {self.central_octahedron}
        )
        self.local_variants = sorted(
            (block for block in self.block_variants if base.IDENTITY in block),
            key=lambda item: (len(item), tuple(sorted(item))),
        )
        assert Counter(len(block) // 12 for block in self.block_variants) == {
            1: 12,
            2: 12,
            4: 1,
        }
        assert Counter(len(block) // 12 for block in self.local_variants) == {
            1: 3,
            2: 6,
            4: 1,
        }

        # At the central B3 vertex, the oriented non-type-2 cut planes
        # distinguish all 25 local block variants.  This is the local
        # injectivity needed by the symmetry canonicalization below.
        signatures = {self._local_cut_signature(block) for block in self.block_variants}
        assert len(signatures) == len(self.block_variants)

        # Across a type-2 facet the two B3 centers have exact signed distances
        # -1 and +1 from its oriented Lorentz plane.  By equivariance the same
        # holds at every translated interface.  Thus an unmatched interface
        # between two represented centers cannot occur in a convex union.
        neighbor_center = base.matrix_vector(self.r2, E0)
        self.base_interface_center_signs = (
            base.lorentz(base.SW2_NORMALS[1], E0),
            base.lorentz(base.SW2_NORMALS[1], neighbor_center),
        )
        assert self.base_interface_center_signs == (-1, 1)

    @staticmethod
    def center(chamber):
        return base.matrix_vector(chamber, E0)

    def blocks_by_center(self, chambers):
        result = defaultdict(set)
        for chamber in chambers:
            result[self.center(chamber)].add(chamber)
        return result

    def _local_cut_signature(self, block):
        cuts = set()
        for chamber in block:
            for face in (0, 2, 3):
                if base.matrix_multiply(chamber, self.reflections[face]) not in block:
                    cuts.add(
                        base.primitive(
                            base.matrix_vector(chamber, base.SW2_NORMALS[face])
                        )
                    )
        expected = {12: 2, 24: 1, 48: 0}[len(block)]
        assert len(cuts) == expected
        return tuple(sorted(cuts))

    def raw_descriptor(self, chambers):
        descriptor = []
        for center, block in self.blocks_by_center(chambers).items():
            descriptor.append((center, self._local_cut_signature(block)))
        return descriptor

    def canonical_key(self, chambers):
        """Complete key for left translation by Gamma(SW2).

        Translating any chamber to the base chamber supplies every possible
        normalization.  A normalized state is encoded by its B3 centers and
        its oriented cut planes; local injectivity was checked in __init__.
        """
        descriptor = self.raw_descriptor(chambers)
        best = None
        for root in sorted(chambers):
            transform = base.inverse_lorentz(root)
            normalized = tuple(
                sorted(
                    (
                        base.matrix_vector(transform, center),
                        tuple(
                            sorted(
                                base.primitive(base.matrix_vector(transform, normal))
                                for normal in cuts
                            )
                        ),
                    )
                    for center, cuts in descriptor
                )
            )
            if best is None or normalized < best:
                best = normalized
        assert best is not None
        return best

    def interfaces_match(self, chambers):
        """Check every interface between two represented B3 stars exactly."""
        centers = {self.center(chamber) for chamber in chambers}
        for chamber in chambers:
            neighbor = base.matrix_multiply(chamber, self.r2)
            if neighbor not in chambers and self.center(neighbor) in centers:
                exposed_normal = base.matrix_vector(
                    chamber, base.SW2_NORMALS[1]
                )
                assert base.lorentz(
                    exposed_normal, self.center(chamber)
                ) == -1
                assert base.lorentz(
                    exposed_normal, self.center(neighbor)
                ) == 1
                return False
        return True

    def expansions(self, chambers):
        """Adjoin every compatible neighboring canonical block."""
        centers = {self.center(chamber) for chamber in chambers}
        open_interfaces = defaultdict(set)
        for chamber in chambers:
            neighbor = base.matrix_multiply(chamber, self.r2)
            neighbor_center = self.center(neighbor)
            if neighbor not in chambers and neighbor_center not in centers:
                open_interfaces[neighbor_center].add(neighbor)

        results = []
        for neighbor_center in sorted(open_interfaces):
            required = open_interfaces[neighbor_center]
            root = min(required)
            for local_block in self.local_variants:
                if len(chambers) + len(local_block) > 12 * self.maximum_units:
                    continue
                new_block = left_image(root, local_block)
                assert not (chambers & new_block)
                if not required <= new_block:
                    continue
                enlarged = chambers | new_block
                if self.interfaces_match(enlarged):
                    results.append(enlarged)
        return results

    def enumerate_states(self):
        # B3 acts transitively on the orientations of each of the three
        # block sizes, so one root of each size suffices.
        roots = [
            min(self.quarters, key=lambda item: tuple(sorted(item))),
            min(self.halves, key=lambda item: tuple(sorted(item))),
            self.central_octahedron,
        ]
        states = {self.canonical_key(root): root for root in roots}
        frontier = dict(states)
        generation_counts = []
        while frontier:
            new = {}
            for key in sorted(frontier):
                for enlarged in self.expansions(frontier[key]):
                    canonical = self.canonical_key(enlarged)
                    if canonical not in states:
                        new.setdefault(canonical, enlarged)
            generation_counts.append(
                {
                    "new_states": len(new),
                    "new_states_by_quarter_units": {
                        str(units): count
                        for units, count in sorted(
                            Counter(len(item) // 12 for item in new.values()).items()
                        )
                    },
                }
            )
            states.update(new)
            frontier = new
        return states, generation_counts

    def boundary_normals(self, chambers):
        planes, _, _ = base.chamber_union_boundary(
            set(chambers), base.SW2_NORMALS, self.reflections
        )
        return planes

    def is_convex(self, chambers, boundary_normals):
        # A Coxeter chamber is entirely on the side of a mirror containing
        # any one strict interior point.  Hence these exact sign tests say
        # that every unmatched chamber facet is globally supporting.
        interior_points = [
            base.matrix_vector(chamber, INTERIOR_POINT) for chamber in chambers
        ]
        return all(
            base.lorentz(normal, point) <= 0
            for normal in boundary_normals
            for point in interior_points
        )

    @staticmethod
    def geometry_classification(shape):
        if shape["finite_vertices"]:
            return "has_finite_boundary_vertex"
        if not shape["ideal_vertices"]:
            return "no_recovered_vertices"
        if shape["degenerate_facets"]:
            return "degenerate_boundary_facet"
        if shape["bad_edges"]:
            return "non_right_boundary_edge"
        if shape["euler_characteristic"] != 2:
            return "non_spherical_boundary"
        if any(valence != 4 for valence in shape["vertex_valences"]):
            return "non_four_valent_ideal_vertex"
        return "ideal_right_angled"

    def run(self):
        # Re-run all pass-1 primary-geometry assertions before the new test.
        _, primary_reconstruction = base.reconstruct_primary_geometry()
        states, generation_counts = self.enumerate_states()

        state_counts = Counter(len(state) // 12 for state in states.values())
        assert state_counts == {1: 1, 2: 2, 3: 4, 4: 17, 5: 52, 6: 235, 7: 1054}

        outcomes = Counter()
        convex_counts = Counter()
        survivors = []
        for canonical in sorted(states):
            chambers = states[canonical]
            units = len(chambers) // 12
            boundary = self.boundary_normals(chambers)
            if not self.is_convex(chambers, boundary):
                outcomes[(units, "nonconvex")] += 1
                continue
            convex_counts[units] += 1
            shape = base.polyhedron_data(boundary)
            classification = self.geometry_classification(shape)
            outcomes[(units, classification)] += 1
            if classification == "ideal_right_angled":
                blocks = self.blocks_by_center(chambers)
                survivors.append(
                    {
                        "quarter_units": units,
                        "sw2_chamber_count": len(chambers),
                        "canonical_block_units": sorted(
                            len(block) // 12 for block in blocks.values()
                        ),
                        "sw2_chamber_matrices": [
                            list(chamber) for chamber in sorted(chambers)
                        ],
                        "boundary_planes": [list(normal) for normal in boundary],
                        "shape": shape,
                    }
                )

        assert len(survivors) == 2
        assert sorted(item["canonical_block_units"] for item in survivors) == [
            [1, 1, 1, 1],
            [4],
        ]
        assert all(item["quarter_units"] == 4 for item in survivors)
        assert all(
            (
                item["shape"]["facets"],
                item["shape"]["vertices"],
                item["shape"]["edges"],
            )
            == (8, 6, 12)
            for item in survivors
        )
        central_survivor = next(
            item for item in survivors if item["canonical_block_units"] == [4]
        )
        standard_octahedron_planes = sorted(
            (1, x, y, z)
            for x in (-1, 1)
            for y in (-1, 1)
            for z in (-1, 1)
        )
        assert central_survivor["boundary_planes"] == [
            list(normal) for normal in standard_octahedron_planes
        ]
        standard_octahedron_gram = [
            [base.lorentz(first, second) for second in standard_octahedron_planes]
            for first in standard_octahedron_planes
        ]
        for item in survivors:
            planes = [tuple(normal) for normal in item["boundary_planes"]]
            gram = [
                [base.lorentz(first, second) for second in planes]
                for first in planes
            ]
            assert gram == standard_octahedron_gram
        spanning_minor = next(
            (
                (list(indices), determinant4([standard_octahedron_planes[i] for i in indices]))
                for indices in itertools.combinations(range(8), 4)
                if determinant4([standard_octahedron_planes[i] for i in indices]) != 0
            ),
            None,
        )
        assert spanning_minor is not None

        return {
            "arithmetic": "exact integers with Lorentz form diag(-1,1,1,1)",
            "maximum_quarter_units": self.maximum_units,
            "maximum_sw2_chambers": 12 * self.maximum_units,
            "source_model": primary_reconstruction,
            "local_canonical_blocks": {
                "oriented_variants_by_quarter_units": {
                    "1": len(self.quarters),
                    "2": len(self.halves),
                    "4": 1,
                },
                "variants_containing_base_chamber_by_quarter_units": {
                    str(units): count
                    for units, count in sorted(
                        Counter(len(block) // 12 for block in self.local_variants).items()
                    )
                },
            },
            "finite_completeness_certificate": {
                "oriented_type_1_or_4_cut_halfspaces_at_B3_center": len(
                    self.allowed_cut_normals
                ),
                "cut_halfspaces_recover_all_oriented_halves": True,
                "orthogonal_pairs_recover_all_oriented_quarters": True,
                "distinct_local_cut_descriptors": len(self.block_variants),
                "type_2_interface_center_signs": list(
                    self.base_interface_center_signs
                ),
                "interface_lemma": (
                    "An unmatched type-2 facet with both B3 centers represented "
                    "has one represented center at Lorentz sign +1 beyond the "
                    "facet, so no convex canonical assembly can have a mismatch."
                ),
            },
            "enumeration": {
                "generation_counts": generation_counts,
                "connected_interface_compatible_states_by_quarter_units": {
                    str(units): state_counts[units] for units in sorted(state_counts)
                },
                "convex_states_by_quarter_units": {
                    str(units): convex_counts[units] for units in sorted(convex_counts)
                },
                "geometry_classification_by_quarter_units": {
                    str(units): {
                        classification: outcomes[(units, classification)]
                        for _, classification in sorted(
                            key for key in outcomes if key[0] == units
                        )
                    }
                    for units in sorted(state_counts)
                },
            },
            "ideal_right_angled_survivors": survivors,
            "survivor_octahedron_certificate": {
                "standard_boundary_gram": standard_octahedron_gram,
                "standard_gram_rank": 4,
                "nonzero_spanning_minor": {
                    "normal_indices": spanning_minor[0],
                    "determinant": spanning_minor[1],
                },
                "all_survivor_grams_equal_standard": True,
                "explanation": (
                    "The eight oriented facet normals span Lorentz four-space. "
                    "Equality of their full Gram matrices therefore extends to "
                    "a Lorentz isometry carrying every survivor half-space to "
                    "the standard ideal right-angled octahedron half-spaces."
                ),
            },
            "conclusion": (
                "In the no-face-3 canonical mixed-block case, every convex ideal "
                "right-angled SW2-chamber union of total volume at most seven "
                "quarter-octahedra has 48 SW2 chambers and is a copy of the "
                "ideal right-angled octahedron."
            ),
            "scope_limit": (
                "This is an exhaustive finite census through 84 SW2 chambers. "
                "It gives no bound on a larger minimal counterexample and does "
                "not settle Conjecture 7.11."
            ),
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="optional JSON evidence path")
    args = parser.parse_args()
    report = MixedCanonicalCensus().run()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
