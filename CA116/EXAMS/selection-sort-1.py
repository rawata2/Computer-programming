#!/usr/bin/env python3

a = [21233, 1906, 32485, 1244, 633]
total = 0

i = 0
while i < len(a):
   total = total + (int(input()) - a[i])
   i = i + 1

print(total)
   
