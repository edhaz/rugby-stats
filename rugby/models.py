import datetime
from rugby import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    place = db.Column(db.Integer, nullable=False)
    games_played = db.Column(db.Integer, nullable=False)
    games_won = db.Column(db.Integer, nullable=False)
    games_drawn = db.Column(db.Integer, nullable=False)
    games_lost = db.Column(db.Integer, nullable=False)
    points_for = db.Column(db.Integer, nullable=False)
    points_against = db.Column(db.Integer, nullable=False)
    points_difference = db.Column(db.Integer, nullable=False)
    points_bonus = db.Column(db.Integer, nullable=False)
    points_total = db.Column(db.Integer, nullable=False)
    season = db.Column(db.String(64), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Team {self.name}>"

    __table_args__ = (
        db.UniqueConstraint("name", "games_played", name="uix_name_games_played"),
    )
