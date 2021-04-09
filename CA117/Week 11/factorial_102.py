#!/usr/bin/env python3

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(12))

if __name__ == '__main__':
    main()
