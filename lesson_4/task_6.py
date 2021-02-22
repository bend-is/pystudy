"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle, count
from random import sample


def func_a(initial: int, limit: int = None):
    if limit is None:
        limit = initial + 10

    for elem in cycle(range(initial, limit + 1)):
        yield elem
        if elem == limit:
            return


def func_b(initial: list = None, max_repeat: int = 3):
    counter = count()
    if initial is None:
        initial = sample(range(30), 5)

    for elem in cycle(initial):
        if elem == initial[0] and next(counter) == max_repeat:
            break
        yield elem


if __name__ == '__main__':
    print(f"Func a: {[v for v in func_a(initial=3, limit=10)]}")
    print(f"Func b: {[v for v in func_b(initial=[1, 2, 3, 4, 5], max_repeat=4)]}")
