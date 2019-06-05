from app import db
import datetime


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    stats = db.relationship('Stats', backref='team_name', lazy='dynamic')

    def __repr__(self):
        return '<Team {}>'.format(self.name)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.Integer, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # round_no = db.relationship('Round', backref='round', lazy='dynamic')

    def __repr__(self):
        return '<Place: {} for team: {}>'.format(self.place, self.team_name.name)


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_no = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.date.today)
#     stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'), nullable=False)
#
    def __repr__(self):
        return '<Round: {} on {}>'.format(self.round_no, self.date)

# class Team(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(64), index=True, unique= True)
#     stats = db.relationship('Stat', backref='team', lazy='dynamic')
#
#     def __repr__(self):
#         return '<Team: {}>'.format(self.team_name)
#
#
# class Stat(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     round_number = db.Column(db.Integer, nullable=False)
#     place = db.Column(db.Integer, nullable=False)
#     team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
#
#     def __repr__(self):
#         return '<Position {} for team_id: {}>'.format(self.place, self.team_id)




    # won = db.Column(db.Integer, nullable=False)
    # drawn = db.Column(db.Integer, nullable=False)
    # lost = db.Column(db.Integer, nullable=False)
    # points_for = db.Column(db.Integer, nullable=False)
    # points_against = db.Column(db.Integer, nullable=False)
    # points_difference = db.Column(db.Integer, nullable=False)
    # bonus = db.Column(db.Integer, nullable=False)
    # points = db.Column(db.Integer, nullable=False)

