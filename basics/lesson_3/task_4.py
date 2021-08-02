"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""
from typing import Union


def get_num_pow_v1(x: int, y: int) -> Union[int, float]:
    return x ** y


def get_num_pow_v2(x: int, y: int) -> Union[int, float]:
    if y == 0:
        return 1

    count = y if y >= 0 else y * -1
    res = x

    for _ in range(1, count):
        res *= x

    return res if y >= 0 else 1 / res


if __name__ == '__main__':
    n_1 = n_2 = 0

    while n_1 <= 0:
        n_1 = int(input("Enter a positive number: "))
    while n_2 >= 0:
        n_2 = int(input("Enter a negative number: "))

    print(f"{n_1}^{n_2} is {get_num_pow_v1(n_1, n_2)} (v1)")
    print(f"{n_1}^{n_2} is {get_num_pow_v2(n_1, n_2)} (v2)")
