#!/usr/bin/env python3
#Standard input consists of two positive integers, 
# n
# and 
# m respectively.
# Write a Python script named hailstone-sequence-1.py which outputs the n terms of the Hailstone sequence beginning with m
# input 5 , 11

n = int(input())
m = int(input())

i = 0
while n > 0:
    if n % 2 == 0:
      n = n / 2
      print(n)
    else:
      n = (3 * i) + 1
      print(n)
    