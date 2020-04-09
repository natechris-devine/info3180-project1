from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info3180-user:unlock@localhost/info3180-proj1" - local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://juezyffmeaymdj:1f873bd892fb051032a3a8e1dd42e03e0959aa99aa4448b105724c30a2e51e7c@ec2-34-197-212-240.compute-1.amazonaws.com:5432/de7oamt5v61gd8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
