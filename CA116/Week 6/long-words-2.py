#!/usr/bin/env python3

if __name__ == "__main__": 
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
x = True
while i < len(a) and x:
    if len(a[i]) >= 6:
       print(a[i])
       x = False
    i = i + 1