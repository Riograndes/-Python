a = input("Поле ввода:").split()
for ind, el in enumerate(a, 1):
    print(ind, el) if len(el) <= 10 else print(ind, (el[:10]))
