from strawberry.fastapi import GraphQLRouter
from .consultas import Query


import strawberry


schema = strawberry.Schema(query=Query)
router = GraphQLRouter(schema)