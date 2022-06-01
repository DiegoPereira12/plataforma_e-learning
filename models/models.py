import imp
from tokenize import String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from app import db

class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    holder_image =  db.Column(db.String(100))
    duration = db.Column(db.String(100))
    date_created = db.Column(db.String(100))
    date_updated = db.Column(db.String(100))

    def __init__(self, name, description, holder_image, duration, date_created, date_update):
        self.name = name
        self.description = description
        self.holder_image = holder_image
        self.duration = duration
        self.date_created = date_created
        self.date_update = date_update

class StudentModel(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    phone = db.Column(db.Intenger(50))
    avatar = db.Column(db.String(100))
    date_created = db.Column(db.String(100))
    date_updated = db.Column(db.String(100))


    def __init__(self, name, nickname, phone, avatar, date_created, date_update):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.avatar = avatar
        self.date_created = date_created
        self.date_update = date_update

class EnrollmentModel(db.Model):
    __tablename__ = 'enrollment'

    id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.String(100))
    course = db.Column(db.String(100))
    date_enroll = db.Column(db.String(100))
    date_close = db.Column(db.String(100))
    score = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def __init__(self, student, course, date_enroll, date_close, score, status):
        self.student = student
        self.course = course
        self.date_enroll = date_enroll
        self.date_close = date_close
        self.score = score
        self.status = status