#!/usr/bin/env python3

import sys

line1, line2 = [line.strip() for line in sys.stdin]
print(line1)
print(line2)

output = ''
for i,j in zip(line1, line2):
    output += '-' if i==j else '*'
    
print(output)
