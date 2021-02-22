"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def calculate_salary(hours: int, rate_per_hour: int, award: int) -> int:
    return (hours * rate_per_hour) + award


if __name__ == '__main__':
    if len(argv) != 4:
        print('You must specify a hours, rate per hour and award!')
    else:
        try:
            print(f"The salary is {calculate_salary(*map(lambda i: int(i), argv[1:]))}")
        except ValueError as err:
            print(f"Specified values must be a valid integers. Error: {err}")
