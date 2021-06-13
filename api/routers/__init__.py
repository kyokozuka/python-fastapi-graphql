from typing import List

from ariadne import (load_schema_from_path,
                    make_executable_schema,
                    graphql_sync,
                    snake_case_fallback_resolvers,
                    ObjectType,
                    QueryType)
from ariadne.asgi import GraphQL
from ariadne.constants import PLAYGROUND_HTML
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cruds.queries import listTodos_resolver, getTodo_resolver
from cruds.mutations import (
    create_todo_resolver,
    update_todo_resolver,
    delete_todo_resolver,)

api = FastAPI(title='Sample App', version='0.1')

api.add_middleware(
    CORSMiddleware,
    allow_origins=[ "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

type_defs = load_schema_from_path("schema.graphql")

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listTodos", listTodos_resolver)
query.set_field("getTodo", getTodo_resolver)

mutation.set_field('createTodo', create_todo_resolver)
mutation.set_field('updateTodo', update_todo_resolver)
mutation.set_field('deleteTodo', delete_todo_resolver)

schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers)
api.add_route('/graphql', GraphQL(schema, debug=True))


@api.get("/")
def resolve_hello():
    return "Hello world!"

