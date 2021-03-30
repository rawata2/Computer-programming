#!/usr/bin/env python3

n = int(input())

i = 0
x = 0
y = 1

while x < n:
    print(x)
    xy = x + y
    x = y
    y = xy
    i = i + 1

