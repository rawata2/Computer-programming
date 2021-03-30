#!/usr/bin/env python3

x = int(input())
y = int(input())
z = int(input())

if x == y and x == z:
  print("equilateral")
elif x == y or x == z:
  print("isosceles")
else:
  print("scalene")