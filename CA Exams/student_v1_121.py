#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, IDnumber):
      self.name = name
      self.address = address
      self.sid = IDnumber

    def __str__(self):
      return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"


def main():
  s1 = Student('Boris Spassky', 'Dublin', 17345654)
  s2 = Student('Bobby Fischer', 'Cork', 17907321)

  assert(s1.name == 'Boris Spassky')
  assert(s1.address == 'Dublin')
  assert(s1.sid == 17345654)

  print(s1)
  print(s2)

if __name__ == '__main__':
  main()
