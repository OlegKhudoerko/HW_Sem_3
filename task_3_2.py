# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random_list import random_list as ls_r


def mult(count):
    ls_mult = []
    for i in range((len(count))//2):
        ls_mult.append(ls[i] * ls[-i-1])

    if len(count) % 2 != 0:
        ls_mult.append(ls[((len(count))//2)])

    return ls_mult


ls = ls_r(int(input("Введите число: ")))
print(ls, '\n', mult(ls))
