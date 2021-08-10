import json

import requests
from bs4 import BeautifulSoup as bs
from bs4 import Tag
import re

salary_reg = re.compile("(\d+).*?(\d+)?(\w+)")
URL = "https://hh.ru"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}


def search(query: str, max_page: int):
    result = []
    params = {"text": query, "page": 0}

    while True:
        res = requests.get(URL + "/search/vacancy", params=params, headers=HEADERS)
        res.raise_for_status()

        soup = bs(res.text, "html.parser")

        for vacancy in soup.findAll("div", {"class": "vacancy-serp-item"}):
            elem = {}

            info = vacancy.find("div", {"class": "vacancy-serp-item__info"})  # type: Tag
            if info:
                elem['name'] = info.getText()
                elem['url'] = info.find('a').get("href")

            salary = vacancy.find("div", {"class": "vacancy-serp-item__sidebar"})  # type: Tag
            if salary:
                mn, mx, currency = parse_salary(salary.getText())
                elem['salary'] = {}
                elem['salary']['min'] = mn
                elem['salary']['max'] = mx
                elem['salary']['currency'] = currency

            if elem:
                result.append(elem)

        print(f"finish page {params['page'] + 1}")

        but = soup.find("a", {"data-qa": "pager-next"})
        if not but or (params["page"] + 1) >= max_page:
            break

        params["page"] += 1

    return result


def parse_salary(sal: str):
    resp = [None, None, None]

    if not sal:
        return resp

    sal = sal.replace("\u202f", "").replace(" ", "")

    match = salary_reg.findall(sal)
    if len(match) == 0 or len(match[0]) != 3:
        return resp

    match = match[0]
    resp[0] = int(match[0]) if match[0] else None
    resp[1] = int(match[1]) if match[1] else None
    resp[2] = match[2] if match[2] else None

    return resp


if __name__ == "__main__":
    q, p = "", ""
    while not q:
        q = input("Type a query for search: ")

    while not p.isdigit():
        p = input("Type a max page number: ")

    search_res = search(q, int(p))

    with open(f"result_{q}.json", "w") as f:
        json.dump(search_res, f, indent=4, ensure_ascii=False, )
