#!/usr/bin/env python3


import sys

list = []

for line in sys.stdin:
    list.append(line.strip())


def fourA(c):
    return len([letter for letter in c if "a" in letter.casefold()])


def twoormoreQ(c):
    return len([letter for letter in c if "q" in letter.casefold()])


def anagram(c):
    if c == "angle":
        return
    toCheck = c.lower()
    for char in "angle":
        toCheck = toCheck.replace(char, "", 1)
    if len(toCheck) > 0:
        return False
    else:
        return True

print(f'Words containing 17 letters: {[c for c in list if len(c) == 17]}')
print(f'Words containing 18+ letters: {[c for c in list if len(c) >= 18]}')
print(f'Words with 4 a\'s: {[c for c in list if fourA(c) == 4]}')
print(f'Words with 2+ q\'s: {[c for c in list if twoormoreQ(c) >= 2]}')
print(f'Words containing cie: {[c for c in list if "cie" in c]}')
print(f'Anagrams of angle: {[c for c in list if len(c) == len("angle") and anagram(c)]}')
