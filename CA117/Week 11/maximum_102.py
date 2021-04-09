#!/usr/bin/env python3

def maximum(arr):
    if not arr[1:]:
        return arr[0]
    else:
        return arr[0] if arr[0] > maximum(arr[1:]) else maximum(arr[1:])

def main():
    max = None
    print(maximum([6, 5, 1, 3, 4]))
    print(maximum([6, 5, 11, 3, 4]))
    print(maximum([6, 15, 11, 13, 14]))
    print(maximum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
