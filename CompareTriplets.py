import sys


a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

scores = [0,0]

for i in range(0, 3):
    x = a[i] - b[i]
    if x > 0:
        scores[0] += 1
    elif x < 0:
        scores[1] += 1

print "%s %s" % (scores[0], scores[1])