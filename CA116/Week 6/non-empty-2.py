#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
x = True

while i < len(a) and x:
   if a[i] != "":
      print(a[i])
      x = False
   i = i + 1
      