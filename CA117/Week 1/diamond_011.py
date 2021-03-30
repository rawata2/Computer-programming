import sys
lines = sys.stdin.readlines()

for x in lines:
    x = int(x)
    i = 1
    while i < x:
        print((" " * (x - i) + ("* " * i)).rstrip())
        i += 1
    while i > 0:
        print((" " * (x - i) + ("* " * i)).rstrip())
        i -= 1

# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# x5 = int(input())

# for s in range(1,x1 + 1):
#   print((x1 - s) * (' ') + (s * ' *'))
# for s in range(x1 - 1, 0, -1):
#   print((x1 - s) * (' ') + (s * ' *'))
# for s in range(1,x2 + 1):
#   print((x2 - s) * (' ') + (s * ' *'))
# for s in range(x2 - 1,0,-1):
#   print((x2 - s) * (' ') + (s * ' *'))
# for s in range(1,x3 + 1):
#   print((x3 - s) * (' ') + (s * ' *'))
# for s in range(x3 - 1,0,-1):
#   print((x3 - s) * (' ') + (s * ' *'))
# for s in range(1,x4 + 1):
#   print((x4 - s) * (' ') + (s * ' *'))
# for s in range(x4 - 1,0,-1):
#   print((x4 - s) * (' ') + (s * ' *'))
# for s in range(1,x5 + 1):
#   print((x5 - s) * (' ') + (s * ' *'))
# for s in range(x5 - 1,0,-1):
#   print((x5 - s) * (' ') + (s * ' *'))
