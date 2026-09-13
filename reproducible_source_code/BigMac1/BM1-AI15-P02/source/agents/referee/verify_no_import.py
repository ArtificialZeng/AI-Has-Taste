#!/usr/bin/env python3
"""Gate-5 no-import verifier for the root A321614 certificate.

This verifier uses only the Python standard library and imports no project
module.  It reconstructs the state graph and Burnside representation from
the board definition, verifies the serialized 68-dimensional representation,
checks an all-n observable Cayley--Hamilton annihilator, recovers the final
rational generating function, and checks a serialized Bezout identity.

The implementation is Python 3.9 compatible.  Every correctness condition
raises an explicit exception and therefore remains active under ``python -O``.
"""

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


class VerificationError(Exception):
    """A fail-closed certificate verification failure."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def require_keys(value, expected, label):
    require(type(value) is dict, label + " must be an object")
    actual = set(value.keys())
    wanted = set(expected)
    require(actual == wanted,
            "%s keys mismatch: missing=%r extra=%r" %
            (label, sorted(wanted - actual), sorted(actual - wanted)))


def require_integer_tree(value, label):
    if type(value) is int:
        return
    if type(value) is list:
        for item in value:
            require_integer_tree(item, label)
        return
    raise VerificationError(label + " contains a non-integer value")


def zero_matrix(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def matrix_vector(matrix, vector):
    require(type(matrix) is list and type(vector) is list,
            "matrix/vector types are invalid")
    require(all(type(row) is list and len(row) == len(vector)
                for row in matrix), "matrix/vector dimensions do not match")
    return [sum(row[j] * vector[j] for j in range(len(vector)))
            for row in matrix]


def scalar_product(left, right):
    require(len(left) == len(right), "scalar-product dimensions do not match")
    return sum(left[i] * right[i] for i in range(len(left)))


def direct_states():
    """Rebuild the twelve maximum-placement states of one 4-by-2 strip."""
    states = []
    for top_row in range(2):
        for bottom_row in range(2, 4):
            for top_side in range(2):
                for bottom_side in range(2):
                    state = ((top_row, top_side),
                             (bottom_row, bottom_side))
                    row_gap = abs(top_row - bottom_row)
                    side_gap = abs(top_side - bottom_side)
                    if max(row_gap, side_gap) > 1:
                        states.append(state)
    return states


def direct_compatible(left, right):
    """Check compatibility of adjacent 4-by-2 strips from cell coordinates."""
    for left_row, left_side in left:
        for right_row, right_side in right:
            column_gap = (2 + right_side) - left_side
            if abs(left_row - right_row) <= 1 and abs(column_gap) <= 1:
                return False
    return True


def state_image(state, horizontal, vertical):
    image = []
    for row, side in state:
        image.append((3 - row if horizontal else row,
                      1 - side if vertical else side))
    return tuple(sorted(image))


def induced_permutation(states, horizontal, vertical):
    lookup = dict((state, index) for index, state in enumerate(states))
    require(len(lookup) == len(states), "duplicate reconstructed state")
    answer = []
    for state in states:
        image = state_image(state, horizontal, vertical)
        require(image in lookup, "symmetry does not preserve state set")
        answer.append(lookup[image])
    return answer


def augmented(matrix, entrance):
    dimension = len(matrix)
    require(len(entrance) == dimension, "bad augmented entrance")
    require(all(type(row) is list and len(row) == dimension for row in matrix),
            "bad augmented matrix")
    result = zero_matrix(dimension + 1, dimension + 1)
    for i in range(dimension):
        result[i + 1][0] = entrance[i]
        for j in range(dimension):
            result[i + 1][j + 1] = matrix[i][j]
    initial = [1] + [0] * dimension
    output = [1] + [1] * dimension
    return result, initial, output


def interleave(matrix, even_initial, odd_initial, output):
    dimension = len(matrix)
    require(len(even_initial) == dimension and
            len(odd_initial) == dimension and len(output) == dimension,
            "bad parity interleaving vectors")
    result = zero_matrix(2 * dimension, 2 * dimension)
    for i in range(dimension):
        result[i][dimension + i] = 1
        for j in range(dimension):
            result[dimension + i][j] = matrix[i][j]
    return result, even_initial + odd_initial, output + [0] * dimension


def block_diagonal(blocks):
    dimension = sum(len(block) for block in blocks)
    result = zero_matrix(dimension, dimension)
    offset = 0
    for block in blocks:
        require(all(type(row) is list and len(row) == len(block)
                    for row in block), "nonsquare diagonal block")
        for i in range(len(block)):
            for j in range(len(block)):
                result[offset + i][offset + j] = block[i][j]
        offset += len(block)
    return result


def polynomial_product(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def trim_fraction_polynomial(poly):
    result = [Fraction(value) for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def fraction_polynomial_product(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return trim_fraction_polynomial(result)


def fraction_polynomial_sum(left, right):
    result = [Fraction(0)] * max(len(left), len(right))
    for i, x in enumerate(left):
        result[i] += x
    for i, x in enumerate(right):
        result[i] += x
    return trim_fraction_polynomial(result)


def fraction_polynomial_divmod(dividend, divisor):
    remainder = trim_fraction_polynomial(dividend)
    divisor = trim_fraction_polynomial(divisor)
    require(divisor != [Fraction(0)], "zero polynomial divisor")
    if len(remainder) < len(divisor):
        return [Fraction(0)], remainder
    quotient = [Fraction(0)] * (len(remainder) - len(divisor) + 1)
    while remainder != [Fraction(0)] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] -= coefficient * value
        remainder = trim_fraction_polynomial(remainder)
    return trim_fraction_polynomial(quotient), remainder


def fraction_polynomial_gcd(left, right):
    a = trim_fraction_polynomial(left)
    b = trim_fraction_polynomial(right)
    while b != [Fraction(0)]:
        unused, remainder = fraction_polynomial_divmod(a, b)
        del unused
        a, b = b, remainder
    require(a != [Fraction(0)], "both gcd inputs are zero")
    return trim_fraction_polynomial([value / a[-1] for value in a])


def parse_fraction_polynomial(value, label):
    require(type(value) is list and len(value) > 0, "missing " + label)
    result = []
    for pair in value:
        require(type(pair) is list and len(pair) == 2,
                "bad rational coefficient in " + label)
        numerator, denominator = pair
        require(type(numerator) is int and type(denominator) is int,
                "non-integer rational encoding in " + label)
        require(denominator > 0, "nonpositive denominator in " + label)
        require(math.gcd(numerator, denominator) == 1,
                "nonreduced rational coefficient in " + label)
        result.append(Fraction(numerator, denominator))
    return result


def json_digest(value):
    encoded = json.dumps(value, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def verify(certificate_path):
    raw = certificate_path.read_bytes()
    try:
        certificate = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise VerificationError("invalid JSON: %s" % exc)

    top_keys = [
        "adjacency", "arithmetic", "board", "branch_values_n0_to_21",
        "cayley_hamilton_observable_certificate", "claim", "environment",
        "fixed_state_indices", "generating_function",
        "global_representation", "involutions", "local_states_zero_based",
        "middle_edge_vectors", "minimality_bezout",
        "orbit_values_n0_to_21", "schema_version",
    ]
    require_keys(certificate, top_keys, "certificate")
    require(certificate["schema_version"] == 1, "unsupported schema version")
    require(certificate["claim"] ==
            "A321614 Barker generating function and minimal order-10 recurrence for all n",
            "claim endpoint mismatch")
    require(certificate["arithmetic"] ==
            "integers and exact rational Bezout coefficients only",
            "arithmetic declaration mismatch")
    expected_board = {
        "rows": 4,
        "columns": "2*n",
        "kings": "2*n",
        "attack": "Chebyshev distance at most 1",
        "group": ["identity", "horizontal", "vertical", "half_turn"],
        "square_n2_convention": "retain the order-four rectangle group",
    }
    require(certificate["board"] == expected_board,
            "board/group endpoint mismatch")
    environment = certificate["environment"]
    require(type(environment) is dict, "environment must be an object")
    require(environment.get("random_seed") is None,
            "certificate declares randomness")
    require(environment.get("third_party_dependencies") == [],
            "certificate declares third-party dependencies")

    states = direct_states()
    require(len(states) == 12, "definition did not reconstruct 12 states")
    encoded_states = [[list(cell) for cell in state] for state in states]
    require(certificate["local_states_zero_based"] == encoded_states,
            "serialized states differ from definition-level states")
    transfer = [[1 if direct_compatible(left, right) else 0
                 for right in states] for left in states]
    require(certificate["adjacency"] == transfer,
            "serialized transfer matrix differs from reconstructed matrix")

    horizontal = induced_permutation(states, True, False)
    vertical = induced_permutation(states, False, True)
    half_turn = induced_permutation(states, True, True)
    permutations = {
        "horizontal": horizontal,
        "vertical": vertical,
        "half_turn": half_turn,
    }
    require(certificate["involutions"] == permutations,
            "serialized symmetry permutations differ from reconstruction")
    for name, permutation in permutations.items():
        require(sorted(permutation) == list(range(12)),
                name + " is not a permutation")
        require(all(permutation[permutation[i]] == i for i in range(12)),
                name + " is not an involution")
    require(all(transfer[i][j] ==
                transfer[horizontal[i]][horizontal[j]]
                for i in range(12) for j in range(12)),
            "horizontal symmetry does not preserve transfer")
    require(all(transfer[i][j] == transfer[vertical[j]][vertical[i]]
                for i in range(12) for j in range(12)),
            "vertical reversal identity failed")
    require(all(transfer[i][j] == transfer[half_turn[j]][half_turn[i]]
                for i in range(12) for j in range(12)),
            "half-turn reversal identity failed")

    h_fixed = [i for i in range(12) if horizontal[i] == i]
    v_fixed = [i for i in range(12) if vertical[i] == i]
    r_fixed = [i for i in range(12) if half_turn[i] == i]
    fixed = {
        "horizontal": h_fixed,
        "vertical": v_fixed,
        "half_turn": r_fixed,
    }
    require(certificate["fixed_state_indices"] == fixed,
            "fixed-state data mismatch")
    require(len(h_fixed) == 2 and len(v_fixed) == 0 and len(r_fixed) == 2,
            "unexpected fixed-state boundary counts")
    horizontal_transfer = [[transfer[i][j] for j in h_fixed]
                           for i in h_fixed]
    vertical_seam = [transfer[i][vertical[i]] for i in range(12)]
    rotation_seam = [transfer[i][half_turn[i]] for i in range(12)]
    middle_edges = {
        "vertical": vertical_seam,
        "half_turn": rotation_seam,
    }
    require(certificate["middle_edge_vectors"] == middle_edges,
            "middle-edge vectors mismatch")
    require(sum(vertical_seam) == 3 and sum(rotation_seam) == 7,
            "unexpected middle-edge boundary counts")

    identity_matrix, identity_input, identity_output = augmented(
        transfer, [1] * 12)
    horizontal_matrix, horizontal_input, horizontal_output = augmented(
        horizontal_transfer, [1] * len(h_fixed))
    vertical_augmented, vertical_even, vertical_output = augmented(
        transfer, vertical_seam)
    vertical_matrix, vertical_input, vertical_observable = interleave(
        vertical_augmented, vertical_even,
        [0] + [1 if i in v_fixed else 0 for i in range(12)],
        vertical_output)
    rotation_augmented, rotation_even, rotation_output = augmented(
        transfer, rotation_seam)
    rotation_matrix, rotation_input, rotation_observable = interleave(
        rotation_augmented, rotation_even,
        [0] + [1 if i in r_fixed else 0 for i in range(12)],
        rotation_output)
    global_matrix = block_diagonal([
        identity_matrix, horizontal_matrix, vertical_matrix, rotation_matrix,
    ])
    global_input = (identity_input + horizontal_input + vertical_input +
                    rotation_input)
    global_output = (identity_output + horizontal_output +
                     vertical_observable + rotation_observable)
    dimension = len(global_matrix)
    require(dimension == 68 and all(len(row) == 68 for row in global_matrix),
            "global representation is not 68 by 68")

    representation = certificate["global_representation"]
    require_keys(representation,
                 ["dimension", "matrix", "input", "output",
                  "matrix_sha256", "input_sha256", "output_sha256"],
                 "global_representation")
    for value, label in (
            (representation["matrix"], "global matrix"),
            (representation["input"], "global input"),
            (representation["output"], "global output")):
        require_integer_tree(value, label)
    require(representation["dimension"] == 68,
            "serialized global dimension mismatch")
    require(representation["matrix"] == global_matrix,
            "serialized global matrix mismatch")
    require(representation["input"] == global_input and
            representation["output"] == global_output,
            "serialized global vectors mismatch")
    require(representation["matrix_sha256"] == json_digest(global_matrix),
            "global matrix digest mismatch")
    require(representation["input_sha256"] == json_digest(global_input),
            "global input digest mismatch")
    require(representation["output_sha256"] == json_digest(global_output),
            "global output digest mismatch")

    factors = [
        [1, -1], [1, -1], [1, -3], [1, -3], [1, -3, 1],
        [1, -1, -1], [1, 0, -3],
    ]
    denominator = [1]
    for factor in factors:
        denominator = polynomial_product(denominator, factor)
    numerator = polynomial_product(
        [1, -2], [1, -6, 17, -18, -2, 7, 6, -3])
    expected_denominator = [
        1, -12, 54, -98, -17, 346, -505, 210, 120, -126, 27,
    ]
    expected_numerator = [1, -8, 29, -52, 34, 11, -8, -15, 6]
    require(denominator == expected_denominator,
            "independent denominator expansion failed")
    require(numerator == expected_numerator,
            "independent numerator expansion failed")
    generating_function = certificate["generating_function"]
    require_keys(generating_function,
                 ["denominator_factors_ascending", "denominator_ascending",
                  "numerator_ascending", "recurrence_coefficients"],
                 "generating_function")
    require(generating_function["denominator_factors_ascending"] == factors,
            "serialized denominator factors mismatch")
    require(generating_function["denominator_ascending"] == denominator,
            "serialized denominator mismatch")
    require(generating_function["numerator_ascending"] == numerator,
            "serialized numerator mismatch")
    require(generating_function["recurrence_coefficients"] ==
            [-value for value in denominator[1:]],
            "serialized recurrence coefficients mismatch")

    powers = [global_input]
    for unused in range(10):
        del unused
        powers.append(matrix_vector(global_matrix, powers[-1]))
    annihilation = [
        sum(denominator[j] * powers[10 - j][i] for j in range(11))
        for i in range(68)
    ]
    cayley_hamilton = certificate["cayley_hamilton_observable_certificate"]
    require_keys(cayley_hamilton,
                 ["polynomial_vector_convention", "annihilation_vector",
                  "checked_moments", "moments",
                  "annihilation_vector_sha256"],
                 "cayley_hamilton_observable_certificate")
    require(cayley_hamilton["polynomial_vector_convention"] ==
            "w=sum(D[j]*B^(10-j)*input,j=0..10)",
            "annihilation-vector convention mismatch")
    require(cayley_hamilton["annihilation_vector"] == annihilation,
            "serialized annihilation vector mismatch")
    require(cayley_hamilton["annihilation_vector_sha256"] ==
            json_digest(annihilation), "annihilation-vector digest mismatch")
    observed = []
    current = annihilation
    for unused in range(68):
        del unused
        observed.append(scalar_product(global_output, current))
        current = matrix_vector(global_matrix, current)
    require(observed == [0] * 68,
            "68-dimensional observable annihilation check failed")
    require(cayley_hamilton["checked_moments"] == 68 and
            cayley_hamilton["moments"] == observed,
            "serialized observable moments mismatch")

    # Recompute the four Burnside branches.  The prefix is an integrity and
    # boundary check only.  The all-n recurrence was proved above: the first
    # 68 observable moments of q(B)b vanish, and Cayley--Hamilton for the
    # 68-dimensional B makes every later observable moment vanish as well.
    branch_data = [
        ("identity", identity_matrix, identity_input, identity_output),
        ("horizontal", horizontal_matrix, horizontal_input,
         horizontal_output),
        ("vertical", vertical_matrix, vertical_input, vertical_observable),
        ("half_turn", rotation_matrix, rotation_input,
         rotation_observable),
    ]
    branch_values = {}
    for name, matrix, initial, output in branch_data:
        values = []
        current = initial
        for unused in range(22):
            del unused
            values.append(scalar_product(output, current))
            current = matrix_vector(matrix, current)
        branch_values[name] = values
    require(branch_values == certificate["branch_values_n0_to_21"],
            "serialized branch boundary values mismatch")
    require([branch_values[name][0] for name in
             ("identity", "horizontal", "vertical", "half_turn")] ==
            [1, 1, 1, 1], "n=0 Burnside boundary mismatch")
    require([branch_values[name][1] for name in
             ("identity", "horizontal", "vertical", "half_turn")] ==
            [12, 2, 0, 2], "n=1 Burnside boundary mismatch")
    require([branch_values[name][2] for name in
             ("identity", "horizontal", "vertical", "half_turn")] ==
            [79, 3, 3, 7], "n=2 Burnside boundary mismatch")
    orbit_values = []
    for n in range(22):
        fixed_sum = sum(branch_values[name][n] for name in
                        ("identity", "horizontal", "vertical", "half_turn"))
        require(fixed_sum % 4 == 0,
                "Burnside sum is nonintegral at n=%d" % n)
        orbit_values.append(fixed_sum // 4)
    require(orbit_values == certificate["orbit_values_n0_to_21"],
            "serialized orbit values mismatch")
    require(orbit_values[:3] == [1, 4, 23],
            "n=0,1,2 orbit boundary mismatch")
    convolution = []
    for n in range(10):
        convolution.append(sum(
            denominator[j] * orbit_values[n - j]
            for j in range(min(n, 10) + 1)))
    require(convolution[:9] == numerator and convolution[9] == 0,
            "initial data do not give the claimed P/Q numerator")

    minimality = certificate["minimality_bezout"]
    require_keys(minimality, ["convention", "U", "V"],
                 "minimality_bezout")
    require(minimality["convention"] ==
            "U*numerator + V*denominator = 1; coefficients ascending",
            "Bezout convention mismatch")
    bezout_u = parse_fraction_polynomial(minimality["U"], "Bezout U")
    bezout_v = parse_fraction_polynomial(minimality["V"], "Bezout V")
    bezout_left = fraction_polynomial_sum(
        fraction_polynomial_product(bezout_u, numerator),
        fraction_polynomial_product(bezout_v, denominator))
    require(bezout_left == [Fraction(1)], "Bezout identity is not 1")
    require(fraction_polynomial_gcd(numerator, denominator) == [Fraction(1)],
            "independently recomputed gcd is not 1")

    return {
        "all_n_basis": "68 observable zeros plus Cayley-Hamilton",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "global_dimension": 68,
        "minimal_denominator_degree": 10,
        "observable_zero_moments": 68,
        "proof_assistant": False,
        "states": 12,
        "status": "PASS",
        "verifier_sha256": hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    if len(sys.argv) != 2:
        print("usage: verify_no_import.py CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        result = verify(Path(sys.argv[1]).resolve())
    except Exception as exc:
        print("FAIL: %s: %s" % (type(exc).__name__, exc), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
