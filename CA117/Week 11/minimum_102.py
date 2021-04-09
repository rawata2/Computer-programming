#!/usr/bin/env python3

def minimum(arr):
    if not arr[1:]:
        return arr[0]
    else:
        return arr[0] if arr[0] < minimum(arr[1:]) else minimum(arr[1:])


def main():
    min = None
    print(minimum([6, 5, 1, 3, 4]))
    print(minimum([6, 5, 11, 3, 4]))
    print(minimum([6, 15, 11, 13, 14]))
    print(minimum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
