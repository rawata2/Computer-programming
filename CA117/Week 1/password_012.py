list = ["256", "abc","aBc" ,"1aBc2", "^@())($$$", "^@a1())B($43$$"]
 
#!/usr/bin/env python3

for i in list:
    i = i.rstrip()
    strength = [False] * 4
    total = 0
    for char in i:
        if char.isdigit():
            strength[0] = True
        elif char.isupper():
            strength[1] = True
        elif char.islower():
            strength[2] = True
        else:
            strength[3] = True
    for val in strength:
        if val:
            total += 1

    print(total)
