# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования 
# встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def calc_bin(d):
 
    b, t = 0, 1

    while d > 0:
        b = b+d % 2*t
        t *= 10
        d //= 2
    return b

num = int(input("Введите число = "))
print(calc_bin(num))