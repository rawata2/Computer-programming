#!/usr/bin/env python3

import sys


def l2d(file):
  lines = file.readlines()
  dict = {}
  keys = lines[0].split()
  values = lines[1].split()
  i = 0
    for word in keys:
      dict[word] = values[i]
      i = i + 1
    return dict


    # read line from fin (keys)
    # read line from fin (values)
    # use while loop to traverse keys and values
    # for each key value and the corresponding mapping to d
    # return d
    # *** no code outside function ***