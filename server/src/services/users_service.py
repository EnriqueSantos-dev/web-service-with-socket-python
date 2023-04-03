from typing import Dict
from models.user import User
from database.db import database
from utils.responses import *


def get_users():
    return build_success_response([user.__dict__() for user in database.values()], 200)


def get_user(user_id: str):
    if user_id not in database.keys():
        return build_error_response(404, "User not found")

    return build_success_response(database[user_id].__dict__(), 200)


def create_user(data: Dict):
    user_model = User(name=data['name'], email=data['email'], age=data['age'])
    database[user_model.id] = user_model

    payload = user_model.__dict__()

    return build_success_response(payload, 201)


def update_user(user_id: str, data: Dict):
    if (user_id not in database.keys()):
        return build_error_response(404, "User not found")

    new_user = User(name=database[user_id].name if not data['name'] else data['name'],
                    email=database[user_id].email if not data['email'] else data['email'],
                    age=database[user_id].age if not data["age"] else data['age'], id=user_id)

    database[user_id] = new_user
    return build_success_response(new_user.__dict__(), 200)


def delete_user(user_id: str):
    if user_id not in database.keys():
        return build_error_response(404, "User not found")

    del database[user_id]
    return build_success_response(None, 204)
