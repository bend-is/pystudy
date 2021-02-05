n = int(input("Enter a number: "))

max_n = n % 10
n //= 10

while n:
    rem = n % 10

    if max_n < rem:
        max_n = rem

    n //= 10

print(f"Max number is {max_n}")
