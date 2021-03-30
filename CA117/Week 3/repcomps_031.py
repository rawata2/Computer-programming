#!/usr/bin/env python3

import sys

def multiples(num):
    return ['X' if n % 3 == 0 else n for n in range(1, num)]


for n in sys.stdin:
    num = int(n) + 1
    print(f'Multiples of 3 replaced: {multiples(num)}')
