#!/usr/bin/env python3

list = [1, 2, 3, 4, 10]
from math import pi

for i in list:
    pos = int(i)
    print(f'{pi:.{pos}f}')