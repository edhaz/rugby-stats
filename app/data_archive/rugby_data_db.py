#! /usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup
import sqlalchemy as db


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
URL_PREFIX = 'https://cdn.soticservers.net/tools/images/teams/logos/RUGBY969513/d/'

engine = db.create_engine('postgresql://localhost/rugby')
conn = engine.connect()

meta = db.MetaData()
meta.reflect(bind=engine)
team_table = meta.tables['team']

select_st = db.select([team_table])
res = conn.execute(select_st)

for _row in res:
    print(_row)


def get_soup():
    r = requests.get('https://www.bbc.co.uk/sport/rugby-union/tables')
    if not r:
        raise Exception("Website not working")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


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


# fout.write("Place,Logo,Team,Played,Won,Drawn,Lost,For,Against,Difference,Bonus,Points\n")
def update_database(master):
    pass


def main():
    print("Running...")
    soup = get_soup()
    master = get_data(soup)
    print(master)
    print("Completed.")


if __name__ == '__main__':
    main()
