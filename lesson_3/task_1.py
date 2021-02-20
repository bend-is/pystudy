"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
from typing import Union


def divider(a: int, b: int) -> Union[float, None]:
    if b == 0:
        print("Division by zero!")
        return
    return a / b


if __name__ == '__main__':
    print(divider(
        int(input("Enter first number: ")),
        int(input("Enter second number: "))
    ))
