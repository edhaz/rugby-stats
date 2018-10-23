#! /usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup
import data_archive.json_creator

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


def get_soup():
    r = requests.get('https://www.premiershiprugby.com/')
    if not r:
        raise Exception("Website not working")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


def get_data(soup):
    names = soup.find_all('div', {"class": "footer-club-img"})
    print(names[0])
    return names


def update_database(master):
    with open(SITE_ROOT + '/tables.csv', 'w') as fout:
        fout.write("Place,Team,Played,Won,Drawn,Lost,For,Against,Difference,Bonus,Points\n")
        for i in master:
            fout.write(",".join(i) + '\n')


def main():
    print("Running logos...")
    soup = get_soup()
    master = get_data(soup)
    #update_database(master)
    #json_creator.run()
    print("Completed.")


if __name__ == '__main__':
    main()
