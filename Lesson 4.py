def a():
    try:
        a = float(input('Выработка в часах: '))
        b = int(input('Ставка:'))
        c = int(input('Премия:'))
        r = a * b + c
        print(f'#Заработная плата сотрудника  {r}')
    except ValueError:
        return print('Попробуйте ввести в виде числа')


a()
