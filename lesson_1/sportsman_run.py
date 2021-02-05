a = int(input("Enter A: "))
b = int(input("Enter B: "))

day = 1

while a < b:
    day += 1
    a += a * 0.1

print(day)
