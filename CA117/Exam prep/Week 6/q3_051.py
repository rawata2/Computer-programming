#!usr/bin/env python3
import sys

def helper(char):
    if char.isupper():
        return c
    return '0'

for line in sys.stdin:
    line = line.strip()
    uppers = ''.join([helper(char) for char in line])
    ul = uppers.split('0')
    print(max(ul, key=len))

