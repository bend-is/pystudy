"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

pi = 3.14
greets = 'Hello world!'

print(greets)

name = input('Please, identify your self: ')
number = input(f"Now {name}, enter your number and I will multiply it by pi: ")

print(f"This is what your wanted: {int(number) * pi}")
