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
        return "Not registered as module "

    def average(self):
        total_marks = 0
        if len(self.marks) > 0:
            for key, value in self.marks.items():
                total_marks += value
            return total_marks / len(self.marks)
        return total_marks

    def __str__(self):
        return "Name: {}\nAddress: {}\nID: {}\nAverage mark: {:.2f}".format(self.name, self.address, self.sid, self.average())

    def __eq__(self, other):
        return self.average() == other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __gt__(self, other):
        return self.average() > other.average()
