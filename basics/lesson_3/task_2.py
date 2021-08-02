"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def collect_user_info(name: str, surname: str, birth_date: str, city: str, email: str, phone: str) -> str:
    return f"That's what we have on you:\n" \
           f"Name: {name}, Surname: {surname}, Birth date: {birth_date}, City: {city}, Email: {email}, Phone: {phone}"


if __name__ == '__main__':
    print("Please identify your self!")
    print(collect_user_info(
        name=input("What's your name?: "),
        surname=input("What is your surname?: "),
        birth_date=input("When were you born?: "),
        city=input("Where do you live?: "),
        email=input("What's your email?: "),
        phone=input("What is your telephone number?: "),
    ))
