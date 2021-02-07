"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

earnings = int(input("Enter company earnings: "))
outgoings = int(input("Enter company outgoings: "))

if earnings > outgoings:
    profit = earnings - outgoings
    print(f"\nCompany work for profit. Profit is {profit}")
    profitability = (profit / earnings) * 100
    print(f"Profitability of company is {profitability:.2f}%\n")
    employee_count = int(input("Enter company employee count: "))
    print(f"\nProfit per employee is {profit / employee_count:.2f}")
else:
    print("\nCompany work for loss")
