from uuid import uuid4
from typing import Optional


class User:
    def __init__(self, name: str, email: str, age: int, id: Optional[str] = None):
        if not id:
            self.id = str(uuid4())
        else:
            self.id = id
        self.name = name
        self.email = email
        self.age = age

    def __dict__(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'age': self.age}
