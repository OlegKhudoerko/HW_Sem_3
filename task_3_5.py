# 5. ** Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibonacci(count):
    a = b = count//count
    ls = [0]

    for i in range(count):
        ls.append(a)
        ls.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return ls


print(*fibonacci(abs(int(input("Введите число: ")))))
