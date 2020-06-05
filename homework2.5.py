list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
num = int(input("Введите число:"))
a = 0
for b in list:
    if num < b:
        a += 1
list.insert(a, num)
print(list)