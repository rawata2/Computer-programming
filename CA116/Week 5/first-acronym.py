#!/usr/bin/env python3 

s = input()

i = 0
while i < len(s) and (s[i] < "A" or "Z" < s[i]):
    i = i + 1

if i < len(s):
   
   j = i
   while j < len(s) and (s[j] >= "A" and "Z" >= s[j]):
     j = j + 1

   print(s[i:j], i)