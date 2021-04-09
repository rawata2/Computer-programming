from math import sqrt

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

def calculator(line):

    s = Stack()

    for token in line.split():
        if token not in binops and token not in uniops:
            s.push(float(token))
        elif token in uniops:
            arg = s.pop()
            s.push(uniops[token](arg))
        elif token in binops:
            rarg = s.pop()
            larg = s.pop()
            s.push(binops[token](larg, rarg))
        else:
            raise IndexError

    if len(s) != 1:
        raise IndexError

    return s.pop()
