from typing import List, Dict
from models.user import User
from database.db import database
from utils.responses import *


def get_users():
    return build_success_response([user.__dict__() for user in database.values()], 200)


def get_user(user_id: str):
    user = database[user_id]

    if (user is None):
        return build_error_response(404, "User not found")

    return build_success_response(user.__dict__(), 200)


def create_user(data: Dict):
    user_model = User(name=data['name'], email=data['email'], age=data['age'])
    database[user_model.id] = user_model

    payload = user_model.__dict__()

    return build_success_response(payload, 201)


def update_user(user_id: str, data: Dict):
    if (user_id not in database.keys()):
        return build_error_response(404, "User not found")

    if (data['name'] is None or data['email'] is None or data['age'] is None):
        return build_error_response(400, "Bad Request")

    new_user = User(name=data['name'],
                    email=data['email'], age=data['age'], id=user_id)

    database[user_id] = new_user

    return build_success_response(new_user.__dict__(), 200)


def delete_user(user_id: str):
    user_exist = database[user_id]

    if (user_exist is None):
        return build_error_response(404, "User not found")

    return build_success_response(database.pop(user_id), 200)
