#!/usr/bin/env python3

import sys 
args = int(sys.argv[1]) + 1
a = []
s = input()
i = 0

while i < len(s) and args != len(a):
    j = i
    while j < len(s) and s[j] != ",":
        j = j + 1
    a.append(s[i:j])
    i = j + 1
print(a[args - 1])