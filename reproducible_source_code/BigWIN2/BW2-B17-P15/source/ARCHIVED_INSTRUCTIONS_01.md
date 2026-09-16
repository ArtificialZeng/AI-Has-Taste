# Independent exact verifier

Input is whitespace-delimited and has exactly this grammar:

```text
AUTOCONV_CERT_V1
n N
weights
w_0 w_1 ... w_(N-1)
end
```

`N` is positive and every weight is a canonical decimal `uint64` (zero is
allowed, leading zeroes are not). No token may follow `end`. The vector must
not be all zero.

Build and run:

```bash
g++ -std=c++17 -O2 -Wall -Wextra -pedantic certificates/verifier.cpp -o certificates/verifier
certificates/verifier --self-test
certificates/verifier certificates/witness.txt
```

The dependency-free Python implementation follows the same algorithm and is
the executable reference in environments without a C++ compiler:

```bash
python3 certificates/verifier.py --self-test
python3 certificates/verifier.py certificates/witness.txt
```

The program squares the polynomial by five independent modular NTTs and
reconstructs every coefficient by CRT. It first proves that the a priori bound
`N*max(weight)^2` is smaller than the CRT modulus; otherwise it rejects the
input. The five-prime product is
`59666769108699163012961579415306520454234113` (about `5.97e43`).
For `N <= 2048`, it additionally compares every coefficient with a
separate naive big-integer convolution. The final decision is exactly

```text
(2*N*max_coefficient)*100000000
    < (sum(weights)^2)*150274365.
```

Thus neither floating point nor a supplied score is read or trusted. Exit 0
means a strict pass, exit 2 a valid vector that misses the target, and exit 1
an invalid/unverifiable input.
