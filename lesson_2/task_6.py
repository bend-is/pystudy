"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.В кортеже должно быть два элемента — номер товара и
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""

i = 1
products = []

while True:
    name = input("Enter a product name or stop to finish: ")

    if name in ['s', 'stop']:
        break

    price = ''
    while not price.isdigit():
        price = input("Enter a product price: ")

    count = ''
    while not count.isdigit():
        count = input("Enter a product count: ")

    unit = input("Enter a product unit type: ")

    products.append((i, {"название": name, "цена": int(price), "количество": int(count), "eд": unit}))
    i += 1

if len(products) != 0:
    print(f"Resulted items: {products}")

    analysis_result = {}

    for _, product in products:
        for k, v in product.items():
            if k not in analysis_result:
                analysis_result[k] = [v]
            elif v not in analysis_result[k]:
                analysis_result[k].append(v)

    print(f"Analysis result: {analysis_result}")
