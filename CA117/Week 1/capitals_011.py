#!/usr/bin/env/python3
import sys

for i in sys.stdin:
    i.strip()
    if len(i) > 1:
        ups = i[0].upper() + i[1:-1].lower() + i[-1].upper()
        print(ups)
