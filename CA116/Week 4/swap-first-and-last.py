#!/usr/bin/env/python3 
s = input()
i = 0
while i < len(s):
    first = s[0]
    middle = s[1:-1]
    last = s[-1]
    i= i + 1

print(last+middle+first)