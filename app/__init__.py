from flask import Flask
from mongoengine import connect
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from datetime import timedelta


app = Flask(__name__)
app.config.from_object('config')
connect('todo_list')

app.secret_key = '7y%r8S9&hFWd^l%eM0Aik8ZLy'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
flask_bcrypt = Bcrypt(app)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=43200)

from app import views
