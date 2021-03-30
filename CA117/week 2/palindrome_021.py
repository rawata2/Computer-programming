#!/usr/bin/env python3
#lines = ["Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.", "Step on no cats.", "Able was I ere I saw Elba.", "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod."]

import sys

def palindrome(s):

  keep = []
  for char in s:
      if char.isalnum():
        keep.append(char)
  return keep == keep[::-1]

for words in sys.stdin:
  words = words.strip().lower()
  print(palindrome(words))
