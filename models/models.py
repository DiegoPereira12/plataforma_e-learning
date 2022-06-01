import imp
from flask_sqlalchemy import SQLAlchemy
from app import db

class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key = True)