"""Classes representing users and administrators."""

class User:
    """Represent a user."""

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")


class Privileges:
    """Store and display administrator privileges."""

    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an administrator."""

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()