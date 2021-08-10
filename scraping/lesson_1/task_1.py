"""
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
 сохранить JSON-вывод в файле *.json.
"""
import json

import requests


def save_repo_list_to_file(login: str) -> str:
    res = requests.get(f'https://api.github.com/users/{login}/repos')
    res.raise_for_status()

    filename = f'repo_list_{login}.json'

    with open(filename, 'w') as f:
        json.dump(res.json(), f, indent=4)

    return filename


if __name__ == '__main__':
    try:
        f_name = save_repo_list_to_file(
            input('enter a login to display a repository list: ')
        )
        print(f'save repository list to file "{f_name}"')
    except requests.HTTPError as e:
        print('user is not found')
