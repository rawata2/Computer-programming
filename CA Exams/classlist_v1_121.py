#!/usr/bin/env python3
class Classlist(object):

    class_list = []

    def add(self, student):
        self.class_list.append(student)

    def remove(self, student_id):
        for index, student in enumerate(self.class_list):
            if student.sid == student_id:
                self.class_list.pop(index)
                break

    def lookup(self, student_id):
        for student in self.class_list:
            if student.sid == student_id:
                return student
        return None


class Student:
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
