from app.models import User
from app import flask_bcrypt
from api.todo_list.manager import TodoListManager


class TodoListController:
    @staticmethod
    def get_user_todo_list(user_id):
        """
        Create an user in the database
        :param user_id: String, user id
        :return: List, user to do list.
        """
        return TodoListManager.get_user_todo_list(user_id=user_id)

    @staticmethod
    def get_user_todo_list_by_id(todo_list_id):
        """
        Create an user in the database
        :param todo_list_id: String, To do list id
        :return: List, user to do list.
        """
        return TodoListManager.get_user_todo_list_by_id(todo_list_id=todo_list_id)

    @staticmethod
    def save_user_todo_list(user_id, todo_description):
        TodoListManager.save_user_todo_list(user_id, todo_description)

    @staticmethod
    def update_user_todo_list(todo_list_id, status):
        TodoListManager.update_user_todo_list(todo_list_id, status)
