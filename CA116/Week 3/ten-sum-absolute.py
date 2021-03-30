#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
   x = int(input())
   if x >= 0:
      total = total + x    
   else:
      total = total + x * -1
   i = i + 1
print(total)
