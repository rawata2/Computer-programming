#!/usr/bin/env python3

import sys

a,b,c = sys.stdin.read().strip().split()
a,b,c = int(a), int(b), int(c)

diff1, diff2, diff3 = 0, 0, 0
if a < b:
    diff1 = b - a
else:
    diff1 = a - b

if b < c:
    diff2 = c - b
else:
    diff2 = b - c

if a < c:
    diff3 = c - a
else:
    diff3 = a - c

if diff1 < diff2 and diff1 < diff3:
    print(diff1)
elif diff2 < diff3:
    print(diff2)
else:
    print(diff3)
    