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

import random

def sum__odd(count):

    if count < 0:
        return "Не корректные данные!"

    ls = random.sample(range(count), count)
    sum = 0

    for i in range(0,count, 2):
        sum += ls[i]
            
    print(ls)
    return sum

num = int(input("Введите число: "))
print(sum__odd(num))
