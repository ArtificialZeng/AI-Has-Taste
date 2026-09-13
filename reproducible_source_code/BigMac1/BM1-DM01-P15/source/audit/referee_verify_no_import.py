#!/usr/bin/env python3
"""Fresh-referee exact verifier for mac01-p15, with no imports.

The arithmetic route is deliberately definition-direct and distinct from the
submitted LCM, stepwise-recurrence, and balanced-tree implementations: it uses
``n!`` itself as a common denominator, reduces the resulting fraction, and
then computes the defining gcd with the same factorial.

Supply the serialized witness path as one line on standard input.  Run with
``python3 -I -S`` so neither site packages nor the project import path is used.
"""


EXPECTED_KEYS = {"schema_version", "n", "p", "expected_h", "claim"}
EXPECTED_CLAIM = (
    "For the reduced harmonic number H_n=U_n/V_n, gcd(U_n,n!)=179."
)


def fail(message):
    raise ValueError(message)


class StrictObjectReader:
    """Minimal strict JSON reader for one flat certificate object."""

    def __init__(self, raw):
        try:
            self.text = raw.decode("utf-8")
        except UnicodeDecodeError:
            fail("certificate is not valid UTF-8")
        self.at = 0

    def space(self):
        while self.at < len(self.text) and self.text[self.at] in " \t\r\n":
            self.at += 1

    def take(self, character):
        self.space()
        if self.at >= len(self.text) or self.text[self.at] != character:
            fail("expected " + character)
        self.at += 1

    def string(self):
        self.space()
        if self.at >= len(self.text) or self.text[self.at] != '"':
            fail("expected a JSON string")
        self.at += 1
        output = []
        simple_escapes = {
            '"': '"',
            "\\": "\\",
            "/": "/",
            "b": "\b",
            "f": "\f",
            "n": "\n",
            "r": "\r",
            "t": "\t",
        }
        while self.at < len(self.text):
            character = self.text[self.at]
            self.at += 1
            if character == '"':
                return "".join(output)
            if ord(character) < 0x20:
                fail("unescaped control character")
            if character != "\\":
                output.append(character)
                continue
            if self.at >= len(self.text):
                fail("unfinished escape")
            escaped = self.text[self.at]
            self.at += 1
            if escaped in simple_escapes:
                output.append(simple_escapes[escaped])
                continue
            if escaped != "u" or self.at + 4 > len(self.text):
                fail("invalid escape")
            digits = self.text[self.at : self.at + 4]
            if any(digit not in "0123456789abcdefABCDEF" for digit in digits):
                fail("invalid unicode escape")
            value = int(digits, 16)
            self.at += 4
            if 0xD800 <= value <= 0xDFFF:
                fail("surrogate escape is outside this certificate schema")
            output.append(chr(value))
        fail("unterminated string")

    def integer(self):
        self.space()
        start = self.at
        if self.at < len(self.text) and self.text[self.at] == "-":
            self.at += 1
        if self.at >= len(self.text) or self.text[self.at] not in "0123456789":
            fail("expected a JSON integer")
        if self.text[self.at] == "0":
            self.at += 1
            if self.at < len(self.text) and self.text[self.at] in "0123456789":
                fail("leading zero in integer")
        else:
            while self.at < len(self.text) and self.text[self.at] in "0123456789":
                self.at += 1
        if self.at < len(self.text) and self.text[self.at] in ".eE":
            fail("non-integral JSON number")
        return int(self.text[start : self.at])

    def object(self):
        self.take("{")
        result = {}
        self.space()
        if self.at < len(self.text) and self.text[self.at] == "}":
            fail("empty certificate")
        while True:
            key = self.string()
            if key in result:
                fail("duplicate JSON member after escape decoding")
            self.take(":")
            self.space()
            if self.at < len(self.text) and self.text[self.at] == '"':
                value = self.string()
            else:
                value = self.integer()
            result[key] = value
            self.space()
            if self.at >= len(self.text):
                fail("unterminated object")
            separator = self.text[self.at]
            self.at += 1
            if separator == "}":
                break
            if separator != ",":
                fail("expected object separator")
        self.space()
        if self.at != len(self.text):
            fail("trailing data after certificate")
        return result


def parse_certificate(raw):
    value = StrictObjectReader(raw).object()
    if set(value) != EXPECTED_KEYS:
        fail("certificate keys do not exactly match the schema")
    for key in ("schema_version", "n", "p", "expected_h"):
        if type(value[key]) is not int:
            fail(key + " is not an integer")
    if value["schema_version"] != 1:
        fail("unsupported schema version")
    if value["n"] != 31862 or value["n"] < 1:
        fail("certificate is outside the frozen witness endpoint")
    if value["p"] != 179 or value["expected_h"] != 179:
        fail("certificate does not claim the frozen target value")
    if value["n"] != value["p"] * (value["p"] - 1):
        fail("certificate index is inconsistent with its stated prime")
    if value["claim"] != EXPECTED_CLAIM:
        fail("certificate claim is not the frozen endpoint binding")
    return value


