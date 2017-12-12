from app.models import User
from app import flask_bcrypt


class UserManager:
    @staticmethod
    def create_user(email, password, first_name, last_name):
        """
        Create an user in the database
        :param email: String, user email. Ie, "some@mail.com"
        :param password: String, user's password. Ie, "my-password"
        :param first_name: String, user's first name. Ie, "Andres"
        :param last_name: String, user's last name. Ie, "Andres"
        """
        user = User(
            email=email,
            password=flask_bcrypt.generate_password_hash(password),
            first_name=first_name,
            last_name=last_name
        )
        user.save()

    @staticmethod
    def get_user_by_email(email):
        """
        Get an user by an email
        :param email: String, user email. Ie, "some@mail.com"
        :return: User object.
        """
        try:
            return User.objects(email=email).first()
        except Exception as e:
            return None

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get an user by an email
        :param user_id: String, user ID.
        :return: User object.
        """
        try:
            return User.objects(id=user_id).first()
        except Exception as e:
            return None
