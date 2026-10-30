class Email:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Person:
    def __init__(self, id: int, name: str, age: int, emails: list = None):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails if emails is not None else []