from app.models import TodoList
from api.custom_exceptions import GeneralException


class TodoListManager:
    @staticmethod
    def get_user_todo_list(user_id):
        """
        Create an user in the database
        :param user_id: String, user id
        :return: List, user to do list.
        """
        try:
            list = []
            todo_list = TodoList.objects(user_id=user_id)
            for i in todo_list:
                list.append({
                    'id': str(i.id),
                    'description': i.description,
                    'status': i.status,
                })
            return list
        except Exception:
            return []

    @staticmethod
    def get_user_todo_list_by_id(todo_list_id):
        """
        Create an user in the database
        :param todo_list_id: String, To do list id
        :return: List, user to do list.
        """
        try:
            return TodoList.objects(id=todo_list_id).first()
        except Exception:
            return None

    @staticmethod
    def save_user_todo_list(user_id, todo_description):
        todo_list = TodoList(user_id=user_id, description=todo_description, status=False)
        todo_list.save()

    @staticmethod
    def update_user_todo_list(todo_list_id, status):
        todo_list = TodoList.objects(id=todo_list_id).first()
        todo_list.status = status
        todo_list.save()
