"""Small exact triage check for A114216; not a 100,000,000 certificate."""

LIMIT = 401_000
sieve = bytearray(b"\x01") * LIMIT
sieve[:2] = b"\x00\x00"
for q in range(2, int((LIMIT - 1) ** 0.5) + 1):
    if sieve[q]:
        sieve[q * q : LIMIT : q] = b"\x00" * (
            (LIMIT - 1 - q * q) // q + 1
        )

a = 0
hits = []
states = {}
selected = {1, 2, 3, 4, 5, 12, 14, 20, 75, 33_899, 33_900}
for n, p in enumerate((q for q in range(LIMIT) if sieve[q]), 1):
    total = a + p
    a = total // (total & -total)
    if a == 1:
        hits.append(n)
    if n in selected:
        states[n] = (p, a, total)
    if n == 33_900:
        break

expected_hits = [1, 2, 5, 12, 14, 20, 75, 33_900]
assert hits == expected_hits
assert states[33_899] == (400_523, 123_729, 494_916)
assert states[33_900] == (400_559, 1, 524_288)
print("hits_through_33900 =", hits)
print("state_33899 =", states[33_899])
print("state_33900 =", states[33_900])
