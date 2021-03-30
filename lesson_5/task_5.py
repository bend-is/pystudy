"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('task_5.txt', 'w') as f:
    while True:
        num = input()
        if not num:
            break
        f.write(f"{num} ")

with open('task_5.txt') as f:
    print(sum(map(int, f.readline().split())))
