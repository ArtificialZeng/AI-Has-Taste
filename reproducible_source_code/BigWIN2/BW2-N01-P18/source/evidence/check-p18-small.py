#!/usr/bin/env python3
"""Exact bounded intake checks; finite words do not certify recurrence."""
import hashlib
import json
import math
import platform
from pathlib import Path


def lucas(n, k, p):
    if k < 0 or k > n:
        return 0
    out = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        out = out * math.comb(a, b) % p
        n //= p
        k //= p
    return out


def coefficient(n, r, p):
    if (n-r) % p:
        return 0
    return lucas(n, (n-r)//p, p)


def times_p(poly, p):
    out = {}
    for degree, value in poly.items():
        for target in (degree+p-1, degree-1):
            out[target] = (out.get(target, 0)+value) % p
    return {d: v for d, v in out.items() if v}


def mul_sparse(a, b, p, limit):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            if i+j <= limit:
                out[i+j] = (out.get(i+j, 0)+ai*bj) % p
    return {d:v for d,v in out.items() if v}


def main():
    limit, series_limit, literal_limit = 4096, 512, 128
    rows = []
    literal_checks = series_checks = binomial_checks = 0
    for p in (2,3,5,7):
        poly = {0:1}
        for n in range(literal_limit+1):
            for r in range(-6,7):
                assert coefficient(n,r,p) == poly.get(-r,0), (p,n,r)
                literal_checks += 1
                if (n-r) % p == 0 and 0 <= (n-r)//p <= n:
                    assert coefficient(n,r,p) == math.comb(n,(n-r)//p) % p
                    binomial_checks += 1
            poly = times_p(poly,p)
        x = {}
        degree = 1
        while degree <= series_limit:
            x[degree] = 1
            degree = p*degree+1
        power = {0:1}
        for r in range(9):
            for n in range(series_limit+1):
                assert power.get(n,0) == coefficient(n,r,p), (p,n,r)
                series_checks += 1
            power = mul_sparse(power,x,p,series_limit)
        assert all(coefficient(n,0,p)==0 for n in range(1,limit+1))
        monomials = []
        for r in range(-6,7):
            values = bytes(coefficient(n,r,p) for n in range(limit+1))
            support = [i for i,v in enumerate(values) if v]
            monomials.append({"r":r,"nonzero_count":len(support),
                              "first_nonzero_indices":support[:24],
                              "values_sha256":hashlib.sha256(values).hexdigest()})
        x_values = [coefficient(n,1,p) for n in range(limit+1)]
        expected = []
        degree = 1
        while degree <= limit:
            expected.append(degree)
            degree = p*degree+1
        assert [i for i,v in enumerate(x_values) if v] == expected
        word = [1]+[0]*(p-1)+[1]
        occurrences = [i for i in range(limit-len(word)+2)
                       if x_values[i:i+len(word)] == word]
        assert occurrences == [1]
        rows.append({"p":p,"monomials":monomials,"Q_x_support":expected,
                     "Q_x_word":word,"Q_x_word_occurrences_within_test":occurrences})
    result = {"schema":1,"python":platform.python_version(),"randomness":"none",
              "arithmetic":"integers and finite fields F_p",
              "primes":[2,3,5,7],"monomial_exponents":[-6,6],
              "n_max":limit,"literal_n_max":literal_limit,
              "literal_coefficient_comparisons":literal_checks,
              "integer_binomial_crosschecks":binomial_checks,
              "positive_monomial_gf_comparisons":series_checks,
              "positive_monomial_gf_scope":"r=0..8,n=0..512",
              "rows":rows,
              "scope":"Finite coefficient and generating-function checks only. A unique word occurrence within n<=4096 is not a proof of nonrecurrence; all-prime/all-Q classification remains unresolved.",
              "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).with_name("p18-intake-check.json")
    output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2))
    print(json.dumps({"output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
