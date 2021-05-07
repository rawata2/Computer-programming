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

    def __str__(self):
        result = ""
        for student in self.class_list:
            result += student.retToClass()
        return result

    def least_popular_module(self):
        module_list = []
        for student in self.class_list:
            for key, value in student.marks.items():
                module_list.append(key)

        iterate = list(set(module_list))
        least = float("inf")
        required_module = module_list[0]
        for module in iterate:
            if least > module_list.count(module):
                least = module_list.count(module)
                required_module = module

        return required_module


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

    def retToClass(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\n"

    def __str__(self):
        return "Name: {}\nAddress: {}\nID: {}\nAverage mark: {:.2f}\n".format(self.name, self.address, self.sid,
                                                                              self.average())

    def __eq__(self, other):
        return self.average() == other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __gt__(self, other):
        return self.average() > other.average()
