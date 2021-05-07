#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, IDnumber):
        self.name = name
        self.address = address
        self.sid = IDnumber
        self.marks = {}

    def add_mark(self, module, mark):
        self.marks.update({module: mark})

    def get_mark(self, module):
        mark = self.marks.get(module)
        if mark is not None:
            return mark
        return "Not registered for module"

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1.get_mark('CA103'))

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2.get_mark('CA117'))

if __name__ == '__main__':
    main()
