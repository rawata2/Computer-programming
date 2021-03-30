#!/usr/bin/env python3 

month = int(input())
day_of_month = int(input()) - 1
day_of_week = (((month - 1) * 30 + day_of_month) % 7) + 1

print(day_of_week)
