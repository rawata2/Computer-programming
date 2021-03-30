#!/usr/bin/env python3

s = input()
n = int(input())

a = s + "-" + s
b = "-" + s
print((a + b + a) * n // 2)