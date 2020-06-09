from random import randint

list = [randint(1, 100) for i in range(20)]
nlist = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
print(f'Исходный список: {list}')
print(f'Новый список: {nlist}')
