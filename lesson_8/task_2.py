"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivision(Exception):
    def __init__(self, text: str):
        self.text = text


def div(a: int, b: int) -> float:
    if b == 0:
        raise MyZeroDivision("Division by zero")

    return a / b


if __name__ == '__main__':
    while True:
        t = input('Enter a divider: ')

        if t == '':
            break
        if not t.isdigit():
            continue

        try:
            print(div(1000, int(t)))
        except MyZeroDivision as e:
            print(e)
