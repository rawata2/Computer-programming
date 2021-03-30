#!/usr/bin/env python3 

mark = int(input())

if mark >= 70:
    print("first", True)
else:
    print("first", False)

if mark >= 50 and mark <= 69:
    print("second", True)
else:
    print("second", False)

if mark >= 40 and mark <= 49:
    print("third", True)
else:
    print("third", False)

if mark < 40:
    print("fail", True)
else:
    print("fail", False)
