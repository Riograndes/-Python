import functools


def func(i, i1):
    return i * i1


print(f'Результат: {functools.reduce(func, [i for i in range(99, 1001) if i % 2 == 0])}')
