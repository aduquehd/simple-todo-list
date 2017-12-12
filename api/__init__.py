from flask_restful import Api
from app import app

from api.user_management.views import User
from api.authentication.views import Authentication
from api.todo_list.views import TodoList

api = Api(app)

api.add_resource(User, '/api/v1/user')
api.add_resource(Authentication, '/api/v1/auth')
api.add_resource(
    TodoList,
    '/api/v1/todo-list',
    '/api/v1/todo-list/<string:todo_list_id>'
)
