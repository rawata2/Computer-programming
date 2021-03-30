#!/usr/bin/env python3

line = '0 4 5 7 1 0 8 10 2 4' , '4 5 7 1 0 2 1'

x = {0: 'zero', 1: 'one', 2:'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

output= [x[int(i)] for i in line.split()]
print(' '.join(output))

# num2word = [x[int(i)] for i in line.split(' ')]
# print(' '.join(num2word))