import itertools

for i in itertools.count(int(input('Введите стартовое число '))):
    print(i)
b = a()
x = 0
for i in b:
    if x < 15:
        print(i)
        x += 1
    else:
        break