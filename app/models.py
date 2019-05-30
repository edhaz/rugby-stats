from app import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True, unique= True)
    stats = db.relationship('Stats', backref='team', lazy='dynamic')

    def __repr__(self):
        return '<Team: {}>'.format(self.team_name)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, nullable=False)
    place = db.Column(db.Integer, nullable=False)
    # won = db.Column(db.Integer, nullable=False)
    # drawn = db.Column(db.Integer, nullable=False)
    # lost = db.Column(db.Integer, nullable=False)
    # points_for = db.Column(db.Integer, nullable=False)
    # points_against = db.Column(db.Integer, nullable=False)
    # points_difference = db.Column(db.Integer, nullable=False)
    # bonus = db.Column(db.Integer, nullable=False)
    # points = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __repr__(self):
        return '<Position {} for team: {}>'.format(self.place, self.team_id.team_name)

