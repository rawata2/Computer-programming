#!/usr/bin/env python3
import sys

for s in sys.stdin:
    s = s.strip()
    chop = s[1:len(s) - 1]
    if len(chop) > 0:
      print(chop)
