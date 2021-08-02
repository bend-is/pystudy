"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __switch_map = {
        'красный': ('желтый', 7),
        'желтый': ('зеленый', 2),
        'зеленый': ('красный', 5),
    }

    def __init__(self, color: str = 'красный'):
        if color not in self.__switch_map.keys():
            raise ValueError(f"Wrong color specified. Allowed colors: {', '.join(self.__switch_map.keys())}")
        self.__color = color

    def running(self) -> None:
        while True:
            print(self.__color)
            self.__color, sleep_time = self.__switch_map[self.__color]
            sleep(sleep_time)


if __name__ == '__main__':
    t = TrafficLight()
    t.running()
