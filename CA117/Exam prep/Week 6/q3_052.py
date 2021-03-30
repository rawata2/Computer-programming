#!/usr.bin/env python3
import sys

def build_dictionary(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            [key, value] = line.strip().split()
            d[key] = int(value)
    return d

def extract_range(d, low, high):
    nd = {}
    for k, v in d.items():
        if v >= low and v <= high:
            nd[k] = v
    return nd

def main():
    pass

if __name__ == '__main__':
    main()

