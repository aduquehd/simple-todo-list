from app import flask_bcrypt
from api.user_management.manager import UserManager
from flask_jwt_extended import (
    create_access_token,
)

from api.custom_exceptions import GeneralException


class AuthenticationController:
    @staticmethod
    def authenticate_user(email, password):
        """
        Create an user in the database
        :param email: String, user email. Ie, "some@mail.com"
        :param password: String, user's password. Ie, "my-password"
        """
        try:
            user = UserManager.get_user_by_email(email)
            if not user:
                raise GeneralException(message="User does not exists", status_code=400)
            password_hash = flask_bcrypt.check_password_hash(user.password, password)
            if user and password_hash:
                return create_access_token(identity={
                    'user_id': str(user.id),
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': email
                })
            else:
                raise GeneralException(message="User and password didn't match", status_code=400)
        except Exception:
            raise

    @staticmethod
    def get_user_by_email(email):
        """
        Get an user by an email
        :param email: String, user email. Ie, "some@mail.com"
        :return: User object.
        """
        return UserManager.get_user_by_email(email)
