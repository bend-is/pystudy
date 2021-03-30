"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def get_class_name(self) -> str:
        return self.__class__.__name__

    def go(self) -> None:
        print(f"The car is moving now.")

    def stop(self) -> None:
        print("The car is stopped now.")

    def turn(self, direction: str) -> None:
        print(f"The car changed it direction to {direction}.")

    def show_speed(self) -> None:
        print(f"The car current speed is {self.speed}.")


class TownCar(Car):
    def show_speed(self) -> None:
        super().show_speed()
        if self.speed > 60:
            print("The car is moving to fast!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> None:
        super().show_speed()
        if self.speed > 40:
            print("The car is moving to fast!")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    directions = ['Left', 'Right']
    town_car = TownCar(70, 'green', 'bmw x7', False)
    sport_car = SportCar(90, 'black', 'Porsche panamera', True)
    work_car = WorkCar(42, 'blue', 'Lada 2106', False)
    police_car = PoliceCar(99, 'white', 'Kio Optima', False)

    for car in [town_car, sport_car, work_car, police_car]:
        print(f"{car.get_class_name()} attributes: "
              f"speed - {car.speed}, color - {car.color}, name - {car.name}, police - {car.is_police}")
        print("Start actions!!!")
        car.go()
        car.turn(random.choice(directions))
        car.show_speed()
        car.stop()
        print()
