# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def random_list(count):
    ls = []
    while count < 0:
        print("Не корректные данные!")
        count = int(input("\nПовторите ввод: "))

    for i in range(count):
        ls.append(round(uniform(1, count), 2))

    return ls


def res_dif(ls):
    max = min = ls[0] % 1

    for i in range(1, len(ls)):
        num = round(ls[i] % 1, 2)
        if num > max:
            max = num
        elif num < min:
            min = num

    result = round(max - min, 2)
    print(f"Min: {min}, Max: {max}. Difference: {result}")
    return result


worksheet = random_list(int(input("Введите число: ")))
print(worksheet)
print(res_dif(worksheet))