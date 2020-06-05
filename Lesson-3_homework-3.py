# список
a = int(input("Введите месяц:"))
while True:
    if 1 <= a <= 12:
        seasonlist = ['Зима', "Весна", "Лето", "Осень", 'Зима']
        print(f'{seasonlist[a // 3]}')
    else:
        print("Смею напомнить что в году 12 месяцев")
    break

# словарь
b = int(input("Введите месяц:"))
while True:
    if 1 <= b <= 12:
        seasondict = {0: 'Зима', 1: "Весна", 2: "Лето", 3: "Осень", 4: 'Зима'}
        print(f'{seasondict[b // 3]}')
    else:
        print("Смею напомнить что в году 12 месяцев")
    break
