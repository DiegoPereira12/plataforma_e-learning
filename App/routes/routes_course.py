from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *

@app.route('/')
def main():
    
    return render_template('main.html')

@app.route('/menu_course')
def menu_course():

    return render_template('menu_course.html')

@app.route('lista_course')
def lista_course():

    return render_template('/lista_course.html', course = CourseModel.query.all())

@app.route('/cadastro_course', methods = ['GET', 'POST'])
def cadastro_course():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['description'] or not request.form['holder_image'] or not request.form['duration'] or not request.form['date_created'] or not request.form['date_updated']:
            flash('Please, fill in all fields')
        else:
            course = CourseModel(request.form['name'], request.form['description'], request.form['holder_image'], request.form['duration'], request.form['date_created'], request.form['date_updated'])

            db.session.add(course)
            db.session.commit()
            flash('Registration successful')

            return redirect(url_for('lista_course'))
    return render_template('cadastro_course.html')    