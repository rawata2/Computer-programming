#!/usr/bin/env python3
import sys

lines = sys.stdin.readlines()

for numbers in lines:
    numbers = [int(n) for n in lines[0].strip().split()]
    numbers = sorted(numbers)
    d, c, b, a = numbers
    
dict = {'A' : a, 'B' : b, 'C' : c, 'D' : d}

order = lines[1]
print(' '.join([str(dict[c]) for c in order.strip()]))

