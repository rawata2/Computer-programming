#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]
for line in lines:
    a,b,c = line.split()
    flag = 0
    for operation in ['+','-','*','/']:
        if eval(a+operation+b)==int(c) or eval(b+operation+a)==int(c):
            print('yes')
            flag = 1
            break
    if flag==0: print('no')
