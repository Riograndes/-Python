# Задание 1
List = [1, 2.2, (1 + 4j), 'строка', ["список"], (1, 2, 3, 4, 5, 'etc'), set("ste1843ets3814"),
        frozenset("fonzer195oez5f9nr"), True, False, bytes(b'text'), bytearray(b'more text'), None, ]
for ind, el in enumerate(List):
    print(f"{ind}) {el}: {type(el)}")
