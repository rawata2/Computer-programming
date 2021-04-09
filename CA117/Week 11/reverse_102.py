#!/usr/bin/env python3

def reverse_list(toRev):
    return [toRev[-1]] + reverse_list(toRev[:-1]) if toRev else []

def main():
    print(reverse_list([1, 2, 3]))
    print(reverse_list([3, 4, 5, 6]))
    print(reverse_list([1, 2]))

if __name__ == '__main__':
    main()
