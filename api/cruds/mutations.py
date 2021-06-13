from datetime import date

from ariadne import convert_kwargs_to_snake_case

from domains.todo import Todo
from db import session


@convert_kwargs_to_snake_case
def create_todo_resolver(obj, info, title, content):
    try:
        today = date.today()
        todo = Todo(title=title, content=content, created_at='2021-06-13')
        session.add(todo)
        session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()}
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]}
    return payload

@convert_kwargs_to_snake_case
def update_todo_resolver(obj, info, id, title, content):
    try:
        todo = Todo.query.get(id)
        if todo:
            todo.title = title
            todo.content = content
        session.add(todo)
        session.commit()
        payload = { "success": True, "todo": todo.to_dict()}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]}
    return payload

@convert_kwargs_to_snake_case
def delete_todo_resolver(obj, info, id):
    try:
        todo = Todo.query.get(id)
        session.delete(todo)
        session.commit()
        payload = {"success": True, "todo": todo.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]}
    return payload

