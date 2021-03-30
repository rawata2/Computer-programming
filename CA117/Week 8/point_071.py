#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

def main():
    p1 = Point()
    p2 = Point(3,0)
    print('{:.1f}'.format(p1.distance(p2)))
    print('{:.1f}'.format(p2.distance(p1)))
    p3 = Point(3,0)
    p3.reflect()
    print('{:.1f}'.format(p3.distance(p2)))
    p4 = Point(1,1)
    print('{:.1f}'.format(p4.distance(p1)))

if __name__ == '__main__':
    main()