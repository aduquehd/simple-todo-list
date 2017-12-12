from app.models import User
from app import flask_bcrypt
from api.user_management.manager import UserManager


class UserController:
    @staticmethod
    def create_user(email, password, first_name, last_name):
        """
        Create an user in the database
        :param email: String, user email. Ie, "some@mail.com"
        :param password: String, user's password. Ie, "my-password"
        :param first_name: String, user's first name. Ie, "Andres"
        :param last_name: String, user's last name. Ie, "Andres"
        """
        UserManager.create_user(email, password, first_name, last_name)

    @staticmethod
    def get_user_by_email(email):
        """
        Get an user by an email
        :param email: String, user email. Ie, "some@mail.com"
        :return: User object.
        """
        return UserManager.get_user_by_email(email)

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get an user by an email
        :param user_id: String, user ID.
        :return: User object.
        """
        return UserManager.get_user_by_id(user_id)
