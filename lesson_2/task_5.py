"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

ratings = [7, 5, 3, 3, 2]

while True:
    new_r = input("Enter a new rating value: ")

    if new_r in ['s', 'stop']:
        break
    elif not new_r.isdigit():
        continue

    new_r = int(new_r)

    if new_r <= ratings[len(ratings) - 1]:
        ratings.append(new_r)
    elif new_r in ratings:
        ratings.insert(ratings.index(new_r), new_r)
    else:
        for i, r in enumerate(ratings):
            if new_r > r:
                ratings.insert(i, new_r)
                break

    print(ratings)
