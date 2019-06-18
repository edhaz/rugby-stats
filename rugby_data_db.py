from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from app.models import Team, Stats, Round
import os
import json


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          "postgresql://localhost/rugby"
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

json_url = os.path.join(SITE_ROOT, "app", "data_archive", "rugby_table.json")
json_data = json.load(open(json_url))


def add_rounds():
    try:
        s = Session()
        for i in range(1, 25):
            r = Round(round_no=i)
            s.add(r)
        s.commit()
        s.close()
    except exc.IntegrityError:
        s.close()
        print("ROUNDS ALREADY PRESENT")


def add_all_teams(data):
    try:
        s = Session()
        for item in data:
            team_to_add = Team(name=item['Team'].lower())
            s.add(team_to_add)
        s.commit()
        s.close()
    except exc.IntegrityError:
        s.close()
        print("TEAMS ALREADY PRESENT")


def add_team_data(data):
    s = Session()
    r = data[0]['Played']
    r_id = s.query(Round).filter_by(round_no=r).first()
    teams = s.query(Team).all()
    rounds = s.query(Stats.round_id).filter_by(round_id=r_id.id).count()
    if rounds == 12:
        print("DATA ALREADY PRESENT")
        return
    for team in teams:
        for item in data:
            print(item)
            r = s.query(Round).filter_by(round_no=item['Played']).first()
            if item['Team'].lower() == team.name:
                add_this = Stats(place=item['Place'], team_name=team, round=r)
                s.add(add_this)
                s.commit()
                print("Added")
            else:
                continue
    s.close()


# add_rounds()
# add_all_teams(json_data)
add_team_data(json_data)

