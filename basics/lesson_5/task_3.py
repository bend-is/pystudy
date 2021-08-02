"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

MIN_SALARY = 20000

with open('task_3.txt') as f:
    total_sal = 0
    sal_count = 0

    for line in f:
        surname, salary = line.split()
        salary = int(salary)
        total_sal += salary
        sal_count += 1

        if salary < MIN_SALARY:
            print(f"Employee {surname} has salary less then minimum salary ({salary})")

    print(f"\nAverage employees salary is {total_sal / sal_count}")
