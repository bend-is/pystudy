"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
import json


class NotEnoughWarehouseItems(Exception):
    def __init__(self, text: str):
        self.text = text


class Warehouse:
    def __init__(self):
        self.storage = {
            "reserve": {},
            "departments": {}
        }

    def add(self, *items) -> None:
        """
        Args:
            items: list of items to add
        Returns:
            None
        Raises:
            TypeError: if items contains a non OfficeEquipment object
        """
        for item in items:
            if not isinstance(item, OfficeEquipment):
                raise TypeError(f"Wrong type specified. Expected {OfficeEquipment.__name__} got {type(item).__name__}")

        reserve = self.storage["reserve"]

        for item in items:
            if not reserve.get(item.get_type()):
                reserve[item.get_type()] = []

            reserve[item.get_type()].append(item)

    def move_to_department(self, department_name: str, item_type: str, count: int = 1) -> None:
        """
        Args:
            department_name: name of the department to move
            item_type: item type to move (e.g. printer, scanner)
            count: count of items to move
        Returns:
            None
        Raises:
            TypeError: if wrong arg types was specified
            ValueError: if count is a less than zero
            NotEnoughWarehouseItems: if in the warehouse specified item type is missing or not enough
        """
        if type(department_name) != str or type(item_type) != str or type(count) != int:
            raise TypeError("Wrong arg types. Valid type is department_name: str, item_type: str, count: int")

        if count < 1:
            raise ValueError("Count arg must be greater than zero")

        departments = self.storage["departments"]

        if not departments.get(department_name):
            departments[department_name] = []

        items = self.storage["reserve"].get(item_type)

        if not items or len(items) < count:
            raise NotEnoughWarehouseItems(f"Not enough {item_type} in the warehouse to move")

        for _ in range(count):
            departments[department_name].append(items.pop())

    def __str__(self):
        return json.dumps(self.storage, default=lambda i: i.__dict__, indent=4)


class OfficeEquipment:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @classmethod
    def get_type(cls) -> str:
        """
        Returns:
            type of office equipment e.g. printer
        """
        return cls.__name__.lower()

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, color_type: str, printer_type: str):
        super().__init__(brand, model)
        self.color_type = color_type
        self.printer_type = printer_type


class Scanner(OfficeEquipment):
    def __init__(self, brand: str, model: str, scanner_type: str):
        super().__init__(brand, model)
        self.scanner_type = scanner_type


class Xerox(OfficeEquipment):
    def __init__(self, brand: str, model: str, xerox_type: str):
        super().__init__(brand, model)
        self.xerox_type = xerox_type


if __name__ == '__main__':
    wh = Warehouse()

    wh.add(
        Scanner("Sony", "E231", "3D"),
        Scanner("Sony", "F231", "3D"),
        Xerox("JB", "K23K.2", "simple"),
        Scanner("Samsung", "S1234", "images"),
        Printer("HP", "C300", "colored", "simple"),
        Printer("HP", "P300", "black-white", "laser"),
    )

    moves = [
        ("data-since", Printer.get_type()),
        ("teaches", Xerox.get_type(), 20),
        ("data-scanners", Scanner.get_type(), 2),
    ]

    for move in moves:
        try:
            wh.move_to_department(*move)
        except NotEnoughWarehouseItems as e:
            print(e)

    print(wh)
