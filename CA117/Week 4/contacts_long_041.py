#!/usr/bin/env python3
#!/usr/bin/env python3
import sys

def contacts(filename):
    dict = {}
    with open(filename, 'r') as fin:
        for line in fin:
            name, number, email = line.strip().split()
            dict[name] = number
            dict[name] = email
    return dict

dict = contacts(sys.argv[1])
email = contacts(sys.argv[1])


for line in sys.stdin:
    name = line.strip()
    print(f'Name: {name}')
    if name in dict:
        print(f'Phone: {dict[name]}')
        print(f'Email: {email[name]}')
    else:
        print('No such contact')


# import sys

# contacts = {i.split()[0]: i.split()[1]
#             for i in open(sys.argv[1]).readlines()}
# email = {i.split()[0]: i.split()[2]
#             for i in open(sys.argv[1]).readlines()}

# for name in sys.stdin:
#     name = name.strip()
#     if name in contacts:
#         print(f'Name: {name}')
#         print(f'Phone: {contacts[name]}')
#         print(f'Email: {email[name]}')
#     else:
#         print(f'Name: {name}')
#         print("No such contact")