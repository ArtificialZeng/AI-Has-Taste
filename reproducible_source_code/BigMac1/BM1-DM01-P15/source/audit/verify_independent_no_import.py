#!/usr/bin/env python3
"""Fresh-context exact checker using no imports and a fraction-sum tree.

Supply the serialized witness path on standard input.  The program deliberately
does not import either project code or the Python standard library.
"""


EXPECTED_KEYS = {"schema_version", "n", "p", "expected_h", "claim"}
EXPECTED_CLAIM = (
    "For the reduced harmonic number H_n=U_n/V_n, gcd(U_n,n!)=179."
)


def fail(message):
    raise ValueError(message)


def parse_string(text, position):
    if position >= len(text) or text[position] != '"':
        fail("expected JSON string")
    position += 1
    chars = []
    escapes = {
        '"': '"',
        "\\": "\\",
        "/": "/",
        "b": "\b",
        "f": "\f",
        "n": "\n",
        "r": "\r",
        "t": "\t",
    }
    while position < len(text):
        char = text[position]
        position += 1
        if char == '"':
            return "".join(chars), position
        if ord(char) < 0x20:
            fail("unescaped control character in JSON string")
        if char != "\\":
            chars.append(char)
            continue
        if position >= len(text):
            fail("unterminated JSON escape")
        escape = text[position]
        position += 1
        if escape in escapes:
            chars.append(escapes[escape])
            continue
        if escape != "u" or position + 4 > len(text):
            fail("invalid JSON escape")
        digits = text[position : position + 4]
        if any(char not in "0123456789abcdefABCDEF" for char in digits):
            fail("invalid JSON unicode escape")
        codepoint = int(digits, 16)
        position += 4
        if 0xD800 <= codepoint <= 0xDFFF:
            fail("surrogate escapes are not accepted by this certificate schema")
        chars.append(chr(codepoint))
    fail("unterminated JSON string")


def skip_space(text, position):
    while position < len(text) and text[position] in " \t\r\n":
        position += 1
    return position


def parse_integer(text, position):
    start = position
    if position < len(text) and text[position] == "-":
        position += 1
    if position >= len(text) or text[position] not in "0123456789":
        fail("expected JSON integer")
    if text[position] == "0":
        position += 1
        if position < len(text) and text[position] in "0123456789":
            fail("leading zero in JSON integer")
    else:
        while position < len(text) and text[position] in "0123456789":
            position += 1
    if position < len(text) and text[position] in ".eE":
        fail("noninteger JSON number")
    return int(text[start:position]), position


