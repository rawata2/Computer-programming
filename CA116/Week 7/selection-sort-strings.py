#!/usr/bin/env python3
a = []
s = input()

while s != "end":
  a.append(int(s))
  s = input()

p = 0
j = 1
i = 0

while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1
# list has been sorted

i = 0
n = int(input())
even = (n / 2) + (n / 2 + 1)
odd = (n + 1 / 2)

while i < len(a):
   if even:
       print(n)
   elif odd:
       print(n)
   i = i + 1