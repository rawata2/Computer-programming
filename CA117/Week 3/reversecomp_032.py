#!/usr/bin/env python3

def search(q, sorted_l):
        low = 0
        high = len(sorted_l) - 1

        while low <= high:
            mid = (low + high) // 2

            if sorted_l[mid] < q:
                low = mid + 1

            elif sorted_l[mid] > q:
                high = mid - 1

            else:
                return True

        return False

with open('dictionary05') as f:
    l = (line.strip() for line in f)
    s1 = sorted([w.lower() for w in l])
    revs = [w for w in l if len(w) >= 5 and search(w[::-1].lower(), s1)]

    print(revs)
