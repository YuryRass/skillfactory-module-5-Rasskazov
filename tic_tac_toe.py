# -*- coding: utf-8 -*-

"""Игра в крестики-нолики"""

import os

SIZE = 3
FIELD = [[None for i in range(SIZE)] for j in range(SIZE)] # поле для игры
# победные серии по оси х:
x_win = [
    [0, 1, 2],
    [2, 1, 0],
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2]
]

# победные серии по оси y:
y_win = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]

def print_field(field):
    """
        Печать таблицы 3х3 
        для игры в крестики-нолики
    """
    str_num = 0
    print("  " + " ".join(str(i) for i in range(SIZE)))
    for string in field:
        print("{0} ".format(str(str_num)) + " ".join(el or '-' for el in string))
        str_num += 1
    print()

def get_winner(field):
    """
        Проверка на победителя либо ничью
        Возвращает True, если есть
        победитель либо игра сыграна вничью
    """
    # res - список со всевозможными победными ситуациями:
    res = [[FIELD[y][x] for y, x in zip(y_list, x_list)] for y_list, x_list in zip(y_win, x_win)]
    stop = 0 # для определения ничьи
    for r in res:
        if r == ['0'] * SIZE:
            print_field(field)
            print("Вы победили!")
            return True
        elif r == ['x'] * SIZE:
            print_field(field)
            print("Победил робот")
            return True
        if None not in r:
            stop += 1
    if stop == len(res):
        print_field(field)
        print("Ничья!")
        return True

def robot_step(field):
    """
        Ход робота: в любую не None клетку
    """
    stop = False
    for y in range(SIZE):
        if stop: break
        for x in range(SIZE):
            if field[y][x] is None:
                field[y][x] = 'x'
                stop = True
                break

def tic_tac_toe():
    """
        Игра в крестики-нолики
        Пользователь - нолик
        Робот - крестик
    """
    while True:
        print_field(FIELD)
        print("Ваш ход ноликом (x, y): ")
        x = int(input("x = "))
        y = int(input("y = "))
        if any([x not in range(SIZE),
                y not in range(SIZE),]):
            os.system('cls||clear')
            continue

        if FIELD[y][x] is not None:
            os.system('cls||clear')
            continue
        else:
            FIELD[y][x] = "0"
        os.system('cls||clear')
        # проверка победителя:
        if get_winner(FIELD):
            break
        # ход робота:
        robot_step(FIELD)

if __name__ == "__main__":
    tic_tac_toe()