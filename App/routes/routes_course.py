from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *

@app.route('/')
def main():
    
    return render_template('main.html')

@app.route('/menu_course')
def menu_course():

    return render_template('menu_course.html')

@app.route('/lista_course')
def lista_course():

    return render_template('/lista_course.html', course = CourseModel.query.all())

@app.route('/cadastro_course', methods = ['GET', 'POST'])
def cadastro_course():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['description'] or not request.form['duration'] or not request.form['date_created'] or not request.form['date_updated']:
            flash('Please, fill in all fields')
        else:
            course = CourseModel(request.form['name'], request.form['description'], request.form['duration'], request.form['date_created'], request.form['date_updated'])

            db.session.add(course)
            db.session.commit()
            flash('Registration successful')

            return redirect(url_for('lista_course'))
    return render_template('cadastro_course.html')

@app.route('/update_course/<id>', methods=['GET', 'POST'])
def update_course(id):

    course = CourseModel.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('update_course.html', course=course)

    if request.method == 'POST':
        course.name = request.form["name"]
        course.description = request.form["description"]
        course.duration = request.form["duration"]
        course.date_created = request.form["date_created"]
        course.date_updated = request.form["date_updated"]

        db.session.add(course)
        db.session.commit()

        return redirect(url_for('lista_course'))

@app.route('/delete_course/<id>', methods=['GET', 'POST'])
def delete_course(id):

    course = CourseModel.query.filter_by(id=id).firts()
    if request.method == 'GET':
        return render_template('delete_course.html', course=course)

    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        flash('Registration successfully deleted')

        return redirect(url_for(lista_course))



