#!/usr/bin/env python3

import sys  
str1 = sys.stdin.readlines()

l1 = []
for i in str1:
    stripped = line.strip()
    chars = list(stripped)

    i = 1
    while i < len(chars):
        chars[i-1], chars[i] = chars[i], chars[i-1]
        i += 2
    print(''.join(chars))
