import requests
from bs4 import BeautifulSoup
import json_creator


def get_soup():
    r = requests.get('https://www.bbc.co.uk/sport/rugby-union/tables')
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_data(soup):
    names = soup.find_all('td')
    table = []
    for i in names:
        table.append(i.string)
    master = []
    counter = 0
    for n in range(len(table) // 12):
        x = table[counter:counter + 11:]
        counter += 11
        master.append(x)
    return master


def update_database(master):
    with open('tables.csv', 'w') as fout:
        fout.write("Place,Team,Played,Won,Drawn,Lost,For,Against,Difference,Bonus,Points\n")
        for i in master:
            fout.write(",".join(i) + '\n')


def main():
    print("Running...")
    soup = get_soup()
    master = get_data(soup)
    update_database(master)
    json_creator.run()
    print("Completed.")


if __name__ == '__main__':
    main()
