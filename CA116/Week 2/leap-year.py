#!/usr/bin/env python3 
year = int(input())

leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if leap_year == 1:
  print(True)
else:
  print(False)