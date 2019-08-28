#! /usr/bin/python3
import os
import requests
import csv
from bs4 import BeautifulSoup
import json_creator

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
URL_PREFIX = 'https://cdn.soticservers.net/tools/images/teams/logos/RUGBY969513/d/'

def get_soup():
    r = requests.get('https://www.bbc.co.uk/sport/rugby-union/tables')
    if not r:
        raise Exception("Website not working")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


def check_duplicate_week(master):
    with open(SITE_ROOT + '/tables.csv', 'r') as fout:
        csv_reader = csv.reader(fout)
        old_csv = [row for row in csv_reader]
    # Accesses ['Played'] from each of the lists for the first team.
    print(master[0][3])
    print(old_csv[1][3])
    if master[0][3] == old_csv[1][3]:
        return True


def get_data(soup):
    names = soup.find_all('td')
    table = []
    for i in names:
        table.append(i.string)
    master = []
    counter = 0
    for n in range(len(table) // 11):
        x = table[counter:counter + 11:]
        if x[1] == "N'hampton":
            x[1] = "Northampton"
        counter += 11
        master.append(x)
    return master


def update_database(master):
    with open(SITE_ROOT + '/tables.csv', 'w') as fout:
        fout.write("Place,Logo,Team,Played,Won,Drawn,Lost,For,Against,Difference,Bonus,Points\n")
        for i in master:
            fout.write(",".join(i) + '\n')


def main():
    print("Running...")
    soup = get_soup()
    master = get_data(soup)
    if check_duplicate_week(master):
        print("Duplicate week, quitting.")
        return False
    update_database(master)
    json_creator.run()
    print("Completed.")


if __name__ == '__main__':
    main()
