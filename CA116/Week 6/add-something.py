#!/usr/bin/env python3 

a = []
m = input()
i = 0



while m != "end":
    a.append(int(m))
    m = input()

n = int(input())

while i < len(a):
    a[i] = a[i] + n
    print(a[i])
    i = i + 1
