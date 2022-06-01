from distutils.log import debug
import imp
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:diego@localhost:5432/e_learning_api"
app.config['SECRET_KEY'] = "random string"

if __name__ == '__main__':
    app.run(debug=True)