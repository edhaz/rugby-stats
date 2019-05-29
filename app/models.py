from datetime import datetime
from app import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True, unique= True)

    def __repr__(self):
        return '<Team: {}>'.format(self.team_name)


class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    position = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __repr__(self):
        return '<Position {} for team: {}'.format(self.position, self.team_id.team_name)

