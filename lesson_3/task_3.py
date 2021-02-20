"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_of_biggest_two(a: int, b: int, c: int) -> int:
    nums = [a, b, c]

    return sum(nums) - min(nums)


if __name__ == '__main__':
    print(sum_of_biggest_two(
        int(input("Enter a number: ")),
        int(input("Enter a number: ")),
        int(input("Enter a number: ")),
    ))
