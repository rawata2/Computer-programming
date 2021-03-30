#!/usr/bin/env python3

s = input()
total = 0
i = 0


while s != "end":
    tokens = s.split()
    if tokens[2] == s:
     total = total + tokens[2]
     i = i + 1
    s = input()
print(total)
