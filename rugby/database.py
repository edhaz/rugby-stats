import csv
from os import path

from sqlalchemy.exc import IntegrityError

from rugby import db, settings
from rugby.models import Team
from rugby.utils import get_current_season


def add_team(data):
    team = _create_team(data)
    db.session.add(team)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def all_teams():
    return db.session.query(Team).group_by(Team.name).order_by(Team.place, Team.created).limit(11)


# For historical data
def add_data(filename: str):
    with open(path.join(settings.DATA_DIR, "2019", filename), "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row[0] == "Place":
                continue
            team = Team(
                name=row[1],
                place=row[0],
                games_played=row[2],
                games_won=row[3],
                games_drawn=row[4],
                games_lost=row[5],
                points_for=row[6],
                points_against=row[7],
                points_difference=row[8],
                points_bonus=row[9],
                points_total=row[10],
            )
            db.session.add(team)
        db.session.commit()


def _create_team(data):
    return Team(
        place=data[0],
        name=data[1],
        games_played=data[2],
        games_won=data[3],
        games_lost=data[4],
        games_drawn=data[5],
        points_for=data[6],
        points_against=data[7],
        points_difference=data[8],
        points_bonus=data[9],
        points_total=data[10],
        season=get_current_season(),
    )
