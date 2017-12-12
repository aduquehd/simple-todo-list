import re
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.authentication.controller import AuthenticationController
from api.custom_exceptions import GeneralException


def email_type(email):
    if not email:
        raise ValueError("The email is required")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("The email has not a valid format")

    return email


class Authentication(Resource):
    method_decorators = {'get': [jwt_required]}

    def get(self):
        current_user = get_jwt_identity()
        return {'current_user': current_user}

    def post(self):
        try:
            data = self.__validate_post_parameters()
            token = AuthenticationController.authenticate_user(data['email'], data['password'])
            if not token:
                return {'message': "User and password didn't match"}
            return {'token': token}, 200
        except GeneralException as e:
            return {'message': e.message}, e.get_status_code

    def __validate_post_parameters(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', dest='email', type=email_type, location='form', required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        return args
