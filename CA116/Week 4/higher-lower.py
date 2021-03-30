#!/usr/bin/env python3
prev = int(input())
curr = int(input())

while prev != curr:
    prev = curr
    curr = int(input())
print("higher", prev)
print("lower" , curr)
