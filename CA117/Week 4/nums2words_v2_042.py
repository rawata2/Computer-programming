#!/usr/bin/env python3
line = ['5 1 2 b 6 7 99 10 8 8 3 4',
'4 3 9 8 2 6 3 0 x 7 1 9 11']

x = {0: 'zero', 1: 'one', 2:'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}            


list1 = []
for i in line:
    splitted = i.strip().split()
    for a in splitted:
        if a.isalpha():
            list1.append("unknown")
        elif int(a) in x:
            list1.append(x[int(a)])    
        else:
            list1.append("unknown")
print(' '.join(list1))


#     splitted = i.strip().split()
#     for a in splitted:
#         if int(a) in x:
#             print(x[int(a)])
#         else:
#             print("unknown")

# print(x.get(int(i), "unknown"))

# for i in sys.stdin:
#     if int(i) in x:
#         print(x[int(i)]))
#     else:
#         print("unknown")
    
    #     print(' '.join(p))
    # else:
    #     print("unknown")

# num2word = [x[int(i)] for i in num.split(' ')]
# print(' '.join(num2word))
# else:
#     print("unknown")