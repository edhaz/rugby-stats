from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from app.models import Team, Stats
import os
import json


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          "postgresql://localhost/rugby"
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

json_url = os.path.join(SITE_ROOT, "app", "data_archive", "rugby_table.json")
json_data = json.load(open(json_url))


def add_team(team):
    try:
        s = Session()
        team_to_add = Team(name=team)
        s.add(team_to_add)
        s.commit()
        s.close()
        print("ADDED {}".format(team))
    except exc.IntegrityError:
        print("TEAM ALREADY PRESENT")


def add_all_teams(data):
    for item in data:
        add_team(item['Team'].lower())


def add_team_position(data):
    s = Session()
    teams = s.query(Team).all()
    for team in teams:
        for item in data:
            if item['Team'].lower() == team.name:
                add_this = Stats(place=item['Place'], team_name=team)
                s.add(add_this)
                s.commit()
                print("Added")
            else:
                continue
    s.close()

    # except:
    #     print("AN ERROR OCCURED")


print(add_team_position(json_data))



