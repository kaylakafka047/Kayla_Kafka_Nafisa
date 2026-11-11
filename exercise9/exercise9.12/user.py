"""A class representing a user."""

class User:
    """Represent a user."""

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")