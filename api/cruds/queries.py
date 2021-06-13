from ariadne import convert_kwargs_to_snake_case
from sqlalchemy.orm import Session

from domains.todo import Todo

def listTodos_resolver(obj, info):
    try:
        todo_model = Todo()
        todos = [todo.to_dict() for todo in Todo.query.all()]
        payload = {
            "success": True,
            "todos": todos}
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]}
    return payload

@convert_kwargs_to_snake_case
def getTodo_resolver(obj, info, id):
    try:
        todo = Todo.query.get(id)
        payload = {
            "success": True,
            "todo": todo.to_dict()}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]}
    return payload
