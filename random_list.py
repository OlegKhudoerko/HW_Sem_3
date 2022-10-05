from random import sample


def random_list(count):
    while count < 0:
        print("Не корректные данные!")
        count = int(input("\nПовторите ввод: "))

    ls = sample(range(count), count)
 
    return ls
