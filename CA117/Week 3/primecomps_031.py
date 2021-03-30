#!/usr/bin/env python3

import sys

for n in sys.stdin.read().splitlines():
    nums = [int(i) for i in range(2, int(n) + 1)]
    print(f'Primes: {[n for n in nums if all(n % y != 0 for y in range(2, n))]}')
