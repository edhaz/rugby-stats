from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_no = db.Column(db.Integer)
    place = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {} for author: {}>'.format(self.round_no, self.user_id)


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

