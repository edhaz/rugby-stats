from app import db
from app.models import Teams, Stats


def add_team(team_name):
    try:
        t = Teams(team_name=team_name)
        db.session.add(t)
        db.session.commit()
        return "Added {}".format(team_name)
    except:
        return "ERROR"


def add_stats(round_number, place, team_id):
    try:
        s = Stats(round_number=round_number, place=place, team_id=team_id)
        db.session.add(s)
        db.session.commit()
    except:
        return "ERROR"
