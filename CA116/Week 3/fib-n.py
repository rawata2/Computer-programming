#!/usr/bin/env python3

n = int(input())

i = 0
y = 1

while i < n:
    print(i)
    iy = i + y
    i = y
    y = iy
    i = i + 1
