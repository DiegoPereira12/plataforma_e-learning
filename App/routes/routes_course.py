from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *

@app.route('/')
def main():
    
    return render_template('main.html')