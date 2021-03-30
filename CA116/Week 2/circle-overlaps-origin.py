#!/usr/bin/env python3

center_x, center_y = int(input())
x, y = int(input())
r = int(input())

if (x - center_x)**2 + (y - center_y)**2 == r**2:
    print("true")
else:
    print("False")

