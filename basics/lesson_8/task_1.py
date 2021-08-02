"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    _delimiter = "-"

    def __init__(self, date: str):
        parsed = Date.parse_date(date)
        Date.validate(parsed)

        self.date = parsed

    @classmethod
    def parse_date(cls, date: str) -> dict:
        parts = date.split(cls._delimiter)
        if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit() or not parts[2].isdigit():
            return {}

        return {
            "day": int(parts[0]),
            "month": int(parts[1]),
            "year": int(parts[2]),
        }

    @staticmethod
    def validate(date: dict):
        day, month, year = date.get("day"), date.get("month"), date.get("year")

        if not day or day < 1:
            raise ValueError('Day value must be specified and be positive')
        elif not month or month < 1 or month > 12:
            raise ValueError('Month value must be specified and be more than 0 and less then 13')
        elif not year or year < 1:
            raise ValueError('Year value must be specified and be positive')

        max_day_count_in_month_map = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if day > max_day_count_in_month_map[month - 1]:
            raise ValueError(
                f'Day value for {month} month must be less than {max_day_count_in_month_map[month - 1]} or equal'
            )


if __name__ == '__main__':
    print(Date('12-01-2000').date)

    c = 0
    test_cases = ['44-01-2000', '0-0-0', '12-20-5000', 'not valid date']

    for d in test_cases:
        try:
            Date(d)
        except ValueError:
            c += 1

    assert c == len(test_cases)
