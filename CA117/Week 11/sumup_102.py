#!/usr/bin/env python3

def sumup(n):
    if int(n) == 0:
        return 0
    else:
        return int(n) + sumup(int(n) - 1)


def main():
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))

if __name__ == '__main__':
    main()
