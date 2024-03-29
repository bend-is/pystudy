"""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

total_profit = 0
profit_count = 0
firm_profits = {}

with open('task_7.txt') as f:
    for line in f:
        name, _, earnings, outgoings = line.split()
        profit = int(earnings) - int(outgoings)
        firm_profits[name] = profit

        if profit > 0:
            profit_count += 1
            total_profit += profit

average_profit = {"average_profit": total_profit / profit_count}

with open('task_7.json', 'w') as f:
    json.dump([firm_profits, average_profit], f)
