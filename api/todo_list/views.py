import re
import argparse
from flask_restful import Resource, reqparse

from api.user_management.controller import UserController
from api.todo_list.controller import TodoListController
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.custom_exceptions import GeneralException


def user_id_type(user_id):
    user = UserController.get_user_by_id(user_id)
    if not user:
        raise ValueError("User don't exist")
    return user_id


class TodoList(Resource):
    method_decorators = {'get': [jwt_required], 'post': [jwt_required]}

    def get(self):
        current_user = get_jwt_identity()
        todo_list = TodoListController.get_user_todo_list(current_user['user_id'])
        return todo_list

    def post(self):
        try:
            data = self.__validate_post_parameters()
            current_user = get_jwt_identity()
            TodoListController.save_user_todo_list(current_user['user_id'], data['description'])
            return {'message': 'Todo list successfully created'}, 201
        except GeneralException as e:
            return {'message': e.message}, e.get_status_code

    def put(self, todo_list_id):
        try:
            data = self.__validate_put_parameters()
            status = True
            if data['status'].lower() == "false":
                status = False
            TodoListController.update_user_todo_list(todo_list_id, status)
            return {'message': "Todo list successfully updated"}
        except GeneralException as e:
            return {'message': e.message}, e.get_status_code

    def __validate_post_parameters(self):
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, help="The description is invalid", required=True)
        args = parser.parse_args()
        return args

    def __validate_put_parameters(self):
        parser = reqparse.RequestParser()
        parser.add_argument('status', choices=('true', 'false'), help="Status is invalid", required=True)
        args = parser.parse_args()
        return args
