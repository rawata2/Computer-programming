# !/usr/bin/env/python3

import sys

for i in sys.stdin:
  i.strip()
  if len(i) % 2 == 0:
    print("No middle character!")
  elif len(i) <= 1:
    print(i)
  else:
    print(i[len(i) // 2])
