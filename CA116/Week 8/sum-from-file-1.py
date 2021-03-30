#!/usr/bin/env python3

with open("numbers.txt") as f:
    lines = f.readlines()

i = 0
total = 0

while i < len(lines):
    total += int(lines[i])
    i = i + 1
print(total)

