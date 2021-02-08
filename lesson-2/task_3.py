"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

seasons_in_list = [
    'зима',
    'зима',
    'весна',
    'весна',
    'весна',
    'лето',
    'лето',
    'лето',
    'осень',
    'осень',
    'осень',
    'зима',
]
seasons_in_dict = {
    "зима": [1, 2, 12],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11],
}

input_month = ''

while not input_month.isdigit() or int(input_month) < 1 or int(input_month) > 12:
    input_month = input('Enter a month number: ')

input_month = int(input_month)

print(f"Season from list: {seasons_in_list[input_month - 1]}")

for season in seasons_in_dict:
    if input_month in seasons_in_dict[season]:
        print(f"Season from dict: {season}")
        break