def gcd(left, right):
    left = abs(left)
    right = abs(right)
    while right != 0:
        left, right = right, left % right
    return left


SHA256_ROUND_CONSTANTS = (
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


def right_rotate(value, amount):
    return ((value >> amount) | (value << (32 - amount))) & 0xFFFFFFFF


def sha256(data):
    padded = bytearray(data)
    original_bits = 8 * len(padded)
    padded.append(0x80)
    while len(padded) % 64 != 56:
        padded.append(0)
    padded.extend(original_bits.to_bytes(8, "big"))
    state = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
    ]
    for block_start in range(0, len(padded), 64):
        schedule = []
        for offset in range(0, 64, 4):
            schedule.append(
                int.from_bytes(padded[block_start + offset : block_start + offset + 4], "big")
            )
        for index in range(16, 64):
            old_15 = schedule[index - 15]
            old_2 = schedule[index - 2]
            sigma_0 = right_rotate(old_15, 7) ^ right_rotate(old_15, 18) ^ (old_15 >> 3)
            sigma_1 = right_rotate(old_2, 17) ^ right_rotate(old_2, 19) ^ (old_2 >> 10)
            schedule.append(
                (schedule[index - 16] + sigma_0 + schedule[index - 7] + sigma_1)
                & 0xFFFFFFFF
            )
        a, b, c, d, e, f, g, h = state
        for index in range(64):
            upper_1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            choose = (e & f) ^ ((~e) & g)
            first = (h + upper_1 + choose + SHA256_ROUND_CONSTANTS[index] + schedule[index]) & 0xFFFFFFFF
            upper_0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            majority = (a & b) ^ (a & c) ^ (b & c)
            second = (upper_0 + majority) & 0xFFFFFFFF
            h, g, f, e, d, c, b, a = (
                g,
                f,
                e,
                (d + first) & 0xFFFFFFFF,
                c,
                b,
                a,
                (first + second) & 0xFFFFFFFF,
            )
        state = [
            (before + after) & 0xFFFFFFFF
            for before, after in zip(state, (a, b, c, d, e, f, g, h))
        ]
    return "".join(format(word, "08x") for word in state)


def decimal_bytes(value):
    """Serialize a large nonnegative integer without Python's digit ceiling."""
    if value == 0:
        return b"0"
    base = 1_000_000_000
    pieces = []
    while value:
        value, remainder = divmod(value, base)
        pieces.append(remainder)
    output = str(pieces.pop())
    while pieces:
        output += format(pieces.pop(), "09d")
    return output.encode("ascii")


def main():
    certificate_path = input().strip()
    if not certificate_path:
        fail("certificate path is required")
    raw = open(certificate_path, "rb").read()
    certificate = parse_certificate(raw)
    n = certificate["n"]

    factorial = 1
    for factor in range(2, n + 1):
        factorial *= factor
    common_numerator = 0
    for denominator_term in range(1, n + 1):
        quotient, remainder = divmod(factorial, denominator_term)
        if remainder != 0:
            fail("factorial is not a common denominator")
        common_numerator += quotient

    cancellation = gcd(common_numerator, factorial)
    numerator = common_numerator // cancellation
    denominator = factorial // cancellation
    if numerator <= 0 or denominator <= 0:
        fail("reduced harmonic fraction violates positivity conventions")
    if gcd(numerator, denominator) != 1:
        fail("fraction did not reduce to lowest terms")
    if numerator * factorial != common_numerator * denominator:
        fail("reduced fraction does not equal the exact harmonic sum")
    computed_h = gcd(numerator, factorial)
    if computed_h != certificate["expected_h"]:
        fail("definition-direct reconstruction did not yield h(n)=179")
    if numerator % 179 != 0 or numerator % (179 * 179) == 0:
        fail("unexpected 179-adic numerator valuation")
    if denominator % 179 == 0:
        fail("179 divides the reduced denominator")

    source = open("audit/referee_verify_no_import.py", "rb").read()
    fields = [
        '"status":"PASS"',
        '"algorithm":"factorial-common-denominator"',
        '"n":' + str(n),
        '"computed_h":' + str(computed_h),
        '"numerator_bits":' + str(numerator.bit_length()),
        '"denominator_bits":' + str(denominator.bit_length()),
        '"numerator_mod_179_squared":' + str(numerator % (179 * 179)),
        '"denominator_mod_179":' + str(denominator % 179),
        '"numerator_sha256_decimal":"' + sha256(decimal_bytes(numerator)) + '"',
        '"denominator_sha256_decimal":"' + sha256(decimal_bytes(denominator)) + '"',
        '"input_sha256":"' + sha256(raw) + '"',
        '"code_sha256":"' + sha256(source) + '"',
    ]
    print("{" + ",".join(fields) + "}")


if __name__ == "__main__":
    main()
