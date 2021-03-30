"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class MyException(Exception):
    def __init__(self, text: str, val):
        self.text = text
        self.val = val


def add_digit_to_list(l: list, val: str) -> None:
    if not val.isdigit():
        raise MyException('Wrong type of value', val)

    l.append(int(val))


if __name__ == '__main__':
    lst = []

    while True:
        t = input('Enter a value to add (stop for exit): ')
        if t == 'stop':
            print(lst)
            break
        try:
            add_digit_to_list(lst, t)
        except MyException as e:
            print(e)
