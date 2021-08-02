"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки https://pythonworld.ru/osnovy/peregruzka-operatorov.html.
"""


class Cell:
    def __init__(self, count: int):
        self.count = count

    def make_order(self, row_cell_count: int) -> str:
        res = ["*" * row_cell_count for _ in range(self.count // row_cell_count)]
        rem = self.count % row_cell_count
        if rem != 0:
            res.append("*" * rem)

        return "\n".join(res)

    def __add__(self, other):
        self._check_type(other)
        return Cell(self.count + other.count)

    def __sub__(self, other):
        self._check_type(other)
        if self.count <= other.count:
            raise ValueError("Difference of two cells can't be negative")

        return Cell(self.count - other.count)

    def __mul__(self, other):
        self._check_type(other)
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        self._check_type(other)
        return Cell(self.count // other.count)

    def _check_type(self, obj) -> None:
        """
        Args:
            obj: any object
        Returns:
            None
        Raises:
            ValueError: if obj arg is not a Cell instance
        """
        if type(obj) != type(self):
            raise ValueError(f"Second value must be instance of {type(self)}")


if __name__ == '__main__':
    c_1 = Cell(13)
    c_2 = Cell(6)

    print(f"Cell 1 order:\n{c_1.make_order(5)}\n")
    print(f"Cell 2 order:\n{c_2.make_order(5)}\n")

    print(f"Cell sum:\n{(c_1 + c_2).make_order(5)}\n")
    print(f"Cell sub:\n{(c_1 - c_2).make_order(5)}\n")
    print(f"Cell mul:\n{(c_1 * c_2).make_order(5)}\n")
    print(f"Cell div:\n{(c_1 / c_2).make_order(5)}")
