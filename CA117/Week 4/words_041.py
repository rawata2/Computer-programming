from string import punctuation
import sys

def count_words(fin):
    d = {}
    for line in fin:
        w1 = line.lower().split()
        for w in w1:
            w = w.strip(punctuation)
            if not w:
                continue
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
    return d
d = count_words(sys.stdin)
for k, v in sorted(d.items()):
  print(f'{k} : {v}')
