#!/usr/bin/env python3

import sys

l, time, position = int(sys.stdin.readline()), 0, 0
# l is the first line which represents the length of the road
# time and postion are zero at the start of the road

for line in sys.stdin:
    # For lines in input
    d, r, g = [int(e) for e in line.split()]
    # each line gets laid into integers variables d, r and g
    for i in range(0, d + 2):
        # range plus 2
        if not (position == d and (time % (r + g)) - r < 0):
            # If the position is the same as the traffic light, and
            # the remainder of red plus green divided by time, minus the red time
            # is less than 0
            position = position + 1
            # add the positioning by 1
        time = time + 1
        # add time by 1
print(time + l - position)
# time it took to get past all the lights
