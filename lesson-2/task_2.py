"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

items = []

while True:
    item = input("Enter a list element to add. Enter 'stop' or 's' if enough: ")
    if item in ['s', 'stop']:
        break

    items.append(item)

print(f"Inputted list: {items}")

i = 1
while i < len(items):
    items[i], items[i - 1] = items[i - 1], items[i]
    i += 2

print(f"Swapped list: {items}")
