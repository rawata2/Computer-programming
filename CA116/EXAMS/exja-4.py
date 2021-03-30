s = input()
i = 0
while i < 0:
    tokens = s.split()
    print(tokens[" "])
    s = input()
    i = i + 1

    #!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    title = tokens[5:]
    a = " ".join(title)
    print(a)
    s = input()