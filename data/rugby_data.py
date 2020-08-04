#! /usr/bin/python3
from os import path
import requests
import datetime
import csv
from bs4 import BeautifulSoup
import json_creator

now = datetime.datetime.now()
# SITE_ROOT = os.path.realpath(os.path.dirname(__file__)) + '/' + str(now.year)
SITE_ROOT = path.join(path.realpath(path.dirname(__file__)), '2019')
URL_PREFIX = 'https://cdn.soticservers.net/tools/images/teams/logos/RUGBY969513/d/'

def get_soup():
    url = 'https://www.bbc.co.uk/sport/rugby-union/tables'
    # url = 'https://www.premiershiprugby.com/gallagher-premiership-rugby/league-table/'
    r = requests.get(url)
    if not r:
        raise Exception(f"Unable to access {url}")
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def check_duplicate_week(master):
    try:
        with open(path.join(SITE_ROOT, 'tables.csv'), 'r') as f:
            csv_reader = csv.reader(f)
            old_csv = [row for row in csv_reader]
    except IOError: return False
    if len(old_csv) <= 1: return False
    if master[0][3] == old_csv[1][3]: return True


def get_data(soup):
    table_rows = soup.find_all('td')
    table = []
    for row in table_rows:
        row_data = row.find_all('span')
        if row_data:
            table.append(row_data[1].text)
    master = []
    counter = 0
    for n in range(len(table) // 11):
        x = table[counter:counter + 11:]
        counter += 11
        master.append(x)
    return master


def update_database(master):
    with open(path.join(SITE_ROOT, 'tables.csv'), 'w') as fout:
        fout.write("Place,Team,Played,Won,Lost,Drawn,For,Against,Difference,Bonus,Points\n")
        for i in master:
            fout.write(",".join(i) + '\n')


def main():
    soup = get_soup()
    master = get_data(soup)
    if check_duplicate_week(master):
        print("Duplicate week, quitting.")
        return False
    update_database(master)
    json_creator.run()


if __name__ == '__main__':
    main()
