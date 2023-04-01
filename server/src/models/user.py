import datetime
from uuid import uuid4
from typing import Optional


class User:
    def __init__(self, name: str, email: str, age: int, id: Optional[str] = None):
        self.id = id or str(uuid4())
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __dict__(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'age': self.age,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()}
