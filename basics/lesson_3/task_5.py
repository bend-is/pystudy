"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
from typing import List


def calculate_sum(numbers: List[str]) -> int:
    return sum(map(int, numbers))


def request_and_sums_numbers() -> None:
    stop_char = "!"
    num_sum = 0

    while True:
        nums = input("Enter a numbers separated by space: ")

        if nums == "":
            continue

        nums = nums.split()
        stop = stop_char in nums

        if stop:
            nums.remove(stop_char)

        num_sum += calculate_sum(nums)
        print(f"Sum of all inputted numbers is {num_sum}")

        if stop:
            break


if __name__ == '__main__':
    request_and_sums_numbers()
