#!/usr/bin/env python3
list = ['valerie.maguire2@mail.dcu.ie', 'fred.quinn33@mail.dcu.ie', 'jimmy.clancy5@mail.dcu.ie']

for i in list:
    names = i.split('.', 1)
    lastNameNum = names[1][0: names[1].index("@")].capitalize()
    print(names[0].capitalize(), "".join([i for i in lastNameNum if not i.isdigit()]))
    
