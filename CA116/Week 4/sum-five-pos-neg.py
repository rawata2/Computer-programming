
#!/usr/bin/env python3

i = 0
n = 5
positive_total = 0
negative_total = 0

while i < n:
    x = int(input())
    if x > 0:
        positive_total = positive_total + x
    else:
        negative_total = negative_total + x
    i = i + 1
print(negative_total, positive_total)
