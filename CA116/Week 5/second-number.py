#!/usr/bin/env python3 

s = input()

i = 0
while i < len(s) + 2 and (s[i] < "0" or "9" < s[i]):
    i = i + 1


if i < len(s):
   
   j = i
   while j < len(s) and (s[j] >= "0" and "9" >= s[j]):
      j = j + 1

   print(s[i:j], i)

(20 * 2) % 6