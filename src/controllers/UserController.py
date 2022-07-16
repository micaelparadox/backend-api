# pseudo code
import sys
from flask import jsonify, render_template, redirect, url_for, request, abort
from models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return render_template('index.html')
def store():
    data = request.get_json()
    ## create a new user object and add it to the database
    new_user = User()
    db.session.add(new_user)
    db.session.commit()
    return jsonify(data)
    
    ...
def show(userId):
    ...
def update(userId):
    ...
def destroy(userId):
    ...