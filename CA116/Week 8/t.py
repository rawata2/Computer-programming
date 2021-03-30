timetable = []
i = 0
s = input()
while i < len(timetable):
    token = timetable[i].split()
    if token[0] == "2":
        day = token[0:]
        timetable = " ".join(day)
        print(timetable)
        i = i + 1


