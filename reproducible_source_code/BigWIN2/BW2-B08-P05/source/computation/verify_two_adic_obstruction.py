#!/usr/bin/env python3
"""Finite residue audit for the human 2-adic proof."""
import hashlib
from pathlib import Path

def main():
    assert not [r for r in range(18) if r % 4 == 2 and r % 8 == 4]
    sixth = [u for u in range(8) if (16 + 24*u) % 64 == 0]
    fourth = [u for u in range(8) if (16 + 16*u) % 32 == 0]
    assert sixth == [2]
    assert fourth == [1, 3, 5, 7]
    assert set(sixth).isdisjoint(fourth)
    h=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(f"PASS two-adic residue obstruction; code_sha256={h}")

if __name__ == "__main__": main()
