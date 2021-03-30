#!/usr/bin/env python3

import sys
line = sys.stdin.readlines()

for char in sys.stdin:
    word, rotate = char.split()
    rotate = int(rotate)
    rotate = rotate % len(word)
    print(word[-rotate:] + word[:-rotate])


        
       
        