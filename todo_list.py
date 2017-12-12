from app import app
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from app import app
from api import api

jwt = JWTManager(app)

app.run()
