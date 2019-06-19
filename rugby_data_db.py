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

    r_id = s.query(Round).filter_by(round_no=data[0]['Played']).first()
    rounds = s.query(Stats.round_id).filter_by(round_id=r_id.id).count()
    if rounds == 12:
        print("DATA ALREADY PRESENT")
        return

    for item in data:
        t = s.query(Team).filter_by(name=item['Team'].lower()).first()
        r = s.query(Round).filter_by(round_no=item['Played']).first()
        add_this = Stats(
            team_name=t,
            round=r,
            place_=int(item['Place']),
            won_=int(item['Won']),
            drawn_=int(item['Drawn']),
            lost_=int(item['Lost']),
            for_=int(item['For']),
            against_=int(item['Against']),
            difference_=int(item['Difference']),
            bonus_=int(item['Bonus']),
            points_=int(item['Points'])
        )
        print(add_this)
        s.add(add_this)
        s.commit()
        print("Added")
    s.close()


add_rounds()
add_all_teams(json_data)
add_team_data(json_data)

