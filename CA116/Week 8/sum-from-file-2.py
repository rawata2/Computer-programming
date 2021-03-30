# WHAT I DID
import sys
with open("numbers.txt") as a:
  lines = a.readlines()

i = 0
args = sys.argv[1:]
total = 0

while i < len(args):
    total += int(args[i])
    i = i + 1
print(total)

# WHAT IT SHOULD HAVE BEEN
#!/usr/bin/env python3

import sys

args = sys.argv[1:]

nums = []

i = 0
while i < len(args):
  with open(args[i]) as f:
    nums += f.readlines()
  i += 1

total = 0
i = 0
while i < len(nums):
  total += int(nums[i])
  i += 1

print(total)