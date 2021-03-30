#!/usr/bin/env python3

import sys
lines = sys.stdin.read()

def splitted(words):
    s = words.split()
    return len(s)

print(splitted(lines))
