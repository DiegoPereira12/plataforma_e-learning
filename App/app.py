from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:diego@localhost:5432/elearning_api"
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes.routes_course import *
from routes.routes_student import *

if __name__ == '__main__':
   app.run(debug=True) 