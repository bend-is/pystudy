"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt') as f:
    lst = [len(line.split()) for line in f]

    print(f"Lines count if file: {len(lst)}")
    [print(f"Line {i + 1} contains {c} words") for i, c in enumerate(lst)]
