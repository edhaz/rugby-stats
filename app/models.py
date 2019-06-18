from app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    stats = db.relationship('Stats', backref='team_name', lazy='dynamic')

    def __repr__(self):
        return '<Team {}>'.format(self.name)


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_no = db.Column(db.Integer, nullable=False, unique=True)
    stats = db.relationship('Stats', backref='round', lazy='dynamic')

    def __repr__(self):
        return '<Round: {}>'.format(self.round_no)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.Integer, index=True, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'), nullable=False)

    def __repr__(self):
        return '<Place: {} for team: {}>'.format(self.place, self.team_name.name)





    # won = db.Column(db.Integer, nullable=False)
    # drawn = db.Column(db.Integer, nullable=False)
    # lost = db.Column(db.Integer, nullable=False)
    # points_for = db.Column(db.Integer, nullable=False)
    # points_against = db.Column(db.Integer, nullable=False)
    # points_difference = db.Column(db.Integer, nullable=False)
    # bonus = db.Column(db.Integer, nullable=False)
    # points = db.Column(db.Integer, nullable=False)

