#!/usr/bin/env python3
#lines = ['cinema iceman', 'dog god', 'house car', 'stub buts', 'angel glean', 'aangl angel', 'a aardvark', 'aardvark a']

import sys

def anagram(left, right):

    for char in left:
        if char in right:
            right = right.replace(char, "", 1)
        else:
            return False
    return right == ''

for i in sys.stdin:
    sep = i.strip().split()
    (left, right) = sep
    func = anagram(left, right)
    print(func)
