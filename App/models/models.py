from flask_sqlalchemy import SQLAlchemy
from app import db
from flask_migrate import Migrate

class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    duration = db.Column(db.String(80))
    date_created = db.Column(db.String(100))
    date_updated = db.Column(db.String(100))

    def __init__(self, name, description, holder_image, duration, date_created, date_updated):
        self.name = name        
        self.description = description
        self.holder_image = holder_image
        self.duration = duration
        self.date_created = date_created   
        self.date_updated = date_updated


class StudentModel(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    phone = db.Column(db.Integer())
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










