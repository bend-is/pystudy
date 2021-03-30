"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname,position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.surname = surname
        self.position = position
        self.name = name
        if type(income.get("wage")) not in [int, float] or type(income.get("bonus")) not in [int, float]:
            raise ValueError("Income must contains wage and bonus and must be a numeric values")
        self._income = income


class Position(Worker):
    def get_full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def get_total_income(self) -> float:
        return sum(self._income.values())


if __name__ == '__main__':
    test_cases = [
        {"name": "Dima", "surname": "Dolgov", "position": "Taskmaster", "income": {"wage": 78000, "bonus": 300}},
        {"name": "Artur", "surname": "Morgan", "position": "Bounty Hunter", "income": {"wage": 99999, "bonus": 2330}},
    ]

    for test_case in test_cases:
        p = Position(test_case["name"], test_case["surname"], test_case["position"], test_case["income"])

        assert test_case["name"] == p.name
        assert test_case["surname"] == p.surname
        assert test_case["position"] == p.position
        assert f"{test_case['surname']} {test_case['name']}" == p.get_full_name()
        assert sum(test_case["income"].values()) == p.get_total_income()

        print(f"{p.get_full_name()} earned total {p.get_total_income()}")
