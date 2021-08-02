"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List


class Matrix:
    def __init__(self, data: List[List[int]]):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError("Second value must also be Matrix")
        elif len(self.data) != len(other.data):
            raise ValueError("Matrix must have equal rows count")

        res = []
        for i, row in enumerate(self.data):
            if len(row) != len(other.data[i]):
                raise ValueError("Matrix must have equal columns count")
            res.append([v + other.data[i][j] for j, v in enumerate(row)])

        return Matrix(res)


if __name__ == '__main__':
    m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m_2 = Matrix([[9, 8, 7], [-14, 5, 14], [23, -22, 11]])

    print(f"First matrix:\n{m_1}\n")
    print(f"Second matrix:\n{m_2}\n")
    print(f"Matrix sum:\n{m_1 + m_2}")
