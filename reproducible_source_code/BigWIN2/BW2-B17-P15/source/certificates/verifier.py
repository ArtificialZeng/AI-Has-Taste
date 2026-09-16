#!/usr/bin/env python3
"""Dependency-free exact verifier for rational step-function witnesses."""
import hashlib
import pathlib
import sys

PRIMES = (
    (998244353, 3),
    (1004535809, 3),
    (469762049, 3),
    (167772161, 3),
    (754974721, 11),
)
TARGET_NUM = 150274365
TARGET_DEN = 100000000


def die(message):
    raise ValueError(message)


def uint(token, positive=False):
    if not token or not token.isascii() or not token.isdigit():
        die("invalid unsigned decimal integer")
    if len(token) > 1 and token[0] == "0":
        die("non-canonical unsigned decimal integer")
    value = int(token)
    if value > 2**64 - 1:
        die("uint64 overflow")
    if positive and value == 0:
        die("integer must be positive")
    return value


def parse(raw):
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        die("input is not ASCII")
    t = text.split()
    if len(t) < 5 or t[0] != "AUTOCONV_CERT_V1" or t[1] != "n":
        die("bad magic/version or missing n field")
    n = uint(t[2], True)
    if n > 500000:
        die("n exceeds verifier limit")
    if t[3] != "weights":
        die("missing weights field")
    if len(t) != n + 5 or t[-1] != "end":
        die("wrong weight count, missing end, or trailing tokens")
    return [uint(x) for x in t[4:-1]]


def ntt(a, invert, mod, root):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        wl = pow(root, (mod - 1) // length, mod)
        if invert:
            wl = pow(wl, mod - 2, mod)
        half = length >> 1
        for base in range(0, n, length):
            w = 1
            for j in range(half):
                x, y = a[base + j], a[base + j + half] * w % mod
                a[base + j] = (x + y) % mod
                a[base + j + half] = (x - y) % mod
                w = w * wl % mod
        length <<= 1
    if invert:
        ni = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = a[i] * ni % mod


def convolution_mod(weights, prime, root, size):
    a = [x % prime for x in weights] + [0] * (size - len(weights))
    ntt(a, False, prime, root)
    a = [x * x % prime for x in a]
    ntt(a, True, prime, root)
    return a[:2 * len(weights) - 1]


def exact_convolution(weights):
    size = 1
    while size < 2 * len(weights) - 1:
        size <<= 1
    if any((p - 1) % size for p, _ in PRIMES):
        die("transform length unsupported by one or more primes")
    modulus = 1
    for p, _ in PRIMES:
        modulus *= p
    bound = len(weights) * max(weights) ** 2
    if bound >= modulus:
        die("CRT modulus insufficient for proven coefficient bound")
    residues = [convolution_mod(weights, p, g, size) for p, g in PRIMES]
    out = []
    for k in range(2 * len(weights) - 1):
        x, m = residues[0][k], PRIMES[0][0]
        for j in range(1, len(PRIMES)):
            p = PRIMES[j][0]
            step = (residues[j][k] - x) % p * pow(m % p, p - 2, p) % p
            x += m * step
            m *= p
        if x > bound:
            die("reconstructed coefficient exceeds proven bound")
        out.append(x)
    if len(weights) <= 2048:
        slow = [0] * len(out)
        for i, x in enumerate(weights):
            for j, y in enumerate(weights):
                slow[i + j] += x * y
        if slow != out:
            die("naive convolution cross-check failed")
    return out


def self_test():
    for w in ([1], [1, 2, 3], [0, 7, 0, 11], [10**9, 999999999]):
        exact_convolution(w)
    print("SELF_TEST_PASS cases=4")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        self_test()
        return 0
    if len(sys.argv) != 2:
        die("usage: verifier.py CERTIFICATE | --self-test")
    path = pathlib.Path(sys.argv[1])
    raw = path.read_bytes()
    weights = parse(raw)
    total = sum(weights)
    if total == 0:
        die("all-zero vector is inadmissible")
    conv = exact_convolution(weights)
    maximum = max(conv)
    argmax = conv.index(maximum)
    lhs = 2 * len(weights) * maximum * TARGET_DEN
    rhs = total * total * TARGET_NUM
    margin = rhs - lhs
    code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(f"CERTIFICATE_PARSED n={len(weights)}")
    print(f"INPUT_SHA256 {input_hash}")
    print(f"CODE_SHA256 {code_hash}")
    print(f"SUM {total}\nMAX_COEFFICIENT {maximum}\nARGMAX_FIRST {argmax}")
    print(f"LHS {lhs}\nRHS {rhs}\nMARGIN {margin}")
    if lhs >= rhs:
        print("VERDICT FAIL_TARGET")
        return 2
    print("VERDICT PASS_STRICT_TARGET")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"VERDICT INVALID: {exc}", file=sys.stderr)
        sys.exit(1)
