#!/usr/bin/env python3
list = ['c cat','AC cat','tac caT','ttac cat']

def contains(left, right):
    for word in left:
        if word in right:
            right = right.replace(word, '', 1)
        else:
            return False
    return True

for i in list:
  [left, right] = i.strip().lower().split()
  print(contains(left,right))
  
      
  
