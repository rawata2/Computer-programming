#!/usr/bin/env/python3
list = ['strawberry','strawberry fields','strawberry fields forever']


for i in list:
    splitted = i.strip().split()
    camel = []
    for a in range(len(splitted) - 1):
        camel.append(splitted[a].lower() + splitted[a][-1].upper())
    print(' '.join(camel))

#remove last lower case letters