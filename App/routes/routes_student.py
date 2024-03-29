from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *


@app.route('/menu_student')
def menu_student():
    
    return render_template('menu_student.html')

@app.route('/lista_student')
def lista_student():

    return render_template('lista_student.html', student = StudentModel.query.all())

@app.route('/cadastro_student', methods = ['GET', 'POST'])
def cadastro_student():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['nickname'] or not request.form['phone'] or not request.form['date_created'] or not request.form['date_updated']:
            flash('Please, fill in all fields')
        else:
            student = StudentModel(request.form['name'], request.form['nickname'], request.form['phone'], request.form['date_created'], request.form['date_updated'])

            db.session.add(student)
            db.session.commit()
            flash('Registration successful')

            return  redirect(url_for('lista_student'))
    return render_template('cadastro_student.html')

@app.route('/update_student/<id>', methods=['GET', 'POST'])
def update_student(id):

    student = StudentModel.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('update_student.html', student=student)

    if request.method == 'POST':
        student.name = request.form["name"]
        student.nickname = request.form["nickname"]
        student.phone = request.form["phone"]
        student.date_created = request.form["date_created"]
        student.date_updated =request.form["date_updated"]

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('lista_student'))

@app.route('/delete_student/<id>', methods=['GET', 'POST'])
def delete_student(id):

    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete_student.html', student=student)

    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        flash('Registration successfully deleted')

        return redirect(url_for('lista_student'))



