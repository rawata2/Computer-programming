#!/usr/bin/env python3
import sys

list = sys.stdin

for i in list:
  nums = i.split()
  base = int(nums[1])
  toConvert = nums[0]
    
  total = 0
  while i < len(toConvert):
    total = total + int(toConvert[len(toConvert) - i - 1]) * (base ** i)
    i = i + 1
 print(total)



 #hel