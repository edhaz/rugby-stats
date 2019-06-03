from app import db
from app.models import Team, Stats


def add_team(team_name):
    try:
        t = Team(name=team_name)
        db.session.add(t)
        db.session.commit()
        return "Added {}".format(team_name)
    except:
        return "ERROR"


def add_stats(round_number, place, team_id):
    try:
        t = Team.query.get(team_id)
        s = Stats(round_no=round_number, place=place, team_name=t)
        db.session.add(s)
        db.session.commit()
    except:
        return "ERROR"
