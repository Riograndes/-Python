import random

list = [random.randint(1, 20) for i in range(20)]
nlist = [a for a in list if list.count(a) < 2]
print(nlist)
