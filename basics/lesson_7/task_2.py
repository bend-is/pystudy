"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloth_expense(self) -> float:
        ...


class Coat(Clothes):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    @property
    def cloth_expense(self) -> float:
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.height = height

    @property
    def cloth_expense(self) -> float:
        return 2 * self.height + 0.3


if __name__ == '__main__':
    c = Coat(name="trench-coat", size=78)
    s = Suit(name="sport-suit", height=15)

    print(f"Cloth expense for {c.name} with {c.size} size - {c.cloth_expense}")
    print(f"Cloth expense for {s.name} with {s.height} height - {s.cloth_expense}")
