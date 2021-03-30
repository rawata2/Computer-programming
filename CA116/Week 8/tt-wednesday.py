#!/usr/bin/env python3

s = input()

while s != "end":
    tokens = s.split()
    if tokens[0] == "3":
        timetable = tokens[0:]
        a = " ".join(timetable)
        print(a)
    s = input()

