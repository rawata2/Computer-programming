
lines = "hello, what, how , where, when, 123, ADNnnbf, FHI"
import sys
import string

lines = sys.stdin.readlines()

total = 0
for words in lines:
    if words in string.punctuation:
        print(words)
    for word in :
        total += 1
print(total)

