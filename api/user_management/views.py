import re
import argparse
from flask_restful import Resource, reqparse

from api.user_management.controller import UserController


def email_type(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("The email is has not a valid format")
    user = UserController.get_user_by_email(email)
    if user:
        raise ValueError("The email {} already exists".format(email))

    return email


class User(Resource):
    def get(self):
        return {'name': "Andres"}

    def post(self):
        data = self.__validate_post_parameters()
        UserController.create_user(**data)
        return {'message': 'User successfully created'}, 201

    def __validate_post_parameters(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'email', dest='email',
            type=email_type, location='form',
            required=True,
        )
        parser.add_argument('password', type=str, help="The password is invalid", required=True)
        parser.add_argument('first_name', type=str, help="The first name is invalid", required=True)
        parser.add_argument('last_name', type=str, help="The last name is invalid", required=True)
        args = parser.parse_args()
        return args
