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
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

input_month = ''

while not input_month.isdigit() or int(input_month) < 1 or int(input_month) > 12:
    input_month = input('Enter a month number: ')

input_month = int(input_month)

print(f"Season from list: {seasons_in_list[input_month - 1]}")
print(f"Season from dict: {seasons_in_dict[input_month]}")
