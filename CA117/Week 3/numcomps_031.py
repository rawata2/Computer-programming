#!/usr/bin/env python3

import sys

def multiples(num):
    return [n for n in range(1, num) if n % 3 == 0]

# def multiples(num):
# return [n for n in range(1, num) if not n % 3]

# lon = [3, 4 , 5 , 6, 7, 8]
    # l = []
    # for n in num:
    #     if n % 3 == 0:
    #         l.append(n)
    # return l

#print(multiples(lon))

def squares(num):
    return [n ** 2 for n in num]


def double4(num):
    return [n * 2 for n in range(1, num) if n % 4 == 0]


def multiples3or4(num):
    return [n for n in range(1, num) if not n % 3 or n % 4 == 0]


def multiples3and4(num):
    return [n for n in range(1, num) if not n % 3 and n % 4 == 0]


for n in sys.stdin:
    num = int(n) + 1
    print(f'Multiples of 3: {multiples(num)}')
    print(f'Multiples of 3 squared: {squares(multiples(num))}')
    print(f'Multiples of 4 doubled: {double4(num)}')
    print(f'Multiples of 3 or 4: {multiples3or4(num)}')
    print(f'Multiples of 3 and 4: {multiples3and4(num)}')
