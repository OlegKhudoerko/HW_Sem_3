# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8
# ---------------------Вариант 1----------------------------------------------------
from random import sample


def sum__odd(count):

    if count < 0:
        return "Не корректные данные!"

    ls = sample(range(count), count)
    sum = 0

    for i in range(0, count, 2):
        sum += ls[i]

    print(ls)
    return sum


num = int(input("Введите число: "))
print(sum__odd(num))

# ---------------------Вариант 2----------------------------------------------------
from random_list import random_list as ls_r


def sum_odd(count):
    sum = 0
    for i in range(0, len(count), 2):
        sum += ls[i]
    return sum


ls = ls_r(int(input("Введите число: ")))
print(ls, '\n', sum_odd(ls))
