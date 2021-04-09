#!/usr/bin/env python3

def power(x, y):
    if y == 0:
         return 1
    else:
        return x * power(x, y - 1)

def main():
    print(power(2, 3))
    print(power(4, 4))
    print(power(2, 32))
    print(power(10, 3))
    print(power(8, 0))

if __name__ == '__main__':
    main()
