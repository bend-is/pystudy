"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length: int, width: int):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values")
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self, mass_per_square_meter: int, depth: int) -> float:
        return (self._length * self._width * mass_per_square_meter * depth) / 1000


if __name__ == '__main__':
    r = Road(20, 5000)
    print(f"{r.calculate_asphalt_mass(25, 5)} т")
