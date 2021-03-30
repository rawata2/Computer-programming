#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    title = tokens[5:]
    a = " ".join(title)
    print(a)
    s = input()

