from werkzeug.security import check_password_hash
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

from app import app, login_manager, flask_bcrypt
from flask import render_template, redirect, request, url_for, flash

from .models import User
from .user import UserObject


@app.route('/', methods=["GET", ])
def index():
    return render_template('base.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')


@app.route('/todo-list', methods=["GET"])
def todo_list():
    return render_template('todo-list.html')


@app.route('/create-user', methods=["POST", "GET"])
def create_user():
    return render_template('create-user.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(username):
    return User()
