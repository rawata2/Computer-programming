#!/liner/bin/env python3

timetable = []
line = input()

while line != "end":
    timetable.append(line)
    line = input()
    
i = 0
n = input()

while i < len(timetable):
    token = timetable[i].split()
    if token[0] == n:
        day = token[0:]
        print( " ".join(day))
        i = i + 1
        
    