def parse_witness(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail("witness is not UTF-8")
    position = skip_space(text, 0)
    if position >= len(text) or text[position] != "{":
        fail("witness root must be a JSON object")
    position += 1
    result = {}
    position = skip_space(text, position)
    if position < len(text) and text[position] == "}":
        fail("witness object is empty")
    while True:
        position = skip_space(text, position)
        key, position = parse_string(text, position)
        if key in result:
            fail("duplicate JSON object key")
        position = skip_space(text, position)
        if position >= len(text) or text[position] != ":":
            fail("expected colon after JSON object key")
        position = skip_space(text, position + 1)
        if position < len(text) and text[position] == '"':
            value, position = parse_string(text, position)
        else:
            value, position = parse_integer(text, position)
        result[key] = value
        position = skip_space(text, position)
        if position >= len(text):
            fail("unterminated JSON object")
        if text[position] == "}":
            position = skip_space(text, position + 1)
            if position != len(text):
                fail("trailing data after JSON object")
            break
        if text[position] != ",":
            fail("expected comma in JSON object")
        position += 1
    if set(result) != EXPECTED_KEYS:
        fail("witness has missing or unexpected keys")
    for key in ("schema_version", "n", "p", "expected_h"):
        if type(result[key]) is not int:
            fail(key + " must be an integer")
    if type(result["claim"]) is not str:
        fail("claim must be a string")
    if result["schema_version"] != 1:
        fail("unsupported witness schema")
    if result["n"] != 31862 or result["p"] != 179:
        fail("witness does not address n=31862 and p=179")
    if result["expected_h"] != 179:
        fail("witness has the wrong expected h value")
    if result["n"] != result["p"] * (result["p"] - 1):
        fail("witness index does not equal p(p-1)")
    if result["claim"] != EXPECTED_CLAIM:
        fail("claim text does not bind the frozen endpoint")
    return result


def gcd(left, right):
    left = abs(left)
    right = abs(right)
    while right:
        left, right = right, left % right
    return left


def harmonic_range(low, high):
    """Return the reduced exact fraction sum(1/k, low <= k <= high)."""
    if low == high:
        return 1, low
    middle = (low + high) // 2
    left_numerator, left_denominator = harmonic_range(low, middle)
    right_numerator, right_denominator = harmonic_range(middle + 1, high)
    common = gcd(left_denominator, right_denominator)
    left_scale = right_denominator // common
    right_scale = left_denominator // common
    numerator = left_numerator * left_scale + right_numerator * right_scale
    denominator = left_denominator * left_scale
    cancellation = gcd(numerator, denominator)
    return numerator // cancellation, denominator // cancellation


SHA256_CONSTANTS = (
    0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
    0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
    0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
    0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
    0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
    0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
    0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
    0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
    0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
    0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
    0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
    0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
    0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
    0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
    0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
    0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2,
)


def rotate_right(value, count):
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF


def sha256(data):
    message = bytearray(data)
    bit_length = len(message) * 8
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message.extend(bit_length.to_bytes(8, "big"))
    state = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
    ]
    for offset in range(0, len(message), 64):
        words = [
            int.from_bytes(message[offset + 4 * index : offset + 4 * index + 4], "big")
            for index in range(16)
        ]
        for index in range(16, 64):
            previous_15 = words[index - 15]
            previous_2 = words[index - 2]
            small_0 = (
                rotate_right(previous_15, 7)
                ^ rotate_right(previous_15, 18)
                ^ (previous_15 >> 3)
            )
            small_1 = (
                rotate_right(previous_2, 17)
                ^ rotate_right(previous_2, 19)
                ^ (previous_2 >> 10)
            )
            words.append(
                (words[index - 16] + small_0 + words[index - 7] + small_1)
                & 0xFFFFFFFF
            )
        a, b, c, d, e, f, g, h = state
        for index in range(64):
            big_1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
            choose = (e & f) ^ ((~e) & g)
            first = (h + big_1 + choose + SHA256_CONSTANTS[index] + words[index]) & 0xFFFFFFFF
            big_0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
            majority = (a & b) ^ (a & c) ^ (b & c)
            second = (big_0 + majority) & 0xFFFFFFFF
            h, g, f, e, d, c, b, a = g, f, e, (d + first) & 0xFFFFFFFF, c, b, a, (first + second) & 0xFFFFFFFF
        state = [
            (old + new) & 0xFFFFFFFF
            for old, new in zip(state, (a, b, c, d, e, f, g, h))
        ]
    return "".join(format(word, "08x") for word in state)


def decimal_bytes(value):
    if value == 0:
        return b"0"
    chunks = []
    while value:
        value, chunk = divmod(value, 1_000_000_000)
        chunks.append(chunk)
    text = str(chunks.pop())
    while chunks:
        text += format(chunks.pop(), "09d")
    return text.encode("ascii")


def main():
    witness_path = input().strip()
    if not witness_path:
        fail("a witness path is required on standard input")
    raw = open(witness_path, "rb").read()
    witness = parse_witness(raw)
    numerator, denominator = harmonic_range(1, witness["n"])
    if gcd(numerator, denominator) != 1:
        fail("fraction-sum tree did not return lowest terms")
    factorial = 1
    for value in range(2, witness["n"] + 1):
        factorial *= value
    computed_h = gcd(numerator, factorial)
    if computed_h != 179:
        fail("exact reconstruction did not yield h(n)=179")
    if numerator % 179 != 0 or numerator % (179 * 179) == 0:
        fail("the reduced numerator does not have 179-adic valuation one")
    if denominator % 179 == 0:
        fail("the reduced denominator is divisible by 179")
    code = open("audit/verify_independent_no_import.py", "rb").read()
    fields = [
        '"status":"PASS"',
        '"algorithm":"balanced-fraction-sum-tree"',
        '"n":' + str(witness["n"]),
        '"computed_h":' + str(computed_h),
        '"numerator_bits":' + str(numerator.bit_length()),
        '"denominator_bits":' + str(denominator.bit_length()),
        '"numerator_mod_179_squared":' + str(numerator % (179 * 179)),
        '"denominator_mod_179":' + str(denominator % 179),
        '"numerator_sha256_decimal":"' + sha256(decimal_bytes(numerator)) + '"',
        '"denominator_sha256_decimal":"' + sha256(decimal_bytes(denominator)) + '"',
        '"input_sha256":"' + sha256(raw) + '"',
        '"code_sha256":"' + sha256(code) + '"',
    ]
    print("{" + ",".join(fields) + "}")


if __name__ == "__main__":
    main()
