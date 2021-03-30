#!/usr/bin/env python3
import sys
line = sys.stdin.readlines()

x = {0: 'zero', 1: 'one', 2:'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}            


list1 = []
for i in line:
    splitted = i.strip().split()
    for a in splitted:
        print(' '.join(x[int(a)] for a in splitted if int(a) in x))

# for i in line:
#   splitted = i.strip().split()
#   print(' '.join(x[int(a)] if int(a) in x else "unknown" for a in splitted))
# print(' '.join(x.get(int(a), "unknown") for a in splitted))


# for i in line:
#     splitted = i.strip().split()
#     for a in splitted:
#        print(' '.join(x[int(a)] for a in splitted if int(a) in x))

# for i in line:
#     splitted = i.strip().split()
# for a in splitted:
#     if int(a) in x:
#         print(' '.join(x[int(a)]))
#     else:
#         print("unkown")