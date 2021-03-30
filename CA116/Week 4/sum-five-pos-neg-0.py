
#!/usr/bin/env python3

positive_total = 0
negative_total = 0
n = int(input())

while n != 0:
    if n > 0:
        positive_total = positive_total + n
    else:
        negative_total = negative_total + n
    n = int(input())  
print(negative_total, positive_total)

