#!/usr/bin/env python3 

a = input()
b = input()
c = input()

if len(a) > len(b) and len(a) > len(c):
    print(a)
elif len(b) > len(a) and len(b) > len(c):
    print(b)
elif len(c) > len (a) and len(c) > len(b):
    print(c)