#!/usr/bin/env python3

n = 10
smallest = int(input())

i = 0
while i < n - 1:
    x = int(input())
    if smallest > x and x >= 1:
       smallest = x
    i = i + 1
print(smallest)