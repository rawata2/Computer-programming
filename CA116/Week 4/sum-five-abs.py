
#!/usr/bin/env python3

i = 0
n = 5
total = 0

while i < n:
    x = int(input())
    if x > 0:
        total = total + x 
    else:
        total = total + x * -1
    i = i + 1
print(total)