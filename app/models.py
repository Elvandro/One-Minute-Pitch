from . import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return f'Users {self.username}'


class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Categories {self.name}'

class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)

    def __repr__(self):
        return f'Pithches {self.pitch}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id =  db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String)
    pitch = db.Column(db.String)
    comment = db.Column(db.String)


    def __repr__(self):
        return f'Comments {self.comment}
