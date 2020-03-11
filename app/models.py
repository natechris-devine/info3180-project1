from . import db
from datetime import date
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(6))
    email = db.Column(db.String(40))
    location = db.Column(db.String(40))
    biography = db.Column(db.String(150))
    profile_picture = db.Column(db.String(100)) # stores the name of the image file to be rendered
    date_created = db.Column(db.Date())

    def __init__(self, first_name, last_name, username, gender, email, location, biography, profile_picture):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_picture = profile_picture
        self.date_created = date.today()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<ID {0}\nUser {1} {2}>'.format(self.id, self.first_name, self.last_name)
