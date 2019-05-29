from app import db


class Rugby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True, unique= True)
    place = db.Column(db.Integer)

    def __repr__(self):
        return '<Team: {}>'.format(self.team_name)
