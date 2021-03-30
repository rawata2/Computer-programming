#!/usr/bin/env python3

import calendar
lines = ['1 3 1990',
        '12 10 1992',
        '9 5 1995']

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

poem = ["Monday's child is fair of face",
        "Tuesday's child is full of grace",
        "Wednesday's child is full of woe",
        "Thursday's child has far to go",
        "Friday's child is loving and giving",
        "Saturday's child works hard for a living",
        "Sunday's child is fair and wise and good in every way"
        ]
        






















#!/usr/bin/env python3

# import sys
# import calendar

# lines = ["Monday's child is fair of face", "Tuesday's child is full of grace",
# "Wednesday's child is full of woe", "Thursday's child has far to go", 
# "Friday's child is loving and giviing", "Saturday's child works hard for a living", 
# "Sunday's child is fair and wise and good in every way"]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# birthdays = sys.stdin.readlines()

# try:
#   for birth in birthdays:
#     birth = birth.strip().split()
#     if int(birth[0]) <= 31 and int(birth[1]) <= 12 and int(birth[2]) <= 2021:
#       day, month, year = birth
#       day_num = calendar.weekday(int(year), int(month), int(day))
#       print(f'You were born on a {days[day_num]} and {lines[day_num]}.')
#     else:
#       print("Not a birthday")
# except ValueError:
#   print("Invalid inputs")