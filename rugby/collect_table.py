import requests
from bs4 import BeautifulSoup
from rugby import database
from rugby.settings import DATA_URL


def soup():
    if not (request := requests.get(DATA_URL)):
        raise Exception(f"Unable to access {DATA_URL}")
    return BeautifulSoup(request.text, "html.parser")


def parse_table(soup):
    table_rows = soup.find_all("td")
    return [row.find_all("span")[1].text for row in table_rows if row.find_all("span")]


def add_table_to_database(table):
    columns = 11
    for i in range(0, len(table), columns):
        raw_team = table[i : i + columns :]
        print(raw_team)
        database.add_team(raw_team)


def main():
    raw_data = soup()
    table = parse_table(raw_data)
    add_table_to_database(table)


if __name__ == "__main__":
    main()
