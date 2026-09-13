#!/bin/sh
set -eu

c++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic \
  src/verifier.cpp -o experiments/verifier_core
python3 src/verify_certificate.py \
  --certificate certificates/n8_certificate.json \
  --core experiments/verifier_core \
  --core-source src/verifier.cpp
