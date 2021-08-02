"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""
from typing import List


def calculate_sum_from_words(words: List[str]) -> int:
    res = 0

    for word in words:
        num = ''.join((letter for letter in word if letter.isdigit()))
        if num != '':
            res += int(num)

    return res


if __name__ == '__main__':
    with open('task_6.txt') as f:
        d = {}

        for line in f:
            words = line.split()
            d[words[0].removesuffix(':')] = calculate_sum_from_words(words[1:])

        print(d)
