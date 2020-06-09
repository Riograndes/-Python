import itertools
import math


def a():
    for c in itertools.count(1):
        yield math.factorial(c)


b = a()
x = 0
for i in b:
    if x < 15:
        print(i)
        x += 1
    else:
        break
