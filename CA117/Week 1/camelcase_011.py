# import sys

# for i in sys.stdin:
#   print(i.title()) 

#!/usr/bin/env/python3
#list = ['strawberry','strawberry fields','strawberry fields forever']
import sys

for i in sys.stdin:
    splitted = i.strip().split()
    camel = []
    for a in splitted:
        camel.append(a.capitalize())
    print(' '.join(camel))

