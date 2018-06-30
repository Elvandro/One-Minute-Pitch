from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(360))
    email = db.Column(db.String(360))
    password = db.Column(db.String(660))
    # Defining the One to many relationship between a user and a pitch
    pitch = db.relationship('Pitch', backref="user", lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(360))

    def __repr__(self):
        return f'Category {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    # Defining the foreign key from the relationship between a user and a pitch
    user_id = db.Column(db.Integer, db.ForeignKey(users.id))

    def __repr__(self):
        return f'Pitch {self.pitch}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id =  db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(360))
    pitch = db.Column(db.String)
    comment = db.Column(db.String)

    def __repr__(self):
        return f'Comment {self.comment}'
